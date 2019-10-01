## class Problem

Generic problem problem, scalar or tensor depending on the pde. Warning, this problem needs to be used with the `set_pde` function in settings

### init
`__init__(rhs=None, exact=None)`

Initialize .  See help(type()) for accurate signature.

### add_dirichlet_value
`add_dirichlet_value(id, value, is_dirichlet_dim=None)`

set the Dirichlet value value for the sideset id. Note the value must be a scalar, vector in 2D, or 3D depending on the problem. is_dirichlet_dim is a vector of boolean specifying which dimentions are fixed, only for vector-based problems.

### add_neumann_value
`add_neumann_value(id, value)`

set the Neumann value value for the sideset id. Note the value must be a scalar, vector in 2D, or 3D depending on the problem

### set_dirichlet_value
`set_dirichlet_value(id, value, is_dirichlet_dim=None)`

set the Dirichlet value value for the sideset id. Note the value must be a scalar, vector in 2D, or 3D depending on the problem. is_dirichlet_dim is a vector of boolean specifying which dimentions are fixed, only for vector-based problems.

### set_displacement
`set_displacement(id, value, is_dim_fixed=None)`

set the displacement value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

### set_force
`set_force(id, value)`

set the force value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

### set_neumann_value
`set_neumann_value(id, value)`

set the Neumann value value for the sideset id. Note the value must be a scalar, vector in 2D, or 3D depending on the problem

### set_velocity
`set_velocity(id, value, is_dim_fixed=None)`

set the velocity value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

### set_x_symmetric
`set_x_symmetric(id)`

x coorinate is fixed, y is allowed to move (Neumann)

### set_xy_symmetric
`set_xy_symmetric(id)`

xy coorinates are fixed, z is allowed to move (Neumann)

### set_xz_symmetric
`set_xz_symmetric(id)`

xz coorinates are fixed, y is allowed to move (Neumann)

### set_y_symmetric
`set_y_symmetric(id)`

y coorinate is fixed, x is allowed to move (Neumann)

### set_yz_symmetric
`set_yz_symmetric(id)`

yz coorinates are fixed, x is allowed to move (Neumann)




## class Settings

Class that encodes the settings of the solver, it models the input json file

### init
`__init__(discr_order=1, pressure_discr_order=1, pde='Laplacian', nl_solver_rhs_steps=1, tend=1, time_steps=10)`

Initialize .  See help(type()) for accurate signature.

### serialize
`serialize()`

stringyfied json description of this class, used to run the solver

### set_advanced_option
`set_advanced_option(key, value)`

Used to set any advanced option not present in this class, for instance set_advanced_option("use_spline",True), see https://polyfem.github.io/documentation/ for full list

### set_isolines_export_path
`set_isolines_export_path(path)`

Sets the path to export the isolines of the solution

### set_material_params
`set_material_params(name, value)`

set the material parameters, for instance set_material_params("E", 200) sets the Young's modulus E to 200. See https://polyfem.github.io/documentation/#formulations for full list

### set_pde
`set_pde(pde)`

Sets the PDE to solve, use any of the polyfempy.PDEs

### set_problem
`set_problem(problem)`

Sets the problem, use any of the problems in Problems or the Problem

### set_solution_export_path
`set_solution_export_path(path)`

Sets the path to save the solution

### set_vtu_export_path
`set_vtu_export_path(path, bounda_only=False)`

Sets the path to export a vtu file with the results, use bounda_only to export only one layer of the mesh in 3d

### set_wireframe_export_path
`set_wireframe_export_path(path)`

Sets the path to export a wireframe of the mesh

pde

Get the PDE

problem

Get the problem




## class DrivenCavity

Classical driven cavity problem in fluid simulation




## class Flow

Inflow/outflow problem for fluids. You can specify the sideset for the moving fluxes, the axial direction of the flow, and the list of obstacle sidesets. https://polyfem.github.io/documentation/#flow

### init
`__init__(inflow=1, outflow=3, inflow_amout=0.25, outflow_amout=0.25, direction=0, obstacle=[7])`

Initialize .  See help(type()) for accurate signature.




## class Franke

Franke problem with exact solution https://polyfem.github.io/documentation/#franke




## class GenericScalar

Generic scalar problem https://polyfem.github.io/documentation/#genericscalar

### add_dirichlet_value
`add_dirichlet_value(id, value)`

add the Dirichlet value value for the sideset id

### add_neumann_value
`add_neumann_value(id, value)`

add the Neumann value value for the sideset id




## class GenericTensor

Generic tensor problem https://polyfem.github.io/documentation/#generictensor

### add_dirichlet_value
`add_dirichlet_value(id, value, is_dirichlet_dim=None)`

add the Dirichlet value value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem. is_dirichlet_dim is a vector of boolean specifying which dimentions are fixed.

### add_neumann_value
`add_neumann_value(id, value)`

add the Neumann value value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

### set_displacement
`set_displacement(id, value, is_dim_fixed=None)`

set the displacement value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

### set_force
`set_force(id, value)`

set the force value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem

### set_velocity
`set_velocity(id, value, is_dim_fixed=None)`

set the velocity value for the sideset id. Note the value must be a vector in 2D or 3D depending on the problem




## class Gravity

time dependent gravity problem https://polyfem.github.io/documentation/#gravity

### init
`__init__(force=0.1)`

Initialize .  See help(type()) for accurate signature.




## class Torsion

3D torsion problem, specify which sideset to fix (fixed_boundary) and which one turns turning_boundary https://polyfem.github.io/documentation/#torsionelastic

### init
`__init__(axis_coordiante=2, n_turns=0.5, fixed_boundary=5, turning_boundary=6)`

