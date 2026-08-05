## Understanding solver logs

The nonlinear solver will log a debug message per iteration with some useful information. Take the following example log:

```
[polyfem] [debug] [Newton] iter=51 f=-1.06006e-06 ||∇f||=0.006432 ||Δx||=0.0037612 Δx⋅∇f(x)=-6.71732e-08 g=9.69072e-05 tol=1e-05 rate=0.0321861 ||step||=0.000121058
```

The terms in order they appear are:

* `iter`: the iteration number
* `f`: the value of the objective function
* `||∇f||`: the $L^2$-norm of the gradient of `f`
* `||Δx||`: the $L^2$-norm of the update direction to our optimization variables (e.g., displacements/positions for elasticity)
* `Δx⋅∇f(x)`: the dot product between these values (this is a measure of how much progress we can expect the optimization can make)
* `g`: the convergence criteria (i.e., the optimization stops when `g < tol`); this depends on the choice of `"useGradNorm"` solver parameter (for more information see [here](../documentation/#nonlinear-solver))
* `tol`: the convergence criteria tolerance
* `rate`: the step size the line-search produced (i.e. $x_{i+1} = x_i + \text{rate} *  \Delta x$)
* `||step||`: the L2 norm of the step (i.e. $\|\text{rate} * \Delta x\| = \text{rate} * \|\Delta x\|$)
