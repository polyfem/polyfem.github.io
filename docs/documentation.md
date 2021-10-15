Json files
----------

Complete example
```json
{
    "default_params": " ",          "Path to another JSON file containing default arguments on which to patch these arguments"
    "mesh": " ",                    "Mesh path (absolute or relative to JSON file)"
    "meshes": [{                    "Multi-mesh input"
        "mesh": " ",                "Mesh path (absolute or relative to JSON file)"
        "position": [0.0, 0.0, 0.0],
        "rotation": [0.0, 0.0, 0.0],
        "rotation_mode": "xyz",
        "scale": [1.0, 1.0, 1.0],
        "enabled": true,
        "body_id": 0,
        "boundary_id": 0
    }],
    "bc_tag": " ",                  "Path to the boundary tag file, each face/edge is associated with an unique number (you can use bc_setter for setting them in 3d)"
    "boundary_id_threshold": -1,    "Distance from bounding box for a face/edge to belong to boundary. Negative falls into defaul: in 2d is 1e-7, in 3d 1e-2"
    "normalize_mesh": true,         "Normalize mesh such that it fits in the [0,1] bounding box"

    "n_refs": 0,                    "Number of uniform refinement"
    "refinenemt_location": 0.5,     "Refiniement location of polyhedra"

    "scalar_formulation": "Laplacian",
    "tensor_formulation": "LinearElasticity",

    "project_to_psd": false,        "Project the local matrices to PSD in for non-linear materials"

    "has_collision": false,         "Enable collision detection"
    "dhat": 0.03,                   "Barrier activation distance, check IPC paper"

    "count_flipped_els": false,     "Count (or not) flipped elements"

    "iso_parametric": false,        "Force isoparametric elements"
    "discr_order": 1,               "Dicretization order, supports P1, P2, P3, P4, Q1, Q2"

    "pressure_discr_order": 1,      "Pressure dicrezation order, for mixed formulation"

    "output": "",                   "Output json path"

    "problem": "Franke",            "Problem to solve"
    "problem_params": {             "Problem specific parameters"
        "is_time_dependent": false  "Is the problem time dependent"
    },

    "n_boundary_samples": 6,        "number of boundary samples (Dirichelt) or quadrature points (Neumann)"
    "quadrature_order": 4,          "quadrature order"
    "BDF_order": 1,                 "Order of BDF for time integration problems"

    "export": {                     "Export options"
        "full_mat": "",             "Stiffnes matrix without boundary conditions"
        "iso_mesh": "",             "Isolines mesh"
        "nodes": "",                "FE nodes"
        "solution": "",             "Solution vector"
        "spectrum": false,          "Spectrum of the stiffness matrix"
        "stiffness_mat": "",        "Stiffmess matrix after setting boundary conditions"
        "vis_boundary_only": false, "Exports only the boundary of volumetric meshes"
        "paraview": "",             "Path for the vtu mesh"
        "wire_mesh": "",            "Wireframe of the mesh"
        "material_params": false,   "Exports lame parameters per tetrahedron",
        "body_ids": false           "Export body ids"
    },

    "use_spline": false,            "Use spline for quad/hex elements"
    "fit_nodes": false,             "Fit nodes for spline basis"

    "integral_constraints": 2,      "Number of constraints for polygonal basis 0, 1, or 2"
    "n_harmonic_samples": 10,       "Number of face/line samples for harmonic bases for polyhedra"

    "B": 3,                         "User provided parameter for pref tolerance"
    "use_p_ref": false,             "Enable prefinement for badly shaped simplices"
    "discr_order_max": 4,           "Maximum allowed dicrezation oder, used in p pref"
    "h1_formula": false,            "Use pref formula for h1 bound"

    "solver_type": "Pardiso",       "Library for linear solver"
    "precond_type": "Eigen::DiagonalPreconditioner",
    "solver_params": {},            "solver specific parameters"

    "nl_solver": "newton",          "Non linear solver"
    "line_search": "armijo",        "Line search for newton solver"
    "nl_solver_rhs_steps": 1,       "Number of incremental load steps"
    "save_solve_sequence": false,   "Save all incremental load steps"

    "params": {                     "Material parameter"
        "k": 1.0,                   "Constant in helmolz"

        "elasticity_tensor": {},    "Elasticity tensor, used in hooke and saint ventant"

        "E": 1.5,                   "Young modulus"
        "nu": 0.3,                  "Poisson's ratio"

        "lambda": 0.329670329,      "Lame parameter, E, nu have priority"
        "mu": 0.384615384,

        "density": 1
    },


    "t0": 0,                        "Start time for time dependent simulations"
    "tend": 1,                      "End time for time dependent simulations"
    "time_steps": 10,               "Number of time steps for time dependent simulations"
    "dt": 0.1,                      "Time step size for time dependent simulations (priority over time_steps)"
    "skip_frame": 1,                "Export every n frame"
    "time_integrator": "ImplicitEuler",
    "time_integrator_params": {},   "Time integrator specific parameters"

    "vismesh_rel_area": 1e-05       "Relative resolution of the output mesh"
}
```