Initialize .  See help(type()) for accurate signature.




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

### compute_errors
`compute_errors()`

compute the error

### export_data
`export_data()`

exports all data specified in the settings

### export_vtu
`export_vtu(path: str)`

exports the solution as vtu

### export_wire
`export_wire(path: str, isolines: bool = False)`

exports wireframe of the mesh

### get_boundary_sidesets
`get_boundary_sidesets() -> tuple`

exports get the boundary sideset, edges in 2d or trangles in 3d

### get_log
`get_log() -> str`

gets the log as json

### get_pressure
`get_pressure() -> array`

returns the pressure

### get_sampled_connectivity_frames
`get_sampled_connectivity_frames() -> List[array]`

returns the connectivity frames for a time dependent problem on a densly sampled mesh, use 'vismesh_rel_area' to control density

### get_sampled_mises
`get_sampled_mises(boundary_only: bool = False) -> array`

returns the von mises stresses on a densly sampled mesh, use 'vismesh_rel_area' to control density

### get_sampled_mises_avg
`get_sampled_mises_avg(boundary_only: bool = False) -> tuple`

returns the von mises stresses and stress tensor averaged around a vertex on a densly sampled mesh, use 'vismesh_rel_area' to control density

### get_sampled_mises_avg_frames
`get_sampled_mises_avg_frames() -> List[array]`

returns the von mises stresses per frame averaged around a vertex on a densly sampled mesh, use 'vismesh_rel_area' to control density

### get_sampled_mises_frames
`get_sampled_mises_frames() -> List[array]`

returns the von mises stresses frames on a densly sampled mesh, use 'vismesh_rel_area' to control density

### get_sampled_points_frames
`get_sampled_points_frames() -> List[array]`

returns the points frames for a time dependent problem on a densly sampled mesh, use 'vismesh_rel_area' to control density

### get_sampled_solution
`get_sampled_solution(boundary_only: bool = False) -> tuple`

returns the solution on a densly sampled mesh, use 'vismesh_rel_area' to control density

### get_sampled_solution_frames
`get_sampled_solution_frames() -> List[array]`

returns the solution frames for a time dependent problem on a densly sampled mesh, use 'vismesh_rel_area' to control density

### get_solution
`get_solution() -> array`

returns the solution

### get_stresses
`get_stresses(boundary_only: bool = False) -> array`

returns the stress tensor on a densly sampled mesh, use 'vismesh_rel_area' to control density

### load_mesh_from_path
`load_mesh_from_path(path: str, normalize_mesh: bool = False, vismesh_rel_area: float = 1e-05, n_refs: int = 0, boundary_id_threshold: float = -1.0)`

Loads a mesh from the path and 'bc_tag' from the json if any bc tags

### load_mesh_from_path_and_tags
`load_mesh_from_path_and_tags(path: str, bc_tag_path: str, normalize_mesh: bool = False, vismesh_rel_area: float = 1e-05, n_refs: int = 0, boundary_id_threshold: float = -1.0)`

Loads a mesh and bc_tags from path

### load_mesh_from_settings
`load_mesh_from_settings(normalize_mesh: bool = False, vismesh_rel_area: float = 1e-05, n_refs: int = 0, boundary_id_threshold: float = -1.0)`

Loads a mesh from the 'mesh' field of the json and 'bc_tag' if any bc tags

### set_boundary_side_set_from_bary
`set_boundary_side_set_from_bary(boundary_marker: Callable[[array[float64[1, n]]], int])`

Sets the side set for the boundary conditions, the functions takes the barycenter of the boundary (edge or face)

### set_boundary_side_set_from_bary_and_boundary
`set_boundary_side_set_from_bary_and_boundary(boundary_marker: Callable[[array[float64[1, n]], bool], int])`

Sets the side set for the boundary conditions, the functions takes the barycenter of the boundary (edge or face) and a flag that says if the element is boundary

### set_boundary_side_set_from_v_ids
`set_boundary_side_set_from_v_ids(boundary_marker: Callable[[List[int], bool], int])`

Sets the side set for the boundary conditions, the functions takes the sorted list of vertex id and a flag that says if the element is boundary

### set_high_order_mesh
`set_high_order_mesh(vertices: array, connectivity: array, nodes_pos: array, nodes_indices: List[List[int]], normalize_mesh: bool = False, vismesh_rel_area: float = 1e-05, n_refs: int = 0, boundary_id_threshold: float = -1.0)`

Loads an high order mesh from vertices, connectivity, nodes, and node indices mapping element to nodes

### set_log_level
`set_log_level(log_level: int)`

sets polyfem log level, valid value between 0 (all logs) and 6 (no logs)

### set_mesh
`set_mesh(vertices: array, connectivity: array, normalize_mesh: bool = False, vismesh_rel_area: float = 1e-05, n_refs: int = 0, boundary_id_threshold: float = -1.0)`

Loads a mesh from vertices and connectivity

### set_rhs
`set_rhs(matrix: array)`

Sets the rhs

### set_rhs_from_path
`set_rhs_from_path(path: str)`

Loads the rhs from a file

### set_settings
`set_settings(json: object)`

load PDE and problem parameters from the settings

### settings
`settings(json: object)`

load PDE and problem parameters from the settings

### solve
`solve()`

solve the pde




## class TensorFormulations

HookeLinearElasticity = 'HookeLinearElasticity'

IncompressibleLinearElasticity = 'IncompressibleLinearElasticity'

LinearElasticity = 'LinearElasticity'

NeoHookean = 'NeoHookean'

NonLinearElasticity = 'NonLinearElasticity'

SaintVenant = 'SaintVenant'

Stokes = 'Stokes'




