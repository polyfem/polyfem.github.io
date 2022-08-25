<!--Automatically generated using JSON Spec Engine-->








!!! summary "`/` (`object`)"
    ```
    /
    ```
    ## Description
    Root of the configuration file.
    ## Required










    ??? summary "`/geometry/*` (`object`)"
        ```
        /geometry/*
        ```
        ## Description
        Each geometry object stores a mesh, a set of transformations applied to it after loading, and a set of selections, which can be used to specify boundary conditions, materials, optimization parameters and other quantities that can be associated with a part of an object.
        ## Required





        ??? summary "`/geometry/*/mesh` (`file`)"
            ```
            /geometry/*/mesh
            ```
            ## Description
            Path of the mesh file to load.
        
            **Extensions:** `['.obj', '.msh', '.stl']`



        ## Optional





        ??? summary "`/geometry/*/type` (`string`)"
            ```
            /geometry/*/type
            ```
            ## Description
            Type of geometry, currently only one supported. In future we will add stuff like planes, spheres, etc
        
            **Default**: `'mesh'`
        
            **Options:** `['mesh']`








        ??? summary "`/geometry/*/extract` (`string`)"
            ```
            /geometry/*/extract
            ```
            ## Description
            Used to extract stuff from the mesh. Eg extract surface extracts the surface from a tet mesh
        
            **Default**: `'volume'`
        
            **Options:** `['volume', 'edges', 'points', 'surface']`








        ??? summary "`/geometry/*/transformation` (`object`)"
            ```
            /geometry/*/transformation
            ```
            ## Description
            Geometric transformations applied to the geometry after loading it.
        
            **Default**: None
            ## Optional










            ??? summary "`/geometry/*/transformation/translation/*` (`float`)"
                ```
                /geometry/*/transformation/translation/*
                ```
                ## Description
                <span class="todo">FIXME:</span> Missing documentation in the specification
            
                **Default**: `0`
















            ??? summary "`/geometry/*/transformation/rotation/*` (`float`)"
                ```
                /geometry/*/transformation/rotation/*
                ```
                ## Description
                <span class="todo">FIXME:</span> Missing documentation in the specification
            
                **Default**: `0`











            ??? summary "`/geometry/*/transformation/rotation_mode` (`string`)"
                ```
                /geometry/*/transformation/rotation_mode
                ```
                ## Description
                Type of rotation, supported are any permutation of (x[0-1]|y[0-1]|z[0-1), axis_angle, quaternion, or rotation_vector
            
                **Default**: `'xyz'`













            ??? summary "`/geometry/*/transformation/scale/*` (`float`)"
                ```
                /geometry/*/transformation/scale/*
                ```
                ## Description
                <span class="todo">FIXME:</span> Missing documentation in the specification
            
                **Default**: `0`









            ??? summary "`/geometry/*/transformation/dimensions`"
                ```
                /geometry/*/transformation/dimensions
                ```


                ??? summary "`/geometry/*/transformation/dimensions` (`float`)"
                    ```
                    /geometry/*/transformation/dimensions
                    ```
                    ## Description
                    Scale the object so that bounding box dimensions match specified dimensions, 2 entries for 2D problems, 3 entries for 3D problems. 
                
                    **Default**: `1`








                ??? summary "`/geometry/*/transformation/dimensions/*` (`float`)"
                    ```
                    /geometry/*/transformation/dimensions/*
                    ```
                    ## Description
                    <span class="todo">FIXME:</span> Missing documentation in the specification
                
                    **Default**: `0`












        ??? summary "`/geometry/*/volume_selection`"
            ```
            /geometry/*/volume_selection
            ```


            ??? summary "`/geometry/*/volume_selection` (`int`)"
                ```
                /geometry/*/volume_selection
                ```
                ## Description
                Assign specified id to all volume elements of the geometry (negative values indicate using the stored values in the MSH (default: 0)).
            
                **Default**: `-1`



            ??? summary "`/geometry/*/volume_selection` (`object`)"
                ```
                /geometry/*/volume_selection
                ```
                ## Description
                Offsets the volume IDs loaded from the mesh.
                ## Required





                ??? summary "`/geometry/*/volume_selection/id_offset` (`int`)"
                    ```
                    /geometry/*/volume_selection/id_offset
                    ```
                    ## Description
                    Offsets the volume IDs loaded from the mesh.
                
                    **Default**: `0`









            ??? summary "`/geometry/*/volume_selection/*`"
                ```
                /geometry/*/volume_selection/*
                ```


                ??? summary "`/geometry/*/volume_selection/*` (`object`)"
                    ```
                    /geometry/*/volume_selection/*
                    ```
                    ## Description
                    Assign the id to all volume elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                
                    **Default**: None
                    ## Required





                    ??? summary "`/geometry/*/volume_selection/*/id` (`int`)"
                        ```
                        /geometry/*/volume_selection/*/id
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification


















                    ??? summary "`/geometry/*/volume_selection/*/box/*/*` (`float`)"
                        ```
                        /geometry/*/volume_selection/*/box/*/*
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `0`









                    ## Optional





                    ??? summary "`/geometry/*/volume_selection/*/relative` (`bool`)"
                        ```
                        /geometry/*/volume_selection/*/relative
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `False`






                ??? summary "`/geometry/*/volume_selection/*` (`object`)"
                    ```
                    /geometry/*/volume_selection/*
                    ```
                    ## Description
                    Assign the id to all volume elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                
                    **Default**: None
                    ## Required





                    ??? summary "`/geometry/*/volume_selection/*/id` (`int`)"
                        ```
                        /geometry/*/volume_selection/*/id
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification








                    ??? summary "`/geometry/*/volume_selection/*/radius` (`float`)"
                        ```
                        /geometry/*/volume_selection/*/radius
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification













                    ??? summary "`/geometry/*/volume_selection/*/center/*` (`float`)"
                        ```
                        /geometry/*/volume_selection/*/center/*
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification






                    ## Optional





                    ??? summary "`/geometry/*/volume_selection/*/relative` (`bool`)"
                        ```
                        /geometry/*/volume_selection/*/relative
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `False`






                ??? summary "`/geometry/*/volume_selection/*` (`object`)"
                    ```
                    /geometry/*/volume_selection/*
                    ```
                    ## Description
                    Assign the id to all volume elements with barycenters in a halfspace. The halfspace boundary plane is defined in one of two ways: (1) by a point in the plane and the normal, which points to the halfspace. (2) By a normal and the offset from the coordinate system origin along the line in the direction of the normal passing through the origin. In the former case, the option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                
                    **Default**: None
                    ## Required





                    ??? summary "`/geometry/*/volume_selection/*/id` (`int`)"
                        ```
                        /geometry/*/volume_selection/*/id
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification













                    ??? summary "`/geometry/*/volume_selection/*/point/*` (`float`)"
                        ```
                        /geometry/*/volume_selection/*/point/*
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
















                    ??? summary "`/geometry/*/volume_selection/*/normal/*` (`float`)"
                        ```
                        /geometry/*/volume_selection/*/normal/*
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification






                    ## Optional





                    ??? summary "`/geometry/*/volume_selection/*/relative` (`bool`)"
                        ```
                        /geometry/*/volume_selection/*/relative
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `False`








                    ??? summary "`/geometry/*/volume_selection/*/offset` (`float`)"
                        ```
                        /geometry/*/volume_selection/*/offset
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification






                ??? summary "`/geometry/*/volume_selection/*` (`object`)"
                    ```
                    /geometry/*/volume_selection/*
                    ```
                    ## Description
                    Same as halfspace, but the boundary plane is axis-aligned. The choice of axis is specified either by a string matching the regexp r"[+-][xyzXYZ]" or an int matching the regular expression [+-]?[123] where the sign is the side of the plane to select and letter or number indicates the axis to which the plane is perpendicular. The offset is the plane offset from the origin. If the relative option is set to true, the offset is with respect to the center of the bounding box.
                
                    **Default**: None
                    ## Required





                    ??? summary "`/geometry/*/volume_selection/*/id` (`int`)"
                        ```
                        /geometry/*/volume_selection/*/id
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification






                    ??? summary "`/geometry/*/volume_selection/*/axis`"
                        ```
                        /geometry/*/volume_selection/*/axis
                        ```


                        ??? summary "`/geometry/*/volume_selection/*/axis` (`int`)"
                            ```
                            /geometry/*/volume_selection/*/axis
                            ```
                            ## Description
                            <span class="todo">FIXME:</span> Missing documentation in the specification



                        ??? summary "`/geometry/*/volume_selection/*/axis` (`string`)"
                            ```
                            /geometry/*/volume_selection/*/axis
                            ```
                            ## Description
                            <span class="todo">FIXME:</span> Missing documentation in the specification








                    ??? summary "`/geometry/*/volume_selection/*/position` (`float`)"
                        ```
                        /geometry/*/volume_selection/*/position
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification



                    ## Optional





                    ??? summary "`/geometry/*/volume_selection/*/relative` (`bool`)"
                        ```
                        /geometry/*/volume_selection/*/relative
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `False`









            ??? summary "`/geometry/*/volume_selection` (`file`)"
                ```
                /geometry/*/volume_selection
                ```
                ## Description
                Load ids from a file; the file is required to have one id per volume element of the geometry
            
                **Extensions:** `['.txt']`






        ??? summary "`/geometry/*/surface_selection`"
            ```
            /geometry/*/surface_selection
            ```


            ??? summary "`/geometry/*/surface_selection` (`int`)"
                ```
                /geometry/*/surface_selection
                ```
                ## Description
                Assign specified id to all surface elements of the geometry
            
                **Default**: `0`



            ??? summary "`/geometry/*/surface_selection` (`object`)"
                ```
                /geometry/*/surface_selection
                ```
                ## Description
                Assigns ids to sides touching the bbox of the model using a threshold. Assigns 1+offset to left, 2+offset to bottom, 3+offset to right, 4+offset to top, 5+offset to front, 6+offset to back, 7+offset to everything else.
                ## Optional





                ??? summary "`/geometry/*/surface_selection/threshold` (`float`)"
                    ```
                    /geometry/*/surface_selection/threshold
                    ```
                    ## Description
                    <span class="todo">FIXME:</span> Missing documentation in the specification
                
                    **Default**: `-1`








                ??? summary "`/geometry/*/surface_selection/offset` (`int`)"
                    ```
                    /geometry/*/surface_selection/offset
                    ```
                    ## Description
                    <span class="todo">FIXME:</span> Missing documentation in the specification
                
                    **Default**: `0`









            ??? summary "`/geometry/*/surface_selection/*`"
                ```
                /geometry/*/surface_selection/*
                ```


                ??? summary "`/geometry/*/surface_selection/*` (`object`)"
                    ```
                    /geometry/*/surface_selection/*
                    ```
                    ## Description
                    Assign the id to all surface elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                
                    **Default**: None
                    ## Required





                    ??? summary "`/geometry/*/surface_selection/*/id` (`int`)"
                        ```
                        /geometry/*/surface_selection/*/id
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification


















                    ??? summary "`/geometry/*/surface_selection/*/box/*/*` (`float`)"
                        ```
                        /geometry/*/surface_selection/*/box/*/*
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `0`









                    ## Optional





                    ??? summary "`/geometry/*/surface_selection/*/relative` (`bool`)"
                        ```
                        /geometry/*/surface_selection/*/relative
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `False`






                ??? summary "`/geometry/*/surface_selection/*` (`object`)"
                    ```
                    /geometry/*/surface_selection/*
                    ```
                    ## Description
                    Assign the id to all surface elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                
                    **Default**: None
                    ## Required





                    ??? summary "`/geometry/*/surface_selection/*/id` (`int`)"
                        ```
                        /geometry/*/surface_selection/*/id
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification








                    ??? summary "`/geometry/*/surface_selection/*/radius` (`float`)"
                        ```
                        /geometry/*/surface_selection/*/radius
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification













                    ??? summary "`/geometry/*/surface_selection/*/center/*` (`float`)"
                        ```
                        /geometry/*/surface_selection/*/center/*
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification






                    ## Optional





                    ??? summary "`/geometry/*/surface_selection/*/relative` (`bool`)"
                        ```
                        /geometry/*/surface_selection/*/relative
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `False`






                ??? summary "`/geometry/*/surface_selection/*` (`object`)"
                    ```
                    /geometry/*/surface_selection/*
                    ```
                    ## Description
                    Assign the id to all surface elements with barycenters in a halfspace. The halfspace boundary plane is defined in one of two ways: (1) by a point in the plane and the normal, which points to the halfspace. (2) By a normal and the offset from the coordinate system origin along the line in the direction of the normal passing through the origin. In the former case, the option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                
                    **Default**: None
                    ## Required





                    ??? summary "`/geometry/*/surface_selection/*/id` (`int`)"
                        ```
                        /geometry/*/surface_selection/*/id
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification













                    ??? summary "`/geometry/*/surface_selection/*/point/*` (`float`)"
                        ```
                        /geometry/*/surface_selection/*/point/*
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
















                    ??? summary "`/geometry/*/surface_selection/*/normal/*` (`float`)"
                        ```
                        /geometry/*/surface_selection/*/normal/*
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification






                    ## Optional





                    ??? summary "`/geometry/*/surface_selection/*/relative` (`bool`)"
                        ```
                        /geometry/*/surface_selection/*/relative
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `False`








                    ??? summary "`/geometry/*/surface_selection/*/offset` (`float`)"
                        ```
                        /geometry/*/surface_selection/*/offset
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification






                ??? summary "`/geometry/*/surface_selection/*` (`object`)"
                    ```
                    /geometry/*/surface_selection/*
                    ```
                    ## Description
                    Same as halfspace, but the boundary plane is axis-aligned. The choice of axis is specified either by a string matching the regexp r"[+-][xyzXYZ]" or an int matching the regular expression [+-]?[123] where the sign is the side of the plane to select and letter or number indicates the axis to which the plane is perpendicular. The offset is the plane offset from the origin. If the relative option is set to true, the offset is with respect to the center of the bounding box.
                
                    **Default**: None
                    ## Required





                    ??? summary "`/geometry/*/surface_selection/*/id` (`int`)"
                        ```
                        /geometry/*/surface_selection/*/id
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification






                    ??? summary "`/geometry/*/surface_selection/*/axis`"
                        ```
                        /geometry/*/surface_selection/*/axis
                        ```


                        ??? summary "`/geometry/*/surface_selection/*/axis` (`int`)"
                            ```
                            /geometry/*/surface_selection/*/axis
                            ```
                            ## Description
                            <span class="todo">FIXME:</span> Missing documentation in the specification



                        ??? summary "`/geometry/*/surface_selection/*/axis` (`string`)"
                            ```
                            /geometry/*/surface_selection/*/axis
                            ```
                            ## Description
                            <span class="todo">FIXME:</span> Missing documentation in the specification








                    ??? summary "`/geometry/*/surface_selection/*/position` (`float`)"
                        ```
                        /geometry/*/surface_selection/*/position
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification



                    ## Optional





                    ??? summary "`/geometry/*/surface_selection/*/relative` (`bool`)"
                        ```
                        /geometry/*/surface_selection/*/relative
                        ```
                        ## Description
                        <span class="todo">FIXME:</span> Missing documentation in the specification
                    
                        **Default**: `False`









            ??? summary "`/geometry/*/surface_selection` (`file`)"
                ```
                /geometry/*/surface_selection
                ```
                ## Description
                Load ids from a file; the file has a list of surface elements of the geometry specified as triples of vertex indices, with one id for each; each triple must correspond to a surface element
            
                **Extensions:** `['.txt']`








        ??? summary "`/geometry/*/curve_selection` (`object`)"
            ```
            /geometry/*/curve_selection
            ```
            ## Description
            Selection of curves
        
            **Default**: None








        ??? summary "`/geometry/*/point_selection` (`object`)"
            ```
            /geometry/*/point_selection
            ```
            ## Description
            Selection of points
        
            **Default**: None








        ??? summary "`/geometry/*/n_refs` (`int`)"
            ```
            /geometry/*/n_refs
            ```
            ## Description
            number of uniform refinements
        
            **Default**: `0`








        ??? summary "`/geometry/*/advanced` (`object`)"
            ```
            /geometry/*/advanced
            ```
            ## Description
            Advanced options for geometry
        
            **Default**: None
            ## Optional





            ??? summary "`/geometry/*/advanced/normalize_mesh` (`bool`)"
                ```
                /geometry/*/advanced/normalize_mesh
                ```
                ## Description
                Rescale the mesh to it fits in the biunit cube
            
                **Default**: `False`








            ??? summary "`/geometry/*/advanced/force_linear_geometry` (`bool`)"
                ```
                /geometry/*/advanced/force_linear_geometry
                ```
                ## Description
                Discard high-order nodes for curved geometries
            
                **Default**: `False`








            ??? summary "`/geometry/*/advanced/refinement_location` (`float`)"
                ```
                /geometry/*/advanced/refinement_location
                ```
                ## Description
                parametric location of the refinement
            
                **Default**: `0.5`








            ??? summary "`/geometry/*/advanced/min_component` (`int`)"
                ```
                /geometry/*/advanced/min_component
                ```
                ## Description
                Size of the minumum component for collision
            
                **Default**: `-1`











        ??? summary "`/geometry/*/enabled` (`bool`)"
            ```
            /geometry/*/enabled
            ```
            ## Description
            Skips the geometry if false
        
            **Default**: `True`








        ??? summary "`/geometry/*/is_obstacle` (`bool`)"
            ```
            /geometry/*/is_obstacle
            ```
            ## Description
            The geometry elements are not included in deforming geometry, only in collision computations
        
            **Default**: `False`

















    ??? summary "`/materials/*`"
        ```
        /materials/*
        ```


        ??? summary "NeoHookean"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, Young's modulus(E), Poisson ratio(nu), Density(rho), type()
        
            **Type**: NeoHookean
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/E` (`float`)"
                ```
                /materials/*/E
                ```
                ## Description
                Young's modulus








            ??? summary "`/materials/*/nu` (`float`)"
                ```
                /materials/*/nu
                ```
                ## Description
                Poisson ratio



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "NeoHookean"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, Lame first(lambda), Lame second(mu), Density(rho), type()
        
            **Type**: NeoHookean
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/lambda` (`float`)"
                ```
                /materials/*/lambda
                ```
                ## Description
                Second lame parameter








            ??? summary "`/materials/*/mu` (`float`)"
                ```
                /materials/*/mu
                ```
                ## Description
                First lame parameters



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "LinearElasticity"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, Young's modulus(E), Poisson ratio(nu), Density(rho), type()
        
            **Type**: LinearElasticity
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/E` (`float`)"
                ```
                /materials/*/E
                ```
                ## Description
                Young's modulus








            ??? summary "`/materials/*/nu` (`float`)"
                ```
                /materials/*/nu
                ```
                ## Description
                Poisson ratio



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "LinearElasticity"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, Lame first(lambda), Lame second(mu), Density(rho), type()
        
            **Type**: LinearElasticity
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/lambda` (`float`)"
                ```
                /materials/*/lambda
                ```
                ## Description
                Second lame parameter








            ??? summary "`/materials/*/mu` (`float`)"
                ```
                /materials/*/mu
                ```
                ## Description
                First lame parameters



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "HookeLinearElasticity"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, E, nu, Density(rho), type()
        
            **Type**: HookeLinearElasticity
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/E` (`float`)"
                ```
                /materials/*/E
                ```
                ## Description
                Young's modulus








            ??? summary "`/materials/*/nu` (`float`)"
                ```
                /materials/*/nu
                ```
                ## Description
                Poisson ratio



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "HookeLinearElasticity"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, E, nu, Density(rho), type()
        
            **Type**: HookeLinearElasticity
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`













            ??? summary "`/materials/*/elasticity_tensor/*` (`float`)"
                ```
                /materials/*/elasticity_tensor/*
                ```
                ## Description
                Entries of elasticity tensor
            
                **Default**: `0`






            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "SaintVenant"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, E, nu, Density(rho), type()
        
            **Type**: SaintVenant
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/E` (`float`)"
                ```
                /materials/*/E
                ```
                ## Description
                Young's modulus








            ??? summary "`/materials/*/nu` (`float`)"
                ```
                /materials/*/nu
                ```
                ## Description
                Poisson ratio



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "SaintVenant"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, E, nu, Density(rho), type()
        
            **Type**: SaintVenant
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`













            ??? summary "`/materials/*/elasticity_tensor/*` (`float`)"
                ```
                /materials/*/elasticity_tensor/*
                ```
                ## Description
                Entries of elasticity tensor
            
                **Default**: `0`






            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "Stokes"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, viscosity, Density(rho), type()
        
            **Type**: Stokes
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/viscosity` (`float`)"
                ```
                /materials/*/viscosity
                ```
                ## Description
                Fuild's viscosity



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "NavierStokes"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, viscosity, Density(rho), type()
        
            **Type**: NavierStokes
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/viscosity` (`float`)"
                ```
                /materials/*/viscosity
                ```
                ## Description
                Fuild's viscosity



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "IncompressibleLinearElasticity"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, Young's modulus(E), Poisson ratio(nu), Density(rho), type()
        
            **Type**: IncompressibleLinearElasticity
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/E` (`float`)"
                ```
                /materials/*/E
                ```
                ## Description
                Young's modulus








            ??? summary "`/materials/*/nu` (`float`)"
                ```
                /materials/*/nu
                ```
                ## Description
                Poisson ratio



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "IncompressibleLinearElasticity"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, Lame first(lambda), Lame second(mu), Density(rho), type()
        
            **Type**: IncompressibleLinearElasticity
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








            ??? summary "`/materials/*/lambda` (`float`)"
                ```
                /materials/*/lambda
                ```
                ## Description
                Second lame parameter








            ??? summary "`/materials/*/mu` (`float`)"
                ```
                /materials/*/mu
                ```
                ## Description
                First lame parameters



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "Laplacian"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, Density(rho), type()
        
            **Type**: Laplacian
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`






        ??? summary "Helmholtz"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, k, Density(rho), type()
        
            **Type**: Helmholtz
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`








            ??? summary "`/materials/*/k` (`float`)"
                ```
                /materials/*/k
                ```
                ## Description
                Scaling for Helmholtz
            
                **Default**: `1`






        ??? summary "Bilaplacian"
            ```
            /materials/*
            ```
            ## Description
            Material Parameters including id, Density(rho), type()
        
            **Type**: Bilaplacian
            ## Required





            ??? summary "`/materials/*/type` (`string`)"
                ```
                /materials/*/type
                ```
                ## Description
                Type of material
            
                **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`



            ## Optional





            ??? summary "`/materials/*/id` (`int`)"
                ```
                /materials/*/id
                ```
                ## Description
                id
            
                **Default**: `0`








            ??? summary "`/materials/*/rho` (`float`)"
                ```
                /materials/*/rho
                ```
                ## Description
                Density
            
                **Default**: `1`









    ## Optional



    ??? summary "`/preset_problem`"
        ```
        /preset_problem
        ```


        ??? summary "Linear"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Linear
        
            **Default**: 'skip'
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "Quadratic"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Quadratic
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "Cubic"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Cubic
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "Sine"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Sine
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "Franke"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Franke
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "FrankeOld"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: FrankeOld
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "GenericScalarExact"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: GenericScalarExact
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? summary "`/preset_problem/func` (`int`)"
                ```
                /preset_problem/func
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0`






        ??? summary "Zero_BC"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Zero_BC
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "Elastic"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Elastic
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "Walk"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Walk
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "TorsionElastic"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: TorsionElastic
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? summary "`/preset_problem/axis_coordiante` (`int`)"
                ```
                /preset_problem/axis_coordiante
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `2`








            ??? summary "`/preset_problem/n_turns` (`float`)"
                ```
                /preset_problem/n_turns
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0.5`








            ??? summary "`/preset_problem/fixed_boundary` (`int`)"
                ```
                /preset_problem/fixed_boundary
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `5`








            ??? summary "`/preset_problem/turning_boundary` (`int`)"
                ```
                /preset_problem/turning_boundary
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `6`













            ??? summary "`/preset_problem/bbox_center/*` (`float`)"
                ```
                /preset_problem/bbox_center/*
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0`









        ??? summary "DoubleTorsionElastic"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: DoubleTorsionElastic
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? summary "`/preset_problem/axis_coordiante0` (`int`)"
                ```
                /preset_problem/axis_coordiante0
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `2`








            ??? summary "`/preset_problem/axis_coordiante1` (`int`)"
                ```
                /preset_problem/axis_coordiante1
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `2`








            ??? summary "`/preset_problem/angular_v0` (`float`)"
                ```
                /preset_problem/angular_v0
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0.5`








            ??? summary "`/preset_problem/angular_v1` (`float`)"
                ```
                /preset_problem/angular_v1
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `-0.5`








            ??? summary "`/preset_problem/turning_boundary0` (`int`)"
                ```
                /preset_problem/turning_boundary0
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `5`








            ??? summary "`/preset_problem/turning_boundary1` (`int`)"
                ```
                /preset_problem/turning_boundary1
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `6`













            ??? summary "`/preset_problem/bbox_center/*` (`float`)"
                ```
                /preset_problem/bbox_center/*
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0`









        ??? summary "ElasticZeroBC"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: ElasticZeroBC
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "ElasticExact"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: ElasticExact
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "ElasticCantileverExact"
            ```
            /preset_problem
            ```
            ## Description
            TODO, add displacement, E, nu, formulation, mesh_size
        
            **Type**: ElasticCantileverExact
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "CompressionElasticExact"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: CompressionElasticExact
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "QuadraticElasticExact"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: QuadraticElasticExact
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "LinearElasticExact"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: LinearElasticExact
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "PointBasedTensor"
            ```
            /preset_problem
            ```
            ## Description
            TODO, add optionals
        
            **Type**: PointBasedTensor
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "Kernel"
            ```
            /preset_problem
            ```
            ## Description
            TODO, add optionals
        
            **Type**: Kernel
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? summary "`/preset_problem/formulation` (`string`)"
                ```
                /preset_problem/formulation
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `''`








            ??? summary "`/preset_problem/n_kernels` (`int`)"
                ```
                /preset_problem/n_kernels
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0`








            ??? summary "`/preset_problem/kernel_distance` (`float`)"
                ```
                /preset_problem/kernel_distance
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0`








            ??? summary "`/preset_problem/kernel_weights` (`string`)"
                ```
                /preset_problem/kernel_weights
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `''`






        ??? summary "Node"
            ```
            /preset_problem
            ```
            ## Description
            TODO, add optionals
        
            **Type**: Node
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "TimeDependentScalar"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: TimeDependentScalar
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "MinSurf"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: MinSurf
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "Gravity"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Gravity
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        ??? summary "ConstantVelocity"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: ConstantVelocity
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "TwoSpheres"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: TwoSpheres
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "DrivenCavity"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: DrivenCavity
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "DrivenCavityC0"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: DrivenCavityC0
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "DrivenCavitySmooth"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: DrivenCavitySmooth
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "Flow"
            ```
            /preset_problem
            ```
            ## Description
            TODO, add inflow, outflow, inflow_amout, outflow_amout, direction, obstacle
        
            **Type**: Flow
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "FlowWithObstacle"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: FlowWithObstacle
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        ??? summary "CornerFlow"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: CornerFlow
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional













        ??? summary "UnitFlowWithObstacle"
            ```
            /preset_problem
            ```
            ## Description
            TODO, add inflow_id, direction, no_slip
        
            **Type**: UnitFlowWithObstacle
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        ??? summary "StokesLaw"
            ```
            /preset_problem
            ```
            ## Description
            TODO, add radius
        
            **Type**: StokesLaw
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional













        ??? summary "TaylorGreenVortex"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: TaylorGreenVortex
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        ??? summary "SimpleStokeProblemExact"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: SimpleStokeProblemExact
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? summary "`/preset_problem/func` (`int`)"
                ```
                /preset_problem/func
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0`






        ??? summary "SineStokeProblemExact"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: SineStokeProblemExact
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "TransientStokeProblemExact"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: TransientStokeProblemExact
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional





            ??? summary "`/preset_problem/func` (`int`)"
                ```
                /preset_problem/func
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0`











        ??? summary "Kovnaszy"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Kovnaszy
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional













        ??? summary "Airfoil"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Airfoil
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional








        ??? summary "Lshape"
            ```
            /preset_problem
            ```
            ## Description
            <span class="todo">TODO</span>
        
            **Type**: Lshape
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            ## Optional













        ??? summary "TestProblem"
            ```
            /preset_problem
            ```
            ## Description
            TODO, type, omega, is_scalar
        
            **Type**: TestProblem
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        ??? summary "BilaplacianProblemWithSolution"
            ```
            /preset_problem
            ```
            ## Description
            TODO, type, omega, is_scalar
        
            **Type**: BilaplacianProblemWithSolution
            ## Required





            ??? summary "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`











    ??? summary "`/common` (`file`)"
        ```
        /common
        ```
        ## Description
        Path to common settings will patch the current file
    
        **Default**: `''`
    
        **Extensions:** `['.json']`








    ??? summary "`/root_path` (`string`)"
        ```
        /root_path
        ```
        ## Description
        path for all relative paths, set automatically to the folder containing this json
    
        **Default**: `''`








    ??? summary "`/space` (`object`)"
        ```
        /space
        ```
        ## Description
        Options related to the FE space.
    
        **Default**: None
        ## Optional



        ??? summary "`/space/discr_order`"
            ```
            /space/discr_order
            ```


            ??? summary "`/space/discr_order` (`int`)"
                ```
                /space/discr_order
                ```
                ## Description
                Lagrange element order for the space for the main unknown, for all elements.
            
                **Default**: `1`



            ??? summary "`/space/discr_order` (`file`)"
                ```
                /space/discr_order
                ```
                ## Description
                Path to file containing Lagrange element order for the space for the main unknown per element.
            
                **Extensions:** `['.txt', '.bin']`








            ??? summary "`/space/discr_order/*` (`object`)"
                ```
                /space/discr_order/*
                ```
                ## Description
                Lagrange element order for the a space tagged with volume ID for the main unknown.
                ## Required



                ??? summary "`/space/discr_order/*/id`"
                    ```
                    /space/discr_order/*/id
                    ```


                    ??? summary "`/space/discr_order/*/id` (`int`)"
                        ```
                        /space/discr_order/*/id
                        ```
                        ## Description
                        Volume selection ID to apply the discr_order to.








                    ??? summary "`/space/discr_order/*/id/*` (`int`)"
                        ```
                        /space/discr_order/*/id/*
                        ```
                        ## Description
                        Volume selection ID to apply the discr_order to.











                ??? summary "`/space/discr_order/*/order` (`int`)"
                    ```
                    /space/discr_order/*/order
                    ```
                    ## Description
                    Lagrange element order for the space for the main unknown, for all elements.














        ??? summary "`/space/pressure_discr_order` (`int`)"
            ```
            /space/pressure_discr_order
            ```
            ## Description
             Lagrange element order for the space for the pressure unknown, for all elements.
        
            **Default**: `1`








        ??? summary "`/space/use_p_ref` (`bool`)"
            ```
            /space/use_p_ref
            ```
            ## Description
            Perform a priori p-refinement based on element shape, as described in 'Decoupling..' paper.
        
            **Default**: `False`








        ??? summary "`/space/advanced` (`object`)"
            ```
            /space/advanced
            ```
            ## Description
            Advanced settings for the FE space.
        
            **Default**: None
            ## Optional





            ??? summary "`/space/advanced/discr_order_max` (`int`)"
                ```
                /space/advanced/discr_order_max
                ```
                ## Description
                Maximal discretization order in adaptive p-refinement and hp-refinement
            
                **Default**: `4`








            ??? summary "`/space/advanced/serendipity` (`bool`)"
                ```
                /space/advanced/serendipity
                ```
                ## Description
                Use serendipity elements for quad/hex elements of degree 2.
            
                **Default**: `False`








            ??? summary "`/space/advanced/isoparametric` (`bool`)"
                ```
                /space/advanced/isoparametric
                ```
                ## Description
                Forces geometric map basis to be the same degree as the main variable basis, irrespective of the degree associated with the geom. map degrees associated with the elements of the geometry.
            
                **Default**: `False`








            ??? summary "`/space/advanced/use_spline` (`bool`)"
                ```
                /space/advanced/use_spline
                ```
                ## Description
                Use bi/triquadratic spline basis for quad/hex elements not adjacent to polyhedral elements, see 'PolySpline..' paper for details.
            
                **Default**: `False`








            ??? summary "`/space/advanced/bc_method` (`string`)"
                ```
                /space/advanced/bc_method
                ```
                ## Description
                Method for imposing analytic Dirichet boundary conditions. If 'lsq' (least-squares fit), then the bc function is sampled at quadrature points, and the FEspace nodal values on the boundary are determined by minimizing L2 norm of the difference. If 'sample', then the analytic bc function is sampled at the boundary nodes.
            
                **Default**: `'lsq'`
            
                **Options:** `['lsq', 'sample']`








            ??? summary "`/space/advanced/n_boundary_samples` (`int`)"
                ```
                /space/advanced/n_boundary_samples
                ```
                ## Description
                Per-element number of boundary samples for analytic Dirichlet and Neumann boundary conditions.
            
                **Default**: `-1`








            ??? summary "`/space/advanced/quadrature_order` (`int`)"
                ```
                /space/advanced/quadrature_order
                ```
                ## Description
                Minimal quadrature order to use in matrix and rhs assembly; the actual order is determined as min(2*(p-1)+1,quadrature_order).
            
                **Default**: `-1`








            ??? summary "`/space/advanced/poly_bases` (`string`)"
                ```
                /space/advanced/poly_bases
                ```
                ## Description
                Type of basis to use for a polygonal element, one of MFSHarmonic, MeanValue, see 'PolySpline..' paper for details.
            
                **Default**: `'MFSHarmonic'`
            
                **Options:** `['MFSHarmonic', 'MeanValue']`








            ??? summary "`/space/advanced/integral_constraints` (`int`)"
                ```
                /space/advanced/integral_constraints
                ```
                ## Description
                Number of constraints for non-conforming polygonal basis;  0, 1, or 2; see 'PolySpline..' paper for details.
            
                **Default**: `2`








            ??? summary "`/space/advanced/n_harmonic_samples` (`int`)"
                ```
                /space/advanced/n_harmonic_samples
                ```
                ## Description
                If MFSHarmonics is used for a polygonal element, number of collocation samples used in the basis construction;see 'PolySpline..' paper for details.
            
                **Default**: `10`








            ??? summary "`/space/advanced/force_no_ref_for_harmonic` (`bool`)"
                ```
                /space/advanced/force_no_ref_for_harmonic
                ```
                ## Description
                If true, do not do uniform global refinement if the mesh contains polygonal elements.
            
                **Default**: `False`








            ??? summary "`/space/advanced/B` (`int`)"
                ```
                /space/advanced/B
                ```
                ## Description
                The target deviation of the error on elements from perfect element error, for a priori geometry-dependent p-refinement, see 'Decoupling .. ' paper.
            
                **Default**: `3`








            ??? summary "`/space/advanced/h1_formula` (`bool`)"
                ```
                /space/advanced/h1_formula
                ```
                ## Description
                
            
                **Default**: `False`








            ??? summary "`/space/advanced/count_flipped_els` (`bool`)"
                ```
                /space/advanced/count_flipped_els
                ```
                ## Description
                Count the number of elements with Jacobian of the geometric map not positive at quadrature points.
            
                **Default**: `True`












    ??? summary "`/time`"
        ```
        /time
        ```


        ??? summary "`/time` (`object`)"
            ```
            /time
            ```
            ## Description
            The time parameters: start time t0, end time tend, time step dt. 
        
            **Default**: 'skip'
            ## Required





            ??? summary "`/time/tend` (`float`)"
                ```
                /time/tend
                ```
                ## Description
                Ending time
            
                **Range:** `(0, inf)`








            ??? summary "`/time/dt` (`float`)"
                ```
                /time/dt
                ```
                ## Description
                Delta t
            
                **Range:** `(0, inf)`



            ## Optional





            ??? summary "`/time/t0` (`float`)"
                ```
                /time/t0
                ```
                ## Description
                Startning time
            
                **Range:** `(0, inf)`
            
                **Default**: `0`








            ??? summary "`/time/integrator` (`string`)"
                ```
                /time/integrator
                ```
                ## Description
                Time integrator
            
                **Default**: `'ImplicitEuler'`
            
                **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`








            ??? summary "`/time/newmark` (`object`)"
                ```
                /time/newmark
                ```
                ## Description
                Options for Newmark
            
                **Default**: None
                ## Optional





                ??? summary "`/time/newmark/gamma` (`float`)"
                    ```
                    /time/newmark/gamma
                    ```
                    ## Description
                    Newmark gamma
                
                    **Default**: `0.5`








                ??? summary "`/time/newmark/beta` (`float`)"
                    ```
                    /time/newmark/beta
                    ```
                    ## Description
                    Newmark beta
                
                    **Default**: `0.25`











            ??? summary "`/time/BDF` (`object`)"
                ```
                /time/BDF
                ```
                ## Description
                Options for BDF
            
                **Default**: None
                ## Optional





                ??? summary "`/time/BDF/steps` (`int`)"
                    ```
                    /time/BDF/steps
                    ```
                    ## Description
                    BDF order
                
                    **Default**: `1`









        ??? summary "`/time` (`object`)"
            ```
            /time
            ```
            ## Description
            The time parameters: start time t0, time step dt, number of time steps. 
            ## Required





            ??? summary "`/time/time_steps` (`int`)"
                ```
                /time/time_steps
                ```
                ## Description
                Number of time steps
            
                **Range:** `(0, inf)`








            ??? summary "`/time/dt` (`float`)"
                ```
                /time/dt
                ```
                ## Description
                Delta t
            
                **Range:** `(0, inf)`



            ## Optional





            ??? summary "`/time/t0` (`float`)"
                ```
                /time/t0
                ```
                ## Description
                Startning time
            
                **Range:** `(0, inf)`
            
                **Default**: `0`








            ??? summary "`/time/integrator` (`string`)"
                ```
                /time/integrator
                ```
                ## Description
                Time integrator
            
                **Default**: `'ImplicitEuler'`
            
                **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`








            ??? summary "`/time/newmark` (`object`)"
                ```
                /time/newmark
                ```
                ## Description
                Options for Newmark
            
                **Default**: None
                ## Optional





                ??? summary "`/time/newmark/gamma` (`float`)"
                    ```
                    /time/newmark/gamma
                    ```
                    ## Description
                    Newmark gamma
                
                    **Default**: `0.5`








                ??? summary "`/time/newmark/beta` (`float`)"
                    ```
                    /time/newmark/beta
                    ```
                    ## Description
                    Newmark beta
                
                    **Default**: `0.25`











            ??? summary "`/time/BDF` (`object`)"
                ```
                /time/BDF
                ```
                ## Description
                Options for BDF
            
                **Default**: None
                ## Optional





                ??? summary "`/time/BDF/steps` (`int`)"
                    ```
                    /time/BDF/steps
                    ```
                    ## Description
                    BDF order
                
                    **Default**: `1`









        ??? summary "`/time` (`object`)"
            ```
            /time
            ```
            ## Description
            The time parameters: start time t0, end time tend, number of time steps. 
            ## Required





            ??? summary "`/time/time_steps` (`int`)"
                ```
                /time/time_steps
                ```
                ## Description
                Number of time steps
            
                **Range:** `(0, inf)`








            ??? summary "`/time/tend` (`float`)"
                ```
                /time/tend
                ```
                ## Description
                Ending time
            
                **Range:** `(0, inf)`



            ## Optional





            ??? summary "`/time/t0` (`float`)"
                ```
                /time/t0
                ```
                ## Description
                Startning time
            
                **Range:** `(0, inf)`
            
                **Default**: `0`








            ??? summary "`/time/integrator` (`string`)"
                ```
                /time/integrator
                ```
                ## Description
                Time integrator
            
                **Default**: `'ImplicitEuler'`
            
                **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`








            ??? summary "`/time/newmark` (`object`)"
                ```
                /time/newmark
                ```
                ## Description
                Options for Newmark
            
                **Default**: None
                ## Optional





                ??? summary "`/time/newmark/gamma` (`float`)"
                    ```
                    /time/newmark/gamma
                    ```
                    ## Description
                    Newmark gamma
                
                    **Default**: `0.5`








                ??? summary "`/time/newmark/beta` (`float`)"
                    ```
                    /time/newmark/beta
                    ```
                    ## Description
                    Newmark beta
                
                    **Default**: `0.25`











            ??? summary "`/time/BDF` (`object`)"
                ```
                /time/BDF
                ```
                ## Description
                Options for BDF
            
                **Default**: None
                ## Optional





                ??? summary "`/time/BDF/steps` (`int`)"
                    ```
                    /time/BDF/steps
                    ```
                    ## Description
                    BDF order
                
                    **Default**: `1`














    ??? summary "`/contact` (`object`)"
        ```
        /contact
        ```
        ## Description
        Contact handling parameters.
    
        **Default**: None
        ## Optional





        ??? summary "`/contact/enabled` (`bool`)"
            ```
            /contact/enabled
            ```
            ## Description
            True if contact handling is enabled
        
            **Default**: `False`








        ??? summary "`/contact/dhat` (`float`)"
            ```
            /contact/dhat
            ```
            ## Description
            IPC barrier function parameter (see IPC paper)
        
            **Default**: `0.001`








        ??? summary "`/contact/dhat_percentage` (`float`)"
            ```
            /contact/dhat_percentage
            ```
            ## Description
            dhat as percentage of the diagonal of the bounding box
        
            **Default**: `0.8`








        ??? summary "`/contact/epsv` (`float`)"
            ```
            /contact/epsv
            ```
            ## Description
            IPC friction smoothing parameter (see IPC paper) 
        
            **Default**: `0.001`








        ??? summary "`/contact/friction_coefficient` (`float`)"
            ```
            /contact/friction_coefficient
            ```
            ## Description
            Friction Coefficient
        
            **Default**: `0`











    ??? summary "`/solver` (`object`)"
        ```
        /solver
        ```
        ## Description
        The settings for the solver including Linear solver, nonlinear solver, and some advanced options
    
        **Default**: None
        ## Optional





        ??? summary "`/solver/linear` (`object`)"
            ```
            /solver/linear
            ```
            ## Description
            Settings for linear solver
        
            **Default**: None
            ## Optional





            ??? summary "`/solver/linear/solver` (`string`)"
                ```
                /solver/linear/solver
                ```
                ## Description
                Linear solver type
            
                **Default**: `''`








            ??? summary "`/solver/linear/precond` (`string`)"
                ```
                /solver/linear/precond
                ```
                ## Description
                Preconditioner for iterative linear solver
            
                **Default**: `''`











        ??? summary "`/solver/nonlinear` (`object`)"
            ```
            /solver/nonlinear
            ```
            ## Description
            Settings for nonlinear solver. Interior-loop linear solver settings are defined in the solver/linear section
        
            **Default**: None
            ## Optional





            ??? summary "`/solver/nonlinear/solver` (`string`)"
                ```
                /solver/nonlinear/solver
                ```
                ## Description
                Nonlinear solver type
            
                **Default**: `'newton'`
            
                **Options:** `['newton', 'lbfgs']`








            ??? summary "`/solver/nonlinear/f_delta` (`float`)"
                ```
                /solver/nonlinear/f_delta
                ```
                ## Description
                Stopping criterion: minimal change of the energy f for the iterations to continue
            
                **Default**: `1e-10`








            ??? summary "`/solver/nonlinear/grad_norm` (`float`)"
                ```
                /solver/nonlinear/grad_norm
                ```
                ## Description
                Stopping criterion: Minimal gradient norm for the iterations to continue
            
                **Default**: `1e-08`








            ??? summary "`/solver/nonlinear/max_iterations` (`int`)"
                ```
                /solver/nonlinear/max_iterations
                ```
                ## Description
                Maximum number of iterations for a non-linear solve.
            
                **Default**: `1000`








            ??? summary "`/solver/nonlinear/use_grad_norm` (`bool`)"
                ```
                /solver/nonlinear/use_grad_norm
                ```
                ## Description
                If true, enable gradient-norm stopping criterion, absolute (if relative_gradient is false), or relative to the initial gradient magnitude before the first iteration, otherwise.
            
                **Default**: `True`








            ??? summary "`/solver/nonlinear/relative_gradient` (`bool`)"
                ```
                /solver/nonlinear/relative_gradient
                ```
                ## Description
                If true, use relative gradient norm threshold, use absolute otherwise
            
                **Default**: `False`








            ??? summary "`/solver/nonlinear/line_search` (`object`)"
                ```
                /solver/nonlinear/line_search
                ```
                ## Description
                Settings for line search in the nonlinear solver
            
                **Default**: None
                ## Optional





                ??? summary "`/solver/nonlinear/line_search/method` (`string`)"
                    ```
                    /solver/nonlinear/line_search/method
                    ```
                    ## Description
                    line search type
                
                    **Default**: `'backtracking'`
                
                    **Options:** `['armijo', 'armijo_alt', 'backtracking', 'more_thuente', 'none']`








                ??? summary "`/solver/nonlinear/line_search/use_grad_norm_tol` (`float`)"
                    ```
                    /solver/nonlinear/line_search/use_grad_norm_tol
                    ```
                    ## Description
                    When the energy is smaller than use_grad_norm_tol, line search uses norm of gradient instead of energy
                
                    **Default**: `0.0001`














        ??? summary "`/solver/augmented_lagrangian` (`object`)"
            ```
            /solver/augmented_lagrangian
            ```
            ## Description
            Parameters for the AL for imposing Dirichlet bc. If the bc are not imposable, we add w*||u - bc||^2 to the energy (u is the solution at the Dirichlet nodes and bc are the Dirichlet values). After convergence, we try to impose bc again, in case of failure we double w until max_weight.
        
            **Default**: None
            ## Optional





            ??? summary "`/solver/augmented_lagrangian/initial_weight` (`float`)"
                ```
                /solver/augmented_lagrangian/initial_weight
                ```
                ## Description
                Initial weight for AL
            
                **Default**: `1000000.0`








            ??? summary "`/solver/augmented_lagrangian/max_weight` (`float`)"
                ```
                /solver/augmented_lagrangian/max_weight
                ```
                ## Description
                Maximum AL weight
            
                **Default**: `100000000000.0`








            ??? summary "`/solver/augmented_lagrangian/force` (`bool`)"
                ```
                /solver/augmented_lagrangian/force
                ```
                ## Description
                Always enable AL, even when BC can be imposed
            
                **Default**: `False`











        ??? summary "`/solver/contact` (`object`)"
            ```
            /solver/contact
            ```
            ## Description
            Settings for contact handling in the solver.
        
            **Default**: None
            ## Optional





            ??? summary "`/solver/contact/CCD` (`object`)"
                ```
                /solver/contact/CCD
                ```
                ## Description
                CCD options
            
                **Default**: None
                ## Optional





                ??? summary "`/solver/contact/CCD/broad_phase` (`string`)"
                    ```
                    /solver/contact/CCD/broad_phase
                    ```
                    ## Description
                    Broad phase collision-detection algorithm to use
                
                    **Default**: `'hash_grid'`
                
                    **Options:** `['hash_grid', 'HG', 'brute_force', 'BF', 'spatial_hash', 'SH', 'sweep_and_tiniest_queue', 'STQ', 'sweep_and_tiniest_queue_gpu', 'STQ_GPU']`








                ??? summary "`/solver/contact/CCD/tolerance` (`float`)"
                    ```
                    /solver/contact/CCD/tolerance
                    ```
                    ## Description
                    CCD tolerance
                
                    **Default**: `1e-06`








                ??? summary "`/solver/contact/CCD/max_iterations` (`float`)"
                    ```
                    /solver/contact/CCD/max_iterations
                    ```
                    ## Description
                    Maximum number of iterations for continuous collision detection
                
                    **Default**: `1000000.0`











            ??? summary "`/solver/contact/friction_iterations` (`int`)"
                ```
                /solver/contact/friction_iterations
                ```
                ## Description
                Maximum number of update iterations for lagged friction formulation (see IPC paper).
            
                **Default**: `1`








            ??? summary "`/solver/contact/friction_convergence_tol` (`float`)"
                ```
                /solver/contact/friction_convergence_tol
                ```
                ## Description
                Tolerence for friction convergence
            
                **Default**: `0.01`






            ??? summary "`/solver/contact/barrier_stiffness`"
                ```
                /solver/contact/barrier_stiffness
                ```


                ??? summary "`/solver/contact/barrier_stiffness` (`string`)"
                    ```
                    /solver/contact/barrier_stiffness
                    ```
                    ## Description
                    How coefficient of clamped log-barrier function for contact is updated
                
                    **Default**: `'adaptive'`
                
                    **Options:** `['adaptive']`



                ??? summary "`/solver/contact/barrier_stiffness` (`float`)"
                    ```
                    /solver/contact/barrier_stiffness
                    ```
                    ## Description
                    The coefficient of clamped log-barrier function value when not adaptive








            ??? summary "`/solver/contact/lagged_damping_weight` (`int`)"
                ```
                /solver/contact/lagged_damping_weight
                ```
                ## Description
                <span class="todo">TODO</span>
            
                **Default**: `0`











        ??? summary "`/solver/ignore_inertia` (`bool`)"
            ```
            /solver/ignore_inertia
            ```
            ## Description
            Ignore inertia in time dependent. Used for doing incremental load.
        
            **Default**: `False`








        ??? summary "`/solver/advanced` (`object`)"
            ```
            /solver/advanced
            ```
            ## Description
            Advanced settings for the solver
        
            **Default**: None
            ## Optional





            ??? summary "`/solver/advanced/cache_size` (`int`)"
                ```
                /solver/advanced/cache_size
                ```
                ## Description
                Maximum number of elements when the assembly values are cached.
            
                **Default**: `900000`








            ??? summary "`/solver/advanced/lump_mass_matrix` (`bool`)"
                ```
                /solver/advanced/lump_mass_matrix
                ```
                ## Description
                If true, use diagonal mass matrix with entries on the diagonal equal to the sum of entries in each row of the full mass matrix.}
            
                **Default**: `False`














    ??? summary "`/boundary_conditions` (`object`)"
        ```
        /boundary_conditions
        ```
        ## Description
        The settings for boundary conditions. 
    
        **Default**: None
        ## Optional



        ??? summary "`/boundary_conditions/rhs`"
            ```
            /boundary_conditions/rhs
            ```


            ??? summary "`/boundary_conditions/rhs` (`float`)"
                ```
                /boundary_conditions/rhs
                ```
                ## Description
                Right-hand side of the system being solved for scalar-valued pdes



            ??? summary "`/boundary_conditions/rhs` (`string`)"
                ```
                /boundary_conditions/rhs
                ```
                ## Description
                Right-hand side of the system being solved as a function of x,y,z,t






            ??? summary "`/boundary_conditions/rhs/*`"
                ```
                /boundary_conditions/rhs/*
                ```


                ??? summary "`/boundary_conditions/rhs/*` (`float`)"
                    ```
                    /boundary_conditions/rhs/*
                    ```
                    ## Description
                    Right-hand side of the system being solved, value
                
                    **Default**: `0`



                ??? summary "`/boundary_conditions/rhs/*` (`string`)"
                    ```
                    /boundary_conditions/rhs/*
                    ```
                    ## Description
                    Right-hand side of the system being solved as a function of x,y,z,t














        ??? summary "`/boundary_conditions/dirichlet_boundary/*`"
            ```
            /boundary_conditions/dirichlet_boundary/*
            ```


            ??? summary "`/boundary_conditions/dirichlet_boundary/*` (`object`)"
                ```
                /boundary_conditions/dirichlet_boundary/*
                ```
                ## Description
                Dirichlet boundary condition.
            
                **Default**: None
                ## Required



                ??? summary "`/boundary_conditions/dirichlet_boundary/*/id`"
                    ```
                    /boundary_conditions/dirichlet_boundary/*/id
                    ```


                    ??? summary "`/boundary_conditions/dirichlet_boundary/*/id` (`int`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/id
                        ```
                        ## Description
                        id of Dirichlet boundary condition from surface selection



                    ??? summary "`/boundary_conditions/dirichlet_boundary/*/id` (`string`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/id
                        ```
                        ## Description
                        select all ids
                    
                        **Options:** `['all']`











                ??? summary "`/boundary_conditions/dirichlet_boundary/*/value/*`"
                    ```
                    /boundary_conditions/dirichlet_boundary/*/value/*
                    ```


                    ??? summary "`/boundary_conditions/dirichlet_boundary/*/value/*` (`string`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/value/*
                        ```
                        ## Description
                        Values of Dirichlet boundary condition for each dimension as a function of x,y,z,t



                    ??? summary "`/boundary_conditions/dirichlet_boundary/*/value/*` (`float`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/value/*
                        ```
                        ## Description
                        Values of Dirichlet boundary condition for each dimension






                ## Optional










                ??? summary "`/boundary_conditions/dirichlet_boundary/*/dimension/*` (`bool`)"
                    ```
                    /boundary_conditions/dirichlet_boundary/*/dimension/*
                    ```
                    ## Description
                    value
                
                    **Default**: `True`









            ??? summary "`/boundary_conditions/dirichlet_boundary/*` (`string`)"
                ```
                /boundary_conditions/dirichlet_boundary/*
                ```
                ## Description
                Dirichlet boundary condition loaded from a file, <node_id> <bc values>, 1 for scalar, 2/3 for tensor depending on dimension
















        ??? summary "`/boundary_conditions/neumann_boundary/*` (`object`)"
            ```
            /boundary_conditions/neumann_boundary/*
            ```
            ## Description
            Neumann boundary condition
        
            **Default**: None
            ## Optional





            ??? summary "`/boundary_conditions/neumann_boundary/*/id` (`int`)"
                ```
                /boundary_conditions/neumann_boundary/*/id
                ```
                ## Description
                id of Neumann boundary condition
            
                **Default**: `1`











            ??? summary "`/boundary_conditions/neumann_boundary/*/value/*`"
                ```
                /boundary_conditions/neumann_boundary/*/value/*
                ```


                ??? summary "`/boundary_conditions/neumann_boundary/*/value/*` (`string`)"
                    ```
                    /boundary_conditions/neumann_boundary/*/value/*
                    ```
                    ## Description
                    Values of Neumann boundary condition for each dimension as function of x,y,z,t
                
                    **Default**: `''`



                ??? summary "`/boundary_conditions/neumann_boundary/*/value/*` (`float`)"
                    ```
                    /boundary_conditions/neumann_boundary/*/value/*
                    ```
                    ## Description
                    Values of Neumann boundary condition for each dimension
                
                    **Default**: `0`






















        ??? summary "`/boundary_conditions/pressure_boundary/*` (`object`)"
            ```
            /boundary_conditions/pressure_boundary/*
            ```
            ## Description
            pressure BC entry
        
            **Default**: None
            ## Required





            ??? summary "`/boundary_conditions/pressure_boundary/*/id` (`int`)"
                ```
                /boundary_conditions/pressure_boundary/*/id
                ```
                ## Description
                id for the pressure Neumann boundary condition











            ??? summary "`/boundary_conditions/pressure_boundary/*/value/*`"
                ```
                /boundary_conditions/pressure_boundary/*/value/*
                ```


                ??? summary "`/boundary_conditions/pressure_boundary/*/value/*` (`string`)"
                    ```
                    /boundary_conditions/pressure_boundary/*/value/*
                    ```
                    ## Description
                    Values of pressure Neumann boundary condition as a function of x,y,z,t



                ??? summary "`/boundary_conditions/pressure_boundary/*/value/*` (`float`)"
                    ```
                    /boundary_conditions/pressure_boundary/*/value/*
                    ```
                    ## Description
                    Values of pressure Neumann boundary condition






            ## Optional





















        ??? summary "`/boundary_conditions/obstacle_displacements/*` (`object`)"
            ```
            /boundary_conditions/obstacle_displacements/*
            ```
            ## Description
            Obstacle displacements
        
            **Default**: None
            ## Required





            ??? summary "`/boundary_conditions/obstacle_displacements/*/id` (`int`)"
                ```
                /boundary_conditions/obstacle_displacements/*/id
                ```
                ## Description
                id of Obstacle displacements











            ??? summary "`/boundary_conditions/obstacle_displacements/*/value/*`"
                ```
                /boundary_conditions/obstacle_displacements/*/value/*
                ```


                ??? summary "`/boundary_conditions/obstacle_displacements/*/value/*` (`string`)"
                    ```
                    /boundary_conditions/obstacle_displacements/*/value/*
                    ```
                    ## Description
                    Values of Obstacle displacements for each dimension as a function of x,y,z,t



                ??? summary "`/boundary_conditions/obstacle_displacements/*/value/*` (`float`)"
                    ```
                    /boundary_conditions/obstacle_displacements/*/value/*
                    ```
                    ## Description
                    Values of Obstacle displacements for each dimension




















    ??? summary "`/initial_conditions` (`object`)"
        ```
        /initial_conditions
        ```
        ## Description
        Initial conditions for the time-dependent problem, imposed on the main variable, its derivative or second derivative
    
        **Default**: None
        ## Optional










        ??? summary "`/initial_conditions/solution/*` (`object`)"
            ```
            /initial_conditions/solution/*
            ```
            ## Description
            A list of (id, value) pairs defining the initial conditions for the main variable values. Ids are set by selection, and values can be floats or formulas.
        
            **Default**: None
            ## Required





            ??? summary "`/initial_conditions/solution/*/id` (`int`)"
                ```
                /initial_conditions/solution/*/id
                ```
                ## Description
                id from volume selections











            ??? summary "`/initial_conditions/solution/*/value/*`"
                ```
                /initial_conditions/solution/*/value/*
                ```


                ??? summary "`/initial_conditions/solution/*/value/*` (`float`)"
                    ```
                    /initial_conditions/solution/*/value/*
                    ```
                    ## Description
                    value



                ??? summary "`/initial_conditions/solution/*/value/*` (`string`)"
                    ```
                    /initial_conditions/solution/*/value/*
                    ```
                    ## Description
                    as a function of x,y,z,t






















        ??? summary "`/initial_conditions/velocity/*` (`object`)"
            ```
            /initial_conditions/velocity/*
            ```
            ## Description
            A list of (id, value) pairs defining the initial conditions for the first derivative of the main variable values. Ids are set by selection, and values can be floats or formulas.
        
            **Default**: None
            ## Required





            ??? summary "`/initial_conditions/velocity/*/id` (`int`)"
                ```
                /initial_conditions/velocity/*/id
                ```
                ## Description
                id from volume selections











            ??? summary "`/initial_conditions/velocity/*/value/*`"
                ```
                /initial_conditions/velocity/*/value/*
                ```


                ??? summary "`/initial_conditions/velocity/*/value/*` (`float`)"
                    ```
                    /initial_conditions/velocity/*/value/*
                    ```
                    ## Description
                    value



                ??? summary "`/initial_conditions/velocity/*/value/*` (`string`)"
                    ```
                    /initial_conditions/velocity/*/value/*
                    ```
                    ## Description
                    value as a function of x,y,z,t






















        ??? summary "`/initial_conditions/acceleration/*` (`object`)"
            ```
            /initial_conditions/acceleration/*
            ```
            ## Description
            entries
        
            **Default**: None
            ## Required





            ??? summary "`/initial_conditions/acceleration/*/id` (`int`)"
                ```
                /initial_conditions/acceleration/*/id
                ```
                ## Description
                id from volume selections











            ??? summary "`/initial_conditions/acceleration/*/value/*`"
                ```
                /initial_conditions/acceleration/*/value/*
                ```


                ??? summary "`/initial_conditions/acceleration/*/value/*` (`float`)"
                    ```
                    /initial_conditions/acceleration/*/value/*
                    ```
                    ## Description
                    value
                
                    **Default**: `0`



                ??? summary "`/initial_conditions/acceleration/*/value/*` (`string`)"
                    ```
                    /initial_conditions/acceleration/*/value/*
                    ```
                    ## Description
                    value as a function of x,y,z,t




















    ??? summary "`/output` (`object`)"
        ```
        /output
        ```
        ## Description
        output settings
    
        **Default**: None
        ## Optional





        ??? summary "`/output/json` (`string`)"
            ```
            /output/json
            ```
            ## Description
            File name for json output statistics on time/error/etc.
        
            **Default**: `''`








        ??? summary "`/output/paraview` (`object`)"
            ```
            /output/paraview
            ```
            ## Description
            Output in paraview format
        
            **Default**: None
            ## Optional





            ??? summary "`/output/paraview/file_name` (`string`)"
                ```
                /output/paraview/file_name
                ```
                ## Description
                Paraview output file name
            
                **Default**: `''`








            ??? summary "`/output/paraview/vismesh_rel_area` (`float`)"
                ```
                /output/paraview/vismesh_rel_area
                ```
                ## Description
                relative area for the upsampled visualisation mesh
            
                **Default**: `1e-05`








            ??? summary "`/output/paraview/skip_frame` (`int`)"
                ```
                /output/paraview/skip_frame
                ```
                ## Description
                export every skip_frame-th frames for time dependent simulations
            
                **Default**: `1`








            ??? summary "`/output/paraview/high_order_mesh` (`bool`)"
                ```
                /output/paraview/high_order_mesh
                ```
                ## Description
                Enables/disables high-order output for paraview. Supported only for isoparametric or linear meshes with high-odrer solutions.
            
                **Default**: `True`








            ??? summary "`/output/paraview/volume` (`bool`)"
                ```
                /output/paraview/volume
                ```
                ## Description
                Export volumetric mesh
            
                **Default**: `True`








            ??? summary "`/output/paraview/surface` (`bool`)"
                ```
                /output/paraview/surface
                ```
                ## Description
                Export surface mesh (in 2d polygon)
            
                **Default**: `False`








            ??? summary "`/output/paraview/wireframe` (`bool`)"
                ```
                /output/paraview/wireframe
                ```
                ## Description
                Export the wireframe of the mesh
            
                **Default**: `False`








            ??? summary "`/output/paraview/options` (`object`)"
                ```
                /output/paraview/options
                ```
                ## Description
                Optional fields in the output
            
                **Default**: None
                ## Optional





                ??? summary "`/output/paraview/options/material` (`bool`)"
                    ```
                    /output/paraview/options/material
                    ```
                    ## Description
                    If true, write out material values sampled on the vertices of the mesh
                
                    **Default**: `False`








                ??? summary "`/output/paraview/options/body_ids` (`bool`)"
                    ```
                    /output/paraview/options/body_ids
                    ```
                    ## Description
                    Export volumes ids
                
                    **Default**: `False`








                ??? summary "`/output/paraview/options/contact_forces` (`bool`)"
                    ```
                    /output/paraview/options/contact_forces
                    ```
                    ## Description
                    If true, write out contact forces for surface
                
                    **Default**: `False`








                ??? summary "`/output/paraview/options/friction_forces` (`bool`)"
                    ```
                    /output/paraview/options/friction_forces
                    ```
                    ## Description
                    If true, write out friction forces for surface
                
                    **Default**: `False`








                ??? summary "`/output/paraview/options/velocity` (`bool`)"
                    ```
                    /output/paraview/options/velocity
                    ```
                    ## Description
                    If true, write out velocities
                
                    **Default**: `False`








                ??? summary "`/output/paraview/options/acceleration` (`bool`)"
                    ```
                    /output/paraview/options/acceleration
                    ```
                    ## Description
                    If true, write out accelerations
                
                    **Default**: `False`














        ??? summary "`/output/data` (`object`)"
            ```
            /output/data
            ```
            ## Description
            File names to write output data to.
        
            **Default**: None
            ## Optional





            ??? summary "`/output/data/solution` (`string`)"
                ```
                /output/data/solution
                ```
                ## Description
                Main variable solution. Unrolled [xyz, xyz, ...] using PolyFEM ordering. If reorder_nodes exports the solution with the same order the vertices of the input mesh as a #n x d file
            
                **Default**: `''`








            ??? summary "`/output/data/full_mat` (`string`)"
                ```
                /output/data/full_mat
                ```
                ## Description
                System matrix without boundary conditions. Doesn't work for non-linear problems
            
                **Default**: `''`








            ??? summary "`/output/data/stiffness_mat` (`string`)"
                ```
                /output/data/stiffness_mat
                ```
                ## Description
                System matrix with boundary conditions. Doesn't work for non-linear problems
            
                **Default**: `''`








            ??? summary "`/output/data/stress_mat` (`string`)"
                ```
                /output/data/stress_mat
                ```
                ## Description
                Exports stress
            
                **Default**: `''`








            ??? summary "`/output/data/u_path` (`string`)"
                ```
                /output/data/u_path
                ```
                ## Description
                Writes the complete solution in PolyFEM format, used to restart the sim
            
                **Default**: `''`








            ??? summary "`/output/data/v_path` (`string`)"
                ```
                /output/data/v_path
                ```
                ## Description
                Writes the complete velocity in PolyFEM format, used to restart the sim
            
                **Default**: `''`








            ??? summary "`/output/data/a_path` (`string`)"
                ```
                /output/data/a_path
                ```
                ## Description
                Writes the complete acceleration in PolyFEM format, used to restart the sim
            
                **Default**: `''`








            ??? summary "`/output/data/mises` (`string`)"
                ```
                /output/data/mises
                ```
                ## Description
                File name to write per-node Von Mises stress values to.
            
                **Default**: `''`








            ??? summary "`/output/data/nodes` (`string`)"
                ```
                /output/data/nodes
                ```
                ## Description
                Writes the FEM nodes
            
                **Default**: `''`








            ??? summary "`/output/data/advanced` (`object`)"
                ```
                /output/data/advanced
                ```
                ## Description
                advanced options
            
                **Default**: None
                ## Optional





                ??? summary "`/output/data/advanced/reorder_nodes` (`bool`)"
                    ```
                    /output/data/advanced/reorder_nodes
                    ```
                    ## Description
                    Reorder nodes accodring to input
                
                    **Default**: `False`














        ??? summary "`/output/advanced` (`object`)"
            ```
            /output/advanced
            ```
            ## Description
            Additional output options
        
            **Default**: None
            ## Optional





            ??? summary "`/output/advanced/timestep_prefix` (`string`)"
                ```
                /output/advanced/timestep_prefix
                ```
                ## Description
                Prefix for output file names for each time step, the final file is step_i.[vtu|vtm] where i is the time index.
            
                **Default**: `'step_'`








            ??? summary "`/output/advanced/sol_on_grid` (`float`)"
                ```
                /output/advanced/sol_on_grid
                ```
                ## Description
                exports the solution sampled on a grid, specify the grid spacing
            
                **Default**: `-1`








            ??? summary "`/output/advanced/compute_error` (`bool`)"
                ```
                /output/advanced/compute_error
                ```
                ## Description
                Enables the computation of the error. If no reference solution is provided, return the norms of the solution
            
                **Default**: `True`








            ??? summary "`/output/advanced/sol_at_node` (`int`)"
                ```
                /output/advanced/sol_at_node
                ```
                ## Description
                Write out solution values at a specific node. the values will be written in the output json file
            
                **Default**: `-1`








            ??? summary "`/output/advanced/vis_boundary_only` (`bool`)"
                ```
                /output/advanced/vis_boundary_only
                ```
                ## Description
                saves only elements touching the boundaries
            
                **Default**: `False`








            ??? summary "`/output/advanced/curved_mesh_size` (`bool`)"
                ```
                /output/advanced/curved_mesh_size
                ```
                ## Description
                upsample curved edges to compute mesh size
            
                **Default**: `False`








            ??? summary "`/output/advanced/save_solve_sequence_debug` (`bool`)"
                ```
                /output/advanced/save_solve_sequence_debug
                ```
                ## Description
                saves AL internal steps, for debugging
            
                **Default**: `False`








            ??? summary "`/output/advanced/save_time_sequence` (`bool`)"
                ```
                /output/advanced/save_time_sequence
                ```
                ## Description
                saves timesteps
            
                **Default**: `True`








            ??? summary "`/output/advanced/save_nl_solve_sequence` (`bool`)"
                ```
                /output/advanced/save_nl_solve_sequence
                ```
                ## Description
                saves obj after every non-linear iteration, for debugging
            
                **Default**: `False`








            ??? summary "`/output/advanced/spectrum` (`bool`)"
                ```
                /output/advanced/spectrum
                ```
                ## Description
                exports the spectrum of the matrix in the output json. Works only if POLYSOLVE_WITH_SPECTRA is enabled
            
                **Default**: `False`











        ??? summary "`/output/reference` (`object`)"
            ```
            /output/reference
            ```
            ## Description
            Write out the analytic/numerical ground-truth solution and or its gradient
        
            **Default**: None
            ## Optional










            ??? summary "`/output/reference/solution/*` (`string`)"
                ```
                /output/reference/solution/*
                ```
                ## Description
                value as a function of x,y,z,t
            
                **Default**: `''`
















            ??? summary "`/output/reference/gradient/*` (`string`)"
                ```
                /output/reference/gradient/*
                ```
                ## Description
                value as a function of x,y,z,t
            
                **Default**: `''`

















    ??? summary "`/input` (`object`)"
        ```
        /input
        ```
        ## Description
        input data
    
        **Default**: None
        ## Optional





        ??? summary "`/input/data` (`object`)"
            ```
            /input/data
            ```
            ## Description
            input to restart time dependent sim
        
            **Default**: None
            ## Optional





            ??? summary "`/input/data/u_path` (`string`)"
                ```
                /input/data/u_path
                ```
                ## Description
                input solution
            
                **Default**: `''`








            ??? summary "`/input/data/v_path` (`string`)"
                ```
                /input/data/v_path
                ```
                ## Description
                input velocity
            
                **Default**: `''`








            ??? summary "`/input/data/a_path` (`string`)"
                ```
                /input/data/a_path
                ```
                ## Description
                input acceleration
            
                **Default**: `''`














    ??? summary "`/authen_t1` (`object`)"
        ```
        /authen_t1
        ```
        ## Description
        use to test to compare different norms of solutions
    
        **Default**: None
        ## Optional





        ??? summary "`/authen_t1/err_h1` (`float`)"
            ```
            /authen_t1/err_h1
            ```
            ## Description
            reference h1 solution's norm
        
            **Default**: `0`








        ??? summary "`/authen_t1/err_h1_semi` (`float`)"
            ```
            /authen_t1/err_h1_semi
            ```
            ## Description
            reference h1 seminorm solution's norm
        
            **Default**: `0`








        ??? summary "`/authen_t1/err_l2` (`float`)"
            ```
            /authen_t1/err_l2
            ```
            ## Description
            reference l2 solution's norm
        
            **Default**: `0`








        ??? summary "`/authen_t1/err_linf` (`float`)"
            ```
            /authen_t1/err_linf
            ```
            ## Description
            reference linf solution's norm
        
            **Default**: `0`








        ??? summary "`/authen_t1/err_linf_grad` (`float`)"
            ```
            /authen_t1/err_linf_grad
            ```
            ## Description
            reference linf solution's gradient norm
        
            **Default**: `0`








        ??? summary "`/authen_t1/err_lp` (`float`)"
            ```
            /authen_t1/err_lp
            ```
            ## Description
            reference l8 solution's gradient norm
        
            **Default**: `0`








        ??? summary "`/authen_t1/margin` (`float`)"
            ```
            /authen_t1/margin
            ```
            ## Description
            reference tolerance used in tests
        
            **Default**: `0`








