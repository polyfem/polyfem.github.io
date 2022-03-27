Each problem has a specific set of optional `problem_params` described here.

## Generic

### GenericScalar
* **Has exact solution**: false
* **Time-dependent**: false
* **Form**: scalar
* **Description**: solves for generic scalar problem with specified rhs
* **Options**:
```js
"rhs": 3                            // Rhs of the problem
"dirichlet_boundary": [             // List of Dirichlet boundaries
{
    "id": 1,                        // Boundary id
    "value": 0                      // Boundary value
},
{
    "id": 2,                        // Boundary id
    "value": "sin(x)+y"             // Formulas are supported
}],
"neumann_boundary": [               // List of Neumann boundaries
{
    "id": 3,                        // Boundary id
    "value": 1,                     // Boundary value
},
{
    "id": 4,                        // Boundary id
    "value": "x^2"                  // Formulas are supported
}]
```

### GenericTensor
**Has exact solution**: false<br/>
**Time-dependent**: false<br/>
**Form**: tesor<br/>
**Description**: solves for generic tensor problem with specified body forces<br/>
**Options**:
```js
"rhs": [1, 2, 3]                    // Rhs of the problem
"dirichlet_boundary": [             // List of Dirichelt boundaries
{
    "id": 1,                        // Boundary id
    "value": [0, 0, 0],             // Boundary vector value
    "dimension": [                  // Which dimension are Dirichelt
            true,
            true,
            false                   // In this case z is free
        ]
},
{
    "id": 2,                        // Boundary id
    "value": ["sin(x)+y", "z^2", 0] // Formulas are supported
}],
"neumann_boundary": [               // List of Neumann boundaries
{
    "id": 3,                        // Boundary id
    "value": [0, 0, 0]              // Boundary vector value
},
{
    "id": 4,                        // Boundary id
    "value": ["sin(z)+y", "z^2", 0] // Formulas are supported
}]
```

## Specific

### CompressionElasticExact
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for<br/>
$\begin{align}
f_{2D}(x,y) &= -\begin{bmatrix}(y^3 + x^2 + xy)/20\\ (3x^4 + xy^2 + x)/20\end{bmatrix}\\
f_{3D}(x,y,z) &= -\begin{bmatrix}(xy + x^2 + y^3 + 6z)/14\\ (zx - z^3 + xy^2 + 3x^4)/14\\ (xyz + y^2z^2 - 2x)/14\end{bmatrix}
\end{align}$

### Cubic
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for<br/>
$f(x,y,z) = (2y-0.9)^4 + 0.1$

### DrivenCavity
**Has exact solution**: false<br/>
**Time-dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for zero right-hand side, and 0.25 for boundary id 1<br/>

### Elastic
**Has exact solution**: false<br/>
**Time-dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for zero right-hand side, -0.25 for boundary id 1/5, 0.25 for id 3/6<br/>

### ElasticExact
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for<br/>
$\begin{align}
f_{2D}(x,y) &= \begin{bmatrix}(y^3 + x^2 + xy)/50\\ (3x^4 + xy^2 + x)/50\end{bmatrix}\\
f_{3D}(x,y,z) &= \begin{bmatrix}(xy + x^2 + y^3 + 6z)/80\\ (xz - z^3 + xy^2 + 3x^4)/80\\ (xyz + y^2 z^2 - 2x)/80\end{bmatrix}
\end{align}$

### ElasticZeroBC
**Has exact solution**: false<br/>
**Time-dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for [0, 0.5, 0] right-hand side and zero boundary condition<br/>

### Flow
**Has exact solution**: false<br/>
**Time-dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for zero right-hand side, [0.25, 0, 0] for boundary id 1/3, [0, 0, 0] for 7<br/>

### Franke
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solves for the 2D and 3D Franke function

### Gravity
**Has exact solution**: false<br/>
**Time-dependent**: true<br/>
**Form**: tensor<br/>
**Description**: solves for 0.1 body force in y direction and zero for boundary 4

### Kernel
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: scalar/tensor<br/>
**Description**: solves the omogenous PDE with `n_kernels` kernels placed on the bounding box at `kernel_distance`<br/>
**Options**: `n_kernels` sets the number of kernels, `kernel_distance` sets the distance from the bounding box

