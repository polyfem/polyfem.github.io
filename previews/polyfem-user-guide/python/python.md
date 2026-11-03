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

!!! important "Current Python API"
    The older `Settings` / `Problem` / `GenericTensor` examples and the
    `Problem.set_displacement(...)` / `set_dirichlet_value(...)` boundary-condition
    setters shown in previous versions of this guide are **not part of the
    current `polyfem-python` binding**. The reference below was generated for an older
    release and should not be treated as a current API reference.

The current Python binding accepts PolyFEM's JSON configuration directly through
`Solver.settings(...)` (also exposed as `set_settings(...)`). Define boundary
conditions using the same JSON schema as the C++ executable; see the
[JSON input guide](json.md) and [generated specification](json_defaults_and_spec.md).

For mesh arrays already in Python, the current binding also exposes
`polyfempy.solve(vertices=..., cells=..., sidesets_func=..., **options)`,
which returns a solver object. The `sidesets_func` callback assigns boundary
IDs; it is **not** the removed boundary-condition-value setter.

Consult the [current Python binding source](https://github.com/polyfem/polyfem-python/blob/main/src/binding.cpp)
for the exposed signatures. The historical [Python API reference](polyfempy_doc.md)
has not yet been regenerated for the current API.

Notebook
--------

For more details and nice interactive example go to the [notebook tutorial](python_examples.ipynb)!

Or just play with the tutorial in [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/polyfem/polyfem.github.io.git/docs?filepath=docs%2Fpython_examples.ipynb)
