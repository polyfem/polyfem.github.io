Python bindings
===============

!!! danger
	The python bindings are in alpha. Expect a lot of API changes and possible bugs. Use at your own peril!

[![Last update](https://anaconda.org/conda-forge/polyfempy/badges/latest_release_date.svg)](https://anaconda.org/conda-forge/polyfempy)
[![Downloads](https://anaconda.org/conda-forge/polyfempy/badges/downloads.svg)](https://anaconda.org/conda-forge/polyfempy)
[![Install](https://anaconda.org/conda-forge/polyfempy/badges/installer/conda.svg)](https://anaconda.org/conda-forge/polyfempy)


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

Polyfempy relies 3 main objects:
1. `Settings` that contains the main settings such discretization order (e.g., $P_1$ or $P_2$), material patameters, formulation, etc.
2. `Problem` that describe the problem you want to solve, that is the boundary conditions and right-hand side. There are some predefined problems, such as `DrivenCavity`, or generic problems, such as `GenericTensor`.
3. `Solver` that is the actual FEM solver.

A typical use of Polyfempy is
```python
settings = polyfempy.Settings()
# set necessary settings, e.g. settings.discr_order = 2

problem = polyfempy.GenericTensor() # or any other problem
# set problem related data, e.g. problem.set_displacement(1, [0, 0], [True, False])

settings.set_problem(problem)
```

For more and nice interactive example go to the [notebook](python_examples.md)!
