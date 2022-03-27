The following formulations are available in the PolyFEM list of possible formulations. The constants can be set in `params`. All formulations support boundary conditions.

## Scalar

### Laplacian
**Constants**: none<br/>
**Description**: solve for \(-\Delta u = f\)

### Bilaplacian (mixed)
**Constants**: none<br/>
**Description**: solve for \(-\Delta^2 u = f\)

### Helmholtz
**Constants**: $k$<br/>
**Description**: solve for \(-\Delta u - k^2 u = f\)

## Tensor

### LinearElasticity
**Constants**: `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for $-\text{div}(\sigma[u]) = f$ where

\[
    \sigma[u] = 2 \mu  \epsilon[u]+ \lambda \text{tr}(\epsilon[u]) I \qquad \epsilon[u] = \frac 1 2 \left(\nabla u^T + \nabla u\right)
\]

### HookeLinearElasticity
**Constants**:  `elasticity_tensor`, `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for $-\text{div}(\sigma[u]) = f$ where

\[
    \sigma[u] = C :  \epsilon[u] \qquad \epsilon[u] = \frac 1 2 \left(\nabla u^T + \nabla u\right)
\]

where $C$ is the elasticity tensor

### IncompressibleLinearElasticity (mixed)
**Constants**: `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for

\begin{align}
-\text{div}(2\mu\epsilon[u] + p I) &= f\\
\text{div}(u) - \lambda^{-1}p &= 0
\end{align}

### SaintVenant
**Constants**: `elasticity_tensor`, `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for $-\text{div}(\sigma[u]) = f$ where

\[
\sigma[u] = C: \epsilon[u]  \qquad \epsilon[u] = \frac 1 2 \left(\nabla u^T \nabla u + \nabla u^T + \nabla u\right)
\]

where $C$ is the elasticity tensor

### NeoHookean
**Constants**: `young`/`nu`, `E`/`nu`, `lambda`/`nu`<br/>
**Description**: solve for $-\text{div}(\sigma[u]) = f$ where

\[
    \sigma[u] = \mu (F[u] - F[u]^{-T}) + \lambda \ln(\det F[u]) F[u]^{-T} \qquad F[u] = \nabla u + I
\]

### Stokes (mixed)
**Constants**: `viscosity` $\nu$<br/>
**Description**: solve for

\begin{align}
    -\nu\Delta u + \nabla p &= f\\
    -\text{div}(u) &= 0
\end{align}

### NavierStokes (mixed)
**Constants**: `viscosity` $\nu$<br/>
**Description**: solve for<br/>

\begin{align}
    u\cdot \nabla u -\nu\Delta u + \nabla p &= f\\
    -\text{div}(u)  &= 0
\end{align}

## Implementing New Formulations

!!! todo 
    Describe how to implement a new formulation in C++.