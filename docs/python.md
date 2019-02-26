Python bindings
===============

!!! danger
	The python bindings are in alpha. Expect a lot of API changes and possible bugs. Use at your own peril!

![Last update](https://anaconda.org/conda-forge/polyfempy/badges/latest_release_date.svg)
![Downloads](https://anaconda.org/conda-forge/polyfempy/badges/downloads.svg)
![Install](https://anaconda.org/conda-forge/polyfempy/badges/installer/conda.svg)


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

Examples
--------

For more and nice interactive example go to the [notebook](python_examples.md)!


### Bended bar

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
mises, _ = solver.get_sampled_mises_avg()
```


### Plotting

There are many python libraries for plotting, I created a simple function to display the results in 3D with [plotly](https://plot.ly/). It can be found in `tests/utils.py`
```python
import plotly.offline as plotly
import plotly.graph_objs as go

import numpy as np


def plot(vertices, connectivity, function):
    x = vertices[:,0]
    y = vertices[:,1]

    if vertices.shape[1] == 3:
        z = vertices[:,2]
    else:
        z = np.zeros(x.shape, dtype=x.dtype)

    if connectivity.shape[1] == 3:
        f = connectivity
    else:
    	#Convert a tet-mesh into face based triangles.
        f = np.ndarray([len(connectivity)*4, 3], dtype=np.int64)
        for i in range(len(connectivity)):
            f[i*4+0] = np.array([connectivity[i][1], connectivity[i][0], connectivity[i][2]])
            f[i*4+1] = np.array([connectivity[i][0], connectivity[i][1], connectivity[i][3]])
            f[i*4+2] = np.array([connectivity[i][1], connectivity[i][2], connectivity[i][3]])
            f[i*4+3] = np.array([connectivity[i][2], connectivity[i][0], connectivity[i][3]])

    mesh = go.Mesh3d(x=x, y=y, z=z,
                     i=f[:,0], j=f[:,1], k=f[:,2],
                     intensity=function, flatshading=function is not None,
                     colorscale='Viridis',
                     contour=dict(show=True, color='#fff'),
                     hoverinfo="all")
    layout = go.Layout(scene=go.layout.Scene(aspectmode='data'))
    fig = go.Figure(data=[mesh], layout=layout)

    plotly.plot(fig)
```


### Plate hole example

Here is the python version of the plate with hole example explained [here](https://polyfem.github.io/tutorial/#boundary-conditions)
```python
import polyfempy as pf


mesh_path = "plane_hole.obj"

settings = pf.Settings()
#Linear P1 elements. If the mesh would be a quad it would be Q1
settings.discr_order = 1
#Normalize the mesh to be in [0,1]^2
settings.normalize_mesh = True

#Choose Young's modulus and poisson ratio
settings.set_material_params("E", 210000)
settings.set_material_params("nu", 0.3)

#We are fine with linear material model
settings.tensor_formulation = pf.TensorFormulations.LinearElasticity

#setup the problem
problem = pf.GenericTensor()
#sideset 1 has zero displacement in x
problem.add_dirichlet_value(1, [0, 0], [True, False])
#sideset 4 has zero displacement in y
problem.add_dirichlet_value(4, [0, 0], [False, True])

#sideset 3 has a force (Neumann) of [100, 0] applied
problem.add_neumann_value(3, [100, 0])

#set the problem
settings.set_problem(problem)

#solve!
solver = pf.Solver()

solver.settings(str(settings))
solver.load_mesh(mesh_path)

solver.solve()

#Get the solution
[pts, tets, disp] = solver.get_sampled_solution()
#diplace the mesh
vertices = pts + disp
#and get the stresses
mises, _ = solver.get_sampled_mises_avg()

#finally plot with the above code
plot(vertices, tets, mises)
```


### Torsion

A non-linear torsion example. Note that it is really similar to the above one.
```python
import polyfempy as pf

mesh_path = "square_beam_h.HYBRID"

settings = pf.Settings()
#It is an hex-mesh so we are using Q1
settings.discr_order = 1
settings.normalize_mesh = False

#Choose Young's modulus and poisson ratio
settings.set_material_params("E", 200)
settings.set_material_params("nu", 0.35)


#Non-linear problem
settings.tensor_formulation = pf.TensorFormulations.NeoHookean
#we want to do 5 steps of incremental loading to avoid ambiguities
settings.nl_solver_rhs_steps = 5

#setup problem with fixed sideset, rotating an number of tours
problem = pf.Torsion()
problem.fixed_boundary = 5
problem.turning_boundary = 6
problem.axis_coordiante = 2
problem.n_turns = 0.5

#coear visualization mesh
settings.vismesh_rel_area = 0.001

settings.set_problem(problem)

#solving!
solver = pf.Solver()

solver.settings(str(settings))
solver.load_mesh(mesh_path)

solver.solve()
#takes ~1 min because it is a complicated non-linear problem!

#get solution and stesses as before
[pts, tets, disp] = solver.get_sampled_solution()
vertices = pts + disp
mises, _ = solver.get_sampled_mises_avg()

#plot the 3d result
plot(vertices, tets, mises)
```
