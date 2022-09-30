# Top of main python script
import os

from sympy import true
os.environ['PYOPENGL_PLATFORM'] = 'egl'  # noqa

import argparse
import pathlib
import xml.etree.ElementTree as ET

import numpy as np
from scipy.spatial.transform import Rotation as R

from matplotlib import cm
from tqdm import tqdm
import imageio.v3 as iio
from natsort import natsorted

import trimesh
import meshio
import igl

import pyrender
from pyrender import RenderFlags as rf


def homogeneous(a):
    assert(len(a) == 3)
    return np.array([*a, 1.0], dtype=float)


def scale(s):
    if isinstance(s, (int, float)):
        return np.diag([s, s, s, 1.0])
    assert(len(s) == 3)
    return np.diag([*s, 1.0])


def translate(t):
    T = np.eye(4, dtype=float)
    T[:3, 3] = t
    return T


def align_vectors(a, b):
    """Create a rotation matrix that aligns vector a to vector b."""
    T = np.eye(4, dtype=float)
    T[:3, :3] = R.align_vectors(
        np.array(b).reshape(1, -1),
        np.array(a).reshape(1, -1)
    )[0].as_matrix()
    return T


def compute_scale_and_shift_to_fit_mesh(V):
    if V.shape[0] == 0:
        return 1.0, np.zeros(3)
    min_point = V.min(axis=0)
    max_point = V.max(axis=0)
    centroid = (min_point + max_point) / 2
    shift = -centroid
    zoom = 4 / abs(max_point - min_point).max()
    return zoom, shift


def create_default_scene(aspectRatio, bg_color=None):
    scene = pyrender.Scene(
        nodes=None,
        bg_color=[0.3, 0.3, 0.5, 1.0] if bg_color is None else bg_color,
        ambient_light=np.full((3,), 0.3)
    )

    key_intensity = 60.0
    lights = [{
        "position": np.array([-3.0, 3.0, 3.0]),
        "target": np.array([0.0, 0.5, 0.0]),
        "intensity": key_intensity,
        "innerConeAngle": np.pi / 8.0,
        "outerConeAngle": np.pi / 4.0,
    }, {
        "position": np.array([3.0, 3.0, 3.0]),
        "target": np.array([-0.1, 0.5, 0.0]),
        "intensity": 0.6 * key_intensity,
        "innerConeAngle": np.pi / 6.0,
        "outerConeAngle": np.pi / 3.0,
    }, {
        "position": np.array([-1.5, 3.5, -3.0]),
        "target": np.array([0.0, 0.0, 0.0]),
        "intensity": 0.3 * key_intensity,
        "innerConeAngle": np.pi / 4.0,
        "outerConeAngle": np.pi / 2.0,
    }]

    for light in lights:
        spot_light = pyrender.SpotLight(
            color=np.ones(3),
            intensity=light["intensity"],
            innerConeAngle=light["innerConeAngle"],
            outerConeAngle=light["outerConeAngle"],
        )
        scene.add(
            spot_light,
            pose=(translate(light["position"])
                  @ align_vectors([0, 0, -1], light["target"] - light["position"]))
        )

    camera_position = np.array([0.0, 0.0, 3.0])
    # camera_position = np.array([0.0, 1.5, 2.65])
    camera_target = np.array([0.0, 0.0, 0.0])
    scene.add(
        pyrender.PerspectiveCamera(
            yfov=np.deg2rad(45),
            znear=0.1,
            zfar=100,
            aspectRatio=aspectRatio
        ),
        pose=(translate(camera_position) @
              align_vectors([0, 0, -1], camera_target - camera_position))
    )

    return scene


