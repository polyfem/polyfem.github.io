JSON Files Structure
--------------------

```js
{
    "default_params": " ",  // Path to another JSON file containing default arguments on which to patch these arguments
    
    "mesh": " ",             // Mesh path (absolute or relative to JSON file)
    "meshes": [ ],           // Multi-mesh input (see meshes)
    "normalize_mesh": false, // Normalize mesh such that it fits in the [0,1] bounding box (default: true)
    
    // Formulation:
    "scalar_formulation": " ",
    // or
    "tensor_formulation": " ",

    // Material parameter
    "params": {
        "k": 1.0,                 // Constant in helmolz

        "elasticity_tensor": {},  // Elasticity tensor, used in hooke and saint ventant

        "E": 1.5,                 // Young modulus
        "nu": 0.3,                // Poisson's ratio

        "lambda": 0.329670329,    // Lamé's first parameter (E and nu have priority)
        "mu": 0.384615384,        // Lamé's second parameter (E and nu have priority)

        "density": 1
    },

    "problem": " ",                 // Problem to solve
    "problem_params": {             // Problem specific parameters
        "is_time_dependent": false  // Is the problem time-dependent
    },

    "has_collision": false,  // Enable collision detection

    "nl_solver": "newton",                // Nonlinear solver
    "solver_type": "Eigen::PardisoLDLT",  // Linear solvers
    "line_search": "backtracking",        // Line search for newton solver
    "solver_params": {},                  // solver specific parameters

    "t0": 0,           // Start time for time-dependent simulations
    "tend": 1,         // End time for time-dependent simulations
    "time_steps": 10,  // Number of time steps for time-dependent simulations
    "dt": 0.1,         // Time step size for time-dependent simulations (priority over time_steps)
    "time_integrator": "ImplicitEuler",
    "time_integrator_params": {},  // Time integrator specific parameters

    "output": "",                   // Output json path
    "save_time_sequence": true,     // Save a PVD time sequence
    "skip_frame": 1,                // Export every n frame
    "vismesh_rel_area": 1e-05       // Relative resolution of the output mesh
    "export": {                     // Export options
        "solution": "",             // Solution vector
        "vis_boundary_only": false, // Exports only the boundary of volumetric meshes
        "paraview": "",             // Path for the vtu mesh
        "wire_mesh": "",            // Wireframe of the mesh
        "material_params": false,   // Exports lame parameters per tetrahedron
        "body_ids": false,          // Export body ids
        "time_sequence": "sim.pvd"  // Name of output PVD time sequencee
    },
}
```

Formulations
------------

Options:<br/>

* **scalar_formulation**: `Helmholtz`, `Laplacian`, `Bilaplacian` (mixed)
* **tensor_formulation**: `HookeLinearElasticity`, `LinearElasticity`, `NeoHookean`, `SaintVenant`, `IncompressibleLinearElasticity` (mixed), `Stokes` (mixed), `NavierStokes` (mixed)

Formulation parameters can be set in `params`. All formulations support boundary conditions.

See [formulations](details/formulations.md) for more details.

Problems
--------

**Options:** `CompressionElasticExact`, `Cubic`, `DrivenCavity`, `Elastic`, `ElasticExact`, `ElasticZeroBC`, `Flow`, `Franke`, `GenericScalar`, `GenericTensor`, `Gravity`, `Kernel`, `Linear`, `LinearElasticExact`, `MinSurf`, `PointBasedTensor`, `Quadratic`, `QuadraticElasticExact`, `Sine`, `TestProblem`, `TimeDependentFlow`, `TimeDependentScalar`, `TorsionElastic`, `Zero_BC`

Each problem has a specific set of optional `problem_params` described here.

See [problems](details/problems.md) for more details.

Time Integrators
----------------

**Options**: `ImplicitEuler`, `ImplicitNewmark`, `BDF`

The parameters for the time integration are stored inside the `"time_integrator_params"` field.

See [time integrators](details/time_integrators.md) for more details.

Solvers
-------

### Linear Solver

PolyFEM offers several linear solver options based on compilation options. For more information, see [PolySolve](polysolve.md) a stand-alone linear solver wrapper library used by PolyFEM.

