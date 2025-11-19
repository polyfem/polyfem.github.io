## Linear Solver

PolyFEM offers several linear solver options based on compilation options. For more information, see [PolySolve](../polysolve.md) a stand-alone linear solver wrapper library used by PolyFEM.

Options: `AMGCL`, `Eigen::BiCGSTAB`, `Eigen::CholmodSupernodalLLT`, `Eigen::ConjugateGradient`, `Eigen::DGMRES`, `Eigen::GMRES`, `Eigen::LeastSquaresConjugateGradient`, `Eigen::MINRES`, `Eigen::PardisoLDLT`, `Eigen::PardisoLU`, `Eigen::SimplicialLDLT`, `Eigen::SparseLU`, `Eigen::UmfPackLU`, `Hypre`, `Pardiso` 


## Nonlinear Solver

To solve nonlinear formulations, PolyFEM offers two options: Newton's method (`newton`) and L-BFGS (`lbfgs`).

The settings for the solver are stored inside the field `"nonlinear"`. General settings include:

* `"grad_norm"` (default: `1e-8`): convergence tolerance on the norm ($L^2$) of the gradient
* `"nl_iterations"` (default: `1000`): maximum number of iterations to spend solving
* `"use_grad_norm"` (default: `true`): whether to use the gradient norm or update direction norm for convergence checks
    * When optimizing a function it is natural to check for a zero (up to tolerance) gradient as this signifies an extremum. However, we also implement the convergence criteria used by [Li et al. [2020]](https://ipc-sim.github.io/). Where instead of the gradient's norm the update direction's $L^\infty$-norm is used. This provides two benefits: (1) it expresses the convergence criteria in the units of the variable (e.g., distance for elasticity) which (2) avoids applying small updates that lead to a marginal change in the variables. Note: this criterion has been well tested for nonlinear elasticity, but your mileage may vary for other formulations.
    <!-- * As a sanity check, there is always a check that $\|\nabla f\| < 10^{-2}$ to make sure the solver does not converge with a large gradient. -->

### Newton's Method

A (projected) Newton's method with line search.

### L-BFGS

A quasi-Newton method, L-BFGS requires more iterations than the full Newton's method but avoids expensive linear solves.

Reference: https://en.wikipedia.org/wiki/Limited-memory_BFGS<br>
Acknowledgments: The L-BFGS solver is implemented using the [LBFGS++](https://github.com/yixuan/LBFGSpp) library.

## Line Search

!!! todo
    Describe line-search and its purpose.

### Backtracking

!!! todo
    Describe this method and its parameters.

### Armijo

!!! todo
    Describe this method and its parameters.

#### Armijo (alt)

!!! todo
    Describe this method and its parameters.

### More-Thuente

!!! todo
    Describe this method and its parameters.