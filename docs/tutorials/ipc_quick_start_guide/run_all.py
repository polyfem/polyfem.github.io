import sys
from collections import namedtuple
import pathlib
import subprocess

sys.path.append("/home/zachary/Development/simrender")  # noqa
import render

polyfem_bin = "/home/zachary/Development/polyfem/build/release/PolyFEM_bin"

input_dir = pathlib.Path(__file__).parent / "input"
output_dir = pathlib.Path(__file__).parent / "output"
videos_dir = pathlib.Path(__file__).parent / "videos"
output_dir.mkdir(exist_ok=True, parents=True)
videos_dir.mkdir(exist_ok=True, parents=True)

for script in input_dir.glob("newmark.json"):
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
        "--log_level", "debug"
    ])

    render_args = render.parse_args([
        "--input", str(list((output_dir / script.stem).glob("*.pvd"))[0]),
        "--output", str(videos_dir / (script.stem + ".mp4")),
        "--bg-color", "46", "48", "62", "255",
        "--base-zoom", "2",
        "--drop-frames", "4"
    ])
    render.main(render_args)
