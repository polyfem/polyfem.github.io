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

The following formulations are available in the PolyFEM list of possible formulations. The constants can be set in `params`. All formulations support boundary conditions. For the elasticity formulations we output:

**Cauchy stress tensor**

\[
    \sigma = \frac 1 J \frac{\partial \Psi}{\partial F} F^T
\]

**Frist Piola Kirchhoff stress tensor** ([Wikipedia](https://en.wikipedia.org/wiki/Stress_(mechanics)#Piola–Kirchhoff_stress_tensor))

\[
    P =  J \sigma F^{-T}
\]

**Second Piola Kirchhoff stress tensor** ([Wikipedia](https://en.wikipedia.org/wiki/Stress_(mechanics)#2nd_Piola–Kirchhoff_stress_tensor))

\[
    S =  J F^{-1} \sigma F^{-T},
\]

where \(\Psi\) is the energy density, \(F\) the deformation gradient, and \(J=\det(F)\).


## Scalar

### Laplacian
* **Constants:** none
* **Description:** solve for \(-\Delta u = f\)

### Bilaplacian (mixed)
* **Constants:** none
* **Description:** solve for \(-\Delta^2 u = f\)

### Helmholtz
* **Constants:** $k$
* **Description:** solve for \(-\Delta u - k^2 u = f\)

## Tensor

### Linear Elasticity
* **Constants:** `E`/`nu`, `lambda`/`mu`
* **Description:** solve for $-\text{div}(\sigma[u]) = f$ where

\[
    \sigma[u] = 2 \mu  \epsilon[u]+ \lambda \text{tr}(\epsilon[u]) I \qquad \epsilon[u] = \frac 1 2 \left(\nabla u^T + \nabla u\right)
\]

### Hooke Linear Elasticity
* **Constants:**  `elasticity_tensor`, `E`/`nu`, `lambda`/`mu`
* **Description:** solve for $-\text{div}(\sigma[u]) = f$ where

\[
    \sigma[u] = C :  \epsilon[u] \qquad \epsilon[u] = \frac 1 2 \left(\nabla u^T + \nabla u\right)
\]

where $C$ is the elasticity tensor

### Incompressible Linear Elasticity (mixed)
* **Constants:** `E`/`nu`, `lambda`/`mu`
* **Description:** solve for

\begin{align}
-\text{div}(2\mu\epsilon[u] + p I) &= f\\
\text{div}(u) - \lambda^{-1}p &= 0
\end{align}

### Saint Venant–Kirchoff Elasticity
* **Constants:** `elasticity_tensor`, `E`/`nu`, `lambda`/`mu`
* **Description:** solve for $-\text{div}(\sigma[u]) = f$ where

\[
\sigma[u] = C: \epsilon[u]  \qquad \epsilon[u] = \frac 1 2 \left(\nabla u^T \nabla u + \nabla u^T + \nabla u\right)
\]

where $C$ is the elasticity tensor

### NeoHookean Elasticity
* **Constants:** `E`/`nu`, `lambda`/`mu`
* **Description:** solve for $-\text{div}(\sigma[u]) = f$ where

\[
    \sigma[u] = \mu (F[u] - F[u]^{-T}) + \lambda \ln(\det F[u]) F[u]^{-T} \qquad F[u] = \nabla u + I
\]

<!-- * **Physical interpretation:** $E$ is the Young's modulus, $\nu$ is Poisson's ratio, $\mu$ is the shear modulus, and $\lambda$ is Lamé's first parameter. -->

### Mooney-Rivlin Elasticity

* **Constants:** `c1`/`c2`/`k=1`
* **Description:** solve for $-\text{div}(\sigma[u]) = f$ where $\sigma[u]=\nabla_u \Psi[u]$. The energy density $\Psi$ is

\[
    \Psi[u] = c_1 (\widetilde{I_1} - d) + c_2 (\widetilde{I_2} - d) + \frac{k}{2} \ln^2(J)
\]

where $d$ is the dimension (2 or 3),

\begin{align}
F = \nabla u + I, \quad J = \det(F), \quad \tilde{F} = \frac{1}{\sqrt[d]{J}} F, \quad \widetilde{C} = \widetilde{F} \widetilde{F}^T, \\
\widetilde{I_1} = \text{tr}\left(\widetilde{C}\right), \quad  \text{and} \quad
\widetilde{I_2} = \frac{1}{2} \left(\left(\trace{\widetilde{C}}\right)^2 - \text{tr}\left(\widetilde{C}^2\right)\right).
\end{align}

* **Reference**: [FEBio documentation](https://help.febio.org/FEBioTheory/FEBio_tm_3-4-Subsection-5.3.1.html)


### Incompressible Ogden Elasticity

* **Constants:** `c`/`m`/`k`
* **Description:** solve for $-\text{div}(\sigma[u]) = f$ where $\sigma[u]=\nabla_u \Psi[u]$. The energy density $\Psi$ is

\[
    \Psi[u] = \sum_{i=1}^N \frac{c_i}{m_i^2} \left(
        \sum_{j=1}^d \tilde{\lambda}_j^{m_i} - d
    \right) +  \frac{1}{2} K  \ln(J)^2
\]

where $N$, the number of terms, is dictated by the number of coefficients given, $d$ is the dimension (2 or 3), $J = \det(F)$ where $F = \nabla u + I$, and $\tilde{\lambda}_j = J^{-\frac{1}{d}}\lambda_j$ are the eigenvalues of $\tilde{F}$ (same as in the [Mooney-Rivlin Elasticity](#mooney-rivlin-elasticity)).

<!-- * **Physical interpretation:**
!!! todo
    Physical interpretation of the coefficients -->

* **Reference**: [FEBio documentation](https://help.febio.org/FEBioTheory/FEBio_tm_3-4-Subsection-5.3.2.html)


### Unconstrained Ogden Elasticity

* **Constants:** `mus`/`alphas`/`Ds`
* **Description:** solve for $-\text{div}(\sigma[u]) = f$ where $\sigma[u]=\nabla_u \Psi[u]$. The energy density $\Psi$ is

\[
    \Psi[u] = \sum_{i=1}^N \frac{2 \mu_i}{\alpha_i^2} \left(
        \sum_{j=1}^d \tilde{\lambda}_j^{\alpha_i} - d
    \right) + \sum_{i=1}^N \frac{\left(J-1\right)^{2 i}}{D_i}
\]

where $N$, the number of terms, is dictated by the number of coefficients given, $d$ is the dimension (2 or 3), $J = \det(F)$ where $F = \nabla u + I$, and $\tilde{\lambda}_j = J^{-\frac{1}{d}}\lambda_j$ where $\lambda_j$ are the eigenvalues of $F.$

<!-- * **Physical interpretation:**
!!! todo
    Physical interpretation of the coefficients -->

* **Reference**: [ABAQUS documentation](https://classes.engineering.wustl.edu/2009/spring/mase5513/abaqus/docs/v6.6/books/stm/default.htm?startat=ch04s06ath124.html)

### Viscous Damping
* **Constants:** `phi`/`psi`
* **Description:** an extra energy that represents dissipation, adding to the elastic energy in transient problems

\[
    R(F,\dot{F})=\psi \|\dot{E}(F,\dot{F})\|^2+\frac{\phi}{2}\text{tr}^2\dot{E}(F,\dot{F})
\]

where $F[u] = \nabla u + I$ and $E[u] = \frac{1}{2}(F^TF-I)$.

The above corresponds to the viscous Piola-Kirchhoff stress

\[
    P=F(2\psi\dot{E}+\phi\text{tr}(\dot{E})I)=\nabla_2 R(F,\dot{F}).
\]

### Stokes (mixed)
* **Constants:** `viscosity` ($\nu$)
* **Description:** solve for

\begin{align}
    -\nu\Delta u + \nabla p &= f\\
    -\text{div}(u) &= 0
\end{align}

### Navier–Stokes (mixed)
* **Constants:** `viscosity` ($\nu$)
* **Description:** solve for

\begin{align}
    u\cdot \nabla u -\nu\Delta u + \nabla p &= f\\
    -\text{div}(u)  &= 0
\end{align}

## Implementing New Formulations

!!! todo
    Describe how to implement a new formulation in C++.
