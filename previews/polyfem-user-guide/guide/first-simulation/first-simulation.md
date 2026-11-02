# Start here: your first PolyFEM simulation

New to PolyFEM? This guide takes you from a working build to a first finite-element solution. You do not need to understand every JSON option to begin.

## 1. Build PolyFEM

Follow the [C++ installation instructions](../cxx_index.md) to compile PolyFEM. From the repository root, the current recommended build commands are:

```sh
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
cmake --build build
```

Ninja is optional; omit `-G Ninja` if you use another CMake generator.

## 2. Run an existing example

The existing [Getting Started tutorial](../tutorials/getting_started.md) includes a **plate with a hole** example and its mesh, input JSON, and expected visualization. Download its [mesh](../img/plate_hole.obj) and save the JSON configuration from that tutorial as `run.json` in the same directory.

From that directory, run the compiled executable (adjust the path for your build location):

```sh
/path/to/polyfem/build/PolyFEM_bin --json run.json
```

The example solves a **Laplacian** problem with the Franke preset. It is deliberately simpler than a mechanics simulation: you can first learn how PolyFEM loads geometry, solves a PDE, and writes results.

## 3. Inspect the result

The example's `output.paraview.file_name` setting requests a VTU result, which you can open in [ParaView](https://www.paraview.org/). Compare the output with the [reference image](../img/plate_hole_solution.png).

## 4. Understand the input

The example introduces five top-level groups:

| JSON group | What it controls |
| --- | --- |
| `geometry` | Which mesh to load and how to interpret it |
| `materials` | Which PDE or material model to solve |
| `preset_problem` | A predefined right-hand side / exact-solution setup |
| `solver` | Numerical solution method |
| `output` | Where to write results |

You do **not** need to memorize these options. Use the [JSON input guide](../json.md) for explanations and the [generated JSON specification](../json_defaults_and_spec.md) for exact available settings.

## 5. Move to elasticity

Once the Laplacian example works, continue in [Getting Started: Boundary Conditions](../tutorials/getting_started.md#boundary-conditions). It shows how to change the plate-with-hole problem to linear elasticity, apply loads, and constrain displacement components.

### If something goes wrong

- **Mesh not found:** Run from the directory containing `run.json` and `plate_hole.obj`, or update the mesh path in JSON.
- **Executable not found:** Check your CMake build directory and the executable path.
- **No result visible:** Check the output location configured in JSON, then load the VTU file in ParaView.

---

**Next:** [Existing tutorials](../tutorials/getting_started.md) · [Technical formulations](../details/formulations.md) · [JSON specification](../json_defaults_and_spec.md)