### Optionals

* **scalar_formulation**: `Helmholtz`, `Laplacian`, `Bilaplacian` (mixed)
* **tensor_formulation**: `HookeLinearElasticity`, `LinearElasticity`, `NeoHookean`, `SaintVenant`, `IncompressibleLinearElasticity` (mixed), `Stokes` (mixed), `NavierStokes` (mixed)

* **problem**: `CompressionElasticExact`, `Cubic`, `DrivenCavity`, `Elastic`, `ElasticExact`, `ElasticZeroBC`, `Flow`, `Franke`, `GenericScalar`, `GenericTensor`, `Gravity`, `Kernel`, `Linear`, `LinearElasticExact`, `MinSurf`, `PointBasedTensor`, `Quadratic`, `QuadraticElasticExact`, `Sine`, `TestProblem`, `TimeDependentFlow`, `TimeDependentScalar`, `TorsionElastic`, `Zero_BC`


* **solver_type**: `AMGCL`, `Eigen::BiCGSTAB`, `Eigen::CholmodSupernodalLLT`, `Eigen::ConjugateGradient`, `Eigen::DGMRES`, `Eigen::GMRES`, `Eigen::LeastSquaresConjugateGradient`, `Eigen::MINRES`, `Eigen::PardisoLDLT`, `Eigen::PardisoLU`, `Eigen::SimplicialLDLT`, `Eigen::SparseLU`, `Eigen::UmfPackLU`, `Hypre`, `Pardiso`
* **nl_solver**: `lbfgs`, `newton`
* **line_search**: `armijo`, `armijo_alt`, `bisection`, `more_thuente`

* **time_integrator**: `ImplicitEuler`, `ImplicitNewmark`


Formulations
------------

List of possible formulations. The constants can be set in `params`. All formulations supports boundary conditions.

### Scalar

#### Laplacian
**Constants**: none<br/>
**Description**: solve for<br/>
$-\Delta u = f$

#### Bilaplacian (mixed)
**Constants**: none<br/>
**Description**: solve for<br/>
$-\Delta^2 u = f$


#### Helmholtz
**Constants**: $k$<br/>
**Description**: solve for<br/>
$-\Delta u - k^2 u = f$


### Tensor

#### LinearElasticity
**Constants**: `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for<br/>
$-\text{div}(\sigma[u]) = f \qquad \sigma[u] = 2 \mu  \epsilon[u]+ \lambda \text{tr}(\epsilon[u]) I \qquad \epsilon[u] = \frac 1 2 \left(\nabla u^T + \nabla u\right)$


#### HookeLinearElasticity
**Constants**:  `elasticity_tensor`, `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for<br/>
$-\text{div}(\sigma[u]) = f \qquad \sigma[u] = C :  \epsilon[u] \qquad \epsilon[u] = \frac 1 2 \left(\nabla u^T + \nabla u\right)$<br/>
where $C$ is the elasticity tensor

#### IncompressibleLinearElasticity (mixed)
**Constants**: `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for<br/>
$\begin{align}
-\text{div}(2\mu\epsilon[u] + p I) &= f\\
\text{div}(u) - \lambda^{-1}p &= 0
\end{align}$

#### SaintVenant
**Constants**: `elasticity_tensor`, `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for<br/>
$-\text{div}(\sigma[u]) = f \qquad \sigma[u] = C: \epsilon[u]  \qquad \epsilon[u] = \frac 1 2 \left(\nabla u^T \nabla u + \nabla u^T + \nabla u\right)$<br/>
where $C$ is the elasticity tensor


