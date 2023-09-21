JSON Files Structure
--------------------

`PolyFEM_bin` expects as input a JSON file containing the setup and parameters of the problem you wish to solve. A basic example of such a file is as follows:

```js
{
    "common": "", // path to another JSON file containing default arguments on which to patch these arguments

    "geometry": [{
        "mesh": "" // mesh path (absolute or relative to JSON file)
    }],

    "time": {                         // time-dependent problem
        "tend": 1,                    // end time
        "dt": 0.1,                    // time step size
        "time_steps": 10,             // (alternativly) number of time steps
        "integrator": "ImplicitEuler" // time integration method
    },

    "contact": {
        "enabled": true // enable contact handling
    },

    "solver": {
        "linear": {
            "solver": "Eigen::PardisoLDLT"
        },
        "nonlinear": {
            "line_search": {
                "method": "backtracking"
            },
            "solver": "newton"
        }
    },

    // Material parameter
    "materials": {
        "type": "NeoHookean", // material model
        "E": 1.5, // Young's modulus
        "nu": 0.3, // Poisson ratio
        "rho": 1 // density
    },

    "output": {
        "json": "sim.json",           // output statistics
        "paraview": {                 // output geometry as paraview VTU files
            "file_name": "sim.pvd",
            "options": {
                "material": true,     // save material properties
                "body_ids": true      // save body ids
            },
            "vismesh_rel_area": 1e-05 // relative area for upsampling the solution
        }
    }
}
```

Materials
---------

Options:<br/>

* **scalar_formulation**: `Helmholtz`, `Laplacian`, `Bilaplacian` (mixed)
* **tensor_formulation**: `HookeLinearElasticity`, `LinearElasticity`, `NeoHookean`, `SaintVenant`, `IncompressibleLinearElasticity` (mixed), `Stokes` (mixed), `NavierStokes` (mixed)

Each formulation has a set of material parameters that can be set alongside it in `materials`.

See [formulations](details/formulations.md) for more details.

<!-- Problems
--------

**Options:** `CompressionElasticExact`, `Cubic`, `DrivenCavity`, `Elastic`, `ElasticExact`, `ElasticZeroBC`, `Flow`, `Franke`, `GenericScalar`, `GenericTensor`, `Gravity`, `Kernel`, `Linear`, `LinearElasticExact`, `MinSurf`, `PointBasedTensor`, `Quadratic`, `QuadraticElasticExact`, `Sine`, `TestProblem`, `TimeDependentFlow`, `TimeDependentScalar`, `TorsionElastic`, `Zero_BC`

Each problem has a specific set of optional `problem_params` described here.

See [problems](details/problems.md) for more details. -->

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

See [solvers](details/solvers.md) for more details.

### Line Search

**Options**: `backtracking`, `armijo`, `armijo_alt`, `more_thuente`

See [solvers](details/solvers.md) for more details.

Contact
-------

```js
"contact": {
    "has_collision": false,           // Enable collision detection
    "dhat": 0.03,                     // Barrier activation distance, check IPC paper
    "mu": 0.0,                        // Coefficient of friction (0 disables friction)
    "epsv": 1e-3,                     // Smoothing parameter for the transition between static and dynamic friction
    "friction_iterations": 1,         // Friction lagging iterations (0 disables friction and < 0 indicates unlimited iterations)
    "friction_convergence_tol": 1e-2, // Friction lagging convergence tolerance
    "barrier_stiffness": "adaptive",
}

"solver": {
    "contact": {
        "broad_phase_method": "hash_grid",
        "ccd_tolerance": 1e-6,
        "ccd_max_iterations": 1e6
    }
},
```

See [contact](details/contact.md) for more details.

Geometry
--------

```js
"geometry": [{
    "mesh": " ", // Mesh path (absolute or relative to JSON file)
    "enabled": true,

    "transformation": {
        "scale": [1, 1, 1],
        "rotation": [0, 0, 0],
        "rotation_mode": "xyz",
        "translation": [0, 0, 0]
    },

    "surface_selection": [],
    "volume_selection": [],

    "is_obstacle": false
}],
```

