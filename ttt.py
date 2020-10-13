import polyfempy as pf
import wildmeshing as wm
# s = pf.Solver()
mesh_path = "plane_hole.svg"

v, f, nodes, F_nodes = wm.triangulate_svg(mesh_path, cut_outside=True)