**Options:** `AMGCL`, `Eigen::BiCGSTAB`, `Eigen::CholmodSupernodalLLT`, `Eigen::ConjugateGradient`, `Eigen::DGMRES`, `Eigen::GMRES`, `Eigen::LeastSquaresConjugateGradient`, `Eigen::MINRES`, `Eigen::PardisoLDLT`, `Eigen::PardisoLU`, `Eigen::SimplicialLDLT`, `Eigen::SparseLU`, `Eigen::UmfPackLU`, `Hypre`, `Pardiso` 


### Nonlinear Solver

**Options:** `newton`, `lbfgs`

The settings for the solver are stored inside the field `"solver_params"`.

See [solvers](details/solvers.md) for more details.

### Line Search

**Options**: `backtracking`, `armijo`, `armijo_alt`, `more_thuente`

See [solvers](details/solvers.md) for more details.

Contact
-------

```js
"has_collision": false,           // Enable collision detection
"dhat": 0.03,                     // Barrier activation distance, check IPC paper
"mu": 0.0,                        // Coefficient of friction (0 disables friction)
"epsv": 1e-3,                     // Smoothing parameter for the transition between static and dynamic friction
"friction_iterations": 1,         // Friction lagging iterations (0 disables friction and < 0 indicates unlimited iterations)
"friction_convergence_tol": 1e-2, // Friction lagging convergence tolerance
"barrier_stiffness": "adaptive",

"solver_params": {
    "broad_phase_method": "hash_grid",
    "ccd_tolerance": 1e-6,
    "ccd_max_iterations": 1e6
},

"obstacles": [ ],                 // Collision obstacle input
```

See [contact](details/contact.md) for more details.

Meshes
------

```js
"meshes": [{                    // Multi-mesh input
    "mesh": " ",                // Mesh path (absolute or relative to JSON file)
    "position": [0.0, 0.0, 0.0],
    "rotation": [0.0, 0.0, 0.0],
    "rotation_mode": "xyz",
    "scale": [1.0, 1.0, 1.0],
    "enabled": true,
    "body_id": 0,
    "boundary_id": 0,
    "bc_tag": " "               // Path (absolute or relative to JSON file)
}],
```

### Mesh
The path to the mesh file (absolute or relative to JSON file).

### Position
The `"position"` field encodes the position of the mesh's origin (not the center of mass). This is equivalent to a translation of the mesh. This must be an array of length $d$, the dimension of the scene.

### Rotation
The `"rotation"` field encodes a rotation around the mesh's origin (not the center of mass). The rotation can either be a single number or array of numbers depending on the `"rotation_mode"`.

The `"rotation_mode"` field indicates how the `"rotation"` is represented. The options are:

* `"axis_angle"`: The `"rotation"` must be an array of four numbers where the first number is the angle of rotation in degrees and the last three are the axis of rotation. The axis will be normalized.
* `"quaternion"`: The `"rotation"` must be an array of four numbers which represent a quaternion $w + xi + yj + zk$. The order of `"rotation"` is `[x, y, z, w]`. The quaternion will be normalized.
* `"rotation_vector"`: The `"rotation"` must be an array of three numbers whose magnitude is the angle of rotation in degrees and normalized version is the axis of rotation.
* `r"[xyz]+"`: Indicates the `"rotation"` is a series of Euler angle rotations in degrees. The `"rotation"` can be either a number or variable-length array as long as the length matches the rotation mode string's length. The Euler rotations will be applied in the order of the string (from left to right).

The default `"rotation_mode"` is `"xyz"` which indicates an Euler angle rotation in the order `x`, `y`, and then `z`.

### Scale
The `"scale"` field encodes the scale of the mesh relative to its origin (not the center of mass). This can either be a single number for uniform scaling or an array of $d$ numbers for scaling in each axis.

### Dimensions
The `"dimensions"` field encodes the absolute size of the mesh's axis-aligned bounding box. This should be an array of $d$ numbers for the dimensions of each axis. This is equivalent to using a scale of `dimensions / initial_dimensions` where nonfinite values are replaced by `1`. If the `"dimensions"` field is present, the `"scale"` field is ignored.

### Enable
A boolean for enabling the body. By default, bodies are enabled.

### Body ID
The `"id"` of the `"body_params"` to use for the entire body.

### Boundary ID
The `"id"` of the boundary conditions (e.g., `"dirichlet_boundary"` or `"neumann_boundary"`) to use on the entirety the body's boundary.

