# Your first PolyFEM simulation

This hands-on introduction starts with a complete, downloadable example, explains each part of the input, and then changes the physics and boundary conditions. You can **run PolyFEM without compiling it** if a suitable prebuilt package is available.

**What you will do:** open the PolyFEM desktop application, load a JSON simulation of a plate with a hole, run it using the **Run** button, inspect the output in ParaView, and then try linear elasticity.

![Plate with a hole and its solution](../img/plate_hole_solution.png)

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

    The command-line examples below use the **C++ executable**, not `polyfempy`. For Python examples, see the [Python guide](../python.md) and [Jupyter tutorial](../python_examples.ipynb).

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

\`\`\`json
"geometry": {
  "mesh": "plate_hole.obj"
}
\`\`\`

A scene with several bodies uses a list of geometries. For example, a sphere and a soft mat may each have their own mesh, transforms, and IDs:

\`\`\`json
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
\`\`\`

This is an **illustrative fragment**, not a complete runnable scene; the actual sphere/mat meshes, contact parameters, and boundary conditions are provided by the [tested sphere–mat example](https://github.com/polyfem/polyfem-data/blob/main/contact/examples/3D/large-ratios/sphere-mat.json).

The input specification lists \`.obj\`, \`.msh\`, \`.stl\`, \`.ply\`, and \`.mesh\` among the accepted mesh-file extensions. **The extension alone does not tell you whether a mesh contains volume cells.** For example, an OBJ containing only triangles is a surface, whereas a Gmsh MSH file can carry tetrahedra or other volume cells. For 3D elasticity you normally need a **volume mesh**, not just a surface shell.

### Geometry operations

Use \`transformation\` to place and resize objects **without modifying their mesh files**:

\`\`\`json
"geometry": {
  "mesh": "part.msh",
  "transformation": {
    "scale": [1, 2, 1],
    "translation": [0, 0.5, 0]
  }
}
\`\`\`

Rotations are also supported. Transforms matter because **geometric boundary selection is performed on the positioned geometry**: if you move or scale a body, absolute selection coordinates may need updating.

\`"advanced": { "normalize_mesh": true }\` rescales the mesh into a standard size. That is convenient for the first numerical example, but for physical simulation you should take care with **units and material parameters**. A mesh measured in millimeters is not interchangeable with one measured in meters if you keep the same physical stiffness, density, loads, and time scale.

!!! tip "Surface obstacles versus deformable bodies"
    A plane or triangulated surface can be used as a collision obstacle (\`"is_obstacle": true\`). It does not automatically become a 3D elastic body with interior degrees of freedom. See the [IPC tutorial](../tutorials/ipc_quick_start_guide/ipc_quick_start_guide.md#collision-obstacles) for surface, edge, and point obstacles.

## 8. Sidesets, body IDs, and boundary conditions

This is one of the most important ideas in PolyFEM.

A **boundary sideset** is a group of *boundary edges* in 2D or *boundary faces* in 3D, identified by an integer. A boundary condition refers to this **ID** rather than listing every edge or face individually. An ID is a **label**, not a coordinate, node number, or material property.

Similarly, a **volume ID** labels a region of elements (triangles/quads in 2D; tets/hexes in 3D). These are often called *body IDs* in examples and are used to assign material parameters.

| Concept | Which primitives are labeled? | Used for |
| --- | --- | --- |
| \`surface_selection\` | Boundary edges/faces | Dirichlet and Neumann conditions, boundary loads, prescribed motion |
| \`volume_selection\` | Interior elements | Material/body assignment and region-specific properties |

**IDs from one category do not automatically determine IDs in the other.** A body with volume ID 2 may have boundary sidesets 1, 3, and 7, and several bodies can reuse a material model with different volume IDs.

### Bounding-box sidesets in the plate example

For the plate-with-hole mesh, the tutorial uses:

\`\`\`json
"surface_selection": { "threshold": 1e-7 }
\`\`\`

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

\`\`\`json
"boundary_conditions": {
  "dirichlet_boundary": [
    { "id": 1, "value": [0, 0], "dimension": [true, false] },
    { "id": 4, "value": [0, 0], "dimension": [false, true] }
  ],
  "neumann_boundary": [
    { "id": 3, "value": [100, 0] }
  ]
}
\`\`\`

This constrains the **x displacement** on sideset 1, the **y displacement** on sideset 4, and applies an **x-directed traction** on sideset 3. The other components remain free where the mask is \`false\`.

In an elasticity problem:

- **Dirichlet** means prescribed **displacement**; zero is a fixed displacement, not zero stress.
- **Neumann** means prescribed **traction** on the selected surface; it is not the same thing as an applied force at one vertex.
- The **right-hand side** \`rhs\` describes a source or body load in the governing equations, not a sideset.
- Leaving a sideset without an explicit traction typically corresponds to a natural/free boundary for this class of problem.

### Two ways to assign IDs

There are two broad approaches, and you can mix them as needed.

**A. Use IDs stored in or supplied alongside the mesh.** This is preferable when your meshing pipeline already knows material regions or boundary tags.

\`\`\`json
"geometry": {
  "mesh": "tagged.msh",
  "surface_selection": "surface_tags.txt",
  "volume_selection": "volume_tags.txt"
}
\`\`\`

The \`.txt\` files need IDs in the order expected by PolyFEM for the corresponding mesh elements. These are **illustrative file names**; you must supply matching mesh and tag files. A mesh format may also carry its own region/body labels, in which case you can preserve them rather than generating new selections.

**B. Compute IDs from geometry.** This is convenient when you only have the mesh, or when you want to describe selections with coordinates.

For example, selecting a region near the minimum-x side of a unit-sized body:

\`\`\`json
"surface_selection": [
  {
    "id": 10,
    "box": [[0, 0, 0], [0.1, 1, 1]],
    "relative": true
  }
]
\`\`\`

The two corners of the box are in **relative bounding-box coordinates**, so this selects boundary faces whose barycenters lie in the first 10% of the body's x extent. The example is 3D; use two coordinates per corner in 2D. It does **not** change the mesh; it assigns a label.

Other geometric selectors supported by the current specification include:

| Selector | Useful for | Main JSON fields |
| --- | --- | --- |
| Box | A region inside an axis-aligned box | \`id\`, \`box\` |
| Sphere | A local region around a point | \`id\`, \`center\`, \`radius\` |
| Cylinder | A cylindrical region along an axis | \`id\`, \`p1\`, \`p2\`, \`radius\` |
| Plane / half-space | Everything on one side of a plane | \`id\`, \`point\`, \`normal\` |
| Axis-aligned half-space | A side such as x less than a given position | \`id\`, \`axis\`, \`position\` |

Selectors work using element or boundary-primitive **barycenters**, not precise intersections with the underlying continuous region. On a coarse mesh, the selected set may not match the exact geometric cut you imagined.

!!! note "Two independent choices"
    **What** you label: surface versus volume. **How** you label it: imported IDs versus geometric selection. These are independent; for instance, a body may load volume IDs from \`.msh\` but use geometric rules to choose the surface patch where you pull it.

For a detailed field-by-field explanation of all selection forms, use the [JSON input guide](../json.md#selections) and [generated specification](../json_defaults_and_spec.md). The old standalone **BC Setter** application is no longer part of the current workflow.

## 9. Materials: from one elastic solid to several regions

The \`materials\` section selects the PDE or constitutive law and its parameters. It is not just a palette or visualization label.

### Start with linear elasticity

\`\`\`json
"materials": {
  "type": "LinearElasticity",
  "E": 210000,
  "nu": 0.3
}
\`\`\`

Here \`E\` is **Young's modulus** (stiffness scale) and \`nu\` is **Poisson's ratio** (lateral contraction relative to stretching). For time-dependent mechanics, \`rho\` controls mass density. Physical values must use consistent units.

The \`LinearElasticity\` model assumes small strains. For larger deformations, use an appropriate nonlinear model instead:

\`\`\`json
"materials": {
  "type": "NeoHookean",
  "E": 1000000,
  "nu": 0.4,
  "rho": 1000
}
\`\`\`

This is a valid example of a **compressible Neo-Hookean** material entry. It does **not** alone define a full simulation: geometry, loads, constraints, and possibly time settings still matter.

### Which material family should I choose?

| Model | When to consider it |
| --- | --- |
| \`Laplacian\`, \`Helmholtz\` | Scalar PDEs / simple numerical examples |
| \`LinearElasticity\` | Small-displacement solids |
| \`SaintVenant\` | Geometrically nonlinear elasticity with a simple constitutive model |
| \`NeoHookean\` | Finite-deformation hyperelastic solids |
| \`MooneyRivlin\` and Ogden variants | More specialized hyperelastic models requiring their own parameters |
| \`HGOFiber\`, \`HGODispersion\`, \`ActiveFiber\` | Anisotropic or active-fiber material models |
| \`Stokes\`, \`NavierStokes\` | Incompressible fluid flow; mixed spaces and fluid parameters are required |
| \`NavierStokesFSI\` | Coupled fluid–structure interaction; **advanced**, with several coupled fields |
| \`ThermoElasticity\` | Coupled displacement and temperature fields |

This is a **guided subset**, not a list of interchangeable options. Each model has its own **required parameters** and mathematical assumptions. See [formulations](../details/formulations.md) and the [generated material specification](../json_defaults_and_spec.md) before switching a real application.

### Multiple materials: connect volume IDs to material IDs

A scene can contain several material regions:

\`\`\`json
"geometry": [
  { "mesh": "stiff_part.msh", "volume_selection": 1 },
  { "mesh": "soft_part.msh", "volume_selection": 2 }
],
"materials": [
  { "id": 1, "type": "NeoHookean", "E": 1e8, "nu": 0.4, "rho": 2000 },
  { "id": 2, "type": "NeoHookean", "E": 1e6, "nu": 0.4, "rho": 1000 }
]
\`\`\`

This is a **configuration fragment**, not a runnable scene: both meshes must exist and you need suitable boundary conditions. Notice the correspondence between \`volume_selection: 1\` and \`materials[0].id: 1\`, and similarly for ID 2.

**Try it:** on a multi-body model, change one material's \`E\` by a factor of 10 while keeping everything else fixed. Compare the displacement field and force response. If you want the complete, documented workflow (including mesh generation and assignment of region IDs), continue with [Simulating Multiple Materials in a Single Mesh](../tutorials/multi-material/multi-material.md).

## 10. Finite-element spaces: separate geometry, approximation, and physics

An FEM computation involves at least three choices:

1. **Mesh:** how the domain is split into elements (triangles, quads, tets, hexes, etc.).
2. **Approximation space:** the shape functions and number/location of degrees of freedom (for example, linear versus quadratic Lagrange).
3. **Physics/material:** which equations the degrees of freedom satisfy (for example, Laplacian versus elasticity).

The last two are **not the same thing**. You can solve the same elasticity model on the same mesh using different approximation orders, or solve different physics using the same FE space.

### Polynomial degree: P1 versus P2

The easiest experiment is to keep the input and change one field:

\`\`\`json
"space": {
  "discr_order": 1
}
\`\`\`

Then try:

\`\`\`json
"space": {
  "discr_order": 2
}
\`\`\`

The order controls the **finite-element approximation**, not the material law. Degree 1 generally means a piecewise-linear solution on simplicial elements; degree 2 adds additional degrees of freedom and can resolve more variation on the same mesh, at greater assembly/solve cost.

**Experiment:** solve the same plate-with-hole problem at orders 1 and 2. Compare the results *without changing the mesh or physics*. For a smooth solution, compare accuracy as well as runtime; it is misleading to conclude one choice is better solely from how smooth a ParaView image looks.

### Basis families

The current JSON specification exposes:

\`\`\`json
"space": {
  "discr_order": 2,
  "basis_type": "Lagrange"
}
\`\`\`

| Basis | Interpretation / restriction |
| --- | --- |
| \`Lagrange\` | Standard nodal finite-element basis; good default |
| \`Spline\` | Spline-based basis on supported quadrilateral/hexahedral discretizations |
| \`Serendipity\` | Reduced-DOF polynomial family on supported quadrilateral/hexahedral meshes |
| \`Bernstein\` | Bernstein basis option (check mesh/feature compatibility before using) |

For **polygonal** elements, PolyFEM has a separate \`poly_basis_type\` selector. Available names in the current specification include \`MFSHarmonic\`, \`MeanValue\`, and \`Wachspress\`. Those are specialized approximation constructions: they are not simply different names for P1.

The \`space.use_p_ref\` option allows geometry-dependent **a priori p-refinement**. It is a separate concept from simply increasing a global \`discr_order\`. For background, see the [technical formulations](../details/formulations.md) and PolyFEM's [Decoupling Simulation Accuracy from Mesh Quality work](https://github.com/polyfem/polyfem).

### Mixed formulations have multiple fields

Not every simulation has a single scalar or displacement vector as its unknown. For example, incompressible flow solves for both **velocity** and **pressure**. Fluid–structure interaction can also include solid displacement and ALE mesh displacement. In those cases, the input material and coupled problem configuration refer to **space IDs** for the different fields; using only a single \`discr_order\` is not a complete mixed formulation setup.

!!! warning "Don't guess a coupled setup"
    A working \`NavierStokesFSI\` example needs more than changing \`materials.type\`. It has required field-space IDs, geometry IDs, viscosity, and nested material choices. Start from a compatible **tested configuration** and consult the [generated JSON specification](../json_defaults_and_spec.md).

### Mesh order is not necessarily solution order

A curved/high-order geometric map describes **where the elements are in physical space**. The \`space.discr_order\` describes **how the unknown field is approximated**. PolyFEM supports separating these decisions in supported cases. Increasing the solution order does not automatically repair a poorly resolved geometric boundary; conversely, a curved mesh can represent geometry well without forcing the solution space to the same order.

## 11. Put it together: a small sequence of experiments

Once the initial plate example works, make one change at a time. This keeps failures attributable to one modeling decision.

| Experiment | Change | Observe |
| --- | --- | --- |
| A. Spatial approximation | \`space.discr_order\` from 1 to 2 | Solution accuracy, runtime, DOF count |
| B. Physics | Laplacian to linear elasticity (Section 6) | Scalar field versus displacement vector |
| C. Constraints | Change the Dirichlet dimension mask | Which displacement component is blocked |
| D. Loads | Change the Neumann traction magnitude | How displacement scales in linear elasticity |
| E. Materials | Change \`E\` or \`nu\` | Stiffness and deformation response |
| F. Mesh | Replace the plate mesh with a compatible 2D mesh | Which sidesets/selection rules still apply |

For experiment F, remember: **the boundary tags of the new mesh may differ**. A JSON file that ran successfully on one mesh may fail or produce an unintended problem on another because its selected sidesets no longer exist or cover the wrong boundary. Check the geometry and labels before assuming the solver is wrong.

## 12. Where to go next

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
