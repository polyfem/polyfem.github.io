from collections import namedtuple
import pathlib
import subprocess
import recordclass

import render

polyfem_bin = "/home/zachary/Development/polyfem/build/release/PolyFEM_bin"

input_dir = pathlib.Path(__file__).parent / "input"
output_dir = pathlib.Path(__file__).parent / "output"
videos_dir = pathlib.Path(__file__).parent / "videos"
output_dir.mkdir(exist_ok=True, parents=True)
videos_dir.mkdir(exist_ok=True, parents=True)

RenderArgs = recordclass.recordclass(
    "RenderArgs", ["input", "output", "width", "height", "fps", "drop_frames", "bg_color"])
render_args = RenderArgs(
    input=[],
    output="anim.mp4",
    width=1920,
    height=1080,
    fps=None,
    drop_frames=0,
    bg_color=[46, 48, 62, 255]
)

for script in input_dir.glob("*.json"):
    if script.name == "ipc-defaults.json":
        continue

    print(script.name)
    # yes_or_no = input("Press enter to run [Y/n]: ")
    # if yes_or_no.lower() == "n":
    #     continue

    subprocess.run([
        polyfem_bin,
        "-j", str(script),
        "-o", str(output_dir / script.stem),
        "--log_level", "error"
    ])

    render_args.input = list((output_dir / script.stem).glob("*.pvd"))
    render_args.output = [videos_dir / (script.stem + ".mp4")]
    render.main(render_args)