### Linear
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for<br/>
f(x,y,z) = x

### LinearElasticExact
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for<br/>
$\begin{align}
f_{2D}(x,y) &= \begin{bmatrix}-(y + x)/50\\ -(3x + y)/50\end{bmatrix}\\
f_{3D}(x,y,z) &= \begin{bmatrix}-(y + x + z)/50\\ -(3x + y - z)/50\\ -(x + y - 2z)/50\end{bmatrix}\\
\end{align}$

### MinSurf
**Has exact solution**: false<br/>
**Time-dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for -10 for rhs, and zero Dirichelt boundary condition

### PointBasedTensor
**Has exact solution**: false<br/>
**Time-dependent**: false<br/>
**Form**: tesor<br/>
**Description**: solves for point-based boudary conditions<br/>
**Options**:
```js
"scaling": 1,               // Scaling factor
"rhs": 0,                   // Right-hand side
"translation": [0, 0, 0]    // Translation
"boundary_ids": [           // List of Dirichelt boundaries
{
    "id": 1,                // Boundary id
    "value": [0, 0, 0]      // Boundary vector value
},
{
    "id": 2,
    "value": {              // Rbf interpolated value
        "function": "",     // Function file
        "points": "",       // Points file
        "rbf": "gaussian",  // Rbf kernel
        "epsilon": 1.5,     // Rbf epsilon
        "coordinate": 2,    // Coordinate to ignore

        "dimension": [      // Which dimension are Dirichlet
            true,
            true,
            false           // In this case z is free
        ]
    }
},
{
    "id": 2,
    "value": {              // Rbf interpolated value
        "function": "",     // Function file
        "points": "",       // Points file
        "triangles": "",    // Triangles file
        "coordinate": 2,    // Coordinate to ignore
    }
}]
```

### Quadratic
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for<br/>
$f(x,y,z) = x^2$

### QuadraticElasticExact
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for<br/>
$\begin{align}
f_{2D}(x,y) &= \begin{bmatrix} -(y^2 + x^2 + xy)/50\\ -(3x^2 + y)/50\end{bmatrix}\\
f_{3D}(x,y,z) &= \begin{bmatrix}-(y^2 + x^2 + xy + yz)/50\\ -(3x^2 + y + z^2)/50\\ -(xz + y^2 - 2z)/50\end{bmatrix}
\end{align}$

### Sine
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for<br/>
$\begin{align}
f(x,y) &= \sin(10x)\sin(10y)\\
f(x,y,z) &= \sin(10x)\sin(10y)\sin(10z)
\end{align}$

### TestProblem
**Has exact solution**: true<br/>
**Time-dependent**: false<br/>
**Form**: scalar<br/>
**Description**: solve for extreme problem to test errors for high order discretizations

### TimeDependentFlow
**Has exact solution**: false<br/>
**Time-dependent**: true<br/>
**Form**: tensor<br/>
**Description**: solve for zero right-hand side, [0.25, 0, 0] for boundary id 1/3, [0, 0, 0] for 7, and zero inital velocity<br/>

### TimeDependentScalar
**Has exact solution**: false<br/>
**Time-dependent**: true<br/>
**Form**: scalar<br/>
**Description**: solve for one right-hand side, zero boundary condition, and zero time boundary<br/>

### TorsionElastic
**Has exact solution**: false<br/>
**Time-dependent**: false<br/>
**Form**: tensor<br/>
**Description**: solve for zero body forces, `fixed_boundary` fixed (zero displacement), `turning_boundary` rotating around `axis_coordiante` for `n_turns`<br/>
**Options**: `fixed_boundary` id of the fixed boundary, `turning_boundary` id of the moving boundary, `axis_coordiante` coordinate of the rotating axis, `n_turns` number of turns

### Zero_BC
* **Has exact solution**: true
* **Time-dependent**: false
* **Form**: tensor
* **Description**: solve for<br>
<center>$\begin{align}
f_{2D}(x,y) &= (1 - x)  x^2 y (1-y)^2\\
f_{3D}(x,y,z) &= (1 - x)  x^2 y (1-y)^2 z (1 - z)
\end{align}$</center>