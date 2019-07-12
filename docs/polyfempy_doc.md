## class Problem

Generic problem problem, scalar or tensor depending on the pde. Warning, this problem needs to be used with the `set_pde` function in settings

**`add_dirichlet_value(id, value, is_dirichlet_dim=None)`**

add the Dirichlet value value for the sideset id. Note the value must be a scalar, vector in 2D, or 3D depending on the problem. is_dirichlet_dim is a vector of boolean specifying which dimentions are fixed, only for vector-based problems.

**`add_neumann_value(id, value)`**

add the Neumann value value for the sideset id. Note the value must be a scalar, vector in 2D, or 3D depending on the problem

**`params()`**

**`set_displacement(id, value, is_dim_fixed=None)`**

set the displacement value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

**`set_force(id, value)`**

set the force value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

**`set_velocity(id, value, is_dim_fixed=None)`**

set the velocity value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

**`set_x_symmetric(id)`**

x coorinate is fixed, y is allowed to move (Neumann)

**`set_xy_symmetric(id)`**

xy coorinates are fixed, z is allowed to move (Neumann)

**`set_xz_symmetric(id)`**

xz coorinates are fixed, y is allowed to move (Neumann)

**`set_y_symmetric(id)`**

y coorinate is fixed, x is allowed to move (Neumann)

**`set_yz_symmetric(id)`**

yz coorinates are fixed, x is allowed to move (Neumann)




## class Settings

Class that encodes the settings of the solver, it models the input json file

**`serialize()`**

stringyfied json description of this class, used to run the solver

**`set_advanced_option(key, value)`**

Used to set any advanced option not present in this class, for instance set_advanced_option("use_spline",True), see https://polyfem.github.io/documentation/ for full list

**`set_isolines_export_path(path)`**

Sets the path to export the isolines of the solution

**`set_material_params(name, value)`**

set the material parameters, for instance set_material_params("E", 200) sets the Young's modulus E to 200. See https://polyfem.github.io/documentation/#formulations for full list

**`set_pde(pde)`**

Sets the PDE to solve, use any of the polyfempy.PDEs

**`set_problem(problem)`**

Sets the problem, use any of the problems in Problems or the Problem

**`set_solution_export_path(path)`**

Sets the path to save the solution

**`set_vtu_export_path(path, bounda_only=False)`**

Sets the path to export a vtu file with the results, use bounda_only to export only one layer of the mesh in 3d

**`set_wireframe_export_path(path)`**

Sets the path to export a wireframe of the mesh




## class DrivenCavity

Classical driven cavity problem in fluid simulation

**`name()`**

**`params()`**




## class Flow

Inflow/outflow problem for fluids. You can specify the sideset for the moving fluxes, the axial direction of the flow, and the list of obstacle sidesets. https://polyfem.github.io/documentation/#flow

**`name()`**

**`params()`**




## class Franke

Franke problem with exact solution https://polyfem.github.io/documentation/#franke

**`name()`**

**`params()`**




## class GenericScalar

Generic scalar problem https://polyfem.github.io/documentation/#genericscalar

**`add_dirichlet_value(id, value)`**

add the Dirichlet value value for the sideset id

**`add_neumann_value(id, value)`**

add the Neumann value value for the sideset id

**`name()`**

**`params()`**




## class GenericTensor

Generic tensor problem https://polyfem.github.io/documentation/#generictensor

**`add_dirichlet_value(id, value, is_dirichlet_dim=None)`**

add the Dirichlet value value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem. is_dirichlet_dim is a vector of boolean specifying which dimentions are fixed.

**`add_neumann_value(id, value)`**

add the Neumann value value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

**`name()`**

**`params()`**

**`set_displacement(id, value, is_dim_fixed=None)`**

set the displacement value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

**`set_force(id, value)`**

set the force value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

**`set_velocity(id, value, is_dim_fixed=None)`**

set the velocity value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem




## class Gravity

time dependent gravity problem https://polyfem.github.io/documentation/#gravity

**`name()`**

**`params()`**




## class Torsion

3D torsion problem, specify which sideset to fix (fixed_boundary) and which one turns turning_boundary https://polyfem.github.io/documentation/#torsionelastic

**`name()`**

**`params()`**




## class PDEs

List of supported partial differential equations

Bilaplacian = 'Bilaplacian'

Helmholtz = 'Helmholtz'

HookeLinearElasticity = 'HookeLinearElasticity'

IncompressibleLinearElasticity = 'IncompressibleLinearElasticity'

Laplacian = 'Laplacian'

LinearElasticity = 'LinearElasticity'

NeoHookean = 'NeoHookean'

NonLinearElasticity = 'NonLinearElasticity'

SaintVenant = 'SaintVenant'

Stokes = 'Stokes'




## class ScalarFormulations

