Python bindings
===============

!!! danger
	The python bindings are in alpha (or pre alpha). Expect a lot of API changes and possible bugs. Use at your own peril!

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


Examples
--------

```python
import polyfempy as pf

mesh_path = "mesh.mesh"

settings = pf.Settings()
settings.discr_order = 1
settings.normalize_mesh = False


settings.set_material_params("E", 200)
settings.set_material_params("nu", 0.35)


settings.tensor_formulation = pf.TensorFormulations.LinearElasticity

problem = pf.GenericTensor()
problem.add_dirichlet_value(2, [0, 0, 0])
problem.add_neumann_value(1,[0, -100, 0])


settings.vismesh_rel_area = 0.00001

settings.set_problem(problem)


solver = pf.Solver()

solver.settings(str(settings))
solver.load_mesh(mesh_path, tag_path)

solver.solve()
```

The `Settings` class is a wrapper for the json input parameters ([documentation](documentation.md)). It contains some of the standard settings, please look at the documentation for details.
To setup a problem you can use one of the predefined problems inside the `Problem.py` file. These are a relevant subset of the problems in Polyfem. Similarly as for the settings, the problems provide utility functions to avoid messing around with jsons.

Once everything is setup you can create a `Solver`, set the settings, load a mesh and solve the problem! Note the solve might require time.
There are many ways to load a mesh and specify side-sets, please refer to the documentation for details.

Once the problem has been solved you can use `get_sampled_solution` to get vertices, connectivity and solution. For elastic problem you can use `get_sampled_mises` or `get_sampled_mises_avg` to obtain the Von Mises stresses at the sampled vertices.

```python
[pts, tets, disp] = solver.get_sampled_solution()
vertices = pts + disp
mises = solver.get_sampled_mises()
```