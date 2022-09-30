# IPC Quick Start Guide

<div class="md-source-date"><small>Author: Zachary Ferguson</small></div>

This is a retelling of the original [IPC Quick Start Guide](https://github.com/ipc-sim/IPC/wiki) from the original IPC codebase.

## Setup

The first step is to clone and build PolyFEM (see [here](../../cxx_index.md) for instructions). This will create the `PolyFEM_bin` executable that we will use to run the examples. To run an example you can use the following command:

```bash
./PolyFEM_bin -j <path/to/example.json> -o <path/to/output/dir>
```

You can also use the `--help` flag to see all the available options.

<!-- We will assume all the example JSON files are in a directory `tutorial`. -->

All files used in this example can be found [here](input/).

### IPC Default Parameters

Since many of the default parameters in PolyFEM differ from those in the original IPC codebase, we provide a JSON file [`ipc-defaults.json`](input/ipc-defaults.json) which maps the default parameter values from IPC to their equivalent parameters in PolyFEM. This file is then included in all the example JSON files using `"common": "ipc-defaults.json"`.

!!! todo
    Describe what each of the default parameters controls.

## Hello World

Let us start with a "Hello World" example of two cubes falling onto a ground plane.

The input JSON for this scene can be found at [`2-cubes-falling.json`](input/2-cubes-falling.json). To run this example, use the following command:

```bash
./PolyFEM_bin -j 2-cubes-falling.json -o 2-cubes-falling
```

This will create a directory `2-cubes-falling` with the following files:

```
$ ls 2-cubes-falling
sim.pvd step_0.vtm step_0.vtu [...] step_200.vtm step_200.vtu
```

We can open the PVD file using [ParaView](https://www.paraview.org/) and play the animation to visualize the simulation:

<video autoplay loop muted playsinline controls>
<source src="../videos/2-cubes-falling.mp4" type="video/mp4">
</video>

---

Let’s take a look at the input JSON file [`2-cubes-falling.json`](input/2-cubes-falling.json):

```json
{% include "input/2-cubes-falling.json" %}
```

The config is simple:

* `"common"`: this includes the default IPC parameters from the `ipc-defaults.json` file.
* `"geometry"`: the geometry of the scene comprised of two cubes and a ground plane.
    * `"mesh"`: the path to the mesh file (a tetrahedral mesh `cube.msh` for the cubes and a triangular mesh `plane.obj` for the ground plane).
    * `"transformation"`: transform the input mesh before running the simulation.
        * `"translation"`: translate the first cube up by 3 units and the second cube up by 1 unit.
    * `"volume_selection"`: assigns an ID to the volume (uniformly) which we will use later.
    * `"is_obstacle"`: specify that the ground plane is a static obstacle.
        * Obstacles are non-simulated geometries with prescribed displacements (here default to zero).
* `"contact"`: parameters for the contact model
    * `"friction_coefficient"`: coefficient of friction for all contacts.

## Physical Materials and Time Steppers

Now let’s make some changes to the hello world script to make the simulation more interesting.

### Stiffer Material

The default material parameters in `ipc-default.json` are:

```json
"materials": {
    "type": "NeoHookean",
    "E": 1e5,
    "nu": 0.4,
    "rho": 1000
}
```

This corresponds to a NeoHookean material with Young’s modulus $E = 10^5~\text{Pa}$, Poisson’s ratio $\nu = 0.4$, and density $\rho = 1000~\frac{\text{kg}}{\text{m}^3}$.

We can change these parameters for all objects in the scene by changing Young's modulus to $10^6~\text{Pa}$:

```json
{% include "input/stiffer.json" %}
```

!!! note
    Notice that we changed the `"common"` parameter to point to the starting example `2-cubes-falling.json`. This means our changes in this file will be applied on top of the changes in the starting example (which also are applied on top of the default parameters in `ipc-defaults.json`).

This will make Young’s modulus 10x larger than the default while keeping density and Poisson’s ratio the same. Let’s see what we get:

<video autoplay loop muted playsinline controls>
<source src="../videos/stiffer.mp4" type="video/mp4">
</video>

Yes! The boxes are stiffer now.

### Multiple Materials

We can also set different materials for different objects:

```json
{% include "input/heavy-top.json" %}
```

We replace our single `"materials"` object with a list of objects with `"id"` keys. These IDs correspond to the `"volume_selection"` from earlier. In general, `"volume_selection"` allows us to select a subset of the mesh's elements and assign a volume ID to them. In this case, we assign a uniform ID to all elements in the cube mesh. With the first cube getting an ID of 1 and the second getting an ID of 2. We then use these volume IDs to assign different materials to each cube. The first cube gets a material that is 3× heavier and 1000× stiffer. While the second cube gets the original material.

<video autoplay loop muted playsinline controls>
<source src="../videos/heavy-top.mp4" type="video/mp4">
</video>

Here we rendered softer material with a lighter yellow color. As we see the top box is nearly rigid now and the bottom box deforms more. Even with this super stiff material PolyFEM stays robust and accurate.

### Simulation Time and Time Step Size

Following the default in IPC, we have been simulating the scene for 5 seconds with a time step size of 0.025s, generating 200 frames.

#### Smaller Time Step Sizes

One option to get more energetic animation (while sticking with implicit Euler stepping -- see also Newmark stepping below) is to apply smaller time step sizes to reduce the numerical damping of implicit Euler time integration:

```json
{% include "input/smaller-dt.json" %}
```

The `"time"` parameter here controls time step size `"dt": 0.005`, which results in a more energetic animation:

<video autoplay loop muted playsinline controls>
<source src="../videos/smaller-dt.mp4" type="video/mp4">
</video>

#### Larger Time Step Sizes (Nearly Quasi-Static)

One of the exciting features of IPC and PolyFEM is that it is robust enough to support extremely large time step sizes on the order of seconds with implicit Euler. In turn, this enables rapid solutions of equilibrium conditions subject to contact, friction and large deformation (via nearly quasi-static solves under numerical damping). For a simple demonstration, we can simulate our hello world example with $\Delta t = 1~\text{s}$:

```json
{% include "input/larger-dt.json" %}
```

The animation now is composed of only 5 frames, 1 for each second. As we see numerical damping is so large that the cubes are barely bouncing.

<video autoplay loop muted playsinline controls>
<source src="../videos/larger-dt.mp4" type="video/mp4">
</video>

## Initial Velocity

To set nonzero initial velocities for objects, we need to specify them as `"initial_consitions"`.

### Initial Linear Velocity

For example, we can set the initial velocity of the top cube to be $-20~\frac{\text{m}}{\text{s}}$ in the negative y direction:

```json
{% include "input/initial-linear-velocity.json" %}
```

Again here we are using the volume IDs to select the top cube.

<video autoplay loop muted playsinline controls>
<source src="../videos/initial-linear-velocity.mp4" type="video/mp4">
</video>

Even for this high-speed impact scene, PolyFEM stays robust and accurate without numerical instabilities or explosions.

### Initial Angular Velocity

Instead of using a constant value for the initial velocity, we can use a tiny expression dependent on the positions.

We can specify an initial angular velocity by computing

$$
\begin{bmatrix}\omega_x & \omega_y & \omega_z\end{bmatrix}
\times
\begin{bmatrix}x & y & z\end{bmatrix}
$$

where $\omega_{\{x, y, z\}}$ are the angular velocity in radians and $x$, $y$, and $z$ are the positions to be evaluated at.

!!! note
    This assumes the center of rotation is at the origin. If you want to rotate around a different point, you need to translate the positions to the origin first.

For example, if we want to rotate the top cube 90 degrees/second around the y-axis, then we compute the initial velocity as

$$
\begin{bmatrix}0 & \frac{\pi}{2} & 0\end{bmatrix}
\times
\begin{bmatrix}x & y & z\end{bmatrix}
=
\begin{bmatrix}\frac{\pi}{2}z & 0 & -\frac{\pi}{2}x\end{bmatrix}
$$

In the JSON we encode this as a string containing the expression:

```json
{% include "input/initial-angular-velocity.json" %}
```

and voila now the top cube is spinning!

<video autoplay loop muted playsinline controls>
<source src="../videos/initial-angular-velocity.mp4" type="video/mp4">
</video>

## Collision Obstacles

In many simulations we want to script the motion of certain objects, the best way to do this is to specify the object as an obstacle and then specify the prescribed displacement.

### Translation

To make the second code an obstacle all we need to do is set `"is_obstacle": true`.
Then we can specify the displacement of this obstacle using the `"boundary_conditions/obstacle_displacements"` field:

```json
{% include "input/translating-obstacle.json" %}
```

Notice that we changed the `"volume_selection"` to `"surface_selection"` because we need to identify the surface on which the boundary conditions apply.

We set the obstacle's displacement to `["t", "t", "t"]` which means the obstacle will translate with a velocity of $[1, 1, 1]$ m/s.

<video autoplay loop muted playsinline controls>
<source src="../videos/translating-obstacle.mp4" type="video/mp4">
</video>

### Rotation

Making the second cube rotate is a bit trickier. We can compute the displacement in Euler’s angle representation as

$$
\begin{bmatrix}
\Delta{x} \\ \Delta{y} \\ \Delta{z}
\end{bmatrix}
=
R_x(\omega_x t) R_y(\omega_y t) R_z(\omega_z t)
\left(
\begin{bmatrix}
x \\ y \\ z
\end{bmatrix}
-
\begin{bmatrix}
c_x \\ c_y \\ c_z
\end{bmatrix}
\right)
+
\begin{bmatrix}
c_x \\ c_y \\ c_z
\end{bmatrix}
-
\begin{bmatrix}
x \\ y \\ z
\end{bmatrix}
$$

where $\Delta\{x,y,z\}$ are the obstacle displacement, $\omega_{\{x,y,z\}}$ are the angular velocities, $c_{\{x,y,z\}}$ is the center of rotation, $R_{\{x,y,z\}}$ are the axis-aligned rotation matrices, and $x$, $y$, and $z$ are the positions to be evaluated at. Computing this by hand can be annoying, so instead, you can use [this Python notebook](rotating-obstacle.ipynb) to compute the expression.

As an example, here we kinematically rotate the second cube with an angular velocity of $[10, 90, 0]$ degrees/second:

```json
{% include "input/rotating-obstacle.json" %}
```

<video autoplay loop muted playsinline controls>
<source src="../videos/rotating-obstacle.mp4" type="video/mp4">
</video>

Here we render obstacles in grey.

### Codimensional Collisions

IPC contact handling is based on distances and so directly supports codimensional (surfaces, edges, points) kinematic collision obstacles!

!!! note
    Currently, PolyFEM does not yet include simulated codimensional materials like shells or rods.

#### Closed Surface

If we script the motion of an object, then for a closed surface the interior tessellation is unnecessary, and we can directly use a surface mesh (`.obj` file)!

```json
{% include "input/rotating-obstacle-surface.json" %}
```

This is equivalent to using a volumetric mesh because PolyFEM automatically extracts and uses the surface for obstacles.

<video autoplay loop muted playsinline controls>
<source src="../videos/rotating-obstacle-surface.mp4" type="video/mp4">
</video>

#### Open Surface

This script replaces the cube with a single triangle (zero volume):

```json
{% include "input/rotating-obstacle-triangle.json" %}
```

<video autoplay loop muted playsinline controls>
<source src="../videos/rotating-obstacle-triangle.mp4" type="video/mp4">
</video>

#### Edges

This script uses the same single triangle but only with its edges. Here we also scale the triangle 2× larger to let the box fall through.

```json
{% include "input/rotating-obstacle-edges.json" %}
```

The `"extract": "edges"` specifies that only the edges of the triangle mesh should be used.

<video autoplay loop muted playsinline controls>
<source src="../videos/rotating-obstacle-edges.mp4" type="video/mp4">
</video>

!!! note
    Alternativly, you can load an edge mesh directly by specifying an `.obj` file with line elements. For example, this is the same edge mesh in OBJ format:
    ```
    v -0.5 0 -0.5
    v  0.5 0 -0.5
    v -0.5 0  0.5
    l 1 3
    l 3 2
    l 2 1
    ```

#### Points

Even crazier, this script uses the same single triangle but only with its points. Here we also scale the point cloud 0.7× smaller to let the box hit the points.

```json
{% include "input/rotating-obstacle-points.json" %}
```

We use the `"extract": "points"` to only use the points of the triangle.

<video autoplay loop muted playsinline controls>
<source src="../videos/rotating-obstacle-points.mp4" type="video/mp4">
</video>

!!! note
    Alternativly, you can load a point cloud directly by specifying an `.obj` file with no triangles or edges. For example, this is the same point cloud in OBJ format:
    ```
    v -0.5 0 -0.5
    v  0.5 0 -0.5
    v -0.5 0  0.5
    ```

## Boundary Conditions

### Dirichlet

For a simulated volumetric object, sometimes we script the motion of part of its vertices as Dirichlet boundary conditions. This can be simply realized by adding `DBC` commands to the end of each shape line just like how we assign object materials individually:

```diff
shapes input 2
input/tetMeshes/cube.msh 0 3 0  0 0 0  1 1 1
- input/tetMeshes/cube.msh 0 1 0  0 0 0  1 1 1
+ input/tetMeshes/cube.msh 0 1 0  0 0 0  1 1 1  DBC -0.1 -0.1 -0.1  0.1 1.1 0.1  -0.2 0 -0.2  0 0 0  DBC 0.9 -0.1 0.9  1.1 1.1 1.1  0.2 0 0.2  0 0 0

selfFric 0.1

ground 0.1 0
```

One can append as many `DBC` commands as needed after each shape line. Each `DBC` command is followed by 12 floating-point numbers, the first 6 form the relative bounding box coordinates of the bottom-left and top-right corner of the selection cuboid, and the last 6 forms the linear velocity followed by angular velocity represented as Euler angles in degree.
For example, the above script first selects all vertices in the left-back and moves them with (`-0.2`, `0`, `-0.2`) m/s, and then it selects the right-front vertices and moves them with (`0.2`, `0`, `0.2`) m/s:

![MDBC](https://raw.githubusercontent.com/ipc-sim/IPC/master/wiki/img/MDBC.gif)

As we see PolyFEM is robust even when there is large deformation.

What is different here from setting kinematic collision objects is that the unselected vertices are still degree-of-freedoms that are simulated. If one selects all vertices of an object by putting the selection box at e.g. (-0.1, -0.1, -0.1) - (1.1, 1.1, 1.1), and sets them with Dirichlet boundary conditions, it will be essentially identical to a kinematic collision object in IPC.

### Neumann

We can also add extra constant body forces to part of the vertices of simulated volumetric objects in addition to gravity. This can be similarly realized by adding `NBC` commands to the end of each shape line just like how we did for Dirichlet boundary conditions above: (`input/tutorialExamples/BC/2cubesFall_NBC.txt`)

```diff
shapes input 2
input/tetMeshes/cube.msh 0 3 0  0 0 0  1 1 1
- input/tetMeshes/cube.msh 0 1 0  0 0 0  1 1 1
+ input/tetMeshes/cube.msh 0 1 0  0 0 0  1 1 1  NBC -0.1 -0.1 -0.1  0.1 1.1 0.1  -50 0 -50  NBC 0.9 -0.1 0.9  1.1 1.1 1.1  50 0 50

selfFric 0.1

ground 0.1 0
```

One can append as many `NBC` commands as needed after each shape line. Each `NBC` command is followed by 9 floating-point numbers, the first 6 form the relative bounding box coordinates of the bottom-left and top-right corner of the selection cuboid, and the last 3 form the linear acceleration in the unit of m/s^2. Here torque is not supported as it is node position-dependent and so more complicated, which is also not usually used as Neumann boundary conditions.
Similar to the configuration in our Dirichlet example, the above script first selects all vertices in the left-back and drags them with an extra acceleration of (`-50`, `0`, `-50`) m/s^2, and then it selects the right-front vertices and moves them with an extra acceleration of (`50`, `0`, `50`) m/s^2:

![NBC](https://raw.githubusercontent.com/ipc-sim/IPC/master/wiki/img/NBC.gif)

Unlike Dirichlet boundary conditions, here the Neumann boundary condition does not directly affect the vertical motion of the object, and it elongates the object only to a static state but not further.

### Timed Boundary Conditions
It is also possible to start and stop boundary conditions at a specific time. This can be done by appending the `DBC` or `NBC` commands with a number for the start and end time: (`input/tutorialExamples/BC/2cubesFall_DBC_timeRange.txt`)
```diff
shapes input 2
input/tetMeshes/cube.msh 0 3 0  0 0 0  1 1 1
input/tetMeshes/cube.msh 0 1 0  0 0 0  1 1 1 \
-    DBC -0.1 -0.1 -0.1  0.1 1.1 0.1  -0.2 0.0 -0.2  0 0 0 \
-    DBC  0.9 -0.1  0.9  1.1 1.1 1.1   0.2 0.0  0.2  0 0 0
+    DBC -0.1 -0.1 -0.1  0.1 1.1 0.1  -0.2 0.0 -0.2  0 0 0  0.0 2.5 \
+    DBC -0.1 -0.1 -0.1  0.1 1.1 0.1   0.0 0.0  0.0  0 0 0  2.5     \
+    DBC  0.9 -0.1  0.9  1.1 1.1 1.1   0.0 0.0  0.0  0 0 0  0.0 2.5 \
+    DBC  0.9 -0.1  0.9  1.1 1.1 1.1   0.2 0.0  0.2  0 0 0  2.5

selfFric 0.1

ground 0.1 0
```
After the required parameters to the `DBC` or `NBC` command, the next numbers are when to start the BC and when to end the BC. By default, the BC is applied from time t=0 to infinity. The end time can be omitted and will default to infinity:

<img src=https://raw.githubusercontent.com/ipc-sim/IPC/master/wiki/img/BCTimeRange.gif width="768px">

## Advanced Settings

### Input Mesh Sequence
The ways of setting kinematic collision object motion described earlier so far support just simple translations or rotations. To support more complex scripting of kinematic collision objects, IPC allows use of input mesh file sequences.

For example, we can specify a folder path to the kinematic collision objects: (`input/tutorialExamples/advanced/2cubesFall_rotateCO_meshSeq.txt`)
```diff
shapes input 2
input/tetMeshes/cube.msh 0 3 0  0 0 0  1 1 1
- input/triMeshes/triangle.seg 0 1 0  0 0 0  2 2 2  angularVelocity 10 90 0
+ input/triMeshes/triangle.seg 0 1 0  0 0 0  2 2 2  meshSeq input/segMeshes/sequence

selfFric 0.1

ground 0.1 0

zoom 0.3
```
In the specified folder `input/segMeshes/sequence` we provide the mesh files (here .seg, or .obj that can be automatically transformed by IPC) of the triangle wire in each frame as n.seg or n.obj, where n is the number of the frame. Here we simply use the mesh output of our triangle wire kinematic collision object simulation, and we are able to reproduce that simulation by loading the triangle wire mesh sequence files! Note that the input sequence must maintain the correct vertex correspondence to the one specified in the `shapes` block.

### Attaching Configuration Initialization
To initialize "attached" configurations, IPC requires a tiny positive gap as it does not support the 0-distance configurations.

The following script sets the upper box in the hello world example right above the lower one: (`input/tutorialExamples/advanced/2cubesFall_attach.txt`)
```diff
shapes input 2
- input/tetMeshes/cube.msh 0 3 0  0 0 0  1 1 1
+ input/tetMeshes/cube.msh 0 2.001 0  0 0 0  1 1 1
input/tetMeshes/cube.msh 0 1 0  0 0 0  1 1 1

selfFric 0.1

ground 0.1 0
```

![attach](https://raw.githubusercontent.com/ipc-sim/IPC/master/wiki/img/attach.gif)

Note the initial gap here is barely visible. In our experience we can set IPC’s contact gap as small as practically needed; i.e., even small enough to fool the ray intersection checks in rendering algorithms. Thus rendering of transparent objects with IPC's small gaps can even have artifacts for valid non-intersecting configurations of the contact surfaces (so, for example, to render the IPC “squeeze out” example, we manually set offsets in the renderer despite having physically correct non-intersecting shapes). Similarly, no two objects can have 0-distance separation : ); even atoms are at distance from each other.

### Newmark Time-Integration
Along with implicit Euler, IPC currently supports implicit Newmark time integration. Other time integrators will be added soon. Implicit Newmark can be applied for improved energy preservation and control. To change the time integrator we can simply set the time integration method.

For example, the following script uses `timeIntegration` keyword to set Newmark (`NM`) to be the time integrator for the stiffer boxes scene without friction. By default, `timeIntegration` is set to `BE` (backward Euler). `input/tutorialExamples/advanced/2cubesFall_NM.txt`:
```diff
shapes input 2
input/tetMeshes/cube.msh 0 3 0  0 0 0  1 1 1
input/tetMeshes/cube.msh 0 1 0  0 0 0  1 1 1

ground 0 0

stiffness 1e6 0.4

time 5 0.005

+ timeIntegration NM
+ dampingRatio 0.1
```
Here we also enable lagged Rayleigh damping using `dampingRatio`. Damping can be useful both for predictive or realistic simulation control of damping and also to extend the effective stability of the underlying Newmark time integration method. The number (say x) followed by `dampingRatio` is a relative parameter for the damping stiffness. The absolute damping stiffness will be set to 0.75 x dt^3, where if x=1, the beginning of time step Newmark incremental potential Hessian (with damping term) will be equal to that of implicit Euler. This provides a starting basis for intuitively setting damping stiffness. To alternately directly set damping stiffness use the keyword `dampingStiff`.
Here in this demo note that we used a smaller time step size at `0.005`s as this is better for the stability of Newmark integration.
<table>
    <tr>
        <th>Newmark, dampingRatio 0.1</th>
        <th>Newmark, dampingRatio 0.2</th>
    </tr>
    <tr>
        <td><img src="https://raw.githubusercontent.com/ipc-sim/IPC/master/wiki/img/NM0.1.gif"/></td>
        <td><img src="https://raw.githubusercontent.com/ipc-sim/IPC/master/wiki/img/NM0.2.gif"/></td>
    </tr>
    <tr>
        <th>Newmark, dampingRatio 0.4</th>
        <th>Backward Euler</th>
    </tr>
    <tr>
        <td><img src="https://raw.githubusercontent.com/ipc-sim/IPC/master/wiki/img/NM0.4.gif"/></td>
        <td><img src="https://raw.githubusercontent.com/ipc-sim/IPC/master/wiki/img/BE.gif"/></td>
    </tr>
</table>

### Accuracy Control

#### Time Integration Accuracy
Time integration accuracy determines how accurate the dynamic time step solve is satisfied. To set the requested time integration accuracy, we can use the `tol` keyword to set Newton tolerance on the infinity norm of the Newton increment in the velocity unit (scaled with bounding box size).

By default, IPC uses
```
tol 1
1e-2
```
where the number following `tol` is the number of tolerances provided, here we provide `1` tolerance which is `1e-2`. This will be set to all time-steps where, with a bounding box diagonal length l, the solver will stop once the current Newton increment cannot change any nodal velocity larger than 1e-2l m/s even if a full step is taken.

For experimentation, if multiple tolerances are provided, IPC will apply them in sequence to different time steps. When the time step number exceeds the number of tolerances provided, IPC will use the last provided tolerance for those frames.

In our experiments, `1e-2` is a relatively large tolerance that consistently provides visually good results without artifacts like early stopping or jittering. We’ve also tested IPC convergence to time-integration accuracies down to `1e-6`. These enable improved accuracy for specific applications, but note that compute costs can then likewise also be more expensive.

#### Contact Accuracy
There are 3 additional accuracies for IPC. Each controls a contact accuracy in IPC: the distance (`dHat`) that IPC sees objects as touching/attaching to exert contact forces; the relative tangent velocity (`epsv`) determining where IPC sees the touching objects as not sliding and so exerts static friction forces; and the maximum amount of friction iterations (`fricIterAmt`) that IPC updates friction tangent and normal forces.

By default IPC uses
```
dHat 1e-3

epsv 1e-3
fricIterAmt 1
```
Similar to Newton tolerance above, `dHat` and `epsv` are both scaled on bounding box size l, which means by default when objects are at a distance smaller than `1e-3`l m there exists contact forces, and 2 attached objects with smaller than `1e-3`l m/s relative tangent velocity will have static friction forces.

The default setting provides a good trade-off between accuracy and efficiency, where there are no visible gaps, no obvious sliding artifacts, or friction force in inaccurate directions. The roller examples and hitting card house examples are all running with this default setting. We’ve tested `dHat` down to `5e-8` (Masonry arch example), `epsv` down to `1e-5` (stable card house example), and fricIterAmt set to 0 (until tangent operator and normal force converges) to obtain even more accurate results. Note that IPC does not guarantee convergence for `fricIterAmt 0`, in practice for more accurate friction in large deformation or high-speed impact scenes, `fricIterAmt` at `2`~`4` so far appears generally sufficient.

### Use Your Own Mesh
For codimensional collision objects (including closed surfaces), one can directly specify the path to their own mesh files (.obj, .seg, or .pt) in the script to use it.

For the simulated objects that are tetrahedral meshes, IPC supports [MSH files](https://gmsh.info/doc/texinfo/gmsh.html#File-formats). IPC supports both ASCII and binary encoded version 2.2 and 4.1 files through the use of [MshIO](https://github.com/qnzhou/MshIO). IPC also supports ASCII version 4.0 MSH files via a custom reader and writer (`IglUtils::readTetMesh_msh4()` and `IglUtils::saveTetMesh_msh4()` in `Utils/IglUtils.cpp`).

If one has a watertight surface mesh, we provide a convenient interface to tetrahedralize the mesh with Tetgen:
In the root directory, run command
```
./src/Projects/MeshProcessing/meshprocessing 0 path_to_input_triMesh.obj 3 1e10 0
```
Here the last 2 arguments are the maximum allowed tetrahedral element volume, and whether to insert more points on the surface for better-shaped elements (0 means “do not insert”).
The output will be `path_to_input_triMesh.msh` in the same folder as the input obj file, and the output .msh file is ready to be used by IPC.

### Restarting a Simulation

IPC saves status files at the end of each time step. These files encode the vertex position, velocities, and accelerations as well as the time step number. You can use these files to resume and/or continue the simulation. To do this add the following line to the config script:

```
restart <path/to/status>
```

where `<path/to/status>` is the path to the output status file (either absolute or relative to the input config scripts path).

## More Simulation Examples
Above are all settings we’ve explored to design IPC examples. We provide the scripts of all IPC examples in `input/paperExamples` and `input/otherExamples` for reference. Here note that these scripts also apply a `script` command that utilizes different C++ implementations for setting boundary conditions and/or collision objects together with additional commands that are not covered in this introduction. These are essentially not all that different from setting them via the scripting files introduced above. Please see our README for a complete description of all script setting options currently available.

It is likely that the settings covered in this document still cannot fullfill some more complex needs. In such cases the best solution is probably to take full control by modifying C++ source codes. `Config.cpp` and `AnimScripter.cpp` are the 2 main classes where we process simulation settings, `TimeStepper/Optimizer.cpp` is where the core simulation algorithm is implemented, and `main.cpp` contains the entry of the program.

Last but not least, you are always welcome to post Github issues if anything is still unclear!