#### NeoHookean
**Constants**: `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for<br/>
$-\text{div}(\sigma[u]) = f \quad \sigma[u] = \mu (F[u] - F[u]^{-T}) + \lambda \ln(\det F[u]) F[u]^{-T} \quad F[u] = \nabla u + I$


#### Stokes (mixed)
**Constants**: `viscosity` $\nu$<br/>
**Description**: solve for<br/>
$\begin{align}
-\nu\Delta u + \nabla p &= f\\
-\text{div}(u) &= 0
\end{align}$


#### NavierStokes (mixed)
**Constants**: `viscosity` $\nu$<br/>
**Description**: solve for<br/>
$\begin{align}
u\cdot \nabla u -\nu\Delta u + \nabla p &= f\\
-\text{div}(u) &= 0
\end{align}$

Problems
--------
Each problem has a specific set of optional `problem_params` described here.

### CompressionElasticExact
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for<br/>
$\begin{align}
f_{2D}(x,y) &= -\begin{bmatrix}(y^3 + x^2 + xy)/20\\ (3x^4 + xy^2 + x)/20\end{bmatrix}\\
f_{3D}(x,y,z) &= -\begin{bmatrix}(xy + x^2 + y^3 + 6z)/14\\ (zx - z^3 + xy^2 + 3x^4)/14\\ (xyz + y^2z^2 - 2x)/14\end{bmatrix}
\end{align}$

### Cubic
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for<br/>
$f(x,y,z) = (2y-0.9)^4 + 0.1$

### DrivenCavity
**Has exact solution**: false<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for zero right-hand side, and 0.25 for boundary id 1<br/>

### Elastic
**Has exact solution**: false<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for zero right-hand side, -0.25 for boundary id 1/5, 0.25 for id 3/6<br/>

### ElasticExact
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for<br/>
$\begin{align}
f_{2D}(x,y) &= \begin{bmatrix}(y^3 + x^2 + xy)/50\\ (3x^4 + xy^2 + x)/50\end{bmatrix}\\
f_{3D}(x,y,z) &= \begin{bmatrix}(xy + x^2 + y^3 + 6z)/80\\ (xz - z^3 + xy^2 + 3x^4)/80\\ (xyz + y^2 z^2 - 2x)/80\end{bmatrix}
\end{align}$

### ElasticZeroBC
**Has exact solution**: false<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for [0, 0.5, 0] right-hand side and zero boundary condition<br/>

### Flow
**Has exact solution**: false<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for zero right-hand side, [0.25, 0, 0] for boundary id 1/3, [0, 0, 0] for 7<br/>

### Franke
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solves for the 2D and 3D Franke function


### GenericScalar
**Has exact solution**: false<br/>
**Time dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solves for generic tensor problem with zero rhs<br/>
**Options**:
```json
"rhs": 3                            "Rhs of the problem"
"dirichlet_boundary": [             "List of Dirichelt boundaries"
{
    "id": 1,                        "Boundary id"
    "value": 0                      "Boundary value"
},
{
    "id": 2,                        "Boundary id"
    "value": "sin(x)+y"             "Formulas are supported"
}],
"neumann_boundary": [               "List of Neumann boundaries"
{
    "id": 3,                        "Boundary id"
    "value": 1,                     "Boundary value"
},
{
    "id": 4,                        "Boundary id"
    "value": "x^2"                  "Formulas are supported"
}]
```

### GenericTensor
**Has exact solution**: false<br/>
**Time dependent**: false<br/>
**Form**: tesor<br/>
**Description**: solves for generic tensor problem with zero body forces<br/>
**Options**:
```json
"rhs": [1, 2, 3]                    "Rhs of the problem"
"dirichlet_boundary": [             "List of Dirichelt boundaries"
{
    "id": 1,                        "Boundary id"
    "value": [0, 0, 0],             "Boundary vector value"
    "dimension": [                  "Which dimension are Dirichelt"
            true,
            true,
            false                   "In this case z is free"
        ]
},
{
    "id": 2,                        "Boundary id"
    "value": ["sin(x)+y", "z^2", 0] "Formulas are supported"
}],
"neumann_boundary": [               "List of Neumann boundaries"
{
    "id": 3,                        "Boundary id"
    "value": [0, 0, 0]              "Boundary vector value"
},
{
    "id": 4,                        "Boundary id"
    "value": ["sin(z)+y", "z^2", 0] "Formulas are supported"
}]
```

### Gravity
**Has exact solution**: false<br/>
**Time dependent**: true<br/>
**Form**: tensor<br/>
**Description**: solves for 0.1 body force in y direction and zero for boundary 4

### Kernel
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: scalar/tensor<br/>
**Description**: solves the omogenous PDE with `n_kernels` kernels placed on the bounding box at `kernel_distance`<br/>
**Options**: `n_kernels` sets the number of kernels, `kernel_distance` sets the distance from the bounding box

### Linear
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for<br/>
f(x,y,z) = x

### LinearElasticExact
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for<br/>
$\begin{align}
f_{2D}(x,y) &= \begin{bmatrix}-(y + x)/50\\ -(3x + y)/50\end{bmatrix}\\
f_{3D}(x,y,z) &= \begin{bmatrix}-(y + x + z)/50\\ -(3x + y - z)/50\\ -(x + y - 2z)/50\end{bmatrix}\\
\end{align}$

### MinSurf
**Has exact solution**: false<br/>
**Time dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for -10 for rhs, and zero Dirichelt boundary condition

### PointBasedTensor
**Has exact solution**: false<br/>
**Time dependent**: false<br/>
**Form**: tesor<br/>
**Description**: solves for point-based boudary conditions<br/>
**Options**:
```json
"scaling": 1,               "Scaling factor"
"rhs": 0,                   "Right-hand side"
"translation": [0, 0, 0]    "Translation"
"boundary_ids": [           "List of Dirichelt boundaries"
{
    "id": 1,                "Boundary id"
    "value": [0, 0, 0]      "Boundary vector value"
},
{
    "id": 2,
    "value": {              "Rbf interpolated value"
        "function": "",     "Function file"
        "points": "",       "Points file"
        "rbf": "gaussian",  "Rbf kernel"
        "epsilon": 1.5,     "Rbf epsilon"
        "coordinate": 2,    "Coordinate to ignore"

        "dimension": [      "Which dimension are Dirichelt"
            true,
            true,
            false           "In this case z is free"
        ]
    }
},
{
    "id": 2,
    "value": {              "Rbf interpolated value"
        "function": "",     "Function file"
        "points": "",       "Points file"
        "triangles": "",    "Triangles file"
        "coordinate": 2,    "Coordinate to ignore"
    }
}]
```

### Quadratic
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for<br/>
$f(x,y,z) = x^2$

### QuadraticElasticExact
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for<br/>
$\begin{align}
f_{2D}(x,y) &= \begin{bmatrix} -(y^2 + x^2 + xy)/50\\ -(3x^2 + y)/50\end{bmatrix}\\
f_{3D}(x,y,z) &= \begin{bmatrix}-(y^2 + x^2 + xy + yz)/50\\ -(3x^2 + y + z^2)/50\\ -(xz + y^2 - 2z)/50\end{bmatrix}
\end{align}$

### Sine
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for<br/>
$\begin{align}
f(x,y) &= \sin(10x)\sin(10y)\\
f(x,y,z) &= \sin(10x)\sin(10y)\sin(10z)
\end{align}$

### TestProblem
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for extreme problem to test errors for high order discretizations

### TimeDependentFlow
**Has exact solution**: false<br/>
**Time dependent**: true<br/>
**Form**: tensor<br/>
**Description**: solve for zero right-hand side, [0.25, 0, 0] for boundary id 1/3, [0, 0, 0] for 7, and zero inital velocity<br/>

### TimeDependentScalar
**Has exact solution**: false<br/>
**Time dependent**: true<br/>
**Form**: scalar<br/>
**Description**: solve for one right-hand side, zero boundary condition, and zero time boundary<br/>

### TorsionElastic
**Has exact solution**: false<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for zero body forces, `fixed_boundary` fixed (zero displacement), `turning_boundary` rotating around `axis_coordiante` for `n_turns`<br/>
**Options**: `fixed_boundary` id of the fixed boundary, `turning_boundary` id of the moving boundary, `axis_coordiante` coordinate of the rotating axis, `n_turns` number of turns

### Zero_BC
**Has exact solution**: true<br/>
**Time dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for<br/>
$\begin{align}
f_{2D}(x,y) &= (1 - x)  x^2 y (1-y)^2\\
f_{3D}(x,y,z) &= (1 - x)  x^2 y (1-y)^2 z (1 - z)
\end{align}$

```json
{
    "position": [0.0, 0.0, 0.0],
    "rotation": [0.0, 0.0, 0.0],
    "rotation_mode": "xyz",
    "scale": [1.0, 1.0, 1.0],
    "enabled": true,
    "body_id": 0,
    "boundary_id": 0
}
```

Time Integrators
----------------

### Implicit Euler

**Constants**:<br>
**Description**: <br>
$\dot{u}^{t+1} = u^t + h \ddot{u}^{t+1}$ <br>
$u^{t+1} = u^t + h \dot{u}^{t+1}$ <br>
where $h$ is the time step size<br>
**Reference**: https://en.wikipedia.org/wiki/Backward_Euler_method

### Implicit Newmark

**Constants**: `beta`, `gamma`<br>
**Description**: <br>
$\dot{u}^{t+1} = \dot{u}^t + (1-\gamma)h\ddot{u}^t + \gamma h\ddot{u}^{t+1}$<br>
$u^{t+1} = u^t + h\dot{u}^t + \tfrac{h^2}{2}((1-2\beta)\ddot{u}^t + 2\beta\ddot{u}^{t+1})$ <br>
where $h$ is the time step size and by default $\gamma = 0.5$ and $\beta = 0.25$<br>
**Reference**: https://en.wikipedia.org/wiki/Newmark-beta_method

Solvers
-------

### Linear Solver

PolyFEM offers a number of linear solver options based on compilation options. For more information see [PolySolve](../solvers), a stand-alone linear solver wrapper library used by PolyFEM.

### Nonlinear Solver

To solve nonlinear formulations, PolyFEM offers two options: Newton's method and L-BFGS.

The settings for the solver are stored inside the field `"solver_params"`. General settings include:

* `"gradNorm"` (default: `1e-8`): convergence tolerance on the norm ($L^2$) of the gradient
* `"nl_iterations"` (default: `3000`): maximum number of iterations to spend solving
* `"useGradNorm"` (default: `true`): whether to use the gradient norm or update direction norm for convergence checks
    * When optimizing a function it is natural to check for a zero (up to tolerance) gradient as this signifies an extrema. However, we also implement the convergence criteria used by [Li et al. [2020]](https://ipc-sim.github.io/). Where instead of the gradient's norm the update direction's $L^\infty$-norm is used. This provides two benifits: (1) it expresses the convergence criteria in the units of the variable (e.g., distance for elasticity) which (2) avoids applying small updates that lead to marginal change in the variables. Note: this criteria has been well tested for nonlinear elasticity, but your milage may vary for other formulations.

#### Newton's Method

A standard Newton's method with line search. Optionally this method can be turned into a projected Newton's method by setting `"project_to_psd": true`.

#### L-BFGS

A quasi-Newton method, L-BFGS requires more iterations than the full Newton's method, but avoids expensive linear solves.

Reference: https://en.wikipedia.org/wiki/Limited-memory_BFGS<br>
Acknowledgments: The L-BFGS solver is implemented using the [LBFGS++](https://github.com/yixuan/LBFGSpp) library.

Meshes
------

### Mesh
The path to the mesh file (absolute or relative to JSON file).

### Position
The `"position"` field encodes the position of the mesh's origin (not the center of mass). This is equivalent to a translation of the mesh. This mush be an array of length $d$, the dimension of the scene.

### Rotation
The `"rotation"` field encodes a rotation around the mesh's origin (not the center of mass). The rotation can either be a single number or array of numbers depending on the `"rotation_mode"`.

The `"rotation_mode"` field indicates how the `"rotation"` is represented. The options are:

* `"axis_angle"`: The `"rotation"` must be an array of four numbers where the first number is the angle of rotation in degrees and the last three are the axis or rotation. The axis will be normalized.
* `"quaternion"`: The `"rotation"` must be an array of four numbers which represent a quaternion $w + xi + yj + zk$. The order of `"rotation"` is `[x, y, z, w]`. The quaternion will be normalized.
* `"rotation_vector"`: The `"rotation"` must be an array of four numbers whose magnitude is the angle of rotation in degrees and normalized version is the axis of rotation.
* `r"[xyz]+"`: Indicates the `"rotation"` is a series of Euler angle rotations. The `"rotation"` can be either a number or variable length array as long as the length matches the rotation mode string's length. The Euler rotations will be applied in the order of the string (from left to right).

The default `"rotation_mode"` is `"xyz"` which indicates a Euler angle rotation in the order `x`, `y`, and then `z`.

### Scale
The `"scale"` field encodes the scale of the mesh relative to its origin (not the center of mass). This can either be a single number for uniform scaling or an array of $d$ numbers for scaling in each axis.

### Enable
A boolean for enabling the body. By default, bodies are enabled.

### Body ID
The `"id"` of the `"body_params"` to use for the entire body.

### Boundary ID
The `"id"` of the boundary conditions (e.g., `"dirichlet_boundary"` or `"neumann_boundary"`) to use on the entirety the body's boundary.
