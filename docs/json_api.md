---
template: no_toc.html
---
<!--Automatically generated using JSON Spec Engine-->








!!! json-spec "`/` (`object`)"
    ```
    /
    ```
    ## Description
    Root of the configuration file.
    ## Required





    ??? json-spec "`/geometry` (`list`)"
        ```
        /geometry
        ```
        ## Description
        List of geometry objects.





        ??? json-spec "`/geometry/*` (`object`)"
            ```
            /geometry/*
            ```
            ## Description
            Each geometry object stores a mesh, a set of transformations applied to it after loading, and a set of selections, which can be used to specify boundary conditions, materials, optimization parameters and other quantities that can be associated with a part of an object.
            ## Required





            ??? json-spec "`/geometry/*/mesh` (`file`)"
                ```
                /geometry/*/mesh
                ```
                ## Description
                Path of the mesh file to load.
            
                **Extensions:** `['.obj', '.msh', '.stl', '.ply', '.mesh']`



            ## Optional





            ??? json-spec "`/geometry/*/type` (`string`)"
                ```
                /geometry/*/type
                ```
                ## Description
                Type of geometry, currently only one supported. In future we will add stuff like planes, spheres, etc.
            
                **Default**: `'mesh'`
            
                **Options:** `['mesh']`








            ??? json-spec "`/geometry/*/extract` (`string`)"
                ```
                /geometry/*/extract
                ```
                ## Description
                Used to extract stuff from the mesh. Eg extract surface extracts the surface from a tet mesh.
            
                **Default**: `'volume'`
            
                **Options:** `['volume', 'edges', 'points', 'surface']`








            ??? json-spec "`/geometry/*/transformation` (`object`)"
                ```
                /geometry/*/transformation
                ```
                ## Description
                Geometric transformations applied to the geometry after loading it.
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/geometry/*/transformation/translation` (`list`)"
                    ```
                    /geometry/*/transformation/translation
                    ```
                    ## Description
                    Translate (two entries for 2D problems or three entries for 3D problems).





                    ??? json-spec "`/geometry/*/transformation/translation/*` (`float`)"
                        ```
                        /geometry/*/transformation/translation/*
                        ```
                        ## Description
                        FIXME: Missing documentation in the specification.
                    
                        **Default**: `0`











                ??? json-spec "`/geometry/*/transformation/rotation` (`list`)"
                    ```
                    /geometry/*/transformation/rotation
                    ```
                    ## Description
                    Rotate, in 2D, one number, the rotation angle, in 3D, three or four Euler angles, axis+angle, or a unit quaternion. Depends on rotation mode.





                    ??? json-spec "`/geometry/*/transformation/rotation/*` (`float`)"
                        ```
                        /geometry/*/transformation/rotation/*
                        ```
                        ## Description
                        FIXME: Missing documentation in the specification.
                    
                        **Default**: `0`











                ??? json-spec "`/geometry/*/transformation/rotation_mode` (`string`)"
                    ```
                    /geometry/*/transformation/rotation_mode
                    ```
                    ## Description
                    Type of rotation, supported are any permutation of [xyz]+, axis_angle, quaternion, or rotation_vector.
                
                    **Default**: `'xyz'`








                ??? json-spec "`/geometry/*/transformation/scale` (`list`)"
                    ```
                    /geometry/*/transformation/scale
                    ```
                    ## Description
                    Scale by specified factors along axes (two entries for 2D problems or three entries for 3D problems).





                    ??? json-spec "`/geometry/*/transformation/scale/*` (`float`)"
                        ```
                        /geometry/*/transformation/scale/*
                        ```
                        ## Description
                        FIXME: Missing documentation in the specification.
                    
                        **Default**: `0`









                ??? json-spec "`/geometry/*/transformation/dimensions`"
                    ```
                    /geometry/*/transformation/dimensions
                    ```


                    === "`/geometry/*/transformation/dimensions` (`float`)"
                        ## Description
                        Scale the object so that bounding box dimensions match specified dimensions, 2 entries for 2D problems, 3 entries for 3D problems.
                    
                        **Default**: `1`



                    === "`/geometry/*/transformation/dimensions` (`list`)"
                        ## Description
                        Scale the object so that bounding box dimensions match specified dimensions, 2 entries for 2D problems, 3 entries for 3D problems.





                        ??? json-spec "`/geometry/*/transformation/dimensions/*` (`float`)"
                            ```
                            /geometry/*/transformation/dimensions/*
                            ```
                            ## Description
                            FIXME: Missing documentation in the specification.
                        
                            **Default**: `0`












            ??? json-spec "`/geometry/*/volume_selection`"
                ```
                /geometry/*/volume_selection
                ```


                === "`/geometry/*/volume_selection` (`int`)"
                    ## Description
                    Assign specified ID to all volume elements of the geometry (negative values indicate using the stored values in the MSH (default: 0)).
                
                    **Default**: `-1`



                === "`/geometry/*/volume_selection` (`object`)"
                    ## Description
                    Offsets the volume IDs loaded from the mesh.
                    ## Required





                    ??? json-spec "`/geometry/*/volume_selection/id_offset` (`int`)"
                        ```
                        /geometry/*/volume_selection/id_offset
                        ```
                        ## Description
                        Offsets the volume IDs loaded from the mesh.
                    
                        **Default**: `0`






                === "`/geometry/*/volume_selection` (`list`)"
                    ## Description
                    List of selection (ID assignment) operations to apply to the geometry; operations can be box, sphere, etc.



                    ??? json-spec "`/geometry/*/volume_selection/*`"
                        ```
                        /geometry/*/volume_selection/*
                        ```


                        === "`/geometry/*/volume_selection/*` (`object`)"
                            ## Description
                            Assign the ID to all volume elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                        
                            **Default**: `None`
                            ## Required





                            ??? json-spec "`/geometry/*/volume_selection/*/id` (`int`)"
                                ```
                                /geometry/*/volume_selection/*/id
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/box` (`list`)"
                                ```
                                /geometry/*/volume_selection/*/box
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/volume_selection/*/box/*` (`list`)"
                                    ```
                                    /geometry/*/volume_selection/*/box/*
                                    ```
                                    ## Description
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/volume_selection/*/box/*/*` (`float`)"
                                        ```
                                        /geometry/*/volume_selection/*/box/*/*
                                        ```
                                        ## Description
                                        FIXME: Missing documentation in the specification.
                                    
                                        **Default**: `0`









                            ## Optional





                            ??? json-spec "`/geometry/*/volume_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/volume_selection/*/relative
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `False`






                        === "`/geometry/*/volume_selection/*` (`object`)"
                            ## Description
                            Assign the ID to all volume elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                        
                            **Default**: `None`
                            ## Required





                            ??? json-spec "`/geometry/*/volume_selection/*/id` (`int`)"
                                ```
                                /geometry/*/volume_selection/*/id
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/radius` (`float`)"
                                ```
                                /geometry/*/volume_selection/*/radius
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/center` (`list`)"
                                ```
                                /geometry/*/volume_selection/*/center
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/volume_selection/*/center/*` (`float`)"
                                    ```
                                    /geometry/*/volume_selection/*/center/*
                                    ```
                                    ## Description
                                    FIXME: Missing documentation in the specification.






                            ## Optional





                            ??? json-spec "`/geometry/*/volume_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/volume_selection/*/relative
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `False`






                        === "`/geometry/*/volume_selection/*` (`object`)"
                            ## Description
                            Assign the ID to all volume elements with barycenters in a halfspace. The halfspace boundary plane is defined in one of two ways: (1) by a point in the plane and the normal, which points to the halfspace. (2) By a normal and the offset from the coordinate system origin along the line in the direction of the normal passing through the origin. In the former case, the option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                        
                            **Default**: `None`
                            ## Required





                            ??? json-spec "`/geometry/*/volume_selection/*/id` (`int`)"
                                ```
                                /geometry/*/volume_selection/*/id
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/point` (`list`)"
                                ```
                                /geometry/*/volume_selection/*/point
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/volume_selection/*/point/*` (`float`)"
                                    ```
                                    /geometry/*/volume_selection/*/point/*
                                    ```
                                    ## Description
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/geometry/*/volume_selection/*/normal` (`list`)"
                                ```
                                /geometry/*/volume_selection/*/normal
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/volume_selection/*/normal/*` (`float`)"
                                    ```
                                    /geometry/*/volume_selection/*/normal/*
                                    ```
                                    ## Description
                                    FIXME: Missing documentation in the specification.






                            ## Optional





                            ??? json-spec "`/geometry/*/volume_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/volume_selection/*/relative
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `False`








                            ??? json-spec "`/geometry/*/volume_selection/*/offset` (`float`)"
                                ```
                                /geometry/*/volume_selection/*/offset
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.






                        === "`/geometry/*/volume_selection/*` (`object`)"
                            ## Description
                            Same as halfspace, but the boundary plane is axis-aligned. The choice of axis is specified either by a string matching the regexp r"[+-][xyzXYZ]" or an int matching the regular expression [+-]?[123] where the sign is the side of the plane to select and letter or number indicates the axis to which the plane is perpendicular. The offset is the plane offset from the origin. If the relative option is set to true, the offset is with respect to the center of the bounding box.
                        
                            **Default**: `None`
                            ## Required





                            ??? json-spec "`/geometry/*/volume_selection/*/id` (`int`)"
                                ```
                                /geometry/*/volume_selection/*/id
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.






                            ??? json-spec "`/geometry/*/volume_selection/*/axis`"
                                ```
                                /geometry/*/volume_selection/*/axis
                                ```


                                === "`/geometry/*/volume_selection/*/axis` (`int`)"
                                    ## Description
                                    FIXME: Missing documentation in the specification.



                                === "`/geometry/*/volume_selection/*/axis` (`string`)"
                                    ## Description
                                    FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/position` (`float`)"
                                ```
                                /geometry/*/volume_selection/*/position
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.



                            ## Optional





                            ??? json-spec "`/geometry/*/volume_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/volume_selection/*/relative
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `False`









                === "`/geometry/*/volume_selection` (`file`)"
                    ## Description
                    Load ids from a file; the file is required to have one ID per volume element of the geometry
                
                    **Extensions:** `['.txt']`






            ??? json-spec "`/geometry/*/surface_selection`"
                ```
                /geometry/*/surface_selection
                ```


                === "`/geometry/*/surface_selection` (`int`)"
                    ## Description
                    Assign specified ID to all surface elements of the geometry
                
                    **Default**: `0`



                === "`/geometry/*/surface_selection` (`object`)"
                    ## Description
                    Assigns ids to sides touching the bbox of the model using a threshold. Assigns 1+offset to left, 2+offset to bottom, 3+offset to right, 4+offset to top, 5+offset to front, 6+offset to back, 7+offset to everything else.
                    ## Optional





                    ??? json-spec "`/geometry/*/surface_selection/threshold` (`float`)"
                        ```
                        /geometry/*/surface_selection/threshold
                        ```
                        ## Description
                        FIXME: Missing documentation in the specification.
                    
                        **Default**: `-1`








                    ??? json-spec "`/geometry/*/surface_selection/offset` (`int`)"
                        ```
                        /geometry/*/surface_selection/offset
                        ```
                        ## Description
                        FIXME: Missing documentation in the specification.
                    
                        **Default**: `0`






                === "`/geometry/*/surface_selection` (`list`)"
                    ## Description
                    List of selection (ID assignment) operations to apply to the geometry; operations can be box, sphere, etc.



                    ??? json-spec "`/geometry/*/surface_selection/*`"
                        ```
                        /geometry/*/surface_selection/*
                        ```


                        === "`/geometry/*/surface_selection/*` (`object`)"
                            ## Description
                            Assign the ID to all surface elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                        
                            **Default**: `None`
                            ## Required





                            ??? json-spec "`/geometry/*/surface_selection/*/id` (`int`)"
                                ```
                                /geometry/*/surface_selection/*/id
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/box` (`list`)"
                                ```
                                /geometry/*/surface_selection/*/box
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/surface_selection/*/box/*` (`list`)"
                                    ```
                                    /geometry/*/surface_selection/*/box/*
                                    ```
                                    ## Description
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/surface_selection/*/box/*/*` (`float`)"
                                        ```
                                        /geometry/*/surface_selection/*/box/*/*
                                        ```
                                        ## Description
                                        FIXME: Missing documentation in the specification.
                                    
                                        **Default**: `0`









                            ## Optional





                            ??? json-spec "`/geometry/*/surface_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/surface_selection/*/relative
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `False`






                        === "`/geometry/*/surface_selection/*` (`object`)"
                            ## Description
                            Assign the ID to all surface elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                        
                            **Default**: `None`
                            ## Required





                            ??? json-spec "`/geometry/*/surface_selection/*/id` (`int`)"
                                ```
                                /geometry/*/surface_selection/*/id
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/radius` (`float`)"
                                ```
                                /geometry/*/surface_selection/*/radius
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/center` (`list`)"
                                ```
                                /geometry/*/surface_selection/*/center
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/surface_selection/*/center/*` (`float`)"
                                    ```
                                    /geometry/*/surface_selection/*/center/*
                                    ```
                                    ## Description
                                    FIXME: Missing documentation in the specification.






                            ## Optional





                            ??? json-spec "`/geometry/*/surface_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/surface_selection/*/relative
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `False`






                        === "`/geometry/*/surface_selection/*` (`object`)"
                            ## Description
                            Assign the ID to all surface elements with barycenters in a halfspace. The halfspace boundary plane is defined in one of two ways: (1) by a point in the plane and the normal, which points to the halfspace. (2) By a normal and the offset from the coordinate system origin along the line in the direction of the normal passing through the origin. In the former case, the option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                        
                            **Default**: `None`
                            ## Required





                            ??? json-spec "`/geometry/*/surface_selection/*/id` (`int`)"
                                ```
                                /geometry/*/surface_selection/*/id
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/point` (`list`)"
                                ```
                                /geometry/*/surface_selection/*/point
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/surface_selection/*/point/*` (`float`)"
                                    ```
                                    /geometry/*/surface_selection/*/point/*
                                    ```
                                    ## Description
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/geometry/*/surface_selection/*/normal` (`list`)"
                                ```
                                /geometry/*/surface_selection/*/normal
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/surface_selection/*/normal/*` (`float`)"
                                    ```
                                    /geometry/*/surface_selection/*/normal/*
                                    ```
                                    ## Description
                                    FIXME: Missing documentation in the specification.






                            ## Optional





                            ??? json-spec "`/geometry/*/surface_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/surface_selection/*/relative
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `False`








                            ??? json-spec "`/geometry/*/surface_selection/*/offset` (`float`)"
                                ```
                                /geometry/*/surface_selection/*/offset
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.






                        === "`/geometry/*/surface_selection/*` (`object`)"
                            ## Description
                            Same as halfspace, but the boundary plane is axis-aligned. The choice of axis is specified either by a string matching the regexp r"[+-][xyzXYZ]" or an int matching the regular expression [+-]?[123] where the sign is the side of the plane to select and letter or number indicates the axis to which the plane is perpendicular. The offset is the plane offset from the origin. If the relative option is set to true, the offset is with respect to the center of the bounding box.
                        
                            **Default**: `None`
                            ## Required





                            ??? json-spec "`/geometry/*/surface_selection/*/id` (`int`)"
                                ```
                                /geometry/*/surface_selection/*/id
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.






                            ??? json-spec "`/geometry/*/surface_selection/*/axis`"
                                ```
                                /geometry/*/surface_selection/*/axis
                                ```


                                === "`/geometry/*/surface_selection/*/axis` (`int`)"
                                    ## Description
                                    FIXME: Missing documentation in the specification.



                                === "`/geometry/*/surface_selection/*/axis` (`string`)"
                                    ## Description
                                    FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/position` (`float`)"
                                ```
                                /geometry/*/surface_selection/*/position
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.



                            ## Optional





                            ??? json-spec "`/geometry/*/surface_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/surface_selection/*/relative
                                ```
                                ## Description
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `False`









                === "`/geometry/*/surface_selection` (`file`)"
                    ## Description
                    Load ids from a file; the file has a list of surface elements of the geometry specified as triples of vertex indices, with one ID for each; each triple must correspond to a surface element
                
                    **Extensions:** `['.txt']`








            ??? json-spec "`/geometry/*/curve_selection` (`object`)"
                ```
                /geometry/*/curve_selection
                ```
                ## Description
                Selection of curves
            
                **Default**: `None`








            ??? json-spec "`/geometry/*/point_selection` (`object`)"
                ```
                /geometry/*/point_selection
                ```
                ## Description
                Selection of points
            
                **Default**: `None`








            ??? json-spec "`/geometry/*/n_refs` (`int`)"
                ```
                /geometry/*/n_refs
                ```
                ## Description
                number of uniform refinements
            
                **Default**: `0`








            ??? json-spec "`/geometry/*/advanced` (`object`)"
                ```
                /geometry/*/advanced
                ```
                ## Description
                Advanced options for geometry
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/geometry/*/advanced/normalize_mesh` (`bool`)"
                    ```
                    /geometry/*/advanced/normalize_mesh
                    ```
                    ## Description
                    Rescale the mesh to it fits in the biunit cube
                
                    **Default**: `False`








                ??? json-spec "`/geometry/*/advanced/force_linear_geometry` (`bool`)"
                    ```
                    /geometry/*/advanced/force_linear_geometry
                    ```
                    ## Description
                    Discard high-order nodes for curved geometries
                
                    **Default**: `False`








                ??? json-spec "`/geometry/*/advanced/refinement_location` (`float`)"
                    ```
                    /geometry/*/advanced/refinement_location
                    ```
                    ## Description
                    parametric location of the refinement
                
                    **Default**: `0.5`








                ??? json-spec "`/geometry/*/advanced/min_component` (`int`)"
                    ```
                    /geometry/*/advanced/min_component
                    ```
                    ## Description
                    Size of the minumum component for collision
                
                    **Default**: `-1`











            ??? json-spec "`/geometry/*/enabled` (`bool`)"
                ```
                /geometry/*/enabled
                ```
                ## Description
                Skips the geometry if false
            
                **Default**: `True`








            ??? json-spec "`/geometry/*/is_obstacle` (`bool`)"
                ```
                /geometry/*/is_obstacle
                ```
                ## Description
                The geometry elements are not included in deforming geometry, only in collision computations
            
                **Default**: `False`














    ??? json-spec "`/materials` (`list`)"
        ```
        /materials
        ```
        ## Description
        Material Parameters lists including ID pointing to volume selection, Young's modulus ($E$), Poisson's ratio ($\nu$), Density ($\rho$), or Lamé constants ($\lambda$ and $\mu$).



        ??? json-spec "`/materials/*`"
            ```
            /materials/*
            ```


            === "NeoHookean"
            
                **Type**: NeoHookean
                ## Description
                Material Parameters including ID, Young's modulus ($E$), Poisson's ratio ($\nu$), density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    ## Description
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    ## Description
                    Poisson's ratio



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "NeoHookean"
            
                **Type**: NeoHookean
                ## Description
                Material Parameters including ID, Lamé first ($\lambda$), Lamé second ($\mu$), density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/lambda` (`float`)"
                    ```
                    /materials/*/lambda
                    ```
                    ## Description
                    Second Lamé parameter








                ??? json-spec "`/materials/*/mu` (`float`)"
                    ```
                    /materials/*/mu
                    ```
                    ## Description
                    First Lamé parameters



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "LinearElasticity"
            
                **Type**: LinearElasticity
                ## Description
                Material Parameters including ID, Young's modulus ($E$), Poisson's ratio ($\nu$), density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    ## Description
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    ## Description
                    Poisson's ratio



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "LinearElasticity"
            
                **Type**: LinearElasticity
                ## Description
                Material Parameters including ID, Lamé first ($\lambda$), Lamé second ($\mu$), density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/lambda` (`float`)"
                    ```
                    /materials/*/lambda
                    ```
                    ## Description
                    Second Lamé parameter








                ??? json-spec "`/materials/*/mu` (`float`)"
                    ```
                    /materials/*/mu
                    ```
                    ## Description
                    First Lamé parameters



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "HookeLinearElasticity"
            
                **Type**: HookeLinearElasticity
                ## Description
                Material Parameters including ID, E, nu, density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    ## Description
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    ## Description
                    Poisson's ratio



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "HookeLinearElasticity"
            
                **Type**: HookeLinearElasticity
                ## Description
                Material Parameters including ID, E, nu, density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/elasticity_tensor` (`list`)"
                    ```
                    /materials/*/elasticity_tensor
                    ```
                    ## Description
                    Symmetric elasticity tensor





                    ??? json-spec "`/materials/*/elasticity_tensor/*` (`float`)"
                        ```
                        /materials/*/elasticity_tensor/*
                        ```
                        ## Description
                        Entries of elasticity tensor
                    
                        **Default**: `0`






                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "SaintVenant"
            
                **Type**: SaintVenant
                ## Description
                Material Parameters including ID, E, nu, density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    ## Description
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    ## Description
                    Poisson's ratio



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "SaintVenant"
            
                **Type**: SaintVenant
                ## Description
                Material Parameters including ID, E, nu, density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/elasticity_tensor` (`list`)"
                    ```
                    /materials/*/elasticity_tensor
                    ```
                    ## Description
                    Symmetric elasticity tensor





                    ??? json-spec "`/materials/*/elasticity_tensor/*` (`float`)"
                        ```
                        /materials/*/elasticity_tensor/*
                        ```
                        ## Description
                        Entries of elasticity tensor
                    
                        **Default**: `0`






                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "Stokes"
            
                **Type**: Stokes
                ## Description
                Material Parameters including ID, viscosity, density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/viscosity` (`float`)"
                    ```
                    /materials/*/viscosity
                    ```
                    ## Description
                    Fuild's viscosity



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "NavierStokes"
            
                **Type**: NavierStokes
                ## Description
                Material Parameters including ID, viscosity, density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/viscosity` (`float`)"
                    ```
                    /materials/*/viscosity
                    ```
                    ## Description
                    Fuild's viscosity



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "IncompressibleLinearElasticity"
            
                **Type**: IncompressibleLinearElasticity
                ## Description
                Material Parameters including ID, Young's modulus ($E$), Poisson's ratio ($\nu$), density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    ## Description
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    ## Description
                    Poisson's ratio



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "IncompressibleLinearElasticity"
            
                **Type**: IncompressibleLinearElasticity
                ## Description
                Material Parameters including ID, Lamé first ($\lambda$), Lamé second ($\mu$), density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/lambda` (`float`)"
                    ```
                    /materials/*/lambda
                    ```
                    ## Description
                    Second Lamé parameter








                ??? json-spec "`/materials/*/mu` (`float`)"
                    ```
                    /materials/*/mu
                    ```
                    ## Description
                    First Lamé parameters



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "Laplacian"
            
                **Type**: Laplacian
                ## Description
                Material Parameters including ID, density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`






            === "Helmholtz"
            
                **Type**: Helmholtz
                ## Description
                Material Parameters including ID, k, density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`








                ??? json-spec "`/materials/*/k` (`float`)"
                    ```
                    /materials/*/k
                    ```
                    ## Description
                    Scaling for Helmholtz
                
                    **Default**: `1`






            === "Bilaplacian"
            
                **Type**: Bilaplacian
                ## Description
                Material Parameters including ID, density ($\rho$)
                ## Required





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    ## Description
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`



                ## Optional





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    ## Description
                    Volume selection ID
                
                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    ## Description
                    Density
                
                    **Default**: `1`









    ## Optional



    ??? json-spec "`/preset_problem`"
        ```
        /preset_problem
        ```


        === "Linear"
        
            **Type**: Linear
            ## Description
            TODO
        
            **Default**: `'skip'`
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Quadratic"
        
            **Type**: Quadratic
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Cubic"
        
            **Type**: Cubic
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Sine"
        
            **Type**: Sine
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Franke"
        
            **Type**: Franke
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "FrankeOld"
        
            **Type**: FrankeOld
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "GenericScalarExact"
        
            **Type**: GenericScalarExact
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? json-spec "`/preset_problem/func` (`int`)"
                ```
                /preset_problem/func
                ```
                ## Description
                TODO
            
                **Default**: `0`






        === "Zero_BC"
        
            **Type**: Zero_BC
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Elastic"
        
            **Type**: Elastic
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Walk"
        
            **Type**: Walk
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "TorsionElastic"
        
            **Type**: TorsionElastic
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? json-spec "`/preset_problem/axis_coordiante` (`int`)"
                ```
                /preset_problem/axis_coordiante
                ```
                ## Description
                TODO
            
                **Default**: `2`








            ??? json-spec "`/preset_problem/n_turns` (`float`)"
                ```
                /preset_problem/n_turns
                ```
                ## Description
                TODO
            
                **Default**: `0.5`








            ??? json-spec "`/preset_problem/fixed_boundary` (`int`)"
                ```
                /preset_problem/fixed_boundary
                ```
                ## Description
                TODO
            
                **Default**: `5`








            ??? json-spec "`/preset_problem/turning_boundary` (`int`)"
                ```
                /preset_problem/turning_boundary
                ```
                ## Description
                TODO
            
                **Default**: `6`








            ??? json-spec "`/preset_problem/bbox_center` (`list`)"
                ```
                /preset_problem/bbox_center
                ```
                ## Description
                TODO





                ??? json-spec "`/preset_problem/bbox_center/*` (`float`)"
                    ```
                    /preset_problem/bbox_center/*
                    ```
                    ## Description
                    TODO
                
                    **Default**: `0`









        === "DoubleTorsionElastic"
        
            **Type**: DoubleTorsionElastic
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? json-spec "`/preset_problem/axis_coordiante0` (`int`)"
                ```
                /preset_problem/axis_coordiante0
                ```
                ## Description
                TODO
            
                **Default**: `2`








            ??? json-spec "`/preset_problem/axis_coordiante1` (`int`)"
                ```
                /preset_problem/axis_coordiante1
                ```
                ## Description
                TODO
            
                **Default**: `2`








            ??? json-spec "`/preset_problem/angular_v0` (`float`)"
                ```
                /preset_problem/angular_v0
                ```
                ## Description
                TODO
            
                **Default**: `0.5`








            ??? json-spec "`/preset_problem/angular_v1` (`float`)"
                ```
                /preset_problem/angular_v1
                ```
                ## Description
                TODO
            
                **Default**: `-0.5`








            ??? json-spec "`/preset_problem/turning_boundary0` (`int`)"
                ```
                /preset_problem/turning_boundary0
                ```
                ## Description
                TODO
            
                **Default**: `5`








            ??? json-spec "`/preset_problem/turning_boundary1` (`int`)"
                ```
                /preset_problem/turning_boundary1
                ```
                ## Description
                TODO
            
                **Default**: `6`








            ??? json-spec "`/preset_problem/bbox_center` (`list`)"
                ```
                /preset_problem/bbox_center
                ```
                ## Description
                TODO





                ??? json-spec "`/preset_problem/bbox_center/*` (`float`)"
                    ```
                    /preset_problem/bbox_center/*
                    ```
                    ## Description
                    TODO
                
                    **Default**: `0`









        === "ElasticZeroBC"
        
            **Type**: ElasticZeroBC
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "ElasticExact"
        
            **Type**: ElasticExact
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "ElasticCantileverExact"
        
            **Type**: ElasticCantileverExact
            ## Description
            TODO, add displacement, E, nu, formulation, mesh_size
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "CompressionElasticExact"
        
            **Type**: CompressionElasticExact
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "QuadraticElasticExact"
        
            **Type**: QuadraticElasticExact
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "LinearElasticExact"
        
            **Type**: LinearElasticExact
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "PointBasedTensor"
        
            **Type**: PointBasedTensor
            ## Description
            TODO, add optionals
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Kernel"
        
            **Type**: Kernel
            ## Description
            TODO, add optionals
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? json-spec "`/preset_problem/formulation` (`string`)"
                ```
                /preset_problem/formulation
                ```
                ## Description
                TODO
            
                **Default**: `''`








            ??? json-spec "`/preset_problem/n_kernels` (`int`)"
                ```
                /preset_problem/n_kernels
                ```
                ## Description
                TODO
            
                **Default**: `0`








            ??? json-spec "`/preset_problem/kernel_distance` (`float`)"
                ```
                /preset_problem/kernel_distance
                ```
                ## Description
                TODO
            
                **Default**: `0`








            ??? json-spec "`/preset_problem/kernel_weights` (`string`)"
                ```
                /preset_problem/kernel_weights
                ```
                ## Description
                TODO
            
                **Default**: `''`






        === "Node"
        
            **Type**: Node
            ## Description
            TODO, add optionals
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "TimeDependentScalar"
        
            **Type**: TimeDependentScalar
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "MinSurf"
        
            **Type**: MinSurf
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Gravity"
        
            **Type**: Gravity
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        === "ConstantVelocity"
        
            **Type**: ConstantVelocity
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "TwoSpheres"
        
            **Type**: TwoSpheres
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "DrivenCavity"
        
            **Type**: DrivenCavity
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "DrivenCavityC0"
        
            **Type**: DrivenCavityC0
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "DrivenCavitySmooth"
        
            **Type**: DrivenCavitySmooth
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Flow"
        
            **Type**: Flow
            ## Description
            TODO, add inflow, outflow, inflow_amout, outflow_amout, direction, obstacle
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "FlowWithObstacle"
        
            **Type**: FlowWithObstacle
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        === "CornerFlow"
        
            **Type**: CornerFlow
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional













        === "UnitFlowWithObstacle"
        
            **Type**: UnitFlowWithObstacle
            ## Description
            TODO, add inflow_id, direction, no_slip
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        === "StokesLaw"
        
            **Type**: StokesLaw
            ## Description
            TODO, add radius
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional













        === "TaylorGreenVortex"
        
            **Type**: TaylorGreenVortex
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        === "SimpleStokeProblemExact"
        
            **Type**: SimpleStokeProblemExact
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? json-spec "`/preset_problem/func` (`int`)"
                ```
                /preset_problem/func
                ```
                ## Description
                TODO
            
                **Default**: `0`






        === "SineStokeProblemExact"
        
            **Type**: SineStokeProblemExact
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "TransientStokeProblemExact"
        
            **Type**: TransientStokeProblemExact
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? json-spec "`/preset_problem/func` (`int`)"
                ```
                /preset_problem/func
                ```
                ## Description
                TODO
            
                **Default**: `0`











        === "Kovnaszy"
        
            **Type**: Kovnaszy
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional













        === "Airfoil"
        
            **Type**: Airfoil
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        === "Lshape"
        
            **Type**: Lshape
            ## Description
            TODO
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional













        === "TestProblem"
        
            **Type**: TestProblem
            ## Description
            TODO, type, omega, is_scalar
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "BilaplacianProblemWithSolution"
        
            **Type**: BilaplacianProblemWithSolution
            ## Description
            TODO, type, omega, is_scalar
            ## Required





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                TODO
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`











    ??? json-spec "`/common` (`file`)"
        ```
        /common
        ```
        ## Description
        Path to common settings will patch the current file.
    
        **Default**: `''`
    
        **Extensions:** `['.json']`








    ??? json-spec "`/root_path` (`string`)"
        ```
        /root_path
        ```
        ## Description
        Path for all relative paths, set automatically to the folder containing this json.
    
        **Default**: `''`








    ??? json-spec "`/space` (`object`)"
        ```
        /space
        ```
        ## Description
        Options related to the FE space.
    
        **Default**: `None`
        ## Optional



        ??? json-spec "`/space/discr_order`"
            ```
            /space/discr_order
            ```


            === "`/space/discr_order` (`int`)"
                ## Description
                Lagrange element order for the space for the main unknown, for all elements.
            
                **Default**: `1`



            === "`/space/discr_order` (`file`)"
                ## Description
                Path to file containing Lagrange element order for the space for the main unknown per element.
            
                **Extensions:** `['.txt', '.bin']`



            === "`/space/discr_order` (`list`)"
                ## Description
                List of Lagrange element order for the space for the main unknown with volume IDs.





                ??? json-spec "`/space/discr_order/*` (`object`)"
                    ```
                    /space/discr_order/*
                    ```
                    ## Description
                    Lagrange element order for the a space tagged with volume ID for the main unknown.
                    ## Required



                    ??? json-spec "`/space/discr_order/*/id`"
                        ```
                        /space/discr_order/*/id
                        ```


                        === "`/space/discr_order/*/id` (`int`)"
                            ## Description
                            Volume selection ID to apply the discr_order to.



                        === "`/space/discr_order/*/id` (`list`)"
                            ## Description
                            List of volume selection IDs to apply the discr_order to.





                            ??? json-spec "`/space/discr_order/*/id/*` (`int`)"
                                ```
                                /space/discr_order/*/id/*
                                ```
                                ## Description
                                Volume selection ID to apply the discr_order to.











                    ??? json-spec "`/space/discr_order/*/order` (`int`)"
                        ```
                        /space/discr_order/*/order
                        ```
                        ## Description
                        Lagrange element order for the space for the main unknown, for all elements.














        ??? json-spec "`/space/pressure_discr_order` (`int`)"
            ```
            /space/pressure_discr_order
            ```
            ## Description
             Lagrange element order for the space for the pressure unknown, for all elements.
        
            **Default**: `1`








        ??? json-spec "`/space/use_p_ref` (`bool`)"
            ```
            /space/use_p_ref
            ```
            ## Description
            Perform a priori p-refinement based on element shape, as described in 'Decoupling..' paper.
        
            **Default**: `False`








        ??? json-spec "`/space/advanced` (`object`)"
            ```
            /space/advanced
            ```
            ## Description
            Advanced settings for the FE space.
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/space/advanced/discr_order_max` (`int`)"
                ```
                /space/advanced/discr_order_max
                ```
                ## Description
                Maximal discretization order in adaptive p-refinement and hp-refinement
            
                **Default**: `4`








            ??? json-spec "`/space/advanced/serendipity` (`bool`)"
                ```
                /space/advanced/serendipity
                ```
                ## Description
                Use serendipity elements for quad/hex elements of degree 2.
            
                **Default**: `False`








            ??? json-spec "`/space/advanced/isoparametric` (`bool`)"
                ```
                /space/advanced/isoparametric
                ```
                ## Description
                Forces geometric map basis to be the same degree as the main variable basis, irrespective of the degree associated with the geom. map degrees associated with the elements of the geometry.
            
                **Default**: `False`








            ??? json-spec "`/space/advanced/use_spline` (`bool`)"
                ```
                /space/advanced/use_spline
                ```
                ## Description
                Use bi/triquadratic spline basis for quad/hex elements not adjacent to polyhedral elements, see 'PolySpline..' paper for details.
            
                **Default**: `False`








            ??? json-spec "`/space/advanced/bc_method` (`string`)"
                ```
                /space/advanced/bc_method
                ```
                ## Description
                Method for imposing analytic Dirichet boundary conditions. If 'lsq' (least-squares fit), then the bc function is sampled at quadrature points, and the FEspace nodal values on the boundary are determined by minimizing L2 norm of the difference. If 'sample', then the analytic bc function is sampled at the boundary nodes.
            
                **Default**: `'lsq'`
            
                **Options:** `['lsq', 'sample']`








            ??? json-spec "`/space/advanced/n_boundary_samples` (`int`)"
                ```
                /space/advanced/n_boundary_samples
                ```
                ## Description
                Per-element number of boundary samples for analytic Dirichlet and Neumann boundary conditions.
            
                **Default**: `-1`








            ??? json-spec "`/space/advanced/quadrature_order` (`int`)"
                ```
                /space/advanced/quadrature_order
                ```
                ## Description
                Minimal quadrature order to use in matrix and rhs assembly; the actual order is determined as min(2*(p-1)+1,quadrature_order).
            
                **Default**: `-1`








            ??? json-spec "`/space/advanced/poly_bases` (`string`)"
                ```
                /space/advanced/poly_bases
                ```
                ## Description
                Type of basis to use for a polygonal element, one of MFSHarmonic, MeanValue, see 'PolySpline..' paper for details.
            
                **Default**: `'MFSHarmonic'`
            
                **Options:** `['MFSHarmonic', 'MeanValue']`








            ??? json-spec "`/space/advanced/integral_constraints` (`int`)"
                ```
                /space/advanced/integral_constraints
                ```
                ## Description
                Number of constraints for non-conforming polygonal basis;  0, 1, or 2; see 'PolySpline..' paper for details.
            
                **Default**: `2`








            ??? json-spec "`/space/advanced/n_harmonic_samples` (`int`)"
                ```
                /space/advanced/n_harmonic_samples
                ```
                ## Description
                If MFSHarmonics is used for a polygonal element, number of collocation samples used in the basis construction;see 'PolySpline..' paper for details.
            
                **Default**: `10`








            ??? json-spec "`/space/advanced/force_no_ref_for_harmonic` (`bool`)"
                ```
                /space/advanced/force_no_ref_for_harmonic
                ```
                ## Description
                If true, do not do uniform global refinement if the mesh contains polygonal elements.
            
                **Default**: `False`








            ??? json-spec "`/space/advanced/B` (`int`)"
                ```
                /space/advanced/B
                ```
                ## Description
                The target deviation of the error on elements from perfect element error, for a priori geometry-dependent p-refinement, see 'Decoupling .. ' paper.
            
                **Default**: `3`








            ??? json-spec "`/space/advanced/h1_formula` (`bool`)"
                ```
                /space/advanced/h1_formula
                ```
                ## Description
                
            
                **Default**: `False`








            ??? json-spec "`/space/advanced/count_flipped_els` (`bool`)"
                ```
                /space/advanced/count_flipped_els
                ```
                ## Description
                Count the number of elements with Jacobian of the geometric map not positive at quadrature points.
            
                **Default**: `True`












    ??? json-spec "`/time`"
        ```
        /time
        ```


        === "`/time` (`object`)"
            ## Description
            The time parameters: start time `t0`, end time `tend`, time step `dt`.
        
            **Default**: `'skip'`
            ## Required





            ??? json-spec "`/time/tend` (`float`)"
                ```
                /time/tend
                ```
                ## Description
                Ending time
            
                **Range:** `[0, inf]`








            ??? json-spec "`/time/dt` (`float`)"
                ```
                /time/dt
                ```
                ## Description
                Time step size $\Delta t$
            
                **Range:** `[0, inf]`



            ## Optional





            ??? json-spec "`/time/t0` (`float`)"
                ```
                /time/t0
                ```
                ## Description
                Startning time
            
                **Default**: `0`
            
                **Range:** `[0, inf]`








            ??? json-spec "`/time/integrator` (`string`)"
                ```
                /time/integrator
                ```
                ## Description
                Time integrator
            
                **Default**: `'ImplicitEuler'`
            
                **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`








            ??? json-spec "`/time/newmark` (`object`)"
                ```
                /time/newmark
                ```
                ## Description
                Options for Newmark
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/time/newmark/gamma` (`float`)"
                    ```
                    /time/newmark/gamma
                    ```
                    ## Description
                    Newmark gamma
                
                    **Default**: `0.5`








                ??? json-spec "`/time/newmark/beta` (`float`)"
                    ```
                    /time/newmark/beta
                    ```
                    ## Description
                    Newmark beta
                
                    **Default**: `0.25`











            ??? json-spec "`/time/BDF` (`object`)"
                ```
                /time/BDF
                ```
                ## Description
                Options for BDF
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/time/BDF/steps` (`int`)"
                    ```
                    /time/BDF/steps
                    ```
                    ## Description
                    BDF order
                
                    **Default**: `1`









        === "`/time` (`object`)"
            ## Description
            The time parameters: start time `t0`, time step `dt`, number of time steps.
            ## Required





            ??? json-spec "`/time/time_steps` (`int`)"
                ```
                /time/time_steps
                ```
                ## Description
                Number of time steps
            
                **Range:** `[0, inf]`








            ??? json-spec "`/time/dt` (`float`)"
                ```
                /time/dt
                ```
                ## Description
                Time step size $\Delta t$
            
                **Range:** `[0, inf]`



            ## Optional





            ??? json-spec "`/time/t0` (`float`)"
                ```
                /time/t0
                ```
                ## Description
                Startning time
            
                **Default**: `0`
            
                **Range:** `[0, inf]`








            ??? json-spec "`/time/integrator` (`string`)"
                ```
                /time/integrator
                ```
                ## Description
                Time integrator
            
                **Default**: `'ImplicitEuler'`
            
                **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`








            ??? json-spec "`/time/newmark` (`object`)"
                ```
                /time/newmark
                ```
                ## Description
                Options for Newmark
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/time/newmark/gamma` (`float`)"
                    ```
                    /time/newmark/gamma
                    ```
                    ## Description
                    Newmark gamma
                
                    **Default**: `0.5`








                ??? json-spec "`/time/newmark/beta` (`float`)"
                    ```
                    /time/newmark/beta
                    ```
                    ## Description
                    Newmark beta
                
                    **Default**: `0.25`











            ??? json-spec "`/time/BDF` (`object`)"
                ```
                /time/BDF
                ```
                ## Description
                Options for BDF
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/time/BDF/steps` (`int`)"
                    ```
                    /time/BDF/steps
                    ```
                    ## Description
                    BDF order
                
                    **Default**: `1`









        === "`/time` (`object`)"
            ## Description
            The time parameters: start time `t0`, end time `tend`, number of time steps.
            ## Required





            ??? json-spec "`/time/time_steps` (`int`)"
                ```
                /time/time_steps
                ```
                ## Description
                Number of time steps
            
                **Range:** `[0, inf]`








            ??? json-spec "`/time/tend` (`float`)"
                ```
                /time/tend
                ```
                ## Description
                Ending time
            
                **Range:** `[0, inf]`



            ## Optional





            ??? json-spec "`/time/t0` (`float`)"
                ```
                /time/t0
                ```
                ## Description
                Startning time
            
                **Default**: `0`
            
                **Range:** `[0, inf]`








            ??? json-spec "`/time/integrator` (`string`)"
                ```
                /time/integrator
                ```
                ## Description
                Time integrator
            
                **Default**: `'ImplicitEuler'`
            
                **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`








            ??? json-spec "`/time/newmark` (`object`)"
                ```
                /time/newmark
                ```
                ## Description
                Options for Newmark
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/time/newmark/gamma` (`float`)"
                    ```
                    /time/newmark/gamma
                    ```
                    ## Description
                    Newmark gamma
                
                    **Default**: `0.5`








                ??? json-spec "`/time/newmark/beta` (`float`)"
                    ```
                    /time/newmark/beta
                    ```
                    ## Description
                    Newmark beta
                
                    **Default**: `0.25`











            ??? json-spec "`/time/BDF` (`object`)"
                ```
                /time/BDF
                ```
                ## Description
                Options for BDF
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/time/BDF/steps` (`int`)"
                    ```
                    /time/BDF/steps
                    ```
                    ## Description
                    BDF order
                
                    **Default**: `1`














    ??? json-spec "`/contact` (`object`)"
        ```
        /contact
        ```
        ## Description
        Contact handling parameters.
    
        **Default**: `None`
        ## Optional





        ??? json-spec "`/contact/enabled` (`bool`)"
            ```
            /contact/enabled
            ```
            ## Description
            True if contact handling is enabled.
        
            **Default**: `False`








        ??? json-spec "`/contact/dhat` (`float`)"
            ```
            /contact/dhat
            ```
            ## Description
            Contact barrier activation distance.
        
            **Default**: `0.001`
        
            **Range:** `[0, inf]`








        ??? json-spec "`/contact/dhat_percentage` (`float`)"
            ```
            /contact/dhat_percentage
            ```
            ## Description
            $\hat{d}$ as percentage of the diagonal of the bounding box
        
            **Default**: `0.8`








        ??? json-spec "`/contact/epsv` (`float`)"
            ```
            /contact/epsv
            ```
            ## Description
            Friction smoothing parameter.
        
            **Default**: `0.001`
        
            **Range:** `[0, inf]`








        ??? json-spec "`/contact/friction_coefficient` (`float`)"
            ```
            /contact/friction_coefficient
            ```
            ## Description
            Coefficient of friction (global)
        
            **Default**: `0`











    ??? json-spec "`/solver` (`object`)"
        ```
        /solver
        ```
        ## Description
        The settings for the solver including linear solver, nonlinear solver, and some advanced options.
    
        **Default**: `None`
        ## Optional





        ??? json-spec "`/solver/linear` (`object`)"
            ```
            /solver/linear
            ```
            ## Description
            Settings for the linear solver.
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/solver/linear/solver` (`string`)"
                ```
                /solver/linear/solver
                ```
                ## Description
                Linear solver type.
            
                **Default**: `''`








            ??? json-spec "`/solver/linear/precond` (`string`)"
                ```
                /solver/linear/precond
                ```
                ## Description
                Preconditioner used if using an iterative linear solver.
            
                **Default**: `''`











        ??? json-spec "`/solver/nonlinear` (`object`)"
            ```
            /solver/nonlinear
            ```
            ## Description
            Settings for nonlinear solver. Interior-loop linear solver settings are defined in the solver/linear section.
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/solver/nonlinear/solver` (`string`)"
                ```
                /solver/nonlinear/solver
                ```
                ## Description
                Nonlinear solver type
            
                **Default**: `'newton'`
            
                **Options:** `['newton', 'lbfgs']`








            ??? json-spec "`/solver/nonlinear/f_delta` (`float`)"
                ```
                /solver/nonlinear/f_delta
                ```
                ## Description
                Stopping criterion: minimal change of the energy f for the iterations to continue.
            
                **Default**: `1e-10`








            ??? json-spec "`/solver/nonlinear/grad_norm` (`float`)"
                ```
                /solver/nonlinear/grad_norm
                ```
                ## Description
                Stopping criterion: Minimal gradient norm for the iterations to continue.
            
                **Default**: `1e-08`








            ??? json-spec "`/solver/nonlinear/max_iterations` (`int`)"
                ```
                /solver/nonlinear/max_iterations
                ```
                ## Description
                Maximum number of iterations for a nonlinear solve.
            
                **Default**: `1000`








            ??? json-spec "`/solver/nonlinear/use_grad_norm` (`bool`)"
                ```
                /solver/nonlinear/use_grad_norm
                ```
                ## Description
                If true, enable gradient-norm stopping criterion, absolute (if relative_gradient is false), or relative to the initial gradient magnitude before the first iteration, otherwise.
            
                **Default**: `True`








            ??? json-spec "`/solver/nonlinear/relative_gradient` (`bool`)"
                ```
                /solver/nonlinear/relative_gradient
                ```
                ## Description
                If true, use relative gradient norm threshold, use absolute otherwise
            
                **Default**: `False`








            ??? json-spec "`/solver/nonlinear/line_search` (`object`)"
                ```
                /solver/nonlinear/line_search
                ```
                ## Description
                Settings for line-search in the nonlinear solver
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/solver/nonlinear/line_search/method` (`string`)"
                    ```
                    /solver/nonlinear/line_search/method
                    ```
                    ## Description
                    Line-search type
                
                    **Default**: `'backtracking'`
                
                    **Options:** `['armijo', 'armijo_alt', 'backtracking', 'more_thuente', 'none']`








                ??? json-spec "`/solver/nonlinear/line_search/use_grad_norm_tol` (`float`)"
                    ```
                    /solver/nonlinear/line_search/use_grad_norm_tol
                    ```
                    ## Description
                    When the energy is smaller than use_grad_norm_tol, line-search uses norm of gradient instead of energy
                
                    **Default**: `0.0001`














        ??? json-spec "`/solver/augmented_lagrangian` (`object`)"
            ```
            /solver/augmented_lagrangian
            ```
            ## Description
            Parameters for the AL for imposing Dirichlet BCs. If the bc are not imposable, we add $w\|u - bc\|^2$ to the energy ($u$ is the solution at the Dirichlet nodes and $bc$ are the Dirichlet values). After convergence, we try to impose bc again, in case of failure we double $w$ until `max_weight`.
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/solver/augmented_lagrangian/initial_weight` (`float`)"
                ```
                /solver/augmented_lagrangian/initial_weight
                ```
                ## Description
                Initial weight for AL
            
                **Default**: `1000000.0`








            ??? json-spec "`/solver/augmented_lagrangian/max_weight` (`float`)"
                ```
                /solver/augmented_lagrangian/max_weight
                ```
                ## Description
                Maximum AL weight
            
                **Default**: `100000000000.0`








            ??? json-spec "`/solver/augmented_lagrangian/force` (`bool`)"
                ```
                /solver/augmented_lagrangian/force
                ```
                ## Description
                Always enable AL, even when BC can be imposed
            
                **Default**: `False`











        ??? json-spec "`/solver/contact` (`object`)"
            ```
            /solver/contact
            ```
            ## Description
            Settings for contact handling in the solver.
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/solver/contact/CCD` (`object`)"
                ```
                /solver/contact/CCD
                ```
                ## Description
                CCD options
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/solver/contact/CCD/broad_phase` (`string`)"
                    ```
                    /solver/contact/CCD/broad_phase
                    ```
                    ## Description
                    Broad phase collision-detection algorithm to use
                
                    **Default**: `'hash_grid'`
                
                    **Options:** `['hash_grid', 'HG', 'brute_force', 'BF', 'spatial_hash', 'SH', 'sweep_and_tiniest_queue', 'STQ', 'sweep_and_tiniest_queue_gpu', 'STQ_GPU']`








                ??? json-spec "`/solver/contact/CCD/tolerance` (`float`)"
                    ```
                    /solver/contact/CCD/tolerance
                    ```
                    ## Description
                    CCD tolerance
                
                    **Default**: `1e-06`








                ??? json-spec "`/solver/contact/CCD/max_iterations` (`float`)"
                    ```
                    /solver/contact/CCD/max_iterations
                    ```
                    ## Description
                    Maximum number of iterations for continuous collision detection
                
                    **Default**: `1000000.0`











            ??? json-spec "`/solver/contact/friction_iterations` (`int`)"
                ```
                /solver/contact/friction_iterations
                ```
                ## Description
                Maximum number of update iterations for lagged friction formulation (see IPC paper).
            
                **Default**: `1`








            ??? json-spec "`/solver/contact/friction_convergence_tol` (`float`)"
                ```
                /solver/contact/friction_convergence_tol
                ```
                ## Description
                Tolerence for friction convergence
            
                **Default**: `0.01`






            ??? json-spec "`/solver/contact/barrier_stiffness`"
                ```
                /solver/contact/barrier_stiffness
                ```


                === "`/solver/contact/barrier_stiffness` (`string`)"
                    ## Description
                    How coefficient of clamped log-barrier function for contact is updated
                
                    **Default**: `'adaptive'`
                
                    **Options:** `['adaptive']`



                === "`/solver/contact/barrier_stiffness` (`float`)"
                    ## Description
                    The coefficient of clamped log-barrier function value when not adaptive
















        ??? json-spec "`/solver/ignore_inertia` (`bool`)"
            ```
            /solver/ignore_inertia
            ```
            ## Description
            Ignore inertia in time dependent. Used for doing incremental load.
        
            **Default**: `False`








        ??? json-spec "`/solver/advanced` (`object`)"
            ```
            /solver/advanced
            ```
            ## Description
            Advanced settings for the solver
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/solver/advanced/cache_size` (`int`)"
                ```
                /solver/advanced/cache_size
                ```
                ## Description
                Maximum number of elements when the assembly values are cached.
            
                **Default**: `900000`








            ??? json-spec "`/solver/advanced/lump_mass_matrix` (`bool`)"
                ```
                /solver/advanced/lump_mass_matrix
                ```
                ## Description
                If true, use diagonal mass matrix with entries on the diagonal equal to the sum of entries in each row of the full mass matrix.}
            
                **Default**: `False`














    ??? json-spec "`/boundary_conditions` (`object`)"
        ```
        /boundary_conditions
        ```
        ## Description
        The settings for boundary conditions.
    
        **Default**: `None`
        ## Optional



        ??? json-spec "`/boundary_conditions/rhs`"
            ```
            /boundary_conditions/rhs
            ```


            === "`/boundary_conditions/rhs` (`float`)"
                ## Description
                Right-hand side of the system being solved for scalar-valued PDEs



            === "`/boundary_conditions/rhs` (`string`)"
                ## Description
                Right-hand side of the system being solved as a function of $x,y,z,t$.



            === "`/boundary_conditions/rhs` (`list`)"
                ## Description
                Right-hand side of the system being solved for vector-valued PDEs.



                ??? json-spec "`/boundary_conditions/rhs/*`"
                    ```
                    /boundary_conditions/rhs/*
                    ```


                    === "`/boundary_conditions/rhs/*` (`float`)"
                        ## Description
                        Right-hand side of the system being solved, value.
                    
                        **Default**: `0`



                    === "`/boundary_conditions/rhs/*` (`string`)"
                        ## Description
                        Right-hand side of the system being solved as a function of $x,y,z,t$.











        ??? json-spec "`/boundary_conditions/dirichlet_boundary` (`list`)"
            ```
            /boundary_conditions/dirichlet_boundary
            ```
            ## Description
            The list of Dirichlet boundary conditions for the main variable. Elements of the list are assignment pairs (ID, value) where ID is assigned by surface selection.



            ??? json-spec "`/boundary_conditions/dirichlet_boundary/*`"
                ```
                /boundary_conditions/dirichlet_boundary/*
                ```


                === "`/boundary_conditions/dirichlet_boundary/*` (`object`)"
                    ## Description
                    Dirichlet boundary condition.
                
                    **Default**: `None`
                    ## Required



                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/id`"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/id
                        ```


                        === "`/boundary_conditions/dirichlet_boundary/*/id` (`int`)"
                            ## Description
                            ID of Dirichlet boundary condition from surface selection.



                        === "`/boundary_conditions/dirichlet_boundary/*/id` (`string`)"
                            ## Description
                            select all ids.
                        
                            **Options:** `['all']`








                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value` (`list`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/value
                        ```
                        ## Description
                        Values of Dirichlet boundary condition, length 1 for scalar-valued pde, 2/3 for vector-valued PDEs depending on the dimension.



                        ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value/*`"
                            ```
                            /boundary_conditions/dirichlet_boundary/*/value/*
                            ```


                            === "`/boundary_conditions/dirichlet_boundary/*/value/*` (`string`)"
                                ## Description
                                Values of Dirichlet boundary condition for each dimension as a function of $x,y,z,t$.



                            === "`/boundary_conditions/dirichlet_boundary/*/value/*` (`float`)"
                                ## Description
                                Values of Dirichlet boundary condition for each dimension.






                    ## Optional





                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/dimension` (`list`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/dimension
                        ```
                        ## Description
                        List of 2 (2D) or 3 (3D) boolean values indicating if the Dirichlet boundary condition  is applied for a particular dimension.





                        ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/dimension/*` (`bool`)"
                            ```
                            /boundary_conditions/dirichlet_boundary/*/dimension/*
                            ```
                            ## Description
                            value
                        
                            **Default**: `True`









                === "`/boundary_conditions/dirichlet_boundary/*` (`string`)"
                    ## Description
                    Dirichlet boundary condition loaded from a file, <node_id> <bc values>, 1 for scalar, 2/3 for tensor depending on dimension.











        ??? json-spec "`/boundary_conditions/neumann_boundary` (`list`)"
            ```
            /boundary_conditions/neumann_boundary
            ```
            ## Description
            The list of Neumann boundary conditions for the main variable. Elements of the list are assignment pairs (ID, value) where ID is assigned by surface selection.





            ??? json-spec "`/boundary_conditions/neumann_boundary/*` (`object`)"
                ```
                /boundary_conditions/neumann_boundary/*
                ```
                ## Description
                Neumann boundary condition
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/boundary_conditions/neumann_boundary/*/id` (`int`)"
                    ```
                    /boundary_conditions/neumann_boundary/*/id
                    ```
                    ## Description
                    ID of Neumann boundary condition
                
                    **Default**: `1`








                ??? json-spec "`/boundary_conditions/neumann_boundary/*/value` (`list`)"
                    ```
                    /boundary_conditions/neumann_boundary/*/value
                    ```
                    ## Description
                    Values of Neumann boundary condition for each dimension



                    ??? json-spec "`/boundary_conditions/neumann_boundary/*/value/*`"
                        ```
                        /boundary_conditions/neumann_boundary/*/value/*
                        ```


                        === "`/boundary_conditions/neumann_boundary/*/value/*` (`string`)"
                            ## Description
                            Values of Neumann boundary condition for each dimension as function of $x,y,z,t$
                        
                            **Default**: `''`



                        === "`/boundary_conditions/neumann_boundary/*/value/*` (`float`)"
                            ## Description
                            Values of Neumann boundary condition for each dimension
                        
                            **Default**: `0`

















        ??? json-spec "`/boundary_conditions/pressure_boundary` (`list`)"
            ```
            /boundary_conditions/pressure_boundary
            ```
            ## Description
            Dirichlet boundary condition for normal * value for vector-valued PDEs.





            ??? json-spec "`/boundary_conditions/pressure_boundary/*` (`object`)"
                ```
                /boundary_conditions/pressure_boundary/*
                ```
                ## Description
                pressure BC entry
            
                **Default**: `None`
                ## Required





                ??? json-spec "`/boundary_conditions/pressure_boundary/*/id` (`int`)"
                    ```
                    /boundary_conditions/pressure_boundary/*/id
                    ```
                    ## Description
                    ID for the pressure Neumann boundary condition








                ??? json-spec "`/boundary_conditions/pressure_boundary/*/value` (`list`)"
                    ```
                    /boundary_conditions/pressure_boundary/*/value
                    ```
                    ## Description
                    Values of pressure Neumann boundary condition



                    ??? json-spec "`/boundary_conditions/pressure_boundary/*/value/*`"
                        ```
                        /boundary_conditions/pressure_boundary/*/value/*
                        ```


                        === "`/boundary_conditions/pressure_boundary/*/value/*` (`string`)"
                            ## Description
                            Values of pressure Neumann boundary condition as a function of $x,y,z,t$



                        === "`/boundary_conditions/pressure_boundary/*/value/*` (`float`)"
                            ## Description
                            Values of pressure Neumann boundary condition






                ## Optional
















        ??? json-spec "`/boundary_conditions/obstacle_displacements` (`list`)"
            ```
            /boundary_conditions/obstacle_displacements
            ```
            ## Description
            The list of obstacle displacements. Each entry is an (ID, value) pair, where ids are set by selection.





            ??? json-spec "`/boundary_conditions/obstacle_displacements/*` (`object`)"
                ```
                /boundary_conditions/obstacle_displacements/*
                ```
                ## Description
                Obstacle displacements
            
                **Default**: `None`
                ## Required





                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/id` (`int`)"
                    ```
                    /boundary_conditions/obstacle_displacements/*/id
                    ```
                    ## Description
                    ID of Obstacle displacements








                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/value` (`list`)"
                    ```
                    /boundary_conditions/obstacle_displacements/*/value
                    ```
                    ## Description
                    Values of Obstacle displacements for each dimension



                    ??? json-spec "`/boundary_conditions/obstacle_displacements/*/value/*`"
                        ```
                        /boundary_conditions/obstacle_displacements/*/value/*
                        ```


                        === "`/boundary_conditions/obstacle_displacements/*/value/*` (`string`)"
                            ## Description
                            Values of Obstacle displacements for each dimension as a function of $x,y,z,t$



                        === "`/boundary_conditions/obstacle_displacements/*/value/*` (`float`)"
                            ## Description
                            Values of Obstacle displacements for each dimension




















    ??? json-spec "`/initial_conditions` (`object`)"
        ```
        /initial_conditions
        ```
        ## Description
        Initial conditions for the time-dependent problem, imposed on the main variable, its derivative or second derivative
    
        **Default**: `None`
        ## Optional





        ??? json-spec "`/initial_conditions/solution` (`list`)"
            ```
            /initial_conditions/solution
            ```
            ## Description
            initial solution





            ??? json-spec "`/initial_conditions/solution/*` (`object`)"
                ```
                /initial_conditions/solution/*
                ```
                ## Description
                A list of (ID, value) pairs defining the initial conditions for the main variable values. Ids are set by selection, and values can be floats or formulas.
            
                **Default**: `None`
                ## Required





                ??? json-spec "`/initial_conditions/solution/*/id` (`int`)"
                    ```
                    /initial_conditions/solution/*/id
                    ```
                    ## Description
                    ID from volume selections








                ??? json-spec "`/initial_conditions/solution/*/value` (`list`)"
                    ```
                    /initial_conditions/solution/*/value
                    ```
                    ## Description
                    value of the solution



                    ??? json-spec "`/initial_conditions/solution/*/value/*`"
                        ```
                        /initial_conditions/solution/*/value/*
                        ```


                        === "`/initial_conditions/solution/*/value/*` (`float`)"
                            ## Description
                            value



                        === "`/initial_conditions/solution/*/value/*` (`string`)"
                            ## Description
                            as a function of $x,y,z,t$

















        ??? json-spec "`/initial_conditions/velocity` (`list`)"
            ```
            /initial_conditions/velocity
            ```
            ## Description
            initial velocity





            ??? json-spec "`/initial_conditions/velocity/*` (`object`)"
                ```
                /initial_conditions/velocity/*
                ```
                ## Description
                A list of (ID, value) pairs defining the initial conditions for the first derivative of the main variable values. Ids are set by selection, and values can be floats or formulas.
            
                **Default**: `None`
                ## Required





                ??? json-spec "`/initial_conditions/velocity/*/id` (`int`)"
                    ```
                    /initial_conditions/velocity/*/id
                    ```
                    ## Description
                    ID from volume selections








                ??? json-spec "`/initial_conditions/velocity/*/value` (`list`)"
                    ```
                    /initial_conditions/velocity/*/value
                    ```
                    ## Description
                    value od the initial velocity



                    ??? json-spec "`/initial_conditions/velocity/*/value/*`"
                        ```
                        /initial_conditions/velocity/*/value/*
                        ```


                        === "`/initial_conditions/velocity/*/value/*` (`float`)"
                            ## Description
                            value



                        === "`/initial_conditions/velocity/*/value/*` (`string`)"
                            ## Description
                            value as a function of $x,y,z,t$

















        ??? json-spec "`/initial_conditions/acceleration` (`list`)"
            ```
            /initial_conditions/acceleration
            ```
            ## Description
            initial acceleration





            ??? json-spec "`/initial_conditions/acceleration/*` (`object`)"
                ```
                /initial_conditions/acceleration/*
                ```
                ## Description
                entries
            
                **Default**: `None`
                ## Required





                ??? json-spec "`/initial_conditions/acceleration/*/id` (`int`)"
                    ```
                    /initial_conditions/acceleration/*/id
                    ```
                    ## Description
                    ID from volume selections








                ??? json-spec "`/initial_conditions/acceleration/*/value` (`list`)"
                    ```
                    /initial_conditions/acceleration/*/value
                    ```
                    ## Description
                    value



                    ??? json-spec "`/initial_conditions/acceleration/*/value/*`"
                        ```
                        /initial_conditions/acceleration/*/value/*
                        ```


                        === "`/initial_conditions/acceleration/*/value/*` (`float`)"
                            ## Description
                            value
                        
                            **Default**: `0`



                        === "`/initial_conditions/acceleration/*/value/*` (`string`)"
                            ## Description
                            value as a function of $x,y,z,t$




















    ??? json-spec "`/output` (`object`)"
        ```
        /output
        ```
        ## Description
        output settings
    
        **Default**: `None`
        ## Optional





        ??? json-spec "`/output/json` (`string`)"
            ```
            /output/json
            ```
            ## Description
            File name for json output statistics on time/error/etc.
        
            **Default**: `''`








        ??? json-spec "`/output/paraview` (`object`)"
            ```
            /output/paraview
            ```
            ## Description
            Output in paraview format
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/output/paraview/file_name` (`string`)"
                ```
                /output/paraview/file_name
                ```
                ## Description
                Paraview output file name
            
                **Default**: `''`








            ??? json-spec "`/output/paraview/vismesh_rel_area` (`float`)"
                ```
                /output/paraview/vismesh_rel_area
                ```
                ## Description
                relative area for the upsampled visualisation mesh
            
                **Default**: `1e-05`








            ??? json-spec "`/output/paraview/skip_frame` (`int`)"
                ```
                /output/paraview/skip_frame
                ```
                ## Description
                export every skip_frame-th frames for time dependent simulations
            
                **Default**: `1`








            ??? json-spec "`/output/paraview/high_order_mesh` (`bool`)"
                ```
                /output/paraview/high_order_mesh
                ```
                ## Description
                Enables/disables high-order output for paraview. Supported only for isoparametric or linear meshes with high-odrer solutions.
            
                **Default**: `True`








            ??? json-spec "`/output/paraview/volume` (`bool`)"
                ```
                /output/paraview/volume
                ```
                ## Description
                Export volumetric mesh
            
                **Default**: `True`








            ??? json-spec "`/output/paraview/surface` (`bool`)"
                ```
                /output/paraview/surface
                ```
                ## Description
                Export surface mesh (in 2d polygon)
            
                **Default**: `False`








            ??? json-spec "`/output/paraview/wireframe` (`bool`)"
                ```
                /output/paraview/wireframe
                ```
                ## Description
                Export the wireframe of the mesh
            
                **Default**: `False`








            ??? json-spec "`/output/paraview/options` (`object`)"
                ```
                /output/paraview/options
                ```
                ## Description
                Optional fields in the output
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/output/paraview/options/material` (`bool`)"
                    ```
                    /output/paraview/options/material
                    ```
                    ## Description
                    If true, write out material values sampled on the vertices of the mesh
                
                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/body_ids` (`bool`)"
                    ```
                    /output/paraview/options/body_ids
                    ```
                    ## Description
                    Export volumes ids
                
                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/contact_forces` (`bool`)"
                    ```
                    /output/paraview/options/contact_forces
                    ```
                    ## Description
                    If true, write out contact forces for surface
                
                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/friction_forces` (`bool`)"
                    ```
                    /output/paraview/options/friction_forces
                    ```
                    ## Description
                    If true, write out friction forces for surface
                
                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/velocity` (`bool`)"
                    ```
                    /output/paraview/options/velocity
                    ```
                    ## Description
                    If true, write out velocities
                
                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/acceleration` (`bool`)"
                    ```
                    /output/paraview/options/acceleration
                    ```
                    ## Description
                    If true, write out accelerations
                
                    **Default**: `False`














        ??? json-spec "`/output/data` (`object`)"
            ```
            /output/data
            ```
            ## Description
            File names to write output data to.
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/output/data/solution` (`string`)"
                ```
                /output/data/solution
                ```
                ## Description
                Main variable solution. Unrolled [xyz, xyz, ...] using PolyFEM ordering. If reorder_nodes exports the solution with the same order the vertices of the input mesh as a #n x d file
            
                **Default**: `''`








            ??? json-spec "`/output/data/full_mat` (`string`)"
                ```
                /output/data/full_mat
                ```
                ## Description
                System matrix without boundary conditions. Doesn't work for nonlinear problems
            
                **Default**: `''`








            ??? json-spec "`/output/data/stiffness_mat` (`string`)"
                ```
                /output/data/stiffness_mat
                ```
                ## Description
                System matrix with boundary conditions. Doesn't work for nonlinear problems
            
                **Default**: `''`








            ??? json-spec "`/output/data/stress_mat` (`string`)"
                ```
                /output/data/stress_mat
                ```
                ## Description
                Exports stress
            
                **Default**: `''`








            ??? json-spec "`/output/data/u_path` (`string`)"
                ```
                /output/data/u_path
                ```
                ## Description
                Writes the complete solution in PolyFEM format, used to restart the sim
            
                **Default**: `''`








            ??? json-spec "`/output/data/v_path` (`string`)"
                ```
                /output/data/v_path
                ```
                ## Description
                Writes the complete velocity in PolyFEM format, used to restart the sim
            
                **Default**: `''`








            ??? json-spec "`/output/data/a_path` (`string`)"
                ```
                /output/data/a_path
                ```
                ## Description
                Writes the complete acceleration in PolyFEM format, used to restart the sim
            
                **Default**: `''`








            ??? json-spec "`/output/data/mises` (`string`)"
                ```
                /output/data/mises
                ```
                ## Description
                File name to write per-node Von Mises stress values to.
            
                **Default**: `''`








            ??? json-spec "`/output/data/nodes` (`string`)"
                ```
                /output/data/nodes
                ```
                ## Description
                Writes the FEM nodes
            
                **Default**: `''`








            ??? json-spec "`/output/data/advanced` (`object`)"
                ```
                /output/data/advanced
                ```
                ## Description
                advanced options
            
                **Default**: `None`
                ## Optional





                ??? json-spec "`/output/data/advanced/reorder_nodes` (`bool`)"
                    ```
                    /output/data/advanced/reorder_nodes
                    ```
                    ## Description
                    Reorder nodes accodring to input
                
                    **Default**: `False`














        ??? json-spec "`/output/advanced` (`object`)"
            ```
            /output/advanced
            ```
            ## Description
            Additional output options
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/output/advanced/timestep_prefix` (`string`)"
                ```
                /output/advanced/timestep_prefix
                ```
                ## Description
                Prefix for output file names for each time step, the final file is step_i.[vtu|vtm] where i is the time index.
            
                **Default**: `'step_'`








            ??? json-spec "`/output/advanced/sol_on_grid` (`float`)"
                ```
                /output/advanced/sol_on_grid
                ```
                ## Description
                exports the solution sampled on a grid, specify the grid spacing
            
                **Default**: `-1`








            ??? json-spec "`/output/advanced/compute_error` (`bool`)"
                ```
                /output/advanced/compute_error
                ```
                ## Description
                Enables the computation of the error. If no reference solution is provided, return the norms of the solution
            
                **Default**: `True`








            ??? json-spec "`/output/advanced/sol_at_node` (`int`)"
                ```
                /output/advanced/sol_at_node
                ```
                ## Description
                Write out solution values at a specific node. the values will be written in the output json file
            
                **Default**: `-1`








            ??? json-spec "`/output/advanced/vis_boundary_only` (`bool`)"
                ```
                /output/advanced/vis_boundary_only
                ```
                ## Description
                saves only elements touching the boundaries
            
                **Default**: `False`








            ??? json-spec "`/output/advanced/curved_mesh_size` (`bool`)"
                ```
                /output/advanced/curved_mesh_size
                ```
                ## Description
                upsample curved edges to compute mesh size
            
                **Default**: `False`








            ??? json-spec "`/output/advanced/save_solve_sequence_debug` (`bool`)"
                ```
                /output/advanced/save_solve_sequence_debug
                ```
                ## Description
                saves AL internal steps, for debugging
            
                **Default**: `False`








            ??? json-spec "`/output/advanced/save_time_sequence` (`bool`)"
                ```
                /output/advanced/save_time_sequence
                ```
                ## Description
                saves timesteps
            
                **Default**: `True`








            ??? json-spec "`/output/advanced/save_nl_solve_sequence` (`bool`)"
                ```
                /output/advanced/save_nl_solve_sequence
                ```
                ## Description
                saves obj after every nonlinear iteration, for debugging
            
                **Default**: `False`








            ??? json-spec "`/output/advanced/spectrum` (`bool`)"
                ```
                /output/advanced/spectrum
                ```
                ## Description
                exports the spectrum of the matrix in the output json. Works only if POLYSOLVE_WITH_SPECTRA is enabled
            
                **Default**: `False`











        ??? json-spec "`/output/reference` (`object`)"
            ```
            /output/reference
            ```
            ## Description
            Write out the analytic/numerical ground-truth solution and or its gradient
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/output/reference/solution` (`list`)"
                ```
                /output/reference/solution
                ```
                ## Description
                reference solution used to compute errors





                ??? json-spec "`/output/reference/solution/*` (`string`)"
                    ```
                    /output/reference/solution/*
                    ```
                    ## Description
                    value as a function of $x,y,z,t$
                
                    **Default**: `''`











            ??? json-spec "`/output/reference/gradient` (`list`)"
                ```
                /output/reference/gradient
                ```
                ## Description
                gradient of the reference solution to compute errors





                ??? json-spec "`/output/reference/gradient/*` (`string`)"
                    ```
                    /output/reference/gradient/*
                    ```
                    ## Description
                    value as a function of $x,y,z,t$
                
                    **Default**: `''`

















    ??? json-spec "`/input` (`object`)"
        ```
        /input
        ```
        ## Description
        input data
    
        **Default**: `None`
        ## Optional





        ??? json-spec "`/input/data` (`object`)"
            ```
            /input/data
            ```
            ## Description
            input to restart time dependent sim
        
            **Default**: `None`
            ## Optional





            ??? json-spec "`/input/data/u_path` (`string`)"
                ```
                /input/data/u_path
                ```
                ## Description
                input solution
            
                **Default**: `''`








            ??? json-spec "`/input/data/v_path` (`string`)"
                ```
                /input/data/v_path
                ```
                ## Description
                input velocity
            
                **Default**: `''`








            ??? json-spec "`/input/data/a_path` (`string`)"
                ```
                /input/data/a_path
                ```
                ## Description
                input acceleration
            
                **Default**: `''`














    ??? json-spec "`/authen_t1` (`object`)"
        ```
        /authen_t1
        ```
        ## Description
        Used to test to compare different norms of solutions.
    
        **Default**: `None`
        ## Optional





        ??? json-spec "`/authen_t1/err_h1` (`float`)"
            ```
            /authen_t1/err_h1
            ```
            ## Description
            Reference h1 solution's norm.
        
            **Default**: `0`








        ??? json-spec "`/authen_t1/err_h1_semi` (`float`)"
            ```
            /authen_t1/err_h1_semi
            ```
            ## Description
            Reference h1 seminorm solution's norm.
        
            **Default**: `0`








        ??? json-spec "`/authen_t1/err_l2` (`float`)"
            ```
            /authen_t1/err_l2
            ```
            ## Description
            Reference $L^2$ solution's norm.
        
            **Default**: `0`








        ??? json-spec "`/authen_t1/err_linf` (`float`)"
            ```
            /authen_t1/err_linf
            ```
            ## Description
            Reference $L^\infty$ solution's norm.
        
            **Default**: `0`








        ??? json-spec "`/authen_t1/err_linf_grad` (`float`)"
            ```
            /authen_t1/err_linf_grad
            ```
            ## Description
            Reference $L^\infty$ solution's gradient norm.
        
            **Default**: `0`








        ??? json-spec "`/authen_t1/err_lp` (`float`)"
            ```
            /authen_t1/err_lp
            ```
            ## Description
            Reference $L^8$ solution's gradient norm.
        
            **Default**: `0`








        ??? json-spec "`/authen_t1/margin` (`float`)"
            ```
            /authen_t1/margin
            ```
            ## Description
            Reference tolerance used in tests.
        
            **Default**: `0`