### BC Tag File

!!! todo
    Describe `bc_tag` input.

Obstacles
---------

```js
"obstacles": [{                 // Collision obstacle input
    "mesh": " ",                // Mesh path (absolute or relative to JSON file)
    "position": [0.0, 0.0, 0.0],
    "rotation": [0.0, 0.0, 0.0],
    "rotation_mode": "xyz",
    "scale": [1.0, 1.0, 1.0],
    "enabled": true,
    "displacement": [0.0, 0.0, 0.0]
}],
```

Obstacles serve as a way of specifying non-simulated collision objects. The syntax of specifying an obstacle is similar to specifying a mesh in the [multi-mesh input](#meshes). The difference is obstacles do not have a `body_id` or `boundary_id` field, but they do have a `displacement` field.

### Mesh
The path to the mesh file (absolute or relative to JSON file). In addition to the standard volumetric meshes supported by simulated meshes, this can be a codimensional/surface mesh (i.e., points, edges, or triangles). Currently, codimensional points and edges are only supported using the OBJ file format. Codimensional points are specified as vertices that are not indexed by any elements. Codimensional edges are specified as OBJ [line elements](https://en.wikipedia.org/wiki/Wavefront_.obj_file#Line_elements).

### Displacement
Specifies the displacement field for the obstacle. This can either be a constant vector or an expression similar to [spatially varying](../tutorial/#spatially-varying-boundary-conditions) and [time-dependent](../tutorial/#time-dependent-boundary-conditions) boundary conditions.

Selections
----------

### Box

An axis-aligned box selection.

**Parameters:**

* `box`: a $2 \times n$ array where the first row is the minimum corner and the second row is the maximum corner
* `relative` (default: `false`): if the coordinates of `box` are relative to the mesh's rest bounding box

!!! example
    `{"box": [[0, 0, 0], [1, 0.1, 1]], "relative": true}` will select all points in the bottom 10% of the mesh (assuming the vertical direction if in the y-axis).

### Sphere

A sphere (or circle in 2D) selection.

**Parameters:**

* `center`: center of the sphere ($n$-length array)
* `radius`: radius of the sphere (float value)
* `relative` (default: `false`): if the `center` is relative to the mesh's rest bounding box and the radius is relative to the mesh's bounding box diagonal

!!! example
    `{"center": [0, 0, 0], "radius": 1}` will select points that are less than 1 unit from the origin.

### Axis-Plane

An axis-aligned plane selection. Everything on one side of the plane is selected.

**Parameters:**

* `axis`: axis aligned with the plane
    * Input can either be a string of format `r"[+-]?[xyzXYZ]"` or int matching the regular expression `[+-]?[123]` where the sign is the side of the plane to select and coordinate is the axis to align the plane with
* `position`: position of the plane along the axis (float value)
* `relative` (default: `false`): if the `position` is relative to the mesh's rest bounding box

!!! example
    `{"axis": "-X", "position": 1}` will select points with a x-coordinate less than 1.

### Plane

A plane selection. Everything on one side of the plane is selected.

**Parameters:**

* `normal`: normal of the plane ($n$-length array)
* `point`: point on the plane (has priority over `offset`) ($n$-length array)
    * (alternatively) `offset`: offset along the normal from the origin defining the point (float value)
* `relative` (default: `false`): if the `point` is relative to the mesh's rest bounding box (does not apply to the offset)

!!! example
    `{"normal": [1, 1, 0], "point": [0, 1, 0]}` will select points $x$ where $(x-p) \cdot n \ge 0$.

Output
------

```js
"output": "",                   // Output json path
"save_time_sequence": true,     // Save a PVD time sequence
"save_solve_sequence": false,   // Save all incremental load steps
"skip_frame": 1,                // Export every n frame
"vismesh_rel_area": 1e-05       // Relative resolution of the output mesh
"export": {
    "sol_at_node": -1,
    "high_order_mesh": true,
    "volume": true,
    "surface": false,
    "wireframe": false,
    "vis_mesh": "",
    "sol_on_grid": -1,
    "paraview": "",             // Path for the vtu mesh
    "vis_boundary_only": false, // Exports only the boundary of volumetric meshes
    "material_params": false,   // Exports lame parameters per tetrahedron
    "body_ids": false,          // Export body ids
    "contact_forces": false,
    "friction_forces": false,
    "velocity": false,
    "acceleration": false,
    "nodes": "",                // FE nodes
    "wire_mesh": "",            // Wireframe of the mesh
    "iso_mesh": "",             // Isolines mesh
    "spectrum": false,          // Spectrum of the stiffness matrix
    "solution": "",             // Solution vector
    "full_mat": "",             // Stiffnes matrix without boundary conditions
    "stiffness_mat": "",        // Stiffmess matrix after setting boundary conditions
    "solution_mat": "",
    "stress_mat": "",
    "u_path": "",
    "v_path": "",
    "a_path": "",
    "mises": "",
    "time_sequence": "sim.pvd"  // Name of output PVD time sequencee
}
```

Restart
-------

For time-dependent simulation, the state variables ($u$, $v = \dot{u}$, and $a = \ddot{u}$) are exported using the following parameters:

```js
"export": {
    "u_path": "<path/to/out_u.ext>",
    "v_path": "<path/to/out_v.ext>",
    "a_path": "<path/to/out_a.ext>"
}
```

The path can be either absolute or relative to the output directory. The format will depend on the file extension: `.txt` corresponds to ASCII and `.bin` corresponds to binary serialization. Other formats may be added in the future, but for now, other extensions will default to the ASCII format.

These files can then be used to initialize (or restart) the simulation from the saved state by specifying:

```js
"import": {
    "u_path": "<path/to/in_u.ext>",
    "v_path": "<path/to/in_v.ext>",
    "a_path": "<path/to/in_a.ext>"
}
```

!!! note
    When restarting the simulation it is necessary to also specify the `"t0": <start_time>` parameter for the starting time. Otherwise, it will assume a starting time of `0`.

Other Parameters
----------------

```js
{
    "bc_tag": " ",                  // Path to the boundary tag file, each face/edge is associated with an unique number (you can use bc_setter for setting them in 3d)
    "boundary_id_threshold": -1,    // Distance from bounding box for a face/edge to belong to boundary. Negative falls into defaul: in 2d is 1e-7, in 3d 1e-2
    "normalize_mesh": true,         // Normalize mesh such that it fits in the [0,1] bounding box

    "n_refs": 0,                    // Number of uniform refinement
    "refinenemt_location": 0.5,     // Refiniement location of polyhedra

    "project_to_psd": false,        // Project the local matrices to PSD in for non-linear materials

    "al_weight": 1e6,
    "max_al_weight": 1e11,

    "count_flipped_els": false,     // Count (or not) flipped elements

    "iso_parametric": false,        // Force isoparametric elements
    "discr_order": 1,               // Dicretization order, supports P1, P2, P3, P4, Q1, Q2

    "pressure_discr_order": 1,      // Pressure dicrezation order, for mixed formulation

    "n_boundary_samples": 6,        // number of boundary samples (Dirichelt) or quadrature points (Neumann)
    "quadrature_order": 4,          // quadrature order
    "BDF_order": 1,                 // Order of BDF for time integration problems

    "export": {                    // Export options
        "full_mat": "",            // Stiffnes matrix without boundary conditions
        "iso_mesh": "",            // Isolines mesh
        "nodes": "",               // FE nodes
        "spectrum": false,         // Spectrum of the stiffness matrix
        "stiffness_mat": "",       // Stiffmess matrix after setting boundary conditions
    },

    "use_spline": false,            // Use spline for quad/hex elements
    "fit_nodes": false,             // Fit nodes for spline basis

    "integral_constraints": 2,      // Number of constraints for polygonal basis 0, 1, or 2
    "n_harmonic_samples": 10,       // Number of face/line samples for harmonic bases for polyhedra

    "B": 3,                         // User provided parameter for pref tolerance
    "use_p_ref": false,             // Enable prefinement for badly shaped simplices
    "discr_order_max": 4,           // Maximum allowed dicrezation oder, used in p pref
    "h1_formula": false,            // Use pref formula for h1 bound

    "precond_type": "Eigen::DiagonalPreconditioner",

    "nl_solver_rhs_steps": 1,       // Number of incremental load steps
    "save_solve_sequence": false,   // Save all incremental load steps
}
```