def render(mesh, width=800, height=600, bg_color=None, zoom=None, shift=None):
    scene = create_default_scene(aspectRatio=width/height, bg_color=bg_color)

    if zoom is None or shift is None:
        zoom, shift = compute_scale_and_shift_to_fit_mesh(mesh.points)
    mesh_pose = scale(zoom) @ translate(shift)

    for cells in mesh.cells:
        if cells.type == "triangle":
            NV, NF, IM, JM = igl.remove_unreferenced(mesh.points, cells.data)
            tmesh = trimesh.Trimesh(NV, NF)
            vertex_colors = mesh.point_data["colors"][JM]
            assert(tmesh.vertices.shape[0] == vertex_colors.shape[0])
            tmesh.visual.vertex_colors = vertex_colors

            mesh_args = dict(
                is_visible=True,
                poses=mesh_pose,
                smooth=False
            )

            scene.add(pyrender.Mesh.from_trimesh(
                tmesh,
                # material=pyrender.Material(
                #     doubleSided=True,
                # ),
                **mesh_args))

            # add wireframe
            VN = trimesh.geometry.weighted_vertex_normals(
                tmesh.vertices.shape[0], tmesh.faces, tmesh.face_normals, tmesh.face_angles)
            tmesh.vertices += 1e-3 * VN
            scene.add(pyrender.Mesh.from_trimesh(
                tmesh,
                material=pyrender.MetallicRoughnessMaterial(
                    baseColorFactor=[0.0, 0.0, 0.0, 1.0],
                ),
                wireframe=True,
                **mesh_args
            ))
        elif cells.type == "line":
            capsule = trimesh.creation.capsule(
                height=1.0, radius=5e-3, count=[4, 4])
            capsule.visual.vertex_colors = [0.0, 0.0, 0.0]
            poses = []
            for edge in cells.data:
                v1, v2 = mesh.points[edge]
                direction = v2 - v1
                length = np.linalg.norm(direction)
                poses.append(
                    mesh_pose
                    @ translate(v1)
                    # cylinder is along z-axis
                    @ align_vectors([0.0, 0.0, 1.0], direction)
                    @ scale([1, 1, length])
                )
            scene.add(pyrender.Mesh.from_trimesh(capsule, poses=poses))
        elif cells.type == "vertex":
            sphere = trimesh.creation.uv_sphere(radius=2.5e-2, count=(4, 4))
            sphere.visual.vertex_colors = [0.0, 0.0, 0.0]
            poses = [mesh_pose @ translate(p) for p in mesh.points[cells.data]]
            scene.add(pyrender.Mesh.from_trimesh(sphere, poses=poses))
        else:
            raise NotImplementedError(f"Unsupported cell type: {cells.type}")

    r = pyrender.OffscreenRenderer(
        viewport_width=width, viewport_height=height, point_size=1.0)
    color, depth = r.render(
        scene, flags=rf.RGBA
        | rf.FACE_NORMALS
        | rf.SHADOWS_DIRECTIONAL
        # | rf.SHADOWS_POINT
        # | rf.FLAT
        | rf.SHADOWS_SPOT
    )
    r.delete()
    return color, depth


def fix_normals(V, F):
    mesh = trimesh.Trimesh(V, F, process=False, validate=False)
    trimesh.repair.fix_normals(mesh)
    return mesh.faces


def load_mesh(path):
    mesh = meshio.read(path)

    V, I, J, _ = igl.remove_duplicate_vertices(
        mesh.points, np.array([], dtype=int), 1e-7)

    CV = []  # codim vertices
    E = []  # edges
    F = []  # triangles
    for cells in mesh.cells:
        if cells.type == "triangle":
            F.append(J[cells.data])
        elif cells.type == "tetra":
            F.append(fix_normals(V, igl.boundary_facets(J[cells.data])))
        elif cells.type == "line":
            E.append(J[cells.data])
        elif cells.type == "vertex":
            CV.append(J[cells.data])
        else:
            raise Exception("Unsupported cell type: {}".format(cells.type))

    cells = []
    if F:
        cells.append(("triangle", np.vstack(F)))
    if E:
        cells.append(("line", np.vstack(E)))
    if CV:
        cells.append(("vertex", np.vstack(CV)))

    if "solution" in mesh.point_data:
        V += mesh.point_data["solution"][I]

    scalars = mesh.point_data["E"][I].flatten()
    unique_scalars = np.array(sorted(np.unique(scalars)))
    if unique_scalars[0] == 0.0:
        assert(len(unique_scalars) > 1)
        unique_scalars = unique_scalars[1:]
    min_scalar = unique_scalars.min()
    max_scalar = unique_scalars.max()
    scalar_range = max_scalar - min_scalar if max_scalar != min_scalar else 1.0
    vertex_colors = (cm.viridis_r if len(unique_scalars) > 1 else cm.viridis)(
        (scalars - min_scalar) / scalar_range).reshape(-1, 4)
    vertex_colors[scalars < min_scalar, :] = np.array([0.4, 0.4, 0.4, 1.0])
    assert(vertex_colors.shape[0] == V.shape[0])
    # vertex_colors[:, 3] = 0.5

    mesh = meshio.Mesh(
        points=V,
        cells=cells,
        point_data={"colors": vertex_colors}
    )

    return mesh


def resolve_path(path, root: pathlib.Path) -> pathlib.Path:
    path = pathlib.Path(path)
    if path.is_absolute():
        return path
    return (root / path).resolve()


