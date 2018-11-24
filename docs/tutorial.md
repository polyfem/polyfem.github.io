Tutorial
========


UI
---

Start the program with `PolyFEM_bin` this will open the UI.
Press the the load button to load a mesh
![Load mesh](img/t1.png)


Then press the numbered button in sequence:

1. Loads the mesh and normalized it
1. Builds the FEM bases, you can change the order by changing discr. To enable *pref* or *spline* check the corresponding boxes (before pushing the button)
1. Build a denser mesh for visualization purposes.
1. Assembles the right-hand side of the problem. You can change the problem with the problem drop-down menu
1. Assembles the matrix. You can change the formulation by changing the drop-down 1D nD Mixed form. The type of formulation depends on the problem. For instance Franke works only with scalar formulations, while Elastic only with tensor problems.
1. Solve problem solves the problem.
1. You can compute the error for problems with given exact solutions. In case of no exact solution, the program will compute the norms of the solutions
![Load mesh](img/t2.png)

At the end you can press save VTU to save the `result.vtu` file in the binary directory. This file can be opened with [Paraview](https://www.paraview.org/)

![Load mesh](img/t3.png)


JSON
----

To run the previous experiment with a json file create a `run.json` containing (refer to [documentation](documentation.md) for the full description):

```json
{
    "mesh": "<mesh.obj>",
    "normalize_mesh": true,

    "n_refs": 0,

    "scalar_formulation": "Laplacian",

    "discr_order": 1,
    "use_spline": false,
    "use_p_ref": false,

    "output": "<stats.json>",

    "problem": "Franke",

    "export": {
        "vis_mesh": "<result.vtu>",
    }
}
```

Then run `PolyFEM_bin --json run.json --cmd`. You can omit the `--cmd` argument to open the UI with the parameters.