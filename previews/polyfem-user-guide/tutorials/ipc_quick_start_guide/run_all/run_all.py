import sys
from collections import namedtuple
import pathlib
import subprocess

simrender_path = pathlib.Path("/home/zachary/Development/personal-projects/simrender")
if simrender_path.exists():
    sys.path.append(str(simrender_path))
    import render

debug = False

polyfem_bin = f"/home/zachary/Development/polyfem/build/{'debug' if debug else 'release'}/PolyFEM_bin"
#polyfem_bin = f"/Users/zachary/Development/research/polyfem/polyfem/build/{'debug' if debug else 'release'}/PolyFEM_bin"

input_dir = pathlib.Path(__file__).parent / "input"
output_dir = pathlib.Path(__file__).parent / "output"
videos_dir = pathlib.Path(__file__).parent / "videos"
output_dir.mkdir(exist_ok=True, parents=True)
videos_dir.mkdir(exist_ok=True, parents=True)

for script in input_dir.glob("*.json"):
    if script.name == "ipc-defaults.json":
        continue

    print(script.name)
    # yes_or_no = input("Press enter to run [Y/n]: ")
    # if yes_or_no.lower() not in ["", "y", "yes"]:
    #     continue

    subprocess.run(
        (["lldb", "--"] if debug else []) + [
            polyfem_bin,
            "-j", str(script),
            "-o", str(output_dir / script.stem),
            "--log_level", "debug"
        ])

    if simrender_path is not None and simrender_path.exists():
        render_args = render.parse_args([
            "--input", str(list((output_dir /
                           script.stem).glob("*.pvd"))[0]),
            "--output", str(videos_dir / (script.stem + ".mp4")),
            "--bg-color", "46", "48", "62", "255",
            "--base-zoom", "2",
            # "--drop-frames", "4"
        ])
        render.main(render_args)
