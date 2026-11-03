# PolyFEM user guide: from first run to advanced simulations

This hands-on introduction starts with a complete, downloadable example, explains each part of the input, and then changes the physics and boundary conditions. You can **run PolyFEM without compiling it** if a suitable prebuilt package is available.

**What you will do:** open the PolyFEM desktop application, load a JSON simulation of a plate with a hole, run it using the **Run** button, inspect the output in ParaView, and then try linear elasticity.

![Plate with a hole and its solution](../img/plate_hole_solution.png)

## How this guide is organized: a progression through tested examples

This page is a **guided tour of the [polyfem-data test and example repository](https://github.com/polyfem/polyfem-data)**, not a separate collection of invented demos. The repository currently contains **414 JSON files**, including **182 under `old-tolerances/`** (historical regression copies). Most aren't good first lessons: some exercise one solver detail, and others inherit a larger scene. The learning path below selects representative **current** examples and introduces one modeling idea at a time.

Each link opens the **actual JSON used in PolyFEM tests**. Read its `geometry`, `materials`, `space`, and `boundary_conditions` fields alongside the explanation in this page. An example with `"common"` or `"patch"` **depends on another JSON file**; load it using its original path and keep the data repository's directory structure, rather than downloading only that one file.

!!! tip "Try the examples in the GUI"
    Download or clone [polyfem-data](https://github.com/polyfem/polyfem-data), launch the packaged **PolyFEM desktop app**, click **Load JSON**, choose an example and click **Run**. Start with short, static cases; dynamics and contact can cost much more. Some regression configurations contain `tests` entries for automated accuracy checks. Those are not the primary user-facing settings.

### The path through the examples

The next sections build up one concept at a time: **first run → mesh → boundary tags → materials → finite-element spaces → dynamics → contact → multiphysics**. Each section links to an actual `polyfem-data` JSON, says which fields to inspect, and suggests a small experiment. You can read the whole guide on this page; open the specialized tutorials only when you want more depth.

### How to read inherited configurations

For instance, [`standard/neohookean.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/neohookean.json) is intentionally compact:

```json
{
  "common": "elastic_common.json",
  "materials": { "type": "NeoHookean", "id": 1, "E": 20000, "nu": 0.3 }
}
```

It inherits mesh, constraints, and solver configuration from [`standard/elastic_common.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/elastic_common.json), which itself refers to [`standard/common.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/common.json) for output settings. Reading only the small top-level JSON would hide most of the actual problem.

A few test cases also use **`patch`**, such as [P2 ball bounce](https://github.com/polyfem/polyfem-data/blob/main/contact/examples/3D/higher-order/ball-bounce/P2.json), which changes the mesh path and FE degree relative to P1. Keep the full parent chain, including meshes. That is also a useful pattern for your own comparisons: reuse one baseline and vary only the part you are studying.

---

## 1. Get PolyFEM

Choose one of these paths:

=== "Download a binary (quickest)"

    PolyFEM's [Artifacts workflow](https://github.com/polyfem/polyfem/actions/workflows/artifacts.yml) packages the executable for **Linux x86-64**, **macOS ARM64**, and **Windows AMD64**.

    1. Open the workflow and choose a **successful run on `main`**. For example, [this successful October 30, 2026 run](https://github.com/polyfem/polyfem/actions/runs/41086941557) contains all three platform packages.
    2. Under **Artifacts**, download the package matching your operating system. GitHub may ask you to sign in.
    3. Extract the Linux `.tar.gz` or Windows `.zip`, or open the macOS `.dmg`. Launch the packaged **PolyFEM desktop application** (`polyfem_app`), using the normal launcher for your platform. The desktop app has **Load JSON**, **Load HDF5**, and **Run** controls.
    4. The command-line `PolyFEM_bin` is a separate option and is not required for the walkthrough.

    !!! note "Workflow artifacts, not tagged releases"
        These packages are built from the project’s `main` branch. They are **CI artifacts** (which can expire), not assets attached to the older [v0.5 GitHub release](https://github.com/polyfem/polyfem/releases/tag/v0.5). Use the latest successful workflow run when the example link expires.

=== "Build from source"

    Building from source is useful when modifying PolyFEM itself or when no prebuilt package matches your platform. You need **CMake 3.25+**, a **C++17 compiler**, Git and an internet connection for initial dependency downloads. Python development headers are also required unless you disable Python support.

    ```sh
    git clone https://github.com/polyfem/polyfem.git
    cd polyfem
    cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release
    cmake --build build
    ```

    Ninja is recommended but optional; omit `-G Ninja` if you are using a different generator. See the [up-to-date PolyFEM build instructions](https://github.com/polyfem/polyfem#compilation) for platform-specific notes.

=== "Python"

    PolyFEM also offers a separate Python interface:

    ```sh
    conda install -c conda-forge polyfempy
    ```

    The desktop-app examples below use the **C++ application**, not `polyfempy`. For Python examples, see the [Python guide](../python.md) and [Jupyter tutorial](../python_examples.ipynb).

## 2. Download a complete first example

Create an empty directory called `polyfem-first-run` and save **both** files there:

- [`run.json`](run.json) — the ready-to-run configuration (open the link and save the file).
- [`plate_hole.obj`](../img/plate_hole.obj) — the example mesh (download it into the same directory).

Your working directory should contain:

```text
polyfem-first-run/
├── plate_hole.obj
└── run.json
```

!!! important "Keep the files together"
    The configuration contains `"mesh": "plate_hole.obj"`. Running it from the directory containing both files avoids path-resolution surprises.

## 3. Run the simulation in the desktop application

1. Launch the **PolyFEM app** (`polyfem_app`) from the downloaded package. If you compiled from source, make sure the application was enabled with `POLYFEM_WITH_APP=ON` and launch the built app.
2. Click **Load JSON** and select `run.json` from your `polyfem-first-run` directory. The mesh path inside the JSON refers to `plate_hole.obj` in that same directory.
3. Click **Run** to start the solve. The interface displays **Running...** while it is executing; wait for it to finish, and check any displayed errors if the input cannot be loaded.
4. Find the generated output in the configured output directory. This example requests **`result.vtu`** and **`stats.json`**.

The application also has a **Load HDF5** button for bundled inputs, but JSON is simpler for a first exercise.

!!! note "Command-line alternative"
    If you prefer scripting or automation, the separate command-line executable accepts the same example:

    ```sh
    /path/to/PolyFEM_bin --json run.json
    ```

    This is optional for beginners. It is **not** how the desktop application is launched.

### What are we solving?

The *Laplacian* is a scalar PDE. This example uses PolyFEM's `Franke` preset, which provides a convenient test problem without requiring you to manually define forces and boundary values. PolyFEM constructs the finite-element system, solves it, and exports the field for visualization.

## 4. Inspect the results

Install [ParaView](https://www.paraview.org/) and open the generated `result.vtu`.

1. Click **Apply** in ParaView after loading the data.
2. Choose the solution field in the **Coloring** dropdown.
3. Compare the visualization with the reference below.

| Input mesh | Reference solution |
| --- | --- |
| ![Plate with a hole](../img/plate_hole_mesh.png) | ![Laplacian solution](../img/plate_hole_solution.png) |

For this scalar problem, you are viewing a field on a fixed geometry, not deforming the mesh. The **Warp By Vector** filter becomes useful when you solve displacement-based elasticity problems.

## 5. Understand `run.json`

Here is the complete example, so you can read it alongside the downloaded file:

```json
{
  "geometry": {
    "advanced": { "normalize_mesh": true },
    "mesh": "plate_hole.obj",
    "surface_selection": { "threshold": 1e-7 }
  },
  "materials": { "type": "Laplacian" },
  "preset_problem": { "type": "Franke" },
  "solver": { "linear": { "solver": "Eigen::SparseLU" } },
  "output": {
    "json": "stats.json",
    "paraview": { "file_name": "result.vtu" }
  }
}
```

| Section | Meaning | Try changing |
| --- | --- | --- |
| `geometry` | Load a mesh and optionally normalize its size | Use a different mesh |
| `surface_selection` | Associate boundary primitives with IDs | Change or specify a boundary selection |
| `materials` | Choose the governing PDE/material | `Laplacian` → `LinearElasticity` |
| `preset_problem` | Supply a built-in test problem | Replace with your own boundary conditions |
| `solver` | Select numerical linear solver | Explore other supported solvers |
| `output` | Write data for diagnostics and visualization | Change the output file name |

For every available setting, use the [JSON input guide](../json.md) and the [automatically generated JSON specification](../json_defaults_and_spec.md). The [interactive JSON builder](https://polyfem.github.io/json-builder/) is another way to explore configuration options.

!!! example "From the test suite: plate with a hole"
    The [tested `standard/plate_hole.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/plate_hole.json) contains precisely this kind of scalar problem. Compare its `geometry`, `materials`, `preset_problem`, and `output` with the downloaded `run.json`. The test-suite version additionally has `tests` entries for numerical regression checks; these are not required to start a simulation.

    **Try:** change only `output.paraview.file_name` and run again. Confirm that you can find the new file. This is a simpler first experiment than changing the PDE.
## 6. Change the problem: linear elasticity

Now use the *same mesh* to solve a vector-valued displacement problem.

1. Copy `run.json` to `elasticity.json`.
2. Replace `"materials": { "type": "Laplacian" }` with:

    ```json
    "materials": {
      "type": "LinearElasticity",
      "E": 210000,
      "nu": 0.3
    }
    ```

3. **Remove the entire `preset_problem` section**, including its trailing comma as needed.
4. Add the following **top-level** `boundary_conditions` section:

    ```json
    "boundary_conditions": {
      "neumann_boundary": [
        { "id": 3, "value": [100, 0] }
      ],
      "dirichlet_boundary": [
        { "id": 1, "value": [0, 0], "dimension": [true, false] },
        { "id": 4, "value": [0, 0], "dimension": [false, true] }
      ]
    }
    ```

5. Change the output filename to `elasticity.vtu`, then return to the **desktop app**, click **Load JSON** to select `elasticity.json`, and click **Run** again. You can also run it using `PolyFEM_bin --json elasticity.json` if you prefer the CLI.

**What changed?** In elasticity, the unknown is a *displacement vector*. Neumann conditions prescribe a force/traction; Dirichlet conditions constrain displacement. The `dimension` masks here restrict only one coordinate at each of the two selected boundaries.

These IDs come from the plate-with-hole boundary-tagging convention used in the [full Getting Started tutorial](../tutorials/getting_started.md#boundary-conditions); they are not automatically meaningful for an arbitrary mesh.

!!! tip "Explore boundary conditions visually"
    In ParaView, color the resulting field and use **Warp By Vector** with the displacement field to see the deformation. You may need to adjust the warp scale to make small displacements noticeable.

!!! example "From the test suite: the elastic baseline"
    [`standard/elastic_common.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/elastic_common.json) is a 3D baseline used by several elastic tests. Look at its two `surface_selection` boxes, the corresponding IDs 1 and 3 in `dirichlet_boundary`, and its reference to `common.json`.

    **Try:** identify which boundaries move left and right without running anything, then compare the displacement vectors. This same connection between boundary tags and conditions is what your plate example uses.
## 7. Meshes: what PolyFEM actually discretizes

The first example uses a **2D plate with a hole**. PolyFEM is not restricted to this mesh or to triangles. Before changing the physics, it helps to distinguish a *surface describing an object* from a *volume discretization of the object*.

| Input geometry | Typical finite elements | What it represents |
| --- | --- | --- |
| 2D triangular mesh | Triangles | A planar PDE or 2D solid |
| 2D quadrilateral mesh | Quads | The same, with tensor-product-style elements |
| 3D tetrahedral volume mesh | Tets | A volumetric solid or fluid domain |
| 3D hexahedral volume mesh | Hexes | A volumetric domain using hex elements |
| Polygonal / polyhedral elements | Polygons / polyhedra | Generalized elements; basis choice matters |
| Surface triangle mesh | Triangles on a surface | Often an input for a **collision obstacle**, not a volumetric elastic solid |

### Loading a mesh

The simplest geometry entry is:

```json
"geometry": {
  "mesh": "plate_hole.obj"
}
```

A scene with several bodies uses a list of geometries. For example, a sphere and a soft mat may each have their own mesh, transforms, and IDs:

```json
"geometry": [
  {
    "mesh": "sphere.msh",
    "transformation": { "translation": [0, 1, 0] },
    "volume_selection": 1
  },
  {
    "mesh": "mat.msh",
    "volume_selection": 2
  }
]
```

This is an **illustrative fragment**, not a complete runnable scene; the actual sphere/mat meshes, contact parameters, and boundary conditions are provided by the [tested sphere–mat example](https://github.com/polyfem/polyfem-data/blob/main/contact/examples/3D/large-ratios/sphere-mat.json).

The input specification lists `.obj`, `.msh`, `.stl`, `.ply`, and `.mesh` among the accepted mesh-file extensions. **The extension alone does not tell you whether a mesh contains volume cells.** For example, an OBJ containing only triangles is a surface, whereas a Gmsh MSH file can carry tetrahedra or other volume cells. For 3D elasticity you normally need a **volume mesh**, not just a surface shell.

!!! example "From the test suite: change element types, keep the physics"
    Compare [`standard/laplace.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/laplace.json) (3D cube volume mesh) with [`standard/laplace_quad.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/laplace_quad.json) (2D quadrilateral mesh). Both use `Laplacian` and the `Franke` preset; notice that their meshes, dimension, and refinement settings differ.

    **Try:** run each from a complete checkout of `polyfem-data`, keeping its relative mesh paths. You are comparing two *different discretized domains*, not a controlled convergence experiment. For a controlled experiment, refine the same mesh or change only the FE degree.
### Geometry operations

Use `transformation` to place and resize objects **without modifying their mesh files**:

```json
"geometry": {
  "mesh": "part.msh",
  "transformation": {
    "scale": [1, 2, 1],
    "translation": [0, 0.5, 0]
  }
}
```

Rotations are also supported. Transforms matter because **geometric boundary selection is performed on the positioned geometry**: if you move or scale a body, absolute selection coordinates may need updating.

`"advanced": { "normalize_mesh": true }` rescales the mesh into a standard size. That is convenient for the first numerical example, but for physical simulation you should take care with **units and material parameters**. A mesh measured in millimeters is not interchangeable with one measured in meters if you keep the same physical stiffness, density, loads, and time scale.

!!! tip "Surface obstacles versus deformable bodies"
    A plane or triangulated surface can be used as a collision obstacle (`"is_obstacle": true`). It does not automatically become a 3D elastic body with interior degrees of freedom. See the [IPC tutorial](../tutorials/ipc_quick_start_guide/ipc_quick_start_guide.md#collision-obstacles) for surface, edge, and point obstacles.

## 8. Sidesets, body IDs, and boundary conditions

This is one of the most important ideas in PolyFEM.

A **boundary sideset** is a group of *boundary edges* in 2D or *boundary faces* in 3D, identified by an integer. A boundary condition refers to this **ID** rather than listing every edge or face individually. An ID is a **label**, not a coordinate, node number, or material property.

Similarly, a **volume ID** labels a region of elements (triangles/quads in 2D; tets/hexes in 3D). These are often called *body IDs* in examples and are used to assign material parameters.

| Concept | Which primitives are labeled? | Used for |
| --- | --- | --- |
| `surface_selection` | Boundary edges/faces | Dirichlet and Neumann conditions, boundary loads, prescribed motion |
| `volume_selection` | Interior elements | Material/body assignment and region-specific properties |

**IDs from one category do not automatically determine IDs in the other.** A body with volume ID 2 may have boundary sidesets 1, 3, and 7, and several bodies can reuse a material model with different volume IDs.

### Bounding-box sidesets in the plate example

For the plate-with-hole mesh, the tutorial uses:

```json
"surface_selection": { "threshold": 1e-7 }
```

This is the **bounding-box side selector**. It labels the outer boundary according to its proximity to the bounding-box faces:

| ID | Side |
| --- | --- |
| 1 | Minimum x (left) |
| 2 | Minimum y (bottom) |
| 3 | Maximum x (right) |
| 4 | Maximum y (top) |
| 5 / 6 | Minimum / maximum z (3D only) |
| 7 | Remaining boundary faces/edges |

The **hole** is an example of an interior boundary that is not on one of the bounding-box sides: it falls into the remaining-boundary category. The threshold controls how close to a box side the barycenter must be for the label to apply. It should be chosen consistently with the mesh scale.

The important connection is now explicit:

```json
"boundary_conditions": {
  "dirichlet_boundary": [
    { "id": 1, "value": [0, 0], "dimension": [true, false] },
    { "id": 4, "value": [0, 0], "dimension": [false, true] }
  ],
  "neumann_boundary": [
    { "id": 3, "value": [100, 0] }
  ]
}
```

This constrains the **x displacement** on sideset 1, the **y displacement** on sideset 4, and applies an **x-directed traction** on sideset 3. The other components remain free where the mask is `false`.

In an elasticity problem:

- **Dirichlet** means prescribed **displacement**; zero is a fixed displacement, not zero stress.
- **Neumann** means prescribed **traction** on the selected surface; it is not the same thing as an applied force at one vertex.
- The **right-hand side** `rhs` describes a source or body load in the governing equations, not a sideset.
- Leaving a sideset without an explicit traction typically corresponds to a natural/free boundary for this class of problem.

!!! example "From the test suite: one mesh, different sidesets"
    The selection tests share an [alien volumetric mesh](https://github.com/polyfem/polyfem-data/tree/main/selection) and a [baseline problem](https://github.com/polyfem/polyfem-data/blob/main/selection/main.json). Compare:

    - [`selection/plane.json`](https://github.com/polyfem/polyfem-data/blob/main/selection/plane.json): half-spaces defined by a point and normal.
    - [`selection/sphere.json`](https://github.com/polyfem/polyfem-data/blob/main/selection/sphere.json): spherical neighborhoods.
    - [`selection/cylinder.json`](https://github.com/polyfem/polyfem-data/blob/main/selection/cylinder.json): cylindrical neighborhoods.
    - [`selection/file.json`](https://github.com/polyfem/polyfem-data/blob/main/selection/file.json): IDs loaded from `alien.txt`.

    Each inherits `main.json` through `common`. **Compare the `geometry.surface_selection` block first**; its two IDs feed the same prescribed displacements in the baseline. Then inspect the geometry and results. Do not compare their numerical errors as if they were solving identical boundary-value problems: the selected boundary regions differ.
### Two ways to assign IDs

There are two broad approaches, and you can mix them as needed.

**A. Use IDs stored in or supplied alongside the mesh.** This is preferable when your meshing pipeline already knows material regions or boundary tags.

```json
"geometry": {
  "mesh": "tagged.msh",
  "surface_selection": "surface_tags.txt",
  "volume_selection": "volume_tags.txt"
}
```

The `.txt` files need IDs in the order expected by PolyFEM for the corresponding mesh elements. These are **illustrative file names**; you must supply matching mesh and tag files. A mesh format may also carry its own region/body labels, in which case you can preserve them rather than generating new selections.

**B. Compute IDs from geometry.** This is convenient when you only have the mesh, or when you want to describe selections with coordinates.

For example, selecting a region near the minimum-x side of a unit-sized body:

```json
"surface_selection": [
  {
    "id": 10,
    "box": [[0, 0, 0], [0.1, 1, 1]],
    "relative": true
  }
]
```

The two corners of the box are in **relative bounding-box coordinates**, so this selects boundary faces whose barycenters lie in the first 10% of the body's x extent. The example is 3D; use two coordinates per corner in 2D. It does **not** change the mesh; it assigns a label.

Other geometric selectors supported by the current specification include:

| Selector | Useful for | Main JSON fields |
| --- | --- | --- |
| Box | A region inside an axis-aligned box | `id`, `box` |
| Sphere | A local region around a point | `id`, `center`, `radius` |
| Cylinder | A cylindrical region along an axis | `id`, `p1`, `p2`, `radius` |
| Plane / half-space | Everything on one side of a plane | `id`, `point`, `normal` |
| Axis-aligned half-space | A side such as x less than a given position | `id`, `axis`, `position` |

Selectors work using element or boundary-primitive **barycenters**, not precise intersections with the underlying continuous region. On a coarse mesh, the selected set may not match the exact geometric cut you imagined.

!!! note "Two independent choices"
    **What** you label: surface versus volume. **How** you label it: imported IDs versus geometric selection. These are independent; for instance, a body may load volume IDs from `.msh` but use geometric rules to choose the surface patch where you pull it.

For a detailed field-by-field explanation of all selection forms, use the [JSON input guide](../json.md#selections) and [generated specification](../json_defaults_and_spec.md). The old standalone **BC Setter** application is no longer part of the current workflow.

## 9. Materials: from one elastic solid to several regions

The `materials` section selects the PDE or constitutive law and its parameters. It is not just a palette or visualization label.

### Start with linear elasticity

```json
"materials": {
  "type": "LinearElasticity",
  "E": 210000,
  "nu": 0.3
}
```

Here `E` is **Young's modulus** (stiffness scale) and `nu` is **Poisson's ratio** (lateral contraction relative to stretching). For time-dependent mechanics, `rho` controls mass density. Physical values must use consistent units.

The `LinearElasticity` model assumes small strains. For larger deformations, use an appropriate nonlinear model instead:

```json
"materials": {
  "type": "NeoHookean",
  "E": 1000000,
  "nu": 0.4,
  "rho": 1000
}
```

This is a valid example of a **compressible Neo-Hookean** material entry. It does **not** alone define a full simulation: geometry, loads, constraints, and possibly time settings still matter.

### Which material family should I choose?

| Model | When to consider it |
| --- | --- |
| `Laplacian`, `Helmholtz` | Scalar PDEs / simple numerical examples |
| `LinearElasticity` | Small-displacement solids |
| `SaintVenant` | Geometrically nonlinear elasticity with a simple constitutive model |
| `NeoHookean` | Finite-deformation hyperelastic solids |
| `MooneyRivlin` and Ogden variants | More specialized hyperelastic models requiring their own parameters |
| `HGOFiber`, `HGODispersion`, `ActiveFiber` | Anisotropic or active-fiber material models |
| `Stokes`, `NavierStokes` | Incompressible fluid flow; mixed spaces and fluid parameters are required |
| `NavierStokesFSI` | Coupled fluid–structure interaction; **advanced**, with several coupled fields |
| `ThermoElasticity` | Coupled displacement and temperature fields |

This is a **guided subset**, not a list of interchangeable options. Each model has its own **required parameters** and mathematical assumptions. See [formulations](../details/formulations.md) and the [generated material specification](../json_defaults_and_spec.md) before switching a real application.

!!! example "From the test suite: change the law, not the domain"
    Read [`standard/hooke.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/hooke.json), [`standard/saint_venant.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/saint_venant.json), and [`standard/neohookean.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/neohookean.json). The first two use a cube and the `ElasticExact` preset; Neo-Hookean inherits the displacement-controlled `elastic_common.json` baseline.

    **Important:** because these inputs do not all have identical boundary conditions, they are examples of material configuration, **not** an apples-to-apples quantitative constitutive-model comparison. To isolate a material law, hold geometry, loads, and constraints fixed and change the material in a copy of one runnable configuration.

    For specialized materials, [`standard/hooke_anisotropic.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/hooke_anisotropic.json) supplies a full elasticity tensor, while [`standard/active-fiber.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/active-fiber.json) builds a composite with `MaterialSum`, `NeoHookean`, `VolumePenalty`, and `ActiveFiber`. Read them after the isotropic cases.
### Multiple materials: connect volume IDs to material IDs

A scene can contain several material regions:

```json
"geometry": [
  { "mesh": "stiff_part.msh", "volume_selection": 1 },
  { "mesh": "soft_part.msh", "volume_selection": 2 }
],
"materials": [
  { "id": 1, "type": "NeoHookean", "E": 1e8, "nu": 0.4, "rho": 2000 },
  { "id": 2, "type": "NeoHookean", "E": 1e6, "nu": 0.4, "rho": 1000 }
]
```

This is a **configuration fragment**, not a runnable scene: both meshes must exist and you need suitable boundary conditions. Notice the correspondence between `volume_selection: 1` and `materials[0].id: 1`, and similarly for ID 2.

**Try it:** on a multi-body model, change one material's `E` by a factor of 10 while keeping everything else fixed. Compare the displacement field and force response. If you want the complete, documented workflow (including mesh generation and assignment of region IDs), continue with [Simulating Multiple Materials in a Single Mesh](../tutorials/multi-material/multi-material.md).

!!! example "From the test suite: one mesh with multiple material IDs"
    [`multi-material/stretch-cubes.json`](https://github.com/polyfem/polyfem-data/blob/main/multi-material/stretch-cubes.json) uses a tagged volume mesh (`cubes_v41.msh`) and three `materials` entries, with IDs 1, 2, and 3. It also uses geometric boxes to select the **left and right boundary regions**, and prescribed motion to stretch the object.

    **Inspect in order:** the mesh file and its *volume IDs* → `materials[].id` → `surface_selection` → `boundary_conditions`. The same integers may appear in different roles, but volume IDs choose material regions while surface IDs choose boundary regions.

    **Try:** make the middle material stiffer by changing only its `E`. Keep the original file and mesh in their repository directory. For the mesh-generation procedure, follow the [existing multi-material tutorial](../tutorials/multi-material/multi-material.md).
## 10. Finite-element spaces: separate geometry, approximation, and physics

An FEM computation involves at least three choices:

1. **Mesh:** how the domain is split into elements (triangles, quads, tets, hexes, etc.).
2. **Approximation space:** the shape functions and number/location of degrees of freedom (for example, linear versus quadratic Lagrange).
3. **Physics/material:** which equations the degrees of freedom satisfy (for example, Laplacian versus elasticity).

The last two are **not the same thing**. You can solve the same elasticity model on the same mesh using different approximation orders, or solve different physics using the same FE space.

### Polynomial degree: P1 versus P2

The easiest experiment is to keep the input and change one field:

```json
"space": {
  "discr_order": 1
}
```

Then try:

```json
"space": {
  "discr_order": 2
}
```

The order controls the **finite-element approximation**, not the material law. Degree 1 generally means a piecewise-linear solution on simplicial elements; degree 2 adds additional degrees of freedom and can resolve more variation on the same mesh, at greater assembly/solve cost.

**Experiment:** solve the same plate-with-hole problem at orders 1 and 2. Compare the results *without changing the mesh or physics*. For a smooth solution, compare accuracy as well as runtime; it is misleading to conclude one choice is better solely from how smooth a ParaView image looks.

!!! example "From the test suite: compare element order"
    [`standard/laplace_3d_b2.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/laplace_3d_b2.json) explicitly chooses `"basis_type": "Bernstein"` and `"discr_order": 2`. For a cleaner P1/P2 experiment on a single problem, duplicate one input (such as the plate) and change only `space.discr_order`.

    **Try:** compare the number of degrees of freedom, solve time, and solution/error statistics. When comparing separate `polyfem-data` files, first check whether they also changed the **mesh order** or refinement level.
### Basis families

The current JSON specification exposes:

```json
"space": {
  "discr_order": 2,
  "basis_type": "Lagrange"
}
```

| Basis | Interpretation / restriction |
| --- | --- |
| `Lagrange` | Standard nodal finite-element basis; good default |
| `Spline` | Spline-based basis on supported quadrilateral/hexahedral discretizations |
| `Serendipity` | Reduced-DOF polynomial family on supported quadrilateral/hexahedral meshes |
| `Bernstein` | Bernstein basis option (check mesh/feature compatibility before using) |

For **polygonal** elements, PolyFEM has a separate `poly_basis_type` selector. Available names in the current specification include `MFSHarmonic`, `MeanValue`, and `Wachspress`. Those are specialized approximation constructions: they are not simply different names for P1.

The `space.use_p_ref` option allows geometry-dependent **a priori p-refinement**. It is a separate concept from simply increasing a global `discr_order`. For background, see the [technical formulations](../details/formulations.md) and PolyFEM's [Decoupling Simulation Accuracy from Mesh Quality work](https://github.com/polyfem/polyfem).

!!! example "From the test suite: spline and polygonal choices"
    The [`standard/laplace_spline.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/laplace_spline.json) configuration uses a quadrilateral mesh and `space.basis_type: "Spline"`. The [`standard/laplace_mv.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/laplace_mv.json) and [`standard/laplace_ws.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/laplace_ws.json) files instead use a polygon mesh with Mean Value and Wachspress `poly_basis_type` options.

    **Try:** compare the two polygon examples first: their configurations have the same mesh and preset, so the polygonal basis is the meaningful change. Then look at the quadrilateral spline example as a separate basis-family demonstration.
### Mixed formulations have multiple fields

Not every simulation has a single scalar or displacement vector as its unknown. For example, incompressible flow solves for both **velocity** and **pressure**. Fluid–structure interaction can also include solid displacement and ALE mesh displacement. In those cases, the input material and coupled problem configuration refer to **space IDs** for the different fields; using only a single `discr_order` is not a complete mixed formulation setup.

!!! warning "Don't guess a coupled setup"
    A working `NavierStokesFSI` example needs more than changing `materials.type`. It has required field-space IDs, geometry IDs, viscosity, and nested material choices. Start from a compatible **tested configuration** and consult the [generated JSON specification](../json_defaults_and_spec.md).

### Mesh order is not necessarily solution order

A curved/high-order geometric map describes **where the elements are in physical space**. The `space.discr_order` describes **how the unknown field is approximated**. PolyFEM supports separating these decisions in supported cases. Increasing the solution order does not automatically repair a poorly resolved geometric boundary; conversely, a curved mesh can represent geometry well without forcing the solution space to the same order.

## 11. Time-dependent simulations: motion and integration

For transient problems, the top-level `time` section determines the simulated interval and time-stepping scheme. A material's density and the problem's initial conditions become especially important. The UI still follows the same workflow: **Load JSON → Run**, but output often becomes a time sequence instead of one VTU.

Start with these actual tests:

- [`interpolation/linear_ramp.json`](https://github.com/polyfem/polyfem-data/blob/main/interpolation/linear_ramp.json) gives boundary IDs 1 and 3 prescribed displacement values, with **different linear-ramp intervals**. It inherits the rest of the scene from `interpolation/main.json`. This demonstrates that *how* a displacement changes over time is separate from *which* boundary receives it.
- [`time-int/euler.json`](https://github.com/polyfem/polyfem-data/blob/main/time-int/euler.json) and [`time-int/newmark.json`](https://github.com/polyfem/polyfem-data/blob/main/time-int/newmark.json) both inherit `time-int/main.json`; they choose `ImplicitEuler` and `ImplicitNewmark` respectively.

```json
"time": {
  "integrator": "ImplicitEuler",
  "tend": 0.1,
  "time_steps": 10
}
```

**Try:** compare the two integrator configurations without editing them first. Then change the time-step count *in a copy*, keeping total simulated time fixed. Compare trajectory/output across steps; do not equate a difference in numerical damping with a material effect.

For a more visual prescribed-motion example, inspect [`time-bc/walking-elephant.json`](https://github.com/polyfem/polyfem-data/blob/main/time-bc/walking-elephant.json). It uses spatial selections and time-dependent boundary motion on an elephant mesh.

## 12. Contact: two bodies and a barrier

Contact is more than two overlapping meshes: the objects must be represented by appropriate geometry, a constitutive model must define their motion, and **collision/contact** must be configured.

Start with [`contact/examples/3D/unit-tests/2-cubes.json`](https://github.com/polyfem/polyfem-data/blob/main/contact/examples/3D/unit-tests/2-cubes.json). It has two cube meshes positioned at different heights, a fixed boundary selection on the lower one, gravity as `rhs`, and a time-dependent solve. Its `common` file supplies shared contact settings; inspect that too.

Next look at [`contact/examples/3D/large-ratios/sphere-mat.json`](https://github.com/polyfem/polyfem-data/blob/main/contact/examples/3D/large-ratios/sphere-mat.json), where the sphere and the mat have **different volume IDs and different Neo-Hookean parameters**. The mat boundaries also move with expressions involving `t`.

**Read in order:** `geometry` (objects and transforms) → `volume_selection` (body/material IDs) → `surface_selection` (prescribed boundaries) → `materials` → `contact` and `time`. Run from the intact data tree; both scenes refer to external meshes and shared settings.

For friction, changing time steps, and codimensional obstacles, the [IPC Quick Start Guide](../tutorials/ipc_quick_start_guide/ipc_quick_start_guide.md) goes much deeper.

## 13. Mixed spaces and coupled physics

A scalar Laplace problem has one unknown; incompressible solids and fluids have **more than one field**. The JSON assigns **FE space IDs**, which are distinct from material-body IDs and boundary sideset IDs.

The [`standard/stokes_static.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/stokes_static.json) example uses velocity in space 0 and pressure in space 1:

```json
"materials": {
  "type": "Stokes",
  "viscosity": 100,
  "velocity_space_id": 0,
  "pressure_space_id": 1
},
"space": {
  "discr_order": [
    { "fe_space": 0, "order": 2 },
    { "fe_space": 1, "order": 1 }
  ]
}
```

Those are **Taylor–Hood-style P2/P1** choices for this example—not different materials, and not two different meshes. [`standard/incompressible.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/incompressible.json) uses analogous displacement/pressure space IDs for incompressible elasticity.

More advanced combinations are represented by:

- [`standard/thermoelastic_heated_clamped_bar.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/thermoelastic_heated_clamped_bar.json): separate displacement and temperature fields, each with its own boundary conditions or right-hand sides.
- [`standard/navier_stokes_transient.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/navier_stokes_transient.json): transient fluid flow with velocity and pressure.
- [`standard/navier_stokes_fsi_simple_square.json`](https://github.com/polyfem/polyfem-data/blob/main/standard/navier_stokes_fsi_simple_square.json): a coupled fluid–structure interaction setup with velocity, pressure, ALE mesh displacement, and solid displacement spaces. It also distinguishes **fluid and solid geometry IDs**.

**Try:** in the FSI file, find each `*_space_id`, then locate its matching entry under `space.discr_order`. Identify the `fe_space` used by each boundary condition. Do **not** attempt to turn a single-field elasticity input into FSI just by changing `materials.type`.

These coupled examples are a reading path first; run them only once the simpler configurations work and you are comfortable interpreting their mesh dependencies, convergence settings, and output.

## 14. Suggested practice sequence

Use real `polyfem-data` files as your starting point. For each exercise, make one copy, identify any `common` or `patch` parent, and keep the referenced mesh and resource files available.

| Exercise | Start from | One change to study |
| --- | --- | --- |
| A. Change resolution | [Plate with a hole](https://github.com/polyfem/polyfem-data/blob/main/standard/plate_hole.json) | Increase `space.discr_order`; compare approximation and cost |
| B. Change boundary labeling | [Alien plane selection](https://github.com/polyfem/polyfem-data/blob/main/selection/plane.json) | Compare with sphere or file selection; inspect affected sidesets |
| C. Change a material region | [Stretching cubes](https://github.com/polyfem/polyfem-data/blob/main/multi-material/stretch-cubes.json) | Change only middle-region `E` |
| D. Change time integration | [Euler](https://github.com/polyfem/polyfem-data/blob/main/time-int/euler.json) | Compare its inherited scene with [Newmark](https://github.com/polyfem/polyfem-data/blob/main/time-int/newmark.json) |
| E. Change FE basis | [Polygonal Mean Value](https://github.com/polyfem/polyfem-data/blob/main/standard/laplace_mv.json) | Compare with [Wachspress](https://github.com/polyfem/polyfem-data/blob/main/standard/laplace_ws.json) |
| F. Identify mixed fields | [Stokes](https://github.com/polyfem/polyfem-data/blob/main/standard/stokes_static.json) | Trace `velocity_space_id`, `pressure_space_id` and FE orders |

The goal is to explain **why** the result changed. If two cases also use different meshes, boundary conditions, or solver settings, they are not a controlled single-parameter comparison.

## 15. Where to go next

- **Time stepping and moving boundary conditions:** the [full Getting Started tutorial](../tutorials/getting_started.md#time-dependent-simulation) introduces `time.dt`, `time.tend`, and time-dependent expressions.
- **Contact and friction:** the [IPC Quick Start Guide](../tutorials/ipc_quick_start_guide/ipc_quick_start_guide.md) begins with two cubes falling onto a plane, then develops stiffness, collision, and time-step variations.
- **Several materials in one scene:** see the [Multi-Material tutorial](../tutorials/multi-material/multi-material.md).
- **Real-world test scenes:** explore the [polyfem-data repository](https://github.com/polyfem/polyfem-data). Its examples are useful as complete configurations, but some refer to meshes and shared JSON files elsewhere in that repository. **Keep their relative paths intact** when running them.

## Troubleshooting

**The app cannot start.** Check that the downloaded package matches your architecture (notably macOS ARM64 versus Intel). The GUI application is `polyfem_app`; `PolyFEM_bin` is the separate CLI executable.

**Cannot open `plate_hole.obj`.** Make sure the mesh was downloaded as a raw OBJ file (not an HTML web page) and lives alongside `run.json`. Run from that directory or use an absolute mesh path.

**The JSON cannot be parsed.** JSON requires commas between entries, double-quoted keys, and no trailing comma after the last property. If you made edits in Step 6, check the transition between the `materials`, `boundary_conditions`, and `solver` blocks.

**The app cannot load the JSON.** Check that `run.json` and the referenced `plate_hole.obj` are available together. The **Load JSON** button expects a JSON configuration, not a mesh file.

**The simulation ran but you cannot see the result.** Search the output directory for `result.vtu`, `elasticity.vtu`, or `stats.json`. Open the VTU file in ParaView and click **Apply**.

**The result doesn't look like the picture.** Check the chosen field and color scale. Elasticity results may need the **Warp By Vector** filter; the Laplacian example does not.
