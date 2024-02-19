# Trajectory Optimization

<div class="md-source-date"><small>Author: Zizhou Huang, Date: Feb. 19, 2024</small></div>

In this tutorial, we will demonstrate how to use polyfem to optimize the initial velocity of throwing a ball to match a given trajectory.

<p float="left">
  <img src="../sim.gif" width="60%" />
</p>

## Prerequisites

The following items are necessary to complete this tutorial. To reproduce the experiment, you can feel free to use either the given mesh files or your own mesh.

- [ ] [Build PolyFEM](../../cxx_index.md)
- [ ] [Download File: square.obj](https://github.com/polyfem/polyfem-data/blob/main/contact/meshes/2D/simple/square.obj)
- [ ] [Download File: circle.msh](https://github.com/polyfem/polyfem-data/blob/main/differentiable/circle.msh)
- [ ] [Download File: barycenter-opt.json](https://github.com/polyfem/polyfem-data/blob/main/differentiable/optimizations/initial-condition-trajectory-opt/barycenter-opt.json)
- [ ] [Download File: barycenter.json](https://github.com/polyfem/polyfem-data/blob/main/differentiable/optimizations/initial-condition-trajectory-opt/barycenter.json)
- [ ] [Download File: barycenter-target.json](https://github.com/polyfem/polyfem-data/blob/main/differentiable/optimizations/initial-condition-trajectory-opt/barycenter-target.json)

The files can also be found at [polyfem-data](https://github.com/polyfem/polyfem-data/blob/main/differentiable/optimizations/initial-condition-trajectory-opt/).

### Build PolyFEM

The instructions for building PolyFEM can be found [here](../../cxx_index.md).

Then you can use it by

```shell
polyfem --help
```

## Setting up the Optimization

We will setup the optimization using PolyFEM's JSON interface. For more details, please refer to the [JSON Input](../../json.md) documentation.

We will only go over the JSON script for the optimization configuration, please refer to other tutorials for the JSON script for the simulation configuration.

### Parameters

```json
{
    "parameters": [
        {
            "number": 2,
            "initial": [4, 0]
        }
    ]
}
```

In `parameters`, we specify the dimension and initial guess of the variable to be optimized. Since we are going to optimize the initial velocity of a ball in 2D, the dimension is 2.

In more complex optimizations, where several types of parameters are optimized, the `parameters` can be a list of variables of different dimensions.

### States

```json
{
    "states": [
        {
            "path": "barycenter.json"
        },
        {
            "path": "barycenter-target.json"
        }
    ]
}
```

In `states`, we specify the path to the JSON files of simulations, they follow the same [rules](../../json.md) for the simulation JSON scripts. PolyFEM will create a number of simulators, one for each JSON file, whose parameters can be optimized. During the optimization, certain parameters in these configurations are optimized, but the optimized values will not overwrite the values in these JSON files. Each simulator gets an ID starting from 0, following the order in this list. The ID of simulators may be used in `variable to simulation` and `functionals`.

Here we have two simulators: The first one is the simulator being optimized, while the second one is a fixed simulation that generates a reference trajectory. These JSON files are only for initializing the simulators, so one can use the same path for multiple simulators if possible.

### Variable to Simulation

```json
{
    "variable_to_simulation": [
        {
            "type": "initial",
            "state": 0,
            "composition": [{
                "type": "append-values",
                "values": [0, 0]
            },{
                "type": "per-body-to-per-node",
                "state": 0
            },{
                "type": "append-const",
                "value": 0,
                "size": 146,
                "start": 0
            }]
        }
    ]
}
```

In `variable to simulation`, we specify how the optimization variables in `parameters` control the simulation configurations. Since different types of parameters in a number of simulations can be controlled at the same time, the `variable to simulation` is a list, where each entry specifies the control of one type of parameter, e.g. initial condition, in one simulation. The `type` specifies the type of parameter in the simulation, and `state` points to the ID of the simulation (according to the order in `states`). 

The initial condition parameter has a dimension of `2 * dim * n_basis`, where `dim` is the dimension of the simulation (2 or 3), `n_basis` is the number of finite element basis in the simulation, because it consists of the initial displacement and velocity at every basis node. This allows the user to specify the initial condition not only as a rigid body transformation, but also as an arbitrary deformation, e.g. stretching and shearing.

In this tutorial, we only optimize the initial velocity of the ball, so we need to build a mapping, which we call `composition` in the JSON script, from the variable of size 2 to the full initial condition parameter of size `2 * dim * n_basis`. The `composition` is a list of some pre-defined mappings, which will apply to the optimization variables in order, and the final output of the mappings will be assigned to the initial condition parameter.

There are two objects with different volume IDs, specified in `barycenter.json` and `barycenter-target.json`, and we only want to control the initial velocity of the ball, with volume ID 1. First, in `append-values` we append two zeros to the optimization variable, which represents the zero initial velocity of the floor. Second, in `per-body-to-per-node` we map the per-volume values to per-node, whose output has the dimension of `dim * n_basis`. Finally, in `append-const` we append more zeros to the start of the vector, to account for the zero initial displacement. Please refer to the [opt-input-spec.json](https://github.com/polyfem/polyfem/blob/main/json-specs/opt-input-spec.json) for the documentation of compositions.

### Functionals

```json
{
    "functionals": [
        {
            "type": "transient_integral",
            "state": 0,
            "integral_type": "uniform",
            "static_objective": 
            {
                "type": "center-target",
                "state": 0,
                "target_state": 1,
                "volume_selection": [1]
            }
        }
    ]
}
```

The `functionals` specify the objective being minimized in the optimization. Please refer to [objective-input-spec.json](https://github.com/polyfem/polyfem/blob/main/json-specs/objective-spec.json) for the documentation of `functionals`.

Here we perform trajectory optimization on the ball, so the objective is the $L^2$ difference between the two ball barycenters in the two simulations, integrated over time.

```json
{
    "type": "center-target",
    "state": 0,
    "target_state": 1,
    "volume_selection": [1]
}
```

The `center-target` computes the $L^2$ difference between the solutions in `state` and `target_state`, integrated over the space with `volume selection` ID 1. We assume that both simulators have the same number of basis and dimension on the same volume selection (number of basis on other volume selections can be different).

```json
{
    "type": "transient_integral",
    "state": 0,
    "integral_type": "uniform",
    "static_objective": { ... }
}
```

The `transient integral` computes the integral over time of the `static objective`. The `integral type` and `state` specify the quadrature scheme and the simulator (the objective gets information like the number of time steps and dt from the simulator).

### Output

```json
"output": {
    "log": {
        "level": 1
    }
}
```

The `output` contains options regarding the logging of the optimization, here `output/log/level` specifies a log level of 1, corresponding to `debugging`, to log the energy and gradient during the optimization. The log level for simulations are specified in each state json, normally the simulation log level is set to `info` or `warn` so that we can focus more on the optimization logs.

### Solver

```json
    "solver": {
        "nonlinear": {
            "history_size": 2,
            "grad_norm": 1e-4
        }
    }
```

The `solver` contains options of the nonlinear solver for the optimization. Since our forward problem and inverse problem share the same nonlinear solver code, the options of the inverse problem are the same as in the forward problem. However, since we can't compute the second order derivatives of the inverse problem, the Newton's method is not available here. By default the solver is [L-BFGS](https://github.com/yixuan/LBFGSpp), a quasi-Newton method using a limited amount of memory.