def parse_vtm(path):
    tree = ET.parse(path)
    root = tree.getroot()
    blocks = root.find("vtkMultiBlockDataSet").findall("Block")
    assert(len(blocks) == 1)
    dataset = blocks[0].find("DataSet")
    return resolve_path(dataset.attrib["file"], path.parent)


def parse_pvd(path, fps=None):
    seq = {
        "meshes": [],
        "output": path.parent.name + ".mp4",
    }

    tree = ET.parse(path)
    root = tree.getroot()
    frames = root.find("Collection").findall("DataSet")
    assert(len(frames) > 0)

    if fps is None:
        assert(len(frames) > 1)
        fps = 1 / (float(frames[1].attrib["timestep"]) -
                   float(frames[0].attrib["timestep"]))
    fps = int(round(max(1, fps)))
    seq["fps"] = fps

    for f in map(lambda f: f.attrib["file"], frames):
        f = resolve_path(f, path.parent)
        if f.suffix == ".vtm":
            f = parse_vtm(f)
        seq["meshes"].append(resolve_path(f, path.parent))

    return seq


def parse_args():
    parser = argparse.ArgumentParser("Render a mesh sequence as a video.")
    parser.add_argument("--input", "-i", nargs="+", required=True, type=pathlib.Path,
                        help="Meshes to render.")
    parser.add_argument("--output", "-o", nargs="+", default=None, type=pathlib.Path,
                        help="Output video file.")
    parser.add_argument("--width", type=int, default=1920,
                        help="Output video width.")
    parser.add_argument("--height", type=int, default=1080,
                        help="Output video height.")
    parser.add_argument("--fps", "-f", type=int, default=None,
                        help="Output video frames per second.")
    parser.add_argument("--drop-frames", type=int, default=0,
                        help="Number of frames to drop.")
    parser.add_argument("--bg-color", "-b", type=float, nargs="+",
                        default=[0.3, 0.3, 0.5, 1.0], help="Background color.")
    return parser.parse_args()


def resolve_output(mesh_sequences, outputs):
    if outputs is None:
        return
    assert(len(outputs) == 1 or len(outputs) == len(mesh_sequences))
    for i, seq in enumerate(mesh_sequences):
        if len(outputs) == 1:
            i = 0
        if outputs[i].suffix == "":
            seq["output"] = outputs[i] / seq["output"]
        else:
            seq["output"] = outputs[i]


def main(args=None):
    if args is None:
        args = parse_args()

    assert(3 <= len(args.bg_color) <= 4)
    args.bg_color = np.array(args.bg_color, dtype=float)
    if args.bg_color.max() > 1.0:
        args.bg_color /= 255.0
    if(len(args.bg_color) == 3):
        args.bg_color = np.array([*args.bg_color, 1.0])

    args.input = natsorted(args.input)

    mesh_sequences = [{
        "meshes": [],
        "fps": 30,
        "output": "anim.mp4",
    }]
    for f in args.input:
        if f.suffix == ".pvd":
            mesh_sequences.append(parse_pvd(f))
        else:
            mesh_sequences[0]["meshes"].append(f)

    resolve_output(mesh_sequences, args.output)

    for seq in mesh_sequences:
        if not seq["meshes"]:
            continue

        if args.drop_frames > 0:
            seq["fps"] //= (args.drop_frames + 1)

        if args.fps is not None:
            seq["fps"] = args.fps

        seq["output"].parent.mkdir(parents=True, exist_ok=True)

        frames = []
        for i, mesh_path in enumerate(pbar := tqdm(seq["meshes"][::args.drop_frames + 1])):
            pbar.set_description(str(seq["output"]))
            mesh = load_mesh(mesh_path)
            if i == 0:
                zoom, shift = compute_scale_and_shift_to_fit_mesh(
                    mesh.points)
            color, _ = render(mesh, width=args.width, height=args.height,
                              bg_color=args.bg_color, zoom=zoom, shift=shift)
            frames.append(color)

        writer_args = dict()
        if seq["output"].suffix == ".mp4":
            macro_block_size = 1
            while (args.width % macro_block_size == 0
                   and args.height % macro_block_size == 0
                   and macro_block_size < 16):
                macro_block_size *= 2
            macro_block_size = max(1, macro_block_size // 2)
            writer_args |= dict(
                fps=seq["fps"],
                quality=5,
                macro_block_size=macro_block_size,
                codec="libx264",
                pixelformat="yuv420p",
            )
        elif seq["output"].suffix == ".gif":
            writer_args |= dict(
                plugin="pillow",
                mode="RGBA",
                duration=len(frames) / seq["fps"],
                loop=0,
                transparency=0,
                disposal=2
            )

        iio.imwrite(seq["output"], frames, **writer_args)


if __name__ == "__main__":
    main()
