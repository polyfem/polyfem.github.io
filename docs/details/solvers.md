## Linear Solver

PolyFEM offers several linear solver options based on compilation options. For more information, see [PolySolve](../polysolve.md), a stand-alone linear solver wrapper library used by PolyFEM.

**Options:** `AMGCL`, `Eigen::BiCGSTAB`, `Eigen::CholmodSupernodalLLT`, `Eigen::ConjugateGradient`, `Eigen::DGMRES`, `Eigen::GMRES`, `Eigen::LeastSquaresConjugateGradient`, `Eigen::MINRES`, `Eigen::PardisoLDLT`, `Eigen::PardisoLU`, `Eigen::SimplicialLDLT`, `Eigen::SparseLU`, `Eigen::UmfPackLU`, `Hypre`, `Pardiso` 

---

## Nonlinear Solver

To solve nonlinear formulations, PolyFEM offers two options: Newton's method (`newton`) and L-BFGS (`lbfgs`).

The settings for the solver are stored inside the field `"nonlinear"`. General settings include:

* `"grad_norm"` (default: `1e-8`): convergence tolerance on the norm ($L^2$) of the gradient
* `"nl_iterations"` (default: `1000`): maximum number of iterations to spend solving
* `"use_grad_norm"` (default: `true`): whether to use the gradient norm or update direction norm for convergence checks
    * When optimizing a function, it is natural to check for a zero (up to tolerance) gradient as this signifies an extremum. However, we also implement the convergence criteria used by [Li et al., 2020](https://ipc-sim.github.io/). Instead of the gradient's norm, the update direction's $L^\infty$-norm is used. This provides two benefits: (1) it expresses the convergence criteria in the units of the variable (e.g., distance for elasticity) and (2) avoids applying small updates that lead to marginal changes in the variables. **Note:** This criterion has been well tested for nonlinear elasticity, but your mileage may vary for other formulations.

### Newton's Method

A (projected) Newton's method with line search.

### L-BFGS

A quasi-Newton method, L-BFGS requires more iterations than the full Newton's method but avoids expensive linear solves.

**Reference:** [Limited-memory BFGS](https://en.wikipedia.org/wiki/Limited-memory_BFGS)  
**Acknowledgments:** The L-BFGS solver is implemented using the [LBFGS++](https://github.com/yixuan/LBFGSpp) library.

---

## Line Search

Line search is a numerical optimization technique used to determine the appropriate step size along a given search direction in iterative optimization algorithms. The primary goal is to ensure sufficient decrease in the objective function, improving convergence speed and stability. By adaptively selecting a step size, line search helps to navigate the optimization landscape efficiently while avoiding overshooting or undershooting.

---

### Backtracking

Backtracking line search is an iterative method that starts with a large initial step size and reduces it iteratively until a sufficient decrease condition, often based on the robust Armijo criterion, is satisfied.

**Parameters:**

- **Initial Step Size:** Starting value for the step size, typically set to `1`.
- **Reduction Factor:** A constant in the range `(0, 1)` that determines how much the step size is reduced in each iteration. Typical values are `0.5` or `0.8`.
- **Armijo Parameter:** A small positive constant, e.g., `1e-4`, which defines the sufficient decrease condition for the step size.

**Algorithm:**

1. Set the initial step size.
2. Evaluate the objective function at the current step size.
3. Check if the robust Armijo condition is satisfied:
   \[
   f(x + \alpha p) \leq f(x) + c \alpha \nabla f(x)^T p
   \]
   where \( \alpha \) is the step size, \( p \) is the search direction, and \( c \) is the Armijo parameter.
4. If the condition is not met, reduce the step size by multiplying it with the reduction factor and repeat.
5. Stop when the condition is satisfied or the step size becomes too small.

---

### Robust Armijo

The robust Armijo method improves the traditional Armijo criterion by incorporating additional tolerance checks to ensure meaningful convergence. It is particularly useful in preventing premature convergence when the objective function changes negligibly.

**Parameters:**

- **Armijo Parameter (c):** A small positive constant, typically `1e-4`, which sets the strictness of the sufficient decrease condition.
- **Delta Relative Tolerance:** A small positive constant defining the threshold for acceptable relative changes in the objective function.

**Mathematical Formulation:**

The standard robust Armijo condition is:
\[
f(x + \alpha p) \leq f(x) + c \alpha \nabla f(x)^T p
\]

If this condition is not met, the relative tolerance criterion is checked:
\[
\frac{|f(x + \alpha p) - f(x)|}{|f(x)|} \leq \text{tolerance}
\]

If both conditions fail, the step size is reduced further.

**Purpose:**

The robust Armijo method ensures optimization steps are meaningful by combining sufficient decrease with relative tolerance checks. This avoids poor solutions caused by steps that barely alter the objective function.

**References:**

- Longva et al., 2023: Introduced numerical robustness improvements for the Armijo line search, making it suitable for more challenging optimization problems. 
- [Wikipedia: Line Search](https://en.wikipedia.org/wiki/Line_search)

---


### More-Thuente

!!! todo
    Describe this method and its parameters.


**References:**

- Jorge Nocedal and Stephen J. Wright, *Numerical Optimization*, Springer, 2006.