### Mesh
The path to the mesh file (absolute or relative to JSON file).

### Enable
A boolean for enabling the body. By default, bodies are enabled.

### Transformation

A pre-transform is applied to the geometry at load. The order of the transformation is scale, rotate, then translate.

#### Scale
The `"scale"` field encodes a scaling of the mesh. This can either be a single number for uniform scaling or an array of $d$ numbers for scaling in each axis.

##### Dimensions
Alternatively, the `"dimensions"` field encodes the absolute size of the mesh's axis-aligned bounding box. This should be an array of $d$ numbers for the dimensions of each axis. This is equivalent to using a scale of `dimensions / initial_dimensions` where nonfinite values are replaced by `1`. If the `"dimensions"` field is present, the `"scale"` field is ignored.

#### Rotation
The `"rotation"` field encodes a rotation around the mesh's origin. The rotation can either be a single number or an array of numbers depending on the `"rotation_mode"`.

The `"rotation_mode"` field indicates how the `"rotation"` is represented. The options are:

* `"axis_angle"`: The `"rotation"` must be an array of four numbers where the first number is the angle of rotation in degrees and the last three are the axis of rotation. The axis will be normalized.
* `"quaternion"`: The `"rotation"` must be an array of four numbers which represent a quaternion $w + xi + yj + zk$. The order of `"rotation"` is `[x, y, z, w]`. The quaternion will be normalized.
* `"rotation_vector"`: The `"rotation"` must be an array of three numbers whose magnitude is the angle of rotation in degrees and the normalized version is the axis of rotation.
* `r"[xyz]+"`: Indicates the `"rotation"` is a series of Euler angle rotations in degrees. The `"rotation"` can be either a number or variable-length array as long as the length matches the rotation mode string's length. The Euler rotations will be applied in the order of the string (from left to right).

The default `"rotation_mode"` is `"xyz"` which indicates an Euler angle rotation in the order `x`, `y`, and then `z`.

#### Translation
The `"translation"` field encodes a translation of the mesh. This must be an array of length $d$, the dimension of the scene.

### Surface Selection

Either
* a single number for a selection ID to apply to all surfaces in the mesh,
* a file path containing one ID per surface element, or
* a single or list of selection objects used to assign a given `"id"` (see [selections](#selections)).

### Volume Selection

Same as surface selection, but for assigning IDs to the volume elements of the mesh.

### Obstacles

Obstacles serve as a way of specifying non-simulated collision objects.

#### Mesh

The path to the mesh file (absolute or relative to JSON file). In addition to the standard volumetric meshes supported by simulated meshes, this can be a codimensional/surface mesh (i.e., points, edges, or triangles). Currently, codimensional points and edges are only supported using the OBJ file format. Codimensional points are specified as vertices that are not indexed by any elements. Codimensional edges are specified as OBJ [line elements](https://en.wikipedia.org/wiki/Wavefront_.obj_file#Line_elements).

<!-- #### Displacement
Specifies the displacement field for the obstacle. This can either be a constant vector or an expression similar to [spatially varying](../tutorial/#spatially-varying-boundary-conditions) and [time-dependent](../tutorial/#time-dependent-boundary-conditions) boundary conditions. -->

#### Surface Selection

Must be a single number.

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

Restart
-------

For time-dependent simulation, the state variables ($u$, $v = \dot{u}$, and $a = \ddot{u}$) are exported using the following parameters:

```js
"output": {
    "data": {
        "state": "<path/to/state.hdf5>"
    }
}
```

The path can be either absolute or relative to the output directory. The state will be saved in [HDF5](https://en.wikipedia.org/wiki/Hierarchical_Data_Format) format containing the keys `u`, `v`, and `a` for the solution, velocity, and acceleration, respectively.

This file can then be used to initialize (or restart) the simulation from the saved state by specifying:

```js
"input": {
    "data": {
        "state": "<path/to/state.hdf5>"
    }
}
```

!!! note
    When restarting the simulation it is necessary to also specify the `"time": {"t0": <start_time>}` parameter for the starting time. Otherwise, it will assume a starting time of `0`.