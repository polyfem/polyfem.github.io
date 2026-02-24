
<style>
    .md-typeset ul {
        margin-left: 0;
    }
    .md-typeset ul li {
        margin-bottom: 0;
        margin-left: 0;
        list-style-type: none;
    }
    .md-typeset div.arithmatex > * {
        margin: 0.1em auto !important;
    }
</style>

## Implicit Euler

* **Parameters:** None
* **Description:**

\begin{align}
\dot{u}^{t+1} &= \dot{u}^t + h \ddot{u}^{t+1}\\
u^{t+1} &= u^t + h \dot{u}^{t+1}
\end{align}

where $h$ is the time step size.

* **Reference:** https://en.wikipedia.org/wiki/Backward_Euler_method

## Implicit Newmark

* **Parameters:** `beta`, `gamma`
* **Description:**

\begin{align}
\dot{u}^{t+1} &= \dot{u}^t + (1-\gamma)h\ddot{u}^t + \gamma h\ddot{u}^{t+1}\\
u^{t+1} &= u^t + h\dot{u}^t + \tfrac{h^2}{2}((1-2\beta)\ddot{u}^t + 2\beta\ddot{u}^{t+1})
\end{align}

where $h$ is the time step size and by default $\gamma = 0.5$ and $\beta = 0.25$.

* **Reference:** https://en.wikipedia.org/wiki/Newmark-beta_method

!!! note
    This is equivalent to the [Trapezoidal rule](https://en.wikipedia.org/wiki/Trapezoidal_rule_(differential_equations)) for $\gamma = 0.5$ and $\beta = 0.25$.

## Backward Differentiation Formula (BDF)

* **Parameters:** `num_steps`
* **Description:** 

\begin{align}
\dot{u}^{t+1} &= (\sum_{i=0}^{n-1} \alpha_i \dot{u}^{t-i}) + h\beta\ddot{u}^{t+1}\\
u^{t+1} &= (\sum_{i=0}^{n-1} \alpha_i u^{t-i}) + h\beta\dot{u}^{t+1}
\end{align}

where $h$ is the time step size, the coefficients $\alpha_i$ and $\beta$ are choosen to make the method $n$-th order accurate, and $n \in \{1, \ldots, 6\}$ is the number of previous steps to consider (default: `num_steps=1`). This is equivalent to [implicit Euler](#implicit-euler) for $n=1$.
To initialize the values for $i > 0$, the method starts from $n=1$ and successively builds the history, increasing $n$ by 1 until the $n$-th step. However, we know this can result in less than order $n$ accuracy [[Nishikawa 2019]](https://www.researchgate.net/publication/332855136_On_Large_Start-Up_Error_of_BDF2).

* **Reference:** https://en.wikipedia.org/wiki/Backward_differentiation_formula