Bilaplacian = 'Bilaplacian'

Helmholtz = 'Helmholtz'

Laplacian = 'Laplacian'




## class Solver

Polyfem solver

**`compute_errors()`**

compute the error

**`export_data()`**

exports all data specified in the settings

**`export_vtu(path: str)`**

exports the solution as vtu

**`export_wire(path: str, isolines: bool = False)`**

exports wireframe of the mesh

**`get_boundary_sidesets() -> tuple`**

exports get the boundary sideset, edges in 2d or trangles in 3d

**`get_log() -> str`**

gets the log as json

**`get_pressure() -> numpy.ndarray`**

returns the pressure

**`get_sampled_connectivity_frames() -> List[numpy.ndarray]`**

returns the connectivity frames for a time dependent problem on a densly sampled mesh, use 'vismesh_rel_area' to control density

**`get_sampled_mises(boundary_only: bool = False) -> numpy.ndarray`**

returns the von mises stresses on a densly sampled mesh, use 'vismesh_rel_area' to control density

**`get_sampled_mises_avg(boundary_only: bool = False) -> tuple`**

returns the von mises stresses and stress tensor averaged around a vertex on a densly sampled mesh, use 'vismesh_rel_area' to control density

**`get_sampled_mises_avg_frames() -> List[numpy.ndarray]`**

returns the von mises stresses per frame averaged around a vertex on a densly sampled mesh, use 'vismesh_rel_area' to control density

**`get_sampled_mises_frames() -> List[numpy.ndarray]`**

returns the von mises stresses frames on a densly sampled mesh, use 'vismesh_rel_area' to control density

**`get_sampled_points_frames() -> List[numpy.ndarray]`**

returns the points frames for a time dependent problem on a densly sampled mesh, use 'vismesh_rel_area' to control density

**`get_sampled_solution(boundary_only: bool = False) -> tuple`**

returns the solution on a densly sampled mesh, use 'vismesh_rel_area' to control density

**`get_sampled_solution_frames() -> List[numpy.ndarray]`**

returns the solution frames for a time dependent problem on a densly sampled mesh, use 'vismesh_rel_area' to control density

**`get_solution() -> numpy.ndarray`**

returns the solution

**`get_stresses(boundary_only: bool = False) -> numpy.ndarray`**

returns the stress tensor on a densly sampled mesh, use 'vismesh_rel_area' to control density

**`load_mesh_from_path(path: str, normalize_mesh: bool = False, vismesh_rel_area: float = 1e-05, n_refs: int = 0, boundary_id_threshold: float = -1.0)`**

Loads a mesh from the path and 'bc_tag' from the json if any bc tags

**`load_mesh_from_path_and_tags(path: str, bc_tag_path: str)`**

Loads a mesh and bc_tags from path

**`load_mesh_from_settings()`**

Loads a mesh from the 'mesh' field of the json and 'bc_tag' if any bc tags

**`set_boundary_side_set_from_bary(boundary_marker: Callable[[numpy.ndarray[float64[1, n]]], int])`**

Sets the side set for the boundary conditions, the functions takes the barycenter of the boundary (edge or face)

**`set_boundary_side_set_from_bary_and_boundary(boundary_marker: Callable[[numpy.ndarray[float64[1, n]], bool], int])`**

Sets the side set for the boundary conditions, the functions takes the barycenter of the boundary (edge or face) and a flag that says if the element is boundary

**`set_boundary_side_set_from_v_ids(boundary_marker: Callable[[List[int], bool], int])`**

Sets the side set for the boundary conditions, the functions takes the sorted list of vertex id and a flag that says if the element is boundary

**`set_high_order_mesh(vertices: numpy.ndarray, connectivity: numpy.ndarray, nodes_pos: numpy.ndarray, nodes_indices: List[List[int]])`**

Loads an high order mesh from vertices, connectivity, nodes, and node indices mapping element to nodes

**`set_log_level(log_level: int)`**

sets polyfem log level, valid value between 0 (all logs) and 6 (no logs)

**`set_mesh(vertices: numpy.ndarray, connectivity: numpy.ndarray)`**

Loads a mesh from vertices and connectivity

**`set_rhs(matrix: numpy.ndarray)`**

Sets the rhs

**`set_rhs_from_path(path: str)`**

Loads the rhs from a file

**`settings(json: object)`**

load PDE and problem parameters from the settings

**`solve()`**

solve the pde




## class TensorFormulations

HookeLinearElasticity = 'HookeLinearElasticity'

IncompressibleLinearElasticity = 'IncompressibleLinearElasticity'

LinearElasticity = 'LinearElasticity'

NeoHookean = 'NeoHookean'

NonLinearElasticity = 'NonLinearElasticity'

SaintVenant = 'SaintVenant'

Stokes = 'Stokes'




