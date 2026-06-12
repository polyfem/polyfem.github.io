Python bindings
===============

!!! warning
	The python bindings are in beta. Expect API changes and possible bugs. Use at your own peril!

[![Last update](https://anaconda.org/conda-forge/polyfempy/badges/latest_release_date.svg)](https://anaconda.org/conda-forge/polyfempy)
[![Downloads](https://anaconda.org/conda-forge/polyfempy/badges/downloads.svg)](https://anaconda.org/conda-forge/polyfempy)
[![Install](https://anaconda.org/conda-forge/polyfempy/badges/installer/conda.svg)](https://anaconda.org/conda-forge/polyfempy)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/polyfem/polyfem.github.io.git/docs?filepath=docs%2Fpython_examples.ipynb)


I am making efforts to provide a simple python interface to Polyfem.

For doing so I am maintaining  a *conda* package which can be easily installed [https://anaconda.org/conda-forge/polyfempy](https://anaconda.org/conda-forge/polyfempy).

Note that the conda deployment is slow and this tutorial will follow the deployment version.

If you hare in a hurry for the juicy latest feature you can clone the repository [Polyfem-python](https://github.com/polyfem/polyfem-python) and use `pip` to install:
```
python setup.py develop
```
and
```
python setup.py test
```
for testing.

Note that the folders tests contain some tests which can be used as documentation.

The documentation can be found [here](polyfempy_doc.md).

Tutorial
--------

Polyfem relies on 3 main objects:

 1. `Settings` that contains the main settings such discretization order (e.g., $P_1$ or $P_2$), material parameters, formulation, etc.
 2. `Problem` that describe the problem you want to solve, that is the boundary conditions and right-hand side. There are some predefined problems, such as `DrivenCavity`, or generic problems, such as `GenericTensor`.
 3. `Solver` that is the actual FEM solver.

The usage of specific problems is indented for benchmarking, in general you want to use the `GenericTensor` for tensor-based PDEs (e.g., elasticity) or `GenericScalar` for scalar PDEs (e.g., Poisson).

A typical use of Polyfem is:
```python
settings = polyfempy.Settings()
# set necessary settings
# e.g. settings.discr_order = 2

problem = polyfempy.GenericTensor() # or any other problem
# set problem related data
# e.g. problem.set_displacement(1, [0, 0], [True, False])

settings.problem = problem

#now we can create a solver and solve
solver = polyfempy.Solver()

solver.settings(settings)
solver.load_mesh_from_path(mesh_path)

solver.solve()
```

**Note 1**: for legacy reasons Polyfem always normalizes the mesh (i.e., rescale it to lay in the $[0,1]^d$ box, you can use `normalize_mesh = False` while loading to disable this feature.

**Note 2**: the solution $u(x)$ of a FEM solver are the coefficients $u_i$ you need to multiply the bases $\varphi_i(x)$ with:
$$
u(x)=\sum u_i \varphi_i(x).
$$
The coefficients $u_i$ are *unrelated* with the mesh vertices because of reordering of the nodes or high-order bases. For instance $P_2$ bases have additional nodes on the edges which do not exist in the mesh.


For this reason Polyfem uses a *visualization mesh* where the solution is sampled at the vertices.
This mesh has two advantages:
1. it solves the problem of nodes reordering and additional nodes in the same way
2. it provides a "true" visualization for high order solution by densely sampling each element (a $P_2$ solution is a piecewise quadratic function which is visualized in a picewise linear fashion, thus the need of a dense element sampling).

To control the resolution of the visualization mesh use `vismesh_rel_area` named-argument while loading.


Notebook
--------

For more details and nice interactive example go to the [notebook tutorial](python_examples.ipynb)!

Or just play with the tutorial in [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/polyfem/polyfem.github.io.git/docs?filepath=docs%2Fpython_examples.ipynb)
