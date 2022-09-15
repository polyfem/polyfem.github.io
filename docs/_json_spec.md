<!--Automatically generated using JSON Spec Engine-->








!!! json-spec "`/` (`object`)"
    ```
    /
    ```
    <h2>Description</h2>
    Root of the configuration file.
    <h2>Required</h2>





    ??? json-spec "`/geometry` (`list`)"
        ```
        /geometry
        ```
        <h2>Description</h2>
        List of geometry objects.





        ??? json-spec "`/geometry/*` (`object`)"
            ```
            /geometry/*
            ```
            <h2>Description</h2>
            Each geometry object stores a mesh, a set of transformations applied to it after loading, and a set of selections, which can be used to specify boundary conditions, materials, optimization parameters and other quantities that can be associated with a part of an object.
            <h2>Required</h2>





            ??? json-spec "`/geometry/*/mesh` (`file`)"
                ```
                /geometry/*/mesh
                ```
                <h2>Description</h2>
                Path of the mesh file to load.

                **Extensions:** `['.obj', '.msh', '.stl', '.ply', '.mesh']`



            <h2>Optional</h2>





            ??? json-spec "`/geometry/*/type` (`string`)"
                ```
                /geometry/*/type
                ```
                <h2>Description</h2>
                Type of geometry, currently only one supported. In future we will add stuff like planes, spheres, etc.

                **Default**: `'mesh'`

                **Options:** `['mesh']`








            ??? json-spec "`/geometry/*/extract` (`string`)"
                ```
                /geometry/*/extract
                ```
                <h2>Description</h2>
                Used to extract stuff from the mesh. Eg extract surface extracts the surface from a tet mesh.

                **Default**: `'volume'`

                **Options:** `['volume', 'edges', 'points', 'surface']`








            ??? json-spec "`/geometry/*/transformation` (`object`)"
                ```
                /geometry/*/transformation
                ```
                <h2>Description</h2>
                Geometric transformations applied to the geometry after loading it.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/geometry/*/transformation/translation` (`list`)"
                    ```
                    /geometry/*/transformation/translation
                    ```
                    <h2>Description</h2>
                    Translate (two entries for 2D problems or three entries for 3D problems).





                    ??? json-spec "`/geometry/*/transformation/translation/*` (`float`)"
                        ```
                        /geometry/*/transformation/translation/*
                        ```
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.

                        **Default**: `0`











                ??? json-spec "`/geometry/*/transformation/rotation` (`list`)"
                    ```
                    /geometry/*/transformation/rotation
                    ```
                    <h2>Description</h2>
                    Rotate, in 2D, one number, the rotation angle, in 3D, three or four Euler angles, axis+angle, or a unit quaternion. Depends on rotation mode.





                    ??? json-spec "`/geometry/*/transformation/rotation/*` (`float`)"
                        ```
                        /geometry/*/transformation/rotation/*
                        ```
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.

                        **Default**: `0`











                ??? json-spec "`/geometry/*/transformation/rotation_mode` (`string`)"
                    ```
                    /geometry/*/transformation/rotation_mode
                    ```
                    <h2>Description</h2>
                    Type of rotation, supported are any permutation of [xyz]+, axis_angle, quaternion, or rotation_vector.

                    **Default**: `'xyz'`








                ??? json-spec "`/geometry/*/transformation/scale` (`list`)"
                    ```
                    /geometry/*/transformation/scale
                    ```
                    <h2>Description</h2>
                    Scale by specified factors along axes (two entries for 2D problems or three entries for 3D problems).





                    ??? json-spec "`/geometry/*/transformation/scale/*` (`float`)"
                        ```
                        /geometry/*/transformation/scale/*
                        ```
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.

                        **Default**: `0`









                ??? json-spec "`/geometry/*/transformation/dimensions`"
                    ```
                    /geometry/*/transformation/dimensions
                    ```


                    === "`/geometry/*/transformation/dimensions` (`float`)"
                        <h2>Description</h2>
                        Scale the object so that bounding box dimensions match specified dimensions, 2 entries for 2D problems, 3 entries for 3D problems.

                        **Default**: `1`



                    === "`/geometry/*/transformation/dimensions` (`list`)"
                        <h2>Description</h2>
                        Scale the object so that bounding box dimensions match specified dimensions, 2 entries for 2D problems, 3 entries for 3D problems.





                        ??? json-spec "`/geometry/*/transformation/dimensions/*` (`float`)"
                            ```
                            /geometry/*/transformation/dimensions/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.

                            **Default**: `0`












            ??? json-spec "`/geometry/*/volume_selection`"
                ```
                /geometry/*/volume_selection
                ```


                === "`/geometry/*/volume_selection` (`int`)"
                    <h2>Description</h2>
                    Assign specified ID to all volume elements of the geometry (negative values indicate using the stored values in the MSH (default: 0)).

                    **Default**: `-1`



                === "`/geometry/*/volume_selection` (`object`)"
                    <h2>Description</h2>
                    Offsets the volume IDs loaded from the mesh.
                    <h2>Required</h2>





                    ??? json-spec "`/geometry/*/volume_selection/id_offset` (`int`)"
                        ```
                        /geometry/*/volume_selection/id_offset
                        ```
                        <h2>Description</h2>
                        Offsets the volume IDs loaded from the mesh.

                        **Default**: `0`






                === "`/geometry/*/volume_selection` (`list`)"
                    <h2>Description</h2>
                    List of selection (ID assignment) operations to apply to the geometry; operations can be box, sphere, etc.



                    ??? json-spec "`/geometry/*/volume_selection/*`"
                        ```
                        /geometry/*/volume_selection/*
                        ```


                        === "`/geometry/*/volume_selection/*` (`object`)"
                            <h2>Description</h2>
                            Assign the ID to all volume elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.

                            **Default**: `None`
                            <h2>Required</h2>





                            ??? json-spec "`/geometry/*/volume_selection/*/id` (`int`)"
                                ```
                                /geometry/*/volume_selection/*/id
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/box` (`list`)"
                                ```
                                /geometry/*/volume_selection/*/box
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/volume_selection/*/box/*` (`list`)"
                                    ```
                                    /geometry/*/volume_selection/*/box/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/volume_selection/*/box/*/*` (`float`)"
                                        ```
                                        /geometry/*/volume_selection/*/box/*/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.

                                        **Default**: `0`









                            <h2>Optional</h2>





                            ??? json-spec "`/geometry/*/volume_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/volume_selection/*/relative
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.

                                **Default**: `False`






                        === "`/geometry/*/volume_selection/*` (`object`)"
                            <h2>Description</h2>
                            Assign the ID to all volume elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.

                            **Default**: `None`
                            <h2>Required</h2>





                            ??? json-spec "`/geometry/*/volume_selection/*/id` (`int`)"
                                ```
                                /geometry/*/volume_selection/*/id
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/radius` (`float`)"
                                ```
                                /geometry/*/volume_selection/*/radius
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/center` (`list`)"
                                ```
                                /geometry/*/volume_selection/*/center
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/volume_selection/*/center/*` (`float`)"
                                    ```
                                    /geometry/*/volume_selection/*/center/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.






                            <h2>Optional</h2>





                            ??? json-spec "`/geometry/*/volume_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/volume_selection/*/relative
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.

                                **Default**: `False`






                        === "`/geometry/*/volume_selection/*` (`object`)"
                            <h2>Description</h2>
                            Assign the ID to all volume elements with barycenters in a halfspace. The halfspace boundary plane is defined in one of two ways: (1) by a point in the plane and the normal, which points to the halfspace. (2) By a normal and the offset from the coordinate system origin along the line in the direction of the normal passing through the origin. In the former case, the option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.

                            **Default**: `None`
                            <h2>Required</h2>





                            ??? json-spec "`/geometry/*/volume_selection/*/id` (`int`)"
                                ```
                                /geometry/*/volume_selection/*/id
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/point` (`list`)"
                                ```
                                /geometry/*/volume_selection/*/point
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/volume_selection/*/point/*` (`float`)"
                                    ```
                                    /geometry/*/volume_selection/*/point/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/geometry/*/volume_selection/*/normal` (`list`)"
                                ```
                                /geometry/*/volume_selection/*/normal
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/volume_selection/*/normal/*` (`float`)"
                                    ```
                                    /geometry/*/volume_selection/*/normal/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.






                            <h2>Optional</h2>





                            ??? json-spec "`/geometry/*/volume_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/volume_selection/*/relative
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.

                                **Default**: `False`








                            ??? json-spec "`/geometry/*/volume_selection/*/offset` (`float`)"
                                ```
                                /geometry/*/volume_selection/*/offset
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.






                        === "`/geometry/*/volume_selection/*` (`object`)"
                            <h2>Description</h2>
                            Same as halfspace, but the boundary plane is axis-aligned. The choice of axis is specified either by a string matching the regexp r"[+-][xyzXYZ]" or an int matching the regular expression [+-]?[123] where the sign is the side of the plane to select and letter or number indicates the axis to which the plane is perpendicular. The offset is the plane offset from the origin. If the relative option is set to true, the offset is with respect to the center of the bounding box.

                            **Default**: `None`
                            <h2>Required</h2>





                            ??? json-spec "`/geometry/*/volume_selection/*/id` (`int`)"
                                ```
                                /geometry/*/volume_selection/*/id
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.






                            ??? json-spec "`/geometry/*/volume_selection/*/axis`"
                                ```
                                /geometry/*/volume_selection/*/axis
                                ```


                                === "`/geometry/*/volume_selection/*/axis` (`int`)"
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.



                                === "`/geometry/*/volume_selection/*/axis` (`string`)"
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/volume_selection/*/position` (`float`)"
                                ```
                                /geometry/*/volume_selection/*/position
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.



                            <h2>Optional</h2>





                            ??? json-spec "`/geometry/*/volume_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/volume_selection/*/relative
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.

                                **Default**: `False`









                === "`/geometry/*/volume_selection` (`file`)"
                    <h2>Description</h2>
                    Load ids from a file; the file is required to have one ID per volume element of the geometry

                    **Extensions:** `['.txt']`






            ??? json-spec "`/geometry/*/surface_selection`"
                ```
                /geometry/*/surface_selection
                ```


                === "`/geometry/*/surface_selection` (`int`)"
                    <h2>Description</h2>
                    Assign specified ID to all surface elements of the geometry

                    **Default**: `0`



                === "`/geometry/*/surface_selection` (`object`)"
                    <h2>Description</h2>
                    Assigns ids to sides touching the bbox of the model using a threshold. Assigns 1+offset to left, 2+offset to bottom, 3+offset to right, 4+offset to top, 5+offset to front, 6+offset to back, 7+offset to everything else.
                    <h2>Optional</h2>





                    ??? json-spec "`/geometry/*/surface_selection/threshold` (`float`)"
                        ```
                        /geometry/*/surface_selection/threshold
                        ```
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.

                        **Default**: `-1`








                    ??? json-spec "`/geometry/*/surface_selection/offset` (`int`)"
                        ```
                        /geometry/*/surface_selection/offset
                        ```
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.

                        **Default**: `0`






                === "`/geometry/*/surface_selection` (`list`)"
                    <h2>Description</h2>
                    List of selection (ID assignment) operations to apply to the geometry; operations can be box, sphere, etc.



                    ??? json-spec "`/geometry/*/surface_selection/*`"
                        ```
                        /geometry/*/surface_selection/*
                        ```


                        === "`/geometry/*/surface_selection/*` (`object`)"
                            <h2>Description</h2>
                            Assign the ID to all surface elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.

                            **Default**: `None`
                            <h2>Required</h2>





                            ??? json-spec "`/geometry/*/surface_selection/*/id` (`int`)"
                                ```
                                /geometry/*/surface_selection/*/id
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/box` (`list`)"
                                ```
                                /geometry/*/surface_selection/*/box
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/surface_selection/*/box/*` (`list`)"
                                    ```
                                    /geometry/*/surface_selection/*/box/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/surface_selection/*/box/*/*` (`float`)"
                                        ```
                                        /geometry/*/surface_selection/*/box/*/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.

                                        **Default**: `0`









                            <h2>Optional</h2>





                            ??? json-spec "`/geometry/*/surface_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/surface_selection/*/relative
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.

                                **Default**: `False`






                        === "`/geometry/*/surface_selection/*` (`object`)"
                            <h2>Description</h2>
                            Assign the ID to all surface elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.

                            **Default**: `None`
                            <h2>Required</h2>





                            ??? json-spec "`/geometry/*/surface_selection/*/id` (`int`)"
                                ```
                                /geometry/*/surface_selection/*/id
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/radius` (`float`)"
                                ```
                                /geometry/*/surface_selection/*/radius
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/center` (`list`)"
                                ```
                                /geometry/*/surface_selection/*/center
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/surface_selection/*/center/*` (`float`)"
                                    ```
                                    /geometry/*/surface_selection/*/center/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.






                            <h2>Optional</h2>





                            ??? json-spec "`/geometry/*/surface_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/surface_selection/*/relative
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.

                                **Default**: `False`






                        === "`/geometry/*/surface_selection/*` (`object`)"
                            <h2>Description</h2>
                            Assign the ID to all surface elements with barycenters in a halfspace. The halfspace boundary plane is defined in one of two ways: (1) by a point in the plane and the normal, which points to the halfspace. (2) By a normal and the offset from the coordinate system origin along the line in the direction of the normal passing through the origin. In the former case, the option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.

                            **Default**: `None`
                            <h2>Required</h2>





                            ??? json-spec "`/geometry/*/surface_selection/*/id` (`int`)"
                                ```
                                /geometry/*/surface_selection/*/id
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/point` (`list`)"
                                ```
                                /geometry/*/surface_selection/*/point
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/surface_selection/*/point/*` (`float`)"
                                    ```
                                    /geometry/*/surface_selection/*/point/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/geometry/*/surface_selection/*/normal` (`list`)"
                                ```
                                /geometry/*/surface_selection/*/normal
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/geometry/*/surface_selection/*/normal/*` (`float`)"
                                    ```
                                    /geometry/*/surface_selection/*/normal/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.






                            <h2>Optional</h2>





                            ??? json-spec "`/geometry/*/surface_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/surface_selection/*/relative
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.

                                **Default**: `False`








                            ??? json-spec "`/geometry/*/surface_selection/*/offset` (`float`)"
                                ```
                                /geometry/*/surface_selection/*/offset
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.






                        === "`/geometry/*/surface_selection/*` (`object`)"
                            <h2>Description</h2>
                            Same as halfspace, but the boundary plane is axis-aligned. The choice of axis is specified either by a string matching the regexp r"[+-][xyzXYZ]" or an int matching the regular expression [+-]?[123] where the sign is the side of the plane to select and letter or number indicates the axis to which the plane is perpendicular. The offset is the plane offset from the origin. If the relative option is set to true, the offset is with respect to the center of the bounding box.

                            **Default**: `None`
                            <h2>Required</h2>





                            ??? json-spec "`/geometry/*/surface_selection/*/id` (`int`)"
                                ```
                                /geometry/*/surface_selection/*/id
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.






                            ??? json-spec "`/geometry/*/surface_selection/*/axis`"
                                ```
                                /geometry/*/surface_selection/*/axis
                                ```


                                === "`/geometry/*/surface_selection/*/axis` (`int`)"
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.



                                === "`/geometry/*/surface_selection/*/axis` (`string`)"
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                            ??? json-spec "`/geometry/*/surface_selection/*/position` (`float`)"
                                ```
                                /geometry/*/surface_selection/*/position
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.



                            <h2>Optional</h2>





                            ??? json-spec "`/geometry/*/surface_selection/*/relative` (`bool`)"
                                ```
                                /geometry/*/surface_selection/*/relative
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.

                                **Default**: `False`









                === "`/geometry/*/surface_selection` (`file`)"
                    <h2>Description</h2>
                    Load ids from a file; the file has a list of surface elements of the geometry specified as triples of vertex indices, with one ID for each; each triple must correspond to a surface element

                    **Extensions:** `['.txt']`








            ??? json-spec "`/geometry/*/curve_selection` (`object`)"
                ```
                /geometry/*/curve_selection
                ```
                <h2>Description</h2>
                Selection of curves

                **Default**: `None`








            ??? json-spec "`/geometry/*/point_selection` (`object`)"
                ```
                /geometry/*/point_selection
                ```
                <h2>Description</h2>
                Selection of points

                **Default**: `None`








            ??? json-spec "`/geometry/*/n_refs` (`int`)"
                ```
                /geometry/*/n_refs
                ```
                <h2>Description</h2>
                number of uniform refinements

                **Default**: `0`








            ??? json-spec "`/geometry/*/advanced` (`object`)"
                ```
                /geometry/*/advanced
                ```
                <h2>Description</h2>
                Advanced options for geometry

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/geometry/*/advanced/normalize_mesh` (`bool`)"
                    ```
                    /geometry/*/advanced/normalize_mesh
                    ```
                    <h2>Description</h2>
                    Rescale the mesh to it fits in the biunit cube

                    **Default**: `False`








                ??? json-spec "`/geometry/*/advanced/force_linear_geometry` (`bool`)"
                    ```
                    /geometry/*/advanced/force_linear_geometry
                    ```
                    <h2>Description</h2>
                    Discard high-order nodes for curved geometries

                    **Default**: `False`








                ??? json-spec "`/geometry/*/advanced/refinement_location` (`float`)"
                    ```
                    /geometry/*/advanced/refinement_location
                    ```
                    <h2>Description</h2>
                    parametric location of the refinement

                    **Default**: `0.5`








                ??? json-spec "`/geometry/*/advanced/min_component` (`int`)"
                    ```
                    /geometry/*/advanced/min_component
                    ```
                    <h2>Description</h2>
                    Size of the minumum component for collision

                    **Default**: `-1`











            ??? json-spec "`/geometry/*/enabled` (`bool`)"
                ```
                /geometry/*/enabled
                ```
                <h2>Description</h2>
                Skips the geometry if false

                **Default**: `True`








            ??? json-spec "`/geometry/*/is_obstacle` (`bool`)"
                ```
                /geometry/*/is_obstacle
                ```
                <h2>Description</h2>
                The geometry elements are not included in deforming geometry, only in collision computations

                **Default**: `False`














    ??? json-spec "`/materials` (`list`)"
        ```
        /materials
        ```
        <h2>Description</h2>
        Material Parameters lists including ID pointing to volume selection, Young's modulus ($E$), Poisson's ratio ($\nu$), Density ($\rho$), or Lamé constants ($\lambda$ and $\mu$).



        ??? json-spec "`/materials/*`"
            ```
            /materials/*
            ```


            === "NeoHookean"

                **Type**: NeoHookean
                <h2>Description</h2>
                Material Parameters including ID, Young's modulus ($E$), Poisson's ratio ($\nu$), density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    <h2>Description</h2>
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    <h2>Description</h2>
                    Poisson's ratio



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "NeoHookean"

                **Type**: NeoHookean
                <h2>Description</h2>
                Material Parameters including ID, Lamé first ($\lambda$), Lamé second ($\mu$), density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/lambda` (`float`)"
                    ```
                    /materials/*/lambda
                    ```
                    <h2>Description</h2>
                    Second Lamé parameter








                ??? json-spec "`/materials/*/mu` (`float`)"
                    ```
                    /materials/*/mu
                    ```
                    <h2>Description</h2>
                    First Lamé parameters



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "LinearElasticity"

                **Type**: LinearElasticity
                <h2>Description</h2>
                Material Parameters including ID, Young's modulus ($E$), Poisson's ratio ($\nu$), density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    <h2>Description</h2>
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    <h2>Description</h2>
                    Poisson's ratio



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "LinearElasticity"

                **Type**: LinearElasticity
                <h2>Description</h2>
                Material Parameters including ID, Lamé first ($\lambda$), Lamé second ($\mu$), density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/lambda` (`float`)"
                    ```
                    /materials/*/lambda
                    ```
                    <h2>Description</h2>
                    Second Lamé parameter








                ??? json-spec "`/materials/*/mu` (`float`)"
                    ```
                    /materials/*/mu
                    ```
                    <h2>Description</h2>
                    First Lamé parameters



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "HookeLinearElasticity"

                **Type**: HookeLinearElasticity
                <h2>Description</h2>
                Material Parameters including ID, E, nu, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    <h2>Description</h2>
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    <h2>Description</h2>
                    Poisson's ratio



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "HookeLinearElasticity"

                **Type**: HookeLinearElasticity
                <h2>Description</h2>
                Material Parameters including ID, E, nu, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/elasticity_tensor` (`list`)"
                    ```
                    /materials/*/elasticity_tensor
                    ```
                    <h2>Description</h2>
                    Symmetric elasticity tensor





                    ??? json-spec "`/materials/*/elasticity_tensor/*` (`float`)"
                        ```
                        /materials/*/elasticity_tensor/*
                        ```
                        <h2>Description</h2>
                        Entries of elasticity tensor

                        **Default**: `0`






                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "SaintVenant"

                **Type**: SaintVenant
                <h2>Description</h2>
                Material Parameters including ID, E, nu, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    <h2>Description</h2>
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    <h2>Description</h2>
                    Poisson's ratio



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "SaintVenant"

                **Type**: SaintVenant
                <h2>Description</h2>
                Material Parameters including ID, E, nu, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/elasticity_tensor` (`list`)"
                    ```
                    /materials/*/elasticity_tensor
                    ```
                    <h2>Description</h2>
                    Symmetric elasticity tensor





                    ??? json-spec "`/materials/*/elasticity_tensor/*` (`float`)"
                        ```
                        /materials/*/elasticity_tensor/*
                        ```
                        <h2>Description</h2>
                        Entries of elasticity tensor

                        **Default**: `0`






                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "Stokes"

                **Type**: Stokes
                <h2>Description</h2>
                Material Parameters including ID, viscosity, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/viscosity` (`float`)"
                    ```
                    /materials/*/viscosity
                    ```
                    <h2>Description</h2>
                    Fuild's viscosity



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "NavierStokes"

                **Type**: NavierStokes
                <h2>Description</h2>
                Material Parameters including ID, viscosity, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/viscosity` (`float`)"
                    ```
                    /materials/*/viscosity
                    ```
                    <h2>Description</h2>
                    Fuild's viscosity



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "IncompressibleLinearElasticity"

                **Type**: IncompressibleLinearElasticity
                <h2>Description</h2>
                Material Parameters including ID, Young's modulus ($E$), Poisson's ratio ($\nu$), density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/E` (`float`)"
                    ```
                    /materials/*/E
                    ```
                    <h2>Description</h2>
                    Young's modulus








                ??? json-spec "`/materials/*/nu` (`float`)"
                    ```
                    /materials/*/nu
                    ```
                    <h2>Description</h2>
                    Poisson's ratio



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "IncompressibleLinearElasticity"

                **Type**: IncompressibleLinearElasticity
                <h2>Description</h2>
                Material Parameters including ID, Lamé first ($\lambda$), Lamé second ($\mu$), density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`








                ??? json-spec "`/materials/*/lambda` (`float`)"
                    ```
                    /materials/*/lambda
                    ```
                    <h2>Description</h2>
                    Second Lamé parameter








                ??? json-spec "`/materials/*/mu` (`float`)"
                    ```
                    /materials/*/mu
                    ```
                    <h2>Description</h2>
                    First Lamé parameters



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "Laplacian"

                **Type**: Laplacian
                <h2>Description</h2>
                Material Parameters including ID, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`






            === "Helmholtz"

                **Type**: Helmholtz
                <h2>Description</h2>
                Material Parameters including ID, k, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`








                ??? json-spec "`/materials/*/k` (`float`)"
                    ```
                    /materials/*/k
                    ```
                    <h2>Description</h2>
                    Scaling for Helmholtz

                    **Default**: `1`






            === "Bilaplacian"

                **Type**: Bilaplacian
                <h2>Description</h2>
                Material Parameters including ID, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material

                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'Stokes', 'NavierStokes', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian']`



                <h2>Optional</h2>





                ??? json-spec "`/materials/*/id` (`int`)"
                    ```
                    /materials/*/id
                    ```
                    <h2>Description</h2>
                    Volume selection ID

                    **Default**: `0`








                ??? json-spec "`/materials/*/rho` (`float`)"
                    ```
                    /materials/*/rho
                    ```
                    <h2>Description</h2>
                    Density

                    **Default**: `1`









    <h2>Optional</h2>



    ??? json-spec "`/preset_problem`"
        ```
        /preset_problem
        ```


        === "Linear"

            **Type**: Linear
            <h2>Description</h2>
            TODO

            **Default**: `'skip'`
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Quadratic"

            **Type**: Quadratic
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Cubic"

            **Type**: Cubic
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Sine"

            **Type**: Sine
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Franke"

            **Type**: Franke
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "FrankeOld"

            **Type**: FrankeOld
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "GenericScalarExact"

            **Type**: GenericScalarExact
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>





            ??? json-spec "`/preset_problem/func` (`int`)"
                ```
                /preset_problem/func
                ```
                <h2>Description</h2>
                TODO

                **Default**: `0`






        === "Zero_BC"

            **Type**: Zero_BC
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Elastic"

            **Type**: Elastic
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Walk"

            **Type**: Walk
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "TorsionElastic"

            **Type**: TorsionElastic
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>





            ??? json-spec "`/preset_problem/axis_coordiante` (`int`)"
                ```
                /preset_problem/axis_coordiante
                ```
                <h2>Description</h2>
                TODO

                **Default**: `2`








            ??? json-spec "`/preset_problem/n_turns` (`float`)"
                ```
                /preset_problem/n_turns
                ```
                <h2>Description</h2>
                TODO

                **Default**: `0.5`








            ??? json-spec "`/preset_problem/fixed_boundary` (`int`)"
                ```
                /preset_problem/fixed_boundary
                ```
                <h2>Description</h2>
                TODO

                **Default**: `5`








            ??? json-spec "`/preset_problem/turning_boundary` (`int`)"
                ```
                /preset_problem/turning_boundary
                ```
                <h2>Description</h2>
                TODO

                **Default**: `6`








            ??? json-spec "`/preset_problem/bbox_center` (`list`)"
                ```
                /preset_problem/bbox_center
                ```
                <h2>Description</h2>
                TODO





                ??? json-spec "`/preset_problem/bbox_center/*` (`float`)"
                    ```
                    /preset_problem/bbox_center/*
                    ```
                    <h2>Description</h2>
                    TODO

                    **Default**: `0`









        === "DoubleTorsionElastic"

            **Type**: DoubleTorsionElastic
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>





            ??? json-spec "`/preset_problem/axis_coordiante0` (`int`)"
                ```
                /preset_problem/axis_coordiante0
                ```
                <h2>Description</h2>
                TODO

                **Default**: `2`








            ??? json-spec "`/preset_problem/axis_coordiante1` (`int`)"
                ```
                /preset_problem/axis_coordiante1
                ```
                <h2>Description</h2>
                TODO

                **Default**: `2`








            ??? json-spec "`/preset_problem/angular_v0` (`float`)"
                ```
                /preset_problem/angular_v0
                ```
                <h2>Description</h2>
                TODO

                **Default**: `0.5`








            ??? json-spec "`/preset_problem/angular_v1` (`float`)"
                ```
                /preset_problem/angular_v1
                ```
                <h2>Description</h2>
                TODO

                **Default**: `-0.5`








            ??? json-spec "`/preset_problem/turning_boundary0` (`int`)"
                ```
                /preset_problem/turning_boundary0
                ```
                <h2>Description</h2>
                TODO

                **Default**: `5`








            ??? json-spec "`/preset_problem/turning_boundary1` (`int`)"
                ```
                /preset_problem/turning_boundary1
                ```
                <h2>Description</h2>
                TODO

                **Default**: `6`








            ??? json-spec "`/preset_problem/bbox_center` (`list`)"
                ```
                /preset_problem/bbox_center
                ```
                <h2>Description</h2>
                TODO





                ??? json-spec "`/preset_problem/bbox_center/*` (`float`)"
                    ```
                    /preset_problem/bbox_center/*
                    ```
                    <h2>Description</h2>
                    TODO

                    **Default**: `0`









        === "ElasticZeroBC"

            **Type**: ElasticZeroBC
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "ElasticExact"

            **Type**: ElasticExact
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "ElasticCantileverExact"

            **Type**: ElasticCantileverExact
            <h2>Description</h2>
            TODO, add displacement, E, nu, formulation, mesh_size
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "CompressionElasticExact"

            **Type**: CompressionElasticExact
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "QuadraticElasticExact"

            **Type**: QuadraticElasticExact
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "LinearElasticExact"

            **Type**: LinearElasticExact
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "PointBasedTensor"

            **Type**: PointBasedTensor
            <h2>Description</h2>
            TODO, add optionals
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Kernel"

            **Type**: Kernel
            <h2>Description</h2>
            TODO, add optionals
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>





            ??? json-spec "`/preset_problem/formulation` (`string`)"
                ```
                /preset_problem/formulation
                ```
                <h2>Description</h2>
                TODO

                **Default**: `''`








            ??? json-spec "`/preset_problem/n_kernels` (`int`)"
                ```
                /preset_problem/n_kernels
                ```
                <h2>Description</h2>
                TODO

                **Default**: `0`








            ??? json-spec "`/preset_problem/kernel_distance` (`float`)"
                ```
                /preset_problem/kernel_distance
                ```
                <h2>Description</h2>
                TODO

                **Default**: `0`








            ??? json-spec "`/preset_problem/kernel_weights` (`string`)"
                ```
                /preset_problem/kernel_weights
                ```
                <h2>Description</h2>
                TODO

                **Default**: `''`






        === "Node"

            **Type**: Node
            <h2>Description</h2>
            TODO, add optionals
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "TimeDependentScalar"

            **Type**: TimeDependentScalar
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "MinSurf"

            **Type**: MinSurf
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Gravity"

            **Type**: Gravity
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>








        === "ConstantVelocity"

            **Type**: ConstantVelocity
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "TwoSpheres"

            **Type**: TwoSpheres
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "DrivenCavity"

            **Type**: DrivenCavity
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "DrivenCavityC0"

            **Type**: DrivenCavityC0
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "DrivenCavitySmooth"

            **Type**: DrivenCavitySmooth
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "Flow"

            **Type**: Flow
            <h2>Description</h2>
            TODO, add inflow, outflow, inflow_amout, outflow_amout, direction, obstacle
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "FlowWithObstacle"

            **Type**: FlowWithObstacle
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>








        === "CornerFlow"

            **Type**: CornerFlow
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>













        === "UnitFlowWithObstacle"

            **Type**: UnitFlowWithObstacle
            <h2>Description</h2>
            TODO, add inflow_id, direction, no_slip
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>








        === "StokesLaw"

            **Type**: StokesLaw
            <h2>Description</h2>
            TODO, add radius
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>













        === "TaylorGreenVortex"

            **Type**: TaylorGreenVortex
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>








        === "SimpleStokeProblemExact"

            **Type**: SimpleStokeProblemExact
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>





            ??? json-spec "`/preset_problem/func` (`int`)"
                ```
                /preset_problem/func
                ```
                <h2>Description</h2>
                TODO

                **Default**: `0`






        === "SineStokeProblemExact"

            **Type**: SineStokeProblemExact
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "TransientStokeProblemExact"

            **Type**: TransientStokeProblemExact
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>





            ??? json-spec "`/preset_problem/func` (`int`)"
                ```
                /preset_problem/func
                ```
                <h2>Description</h2>
                TODO

                **Default**: `0`











        === "Kovnaszy"

            **Type**: Kovnaszy
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>













        === "Airfoil"

            **Type**: Airfoil
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>








        === "Lshape"

            **Type**: Lshape
            <h2>Description</h2>
            TODO
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`



            <h2>Optional</h2>













        === "TestProblem"

            **Type**: TestProblem
            <h2>Description</h2>
            TODO, type, omega, is_scalar
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`






        === "BilaplacianProblemWithSolution"

            **Type**: BilaplacianProblemWithSolution
            <h2>Description</h2>
            TODO, type, omega, is_scalar
            <h2>Required</h2>





            ??? json-spec "`/preset_problem/type` (`string`)"
                ```
                /preset_problem/type
                ```
                <h2>Description</h2>
                Type of preset problem to use.

                **Options:** `['Linear', 'Quadratic', 'Cubic', 'Sine', 'Franke', 'FrankeOld', 'GenericScalarExact', 'Zero_BC', 'Elastic', 'Walk', 'TorsionElastic', 'DoubleTorsionElastic', 'ElasticZeroBC', 'ElasticExact', 'ElasticCantileverExact', 'CompressionElasticExact', 'QuadraticElasticExact', 'LinearElasticExact', 'PointBasedTensor', 'Kernel', 'Node', 'TimeDependentScalar', 'MinSurf', 'Gravity', 'ConstantVelocity', 'TwoSpheres', 'DrivenCavity', 'DrivenCavityC0', 'DrivenCavitySmooth', 'Flow', 'FlowWithObstacle', 'CornerFlow', 'UnitFlowWithObstacle', 'StokesLaw', 'TaylorGreenVortex', 'SimpleStokeProblemExact', 'SineStokeProblemExact', 'TransientStokeProblemExact', 'Kovnaszy', 'Airfoil', 'Lshape', 'TestProblem', 'BilaplacianProblemWithSolution']`











    ??? json-spec "`/common` (`file`)"
        ```
        /common
        ```
        <h2>Description</h2>
        Path to common settings will patch the current file.

        **Default**: `''`

        **Extensions:** `['.json']`








    ??? json-spec "`/root_path` (`string`)"
        ```
        /root_path
        ```
        <h2>Description</h2>
        Path for all relative paths, set automatically to the folder containing this json.

        **Default**: `''`








    ??? json-spec "`/space` (`object`)"
        ```
        /space
        ```
        <h2>Description</h2>
        Options related to the FE space.

        **Default**: `None`
        <h2>Optional</h2>



        ??? json-spec "`/space/discr_order`"
            ```
            /space/discr_order
            ```


            === "`/space/discr_order` (`int`)"
                <h2>Description</h2>
                Lagrange element order for the space for the main unknown, for all elements.

                **Default**: `1`



            === "`/space/discr_order` (`file`)"
                <h2>Description</h2>
                Path to file containing Lagrange element order for the space for the main unknown per element.

                **Extensions:** `['.txt', '.bin']`



            === "`/space/discr_order` (`list`)"
                <h2>Description</h2>
                List of Lagrange element order for the space for the main unknown with volume IDs.





                ??? json-spec "`/space/discr_order/*` (`object`)"
                    ```
                    /space/discr_order/*
                    ```
                    <h2>Description</h2>
                    Lagrange element order for the a space tagged with volume ID for the main unknown.
                    <h2>Required</h2>



                    ??? json-spec "`/space/discr_order/*/id`"
                        ```
                        /space/discr_order/*/id
                        ```


                        === "`/space/discr_order/*/id` (`int`)"
                            <h2>Description</h2>
                            Volume selection ID to apply the discr_order to.



                        === "`/space/discr_order/*/id` (`list`)"
                            <h2>Description</h2>
                            List of volume selection IDs to apply the discr_order to.





                            ??? json-spec "`/space/discr_order/*/id/*` (`int`)"
                                ```
                                /space/discr_order/*/id/*
                                ```
                                <h2>Description</h2>
                                Volume selection ID to apply the discr_order to.











                    ??? json-spec "`/space/discr_order/*/order` (`int`)"
                        ```
                        /space/discr_order/*/order
                        ```
                        <h2>Description</h2>
                        Lagrange element order for the space for the main unknown, for all elements.














        ??? json-spec "`/space/pressure_discr_order` (`int`)"
            ```
            /space/pressure_discr_order
            ```
            <h2>Description</h2>
             Lagrange element order for the space for the pressure unknown, for all elements.

            **Default**: `1`








        ??? json-spec "`/space/use_p_ref` (`bool`)"
            ```
            /space/use_p_ref
            ```
            <h2>Description</h2>
            Perform a priori p-refinement based on element shape, as described in 'Decoupling..' paper.

            **Default**: `False`








        ??? json-spec "`/space/advanced` (`object`)"
            ```
            /space/advanced
            ```
            <h2>Description</h2>
            Advanced settings for the FE space.

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/space/advanced/discr_order_max` (`int`)"
                ```
                /space/advanced/discr_order_max
                ```
                <h2>Description</h2>
                Maximal discretization order in adaptive p-refinement and hp-refinement

                **Default**: `4`








            ??? json-spec "`/space/advanced/serendipity` (`bool`)"
                ```
                /space/advanced/serendipity
                ```
                <h2>Description</h2>
                Use serendipity elements for quad/hex elements of degree 2.

                **Default**: `False`








            ??? json-spec "`/space/advanced/isoparametric` (`bool`)"
                ```
                /space/advanced/isoparametric
                ```
                <h2>Description</h2>
                Forces geometric map basis to be the same degree as the main variable basis, irrespective of the degree associated with the geom. map degrees associated with the elements of the geometry.

                **Default**: `False`








            ??? json-spec "`/space/advanced/use_spline` (`bool`)"
                ```
                /space/advanced/use_spline
                ```
                <h2>Description</h2>
                Use bi/triquadratic spline basis for quad/hex elements not adjacent to polyhedral elements, see 'PolySpline..' paper for details.

                **Default**: `False`








            ??? json-spec "`/space/advanced/bc_method` (`string`)"
                ```
                /space/advanced/bc_method
                ```
                <h2>Description</h2>
                Method for imposing analytic Dirichet boundary conditions. If 'lsq' (least-squares fit), then the bc function is sampled at quadrature points, and the FEspace nodal values on the boundary are determined by minimizing L2 norm of the difference. If 'sample', then the analytic bc function is sampled at the boundary nodes.

                **Default**: `'lsq'`

                **Options:** `['lsq', 'sample']`








            ??? json-spec "`/space/advanced/n_boundary_samples` (`int`)"
                ```
                /space/advanced/n_boundary_samples
                ```
                <h2>Description</h2>
                Per-element number of boundary samples for analytic Dirichlet and Neumann boundary conditions.

                **Default**: `-1`








            ??? json-spec "`/space/advanced/quadrature_order` (`int`)"
                ```
                /space/advanced/quadrature_order
                ```
                <h2>Description</h2>
                Minimal quadrature order to use in matrix and rhs assembly; the actual order is determined as min(2*(p-1)+1,quadrature_order).

                **Default**: `-1`








            ??? json-spec "`/space/advanced/mass_quadrature_order` (`int`)"
                ```
                /space/advanced/mass_quadrature_order
                ```
                <h2>Description</h2>
                Minimal quadrature order to use in mass matrix assembler; the actual order is determined as min(2*p+1,quadrature_order)

                **Default**: `-1`








            ??? json-spec "`/space/advanced/poly_bases` (`string`)"
                ```
                /space/advanced/poly_bases
                ```
                <h2>Description</h2>
                Type of basis to use for a polygonal element, one of MFSHarmonic, MeanValue, see 'PolySpline..' paper for details.

                **Default**: `'MFSHarmonic'`

                **Options:** `['MFSHarmonic', 'MeanValue']`








            ??? json-spec "`/space/advanced/integral_constraints` (`int`)"
                ```
                /space/advanced/integral_constraints
                ```
                <h2>Description</h2>
                Number of constraints for non-conforming polygonal basis;  0, 1, or 2; see 'PolySpline..' paper for details.

                **Default**: `2`








            ??? json-spec "`/space/advanced/n_harmonic_samples` (`int`)"
                ```
                /space/advanced/n_harmonic_samples
                ```
                <h2>Description</h2>
                If MFSHarmonics is used for a polygonal element, number of collocation samples used in the basis construction;see 'PolySpline..' paper for details.

                **Default**: `10`








            ??? json-spec "`/space/advanced/force_no_ref_for_harmonic` (`bool`)"
                ```
                /space/advanced/force_no_ref_for_harmonic
                ```
                <h2>Description</h2>
                If true, do not do uniform global refinement if the mesh contains polygonal elements.

                **Default**: `False`








            ??? json-spec "`/space/advanced/B` (`int`)"
                ```
                /space/advanced/B
                ```
                <h2>Description</h2>
                The target deviation of the error on elements from perfect element error, for a priori geometry-dependent p-refinement, see 'Decoupling .. ' paper.

                **Default**: `3`








            ??? json-spec "`/space/advanced/h1_formula` (`bool`)"
                ```
                /space/advanced/h1_formula
                ```
                <h2>Description</h2>


                **Default**: `False`








            ??? json-spec "`/space/advanced/count_flipped_els` (`bool`)"
                ```
                /space/advanced/count_flipped_els
                ```
                <h2>Description</h2>
                Count the number of elements with Jacobian of the geometric map not positive at quadrature points.

                **Default**: `True`












    ??? json-spec "`/time`"
        ```
        /time
        ```


        === "`/time` (`object`)"
            <h2>Description</h2>
            The time parameters: start time `t0`, end time `tend`, time step `dt`.

            **Default**: `'skip'`
            <h2>Required</h2>





            ??? json-spec "`/time/tend` (`float`)"
                ```
                /time/tend
                ```
                <h2>Description</h2>
                Ending time

                **Range:** `[0, inf]`








            ??? json-spec "`/time/dt` (`float`)"
                ```
                /time/dt
                ```
                <h2>Description</h2>
                Time step size $\Delta t$

                **Range:** `[0, inf]`



            <h2>Optional</h2>





            ??? json-spec "`/time/t0` (`float`)"
                ```
                /time/t0
                ```
                <h2>Description</h2>
                Startning time

                **Default**: `0`

                **Range:** `[0, inf]`








            ??? json-spec "`/time/integrator` (`string`)"
                ```
                /time/integrator
                ```
                <h2>Description</h2>
                Time integrator

                **Default**: `'ImplicitEuler'`

                **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`








            ??? json-spec "`/time/newmark` (`object`)"
                ```
                /time/newmark
                ```
                <h2>Description</h2>
                Options for Newmark

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/time/newmark/gamma` (`float`)"
                    ```
                    /time/newmark/gamma
                    ```
                    <h2>Description</h2>
                    Newmark gamma

                    **Default**: `0.5`








                ??? json-spec "`/time/newmark/beta` (`float`)"
                    ```
                    /time/newmark/beta
                    ```
                    <h2>Description</h2>
                    Newmark beta

                    **Default**: `0.25`











            ??? json-spec "`/time/BDF` (`object`)"
                ```
                /time/BDF
                ```
                <h2>Description</h2>
                Options for BDF

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/time/BDF/steps` (`int`)"
                    ```
                    /time/BDF/steps
                    ```
                    <h2>Description</h2>
                    BDF order

                    **Default**: `1`









        === "`/time` (`object`)"
            <h2>Description</h2>
            The time parameters: start time `t0`, time step `dt`, number of time steps.
            <h2>Required</h2>





            ??? json-spec "`/time/time_steps` (`int`)"
                ```
                /time/time_steps
                ```
                <h2>Description</h2>
                Number of time steps

                **Range:** `[0, inf]`








            ??? json-spec "`/time/dt` (`float`)"
                ```
                /time/dt
                ```
                <h2>Description</h2>
                Time step size $\Delta t$

                **Range:** `[0, inf]`



            <h2>Optional</h2>





            ??? json-spec "`/time/t0` (`float`)"
                ```
                /time/t0
                ```
                <h2>Description</h2>
                Startning time

                **Default**: `0`

                **Range:** `[0, inf]`








            ??? json-spec "`/time/integrator` (`string`)"
                ```
                /time/integrator
                ```
                <h2>Description</h2>
                Time integrator

                **Default**: `'ImplicitEuler'`

                **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`








            ??? json-spec "`/time/newmark` (`object`)"
                ```
                /time/newmark
                ```
                <h2>Description</h2>
                Options for Newmark

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/time/newmark/gamma` (`float`)"
                    ```
                    /time/newmark/gamma
                    ```
                    <h2>Description</h2>
                    Newmark gamma

                    **Default**: `0.5`








                ??? json-spec "`/time/newmark/beta` (`float`)"
                    ```
                    /time/newmark/beta
                    ```
                    <h2>Description</h2>
                    Newmark beta

                    **Default**: `0.25`











            ??? json-spec "`/time/BDF` (`object`)"
                ```
                /time/BDF
                ```
                <h2>Description</h2>
                Options for BDF

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/time/BDF/steps` (`int`)"
                    ```
                    /time/BDF/steps
                    ```
                    <h2>Description</h2>
                    BDF order

                    **Default**: `1`









        === "`/time` (`object`)"
            <h2>Description</h2>
            The time parameters: start time `t0`, end time `tend`, number of time steps.
            <h2>Required</h2>





            ??? json-spec "`/time/time_steps` (`int`)"
                ```
                /time/time_steps
                ```
                <h2>Description</h2>
                Number of time steps

                **Range:** `[0, inf]`








            ??? json-spec "`/time/tend` (`float`)"
                ```
                /time/tend
                ```
                <h2>Description</h2>
                Ending time

                **Range:** `[0, inf]`



            <h2>Optional</h2>





            ??? json-spec "`/time/t0` (`float`)"
                ```
                /time/t0
                ```
                <h2>Description</h2>
                Startning time

                **Default**: `0`

                **Range:** `[0, inf]`








            ??? json-spec "`/time/integrator` (`string`)"
                ```
                /time/integrator
                ```
                <h2>Description</h2>
                Time integrator

                **Default**: `'ImplicitEuler'`

                **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`








            ??? json-spec "`/time/newmark` (`object`)"
                ```
                /time/newmark
                ```
                <h2>Description</h2>
                Options for Newmark

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/time/newmark/gamma` (`float`)"
                    ```
                    /time/newmark/gamma
                    ```
                    <h2>Description</h2>
                    Newmark gamma

                    **Default**: `0.5`








                ??? json-spec "`/time/newmark/beta` (`float`)"
                    ```
                    /time/newmark/beta
                    ```
                    <h2>Description</h2>
                    Newmark beta

                    **Default**: `0.25`











            ??? json-spec "`/time/BDF` (`object`)"
                ```
                /time/BDF
                ```
                <h2>Description</h2>
                Options for BDF

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/time/BDF/steps` (`int`)"
                    ```
                    /time/BDF/steps
                    ```
                    <h2>Description</h2>
                    BDF order

                    **Default**: `1`














    ??? json-spec "`/contact` (`object`)"
        ```
        /contact
        ```
        <h2>Description</h2>
        Contact handling parameters.

        **Default**: `None`
        <h2>Optional</h2>





        ??? json-spec "`/contact/enabled` (`bool`)"
            ```
            /contact/enabled
            ```
            <h2>Description</h2>
            True if contact handling is enabled.

            **Default**: `False`








        ??? json-spec "`/contact/dhat` (`float`)"
            ```
            /contact/dhat
            ```
            <h2>Description</h2>
            Contact barrier activation distance.

            **Default**: `0.001`

            **Range:** `[0, inf]`








        ??? json-spec "`/contact/dhat_percentage` (`float`)"
            ```
            /contact/dhat_percentage
            ```
            <h2>Description</h2>
            $\hat{d}$ as percentage of the diagonal of the bounding box

            **Default**: `0.8`








        ??? json-spec "`/contact/epsv` (`float`)"
            ```
            /contact/epsv
            ```
            <h2>Description</h2>
            Friction smoothing parameter.

            **Default**: `0.001`

            **Range:** `[0, inf]`








        ??? json-spec "`/contact/friction_coefficient` (`float`)"
            ```
            /contact/friction_coefficient
            ```
            <h2>Description</h2>
            Coefficient of friction (global)

            **Default**: `0`











    ??? json-spec "`/solver` (`object`)"
        ```
        /solver
        ```
        <h2>Description</h2>
        The settings for the solver including linear solver, nonlinear solver, and some advanced options.

        **Default**: `None`
        <h2>Optional</h2>





        ??? json-spec "`/solver/linear` (`object`)"
            ```
            /solver/linear
            ```
            <h2>Description</h2>
            Settings for the linear solver.

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/solver/linear/solver` (`string`)"
                ```
                /solver/linear/solver
                ```
                <h2>Description</h2>
                Linear solver type.

                **Default**: `''`

                **Options:** `['Eigen::SimplicialLDLT', 'Eigen::SparseLU', 'Eigen::CholmodSupernodalLLT', 'Eigen::UmfPackLU', 'Eigen::SuperLU', 'Eigen::PardisoLDLT', 'Eigen::PardisoLU', 'Pardiso', 'Hypre', 'AMGCL', 'Eigen::LeastSquaresConjugateGradient', 'Eigen::DGMRES', 'Eigen::ConjugateGradient', 'Eigen::BiCGSTAB', 'Eigen::GMRES', 'Eigen::MINRES']`








            ??? json-spec "`/solver/linear/precond` (`string`)"
                ```
                /solver/linear/precond
                ```
                <h2>Description</h2>
                Preconditioner used if using an iterative linear solver.

                **Default**: `''`

                **Options:** `['Eigen::IdentityPreconditioner', 'Eigen::DiagonalPreconditioner', 'Eigen::IncompleteCholesky', 'Eigen::LeastSquareDiagonalPreconditioner', 'Eigen::IncompleteLUT']`








            ??? json-spec "`/solver/linear/Eigen::LeastSquaresConjugateGradient` (`object`)"
                ```
                /solver/linear/Eigen::LeastSquaresConjugateGradient
                ```
                <h2>Description</h2>
                Settings for the Eigen's Least Squares Conjugate Gradient solver.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/linear/Eigen::LeastSquaresConjugateGradient/max_iter` (`int`)"
                    ```
                    /solver/linear/Eigen::LeastSquaresConjugateGradient/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.

                    **Default**: `1000`








                ??? json-spec "`/solver/linear/Eigen::LeastSquaresConjugateGradient/tolerance` (`float`)"
                    ```
                    /solver/linear/Eigen::LeastSquaresConjugateGradient/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.

                    **Default**: `1e-12`











            ??? json-spec "`/solver/linear/Eigen::DGMRES` (`object`)"
                ```
                /solver/linear/Eigen::DGMRES
                ```
                <h2>Description</h2>
                Settings for the Eigen's DGMRES solver.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/linear/Eigen::DGMRES/max_iter` (`int`)"
                    ```
                    /solver/linear/Eigen::DGMRES/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.

                    **Default**: `1000`








                ??? json-spec "`/solver/linear/Eigen::DGMRES/tolerance` (`float`)"
                    ```
                    /solver/linear/Eigen::DGMRES/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.

                    **Default**: `1e-12`











            ??? json-spec "`/solver/linear/Eigen::ConjugateGradient` (`object`)"
                ```
                /solver/linear/Eigen::ConjugateGradient
                ```
                <h2>Description</h2>
                Settings for the Eigen's Conjugate Gradient solver.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/linear/Eigen::ConjugateGradient/max_iter` (`int`)"
                    ```
                    /solver/linear/Eigen::ConjugateGradient/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.

                    **Default**: `1000`








                ??? json-spec "`/solver/linear/Eigen::ConjugateGradient/tolerance` (`float`)"
                    ```
                    /solver/linear/Eigen::ConjugateGradient/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.

                    **Default**: `1e-12`











            ??? json-spec "`/solver/linear/Eigen::BiCGSTAB` (`object`)"
                ```
                /solver/linear/Eigen::BiCGSTAB
                ```
                <h2>Description</h2>
                Settings for the Eigen's BiCGSTAB solver.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/linear/Eigen::BiCGSTAB/max_iter` (`int`)"
                    ```
                    /solver/linear/Eigen::BiCGSTAB/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.

                    **Default**: `1000`








                ??? json-spec "`/solver/linear/Eigen::BiCGSTAB/tolerance` (`float`)"
                    ```
                    /solver/linear/Eigen::BiCGSTAB/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.

                    **Default**: `1e-12`











            ??? json-spec "`/solver/linear/Eigen::GMRES` (`object`)"
                ```
                /solver/linear/Eigen::GMRES
                ```
                <h2>Description</h2>
                Settings for the Eigen's GMRES solver.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/linear/Eigen::GMRES/max_iter` (`int`)"
                    ```
                    /solver/linear/Eigen::GMRES/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.

                    **Default**: `1000`








                ??? json-spec "`/solver/linear/Eigen::GMRES/tolerance` (`float`)"
                    ```
                    /solver/linear/Eigen::GMRES/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.

                    **Default**: `1e-12`











            ??? json-spec "`/solver/linear/Eigen::MINRES` (`object`)"
                ```
                /solver/linear/Eigen::MINRES
                ```
                <h2>Description</h2>
                Settings for the Eigen's MINRES solver.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/linear/Eigen::MINRES/max_iter` (`int`)"
                    ```
                    /solver/linear/Eigen::MINRES/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.

                    **Default**: `1000`








                ??? json-spec "`/solver/linear/Eigen::MINRES/tolerance` (`float`)"
                    ```
                    /solver/linear/Eigen::MINRES/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.

                    **Default**: `1e-12`











            ??? json-spec "`/solver/linear/Pardiso` (`object`)"
                ```
                /solver/linear/Pardiso
                ```
                <h2>Description</h2>
                Settings for the Pardiso solver.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/linear/Pardiso/mtype` (`int`)"
                    ```
                    /solver/linear/Pardiso/mtype
                    ```
                    <h2>Description</h2>
                    Matrix type.

                    **Default**: `11`

                    **Options:** `[1, 2, -2, 3, 4, -4, 6, 11, 13]`











            ??? json-spec "`/solver/linear/Hypre` (`object`)"
                ```
                /solver/linear/Hypre
                ```
                <h2>Description</h2>
                Settings for the Hypre solver.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/linear/Hypre/max_iter` (`int`)"
                    ```
                    /solver/linear/Hypre/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.

                    **Default**: `1000`








                ??? json-spec "`/solver/linear/Hypre/pre_max_iter` (`int`)"
                    ```
                    /solver/linear/Hypre/pre_max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of pre iterations.

                    **Default**: `1`








                ??? json-spec "`/solver/linear/Hypre/tolerance` (`float`)"
                    ```
                    /solver/linear/Hypre/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.

                    **Default**: `1e-10`











            ??? json-spec "`/solver/linear/AMGCL` (`object`)"
                ```
                /solver/linear/AMGCL
                ```
                <h2>Description</h2>
                Settings for the AMGCL solver.

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/linear/AMGCL/solver` (`object`)"
                    ```
                    /solver/linear/AMGCL/solver
                    ```
                    <h2>Description</h2>
                    Solver settings for the AMGCL.

                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/linear/AMGCL/solver/tol` (`float`)"
                        ```
                        /solver/linear/AMGCL/solver/tol
                        ```
                        <h2>Description</h2>
                        Convergence tolerance.

                        **Default**: `1e-10`








                    ??? json-spec "`/solver/linear/AMGCL/solver/maxiter` (`int`)"
                        ```
                        /solver/linear/AMGCL/solver/maxiter
                        ```
                        <h2>Description</h2>
                        Maximum number of iterations.

                        **Default**: `1000`








                    ??? json-spec "`/solver/linear/AMGCL/solver/type` (`string`)"
                        ```
                        /solver/linear/AMGCL/solver/type
                        ```
                        <h2>Description</h2>
                        Type of solver to use.

                        **Default**: `'cg'`











                ??? json-spec "`/solver/linear/AMGCL/precond` (`object`)"
                    ```
                    /solver/linear/AMGCL/precond
                    ```
                    <h2>Description</h2>
                    Preconditioner settings for the AMGCL.

                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/linear/AMGCL/precond/relax` (`object`)"
                        ```
                        /solver/linear/AMGCL/precond/relax
                        ```
                        <h2>Description</h2>
                        Preconditioner settings for the AMGCL.

                        **Default**: `None`
                        <h2>Optional</h2>





                        ??? json-spec "`/solver/linear/AMGCL/precond/relax/degree` (`int`)"
                            ```
                            /solver/linear/AMGCL/precond/relax/degree
                            ```
                            <h2>Description</h2>
                            Degree of the polynomial.

                            **Default**: `16`








                        ??? json-spec "`/solver/linear/AMGCL/precond/relax/type` (`string`)"
                            ```
                            /solver/linear/AMGCL/precond/relax/type
                            ```
                            <h2>Description</h2>
                            Type of relaxation to use.

                            **Default**: `'chebyshev'`








                        ??? json-spec "`/solver/linear/AMGCL/precond/relax/power_iters` (`int`)"
                            ```
                            /solver/linear/AMGCL/precond/relax/power_iters
                            ```
                            <h2>Description</h2>
                            Number of power iterations.

                            **Default**: `100`








                        ??? json-spec "`/solver/linear/AMGCL/precond/relax/higher` (`float`)"
                            ```
                            /solver/linear/AMGCL/precond/relax/higher
                            ```
                            <h2>Description</h2>
                            Higher level relaxation.

                            **Default**: `2`








                        ??? json-spec "`/solver/linear/AMGCL/precond/relax/lower` (`float`)"
                            ```
                            /solver/linear/AMGCL/precond/relax/lower
                            ```
                            <h2>Description</h2>
                            Lower level relaxation.

                            **Default**: `0.008333333333`








                        ??? json-spec "`/solver/linear/AMGCL/precond/relax/scale` (`bool`)"
                            ```
                            /solver/linear/AMGCL/precond/relax/scale
                            ```
                            <h2>Description</h2>
                            Scale.

                            **Default**: `True`











                    ??? json-spec "`/solver/linear/AMGCL/precond/class` (`string`)"
                        ```
                        /solver/linear/AMGCL/precond/class
                        ```
                        <h2>Description</h2>
                        Type of preconditioner to use.

                        **Default**: `'amg'`








                    ??? json-spec "`/solver/linear/AMGCL/precond/max_levels` (`int`)"
                        ```
                        /solver/linear/AMGCL/precond/max_levels
                        ```
                        <h2>Description</h2>
                        Maximum number of levels.

                        **Default**: `6`








                    ??? json-spec "`/solver/linear/AMGCL/precond/direct_coarse` (`bool`)"
                        ```
                        /solver/linear/AMGCL/precond/direct_coarse
                        ```
                        <h2>Description</h2>
                        Use direct solver for the coarsest level.

                        **Default**: `False`








                    ??? json-spec "`/solver/linear/AMGCL/precond/ncycle` (`int`)"
                        ```
                        /solver/linear/AMGCL/precond/ncycle
                        ```
                        <h2>Description</h2>
                        Number of cycles.

                        **Default**: `2`








                    ??? json-spec "`/solver/linear/AMGCL/precond/coarsening` (`object`)"
                        ```
                        /solver/linear/AMGCL/precond/coarsening
                        ```
                        <h2>Description</h2>
                        Coarsening parameters.

                        **Default**: `None`
                        <h2>Optional</h2>





                        ??? json-spec "`/solver/linear/AMGCL/precond/coarsening/type` (`string`)"
                            ```
                            /solver/linear/AMGCL/precond/coarsening/type
                            ```
                            <h2>Description</h2>
                            Coarsening type.

                            **Default**: `'smoothed_aggregation'`








                        ??? json-spec "`/solver/linear/AMGCL/precond/coarsening/estimate_spectral_radius` (`bool`)"
                            ```
                            /solver/linear/AMGCL/precond/coarsening/estimate_spectral_radius
                            ```
                            <h2>Description</h2>
                            Should the spectral radius be estimated.

                            **Default**: `True`








                        ??? json-spec "`/solver/linear/AMGCL/precond/coarsening/relax` (`float`)"
                            ```
                            /solver/linear/AMGCL/precond/coarsening/relax
                            ```
                            <h2>Description</h2>
                            Coarsening relaxation.

                            **Default**: `1`








                        ??? json-spec "`/solver/linear/AMGCL/precond/coarsening/aggr` (`object`)"
                            ```
                            /solver/linear/AMGCL/precond/coarsening/aggr
                            ```
                            <h2>Description</h2>
                            Aggregation settings.

                            **Default**: `None`
                            <h2>Optional</h2>





                            ??? json-spec "`/solver/linear/AMGCL/precond/coarsening/aggr/eps_strong` (`float`)"
                                ```
                                /solver/linear/AMGCL/precond/coarsening/aggr/eps_strong
                                ```
                                <h2>Description</h2>
                                Aggregation epsilon strong.

                                **Default**: `0`























        ??? json-spec "`/solver/nonlinear` (`object`)"
            ```
            /solver/nonlinear
            ```
            <h2>Description</h2>
            Settings for nonlinear solver. Interior-loop linear solver settings are defined in the solver/linear section.

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/solver/nonlinear/solver` (`string`)"
                ```
                /solver/nonlinear/solver
                ```
                <h2>Description</h2>
                Nonlinear solver type

                **Default**: `'newton'`

                **Options:** `['newton', 'lbfgs']`








            ??? json-spec "`/solver/nonlinear/f_delta` (`float`)"
                ```
                /solver/nonlinear/f_delta
                ```
                <h2>Description</h2>
                Stopping criterion: minimal change of the energy f for the iterations to continue.

                **Default**: `1e-10`








            ??? json-spec "`/solver/nonlinear/grad_norm` (`float`)"
                ```
                /solver/nonlinear/grad_norm
                ```
                <h2>Description</h2>
                Stopping criterion: Minimal gradient norm for the iterations to continue.

                **Default**: `1e-08`








            ??? json-spec "`/solver/nonlinear/first_grad_norm_tol` (`float`)"
                ```
                /solver/nonlinear/first_grad_norm_tol
                ```
                <h2>Description</h2>
                Minimal gradient norm for the iterations to not start, assume we already are at a minimum.

                **Default**: `1e-10`








            ??? json-spec "`/solver/nonlinear/max_iterations` (`int`)"
                ```
                /solver/nonlinear/max_iterations
                ```
                <h2>Description</h2>
                Maximum number of iterations for a nonlinear solve.

                **Default**: `1000`








            ??? json-spec "`/solver/nonlinear/use_grad_norm` (`bool`)"
                ```
                /solver/nonlinear/use_grad_norm
                ```
                <h2>Description</h2>
                If true, enable gradient-norm stopping criterion, absolute (if relative_gradient is false), or relative to the initial gradient magnitude before the first iteration, otherwise.

                **Default**: `True`








            ??? json-spec "`/solver/nonlinear/relative_gradient` (`bool`)"
                ```
                /solver/nonlinear/relative_gradient
                ```
                <h2>Description</h2>
                If true, use relative gradient norm threshold, use absolute otherwise

                **Default**: `False`








            ??? json-spec "`/solver/nonlinear/line_search` (`object`)"
                ```
                /solver/nonlinear/line_search
                ```
                <h2>Description</h2>
                Settings for line-search in the nonlinear solver

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/nonlinear/line_search/method` (`string`)"
                    ```
                    /solver/nonlinear/line_search/method
                    ```
                    <h2>Description</h2>
                    Line-search type

                    **Default**: `'backtracking'`

                    **Options:** `['armijo', 'armijo_alt', 'backtracking', 'more_thuente', 'none']`








                ??? json-spec "`/solver/nonlinear/line_search/use_grad_norm_tol` (`float`)"
                    ```
                    /solver/nonlinear/line_search/use_grad_norm_tol
                    ```
                    <h2>Description</h2>
                    When the energy is smaller than use_grad_norm_tol, line-search uses norm of gradient instead of energy

                    **Default**: `0.0001`














        ??? json-spec "`/solver/augmented_lagrangian` (`object`)"
            ```
            /solver/augmented_lagrangian
            ```
            <h2>Description</h2>
            Parameters for the AL for imposing Dirichlet BCs. If the bc are not imposable, we add $w\|u - bc\|^2$ to the energy ($u$ is the solution at the Dirichlet nodes and $bc$ are the Dirichlet values). After convergence, we try to impose bc again, in case of failure we double $w$ until `max_weight`.

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/solver/augmented_lagrangian/initial_weight` (`float`)"
                ```
                /solver/augmented_lagrangian/initial_weight
                ```
                <h2>Description</h2>
                Initial weight for AL

                **Default**: `1000000.0`








            ??? json-spec "`/solver/augmented_lagrangian/max_weight` (`float`)"
                ```
                /solver/augmented_lagrangian/max_weight
                ```
                <h2>Description</h2>
                Maximum AL weight

                **Default**: `100000000000.0`








            ??? json-spec "`/solver/augmented_lagrangian/force` (`bool`)"
                ```
                /solver/augmented_lagrangian/force
                ```
                <h2>Description</h2>
                Always enable AL, even when BC can be imposed

                **Default**: `False`











        ??? json-spec "`/solver/contact` (`object`)"
            ```
            /solver/contact
            ```
            <h2>Description</h2>
            Settings for contact handling in the solver.

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/solver/contact/CCD` (`object`)"
                ```
                /solver/contact/CCD
                ```
                <h2>Description</h2>
                CCD options

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/contact/CCD/broad_phase` (`string`)"
                    ```
                    /solver/contact/CCD/broad_phase
                    ```
                    <h2>Description</h2>
                    Broad phase collision-detection algorithm to use

                    **Default**: `'hash_grid'`

                    **Options:** `['hash_grid', 'HG', 'brute_force', 'BF', 'spatial_hash', 'SH', 'sweep_and_tiniest_queue', 'STQ', 'sweep_and_tiniest_queue_gpu', 'STQ_GPU']`








                ??? json-spec "`/solver/contact/CCD/tolerance` (`float`)"
                    ```
                    /solver/contact/CCD/tolerance
                    ```
                    <h2>Description</h2>
                    CCD tolerance

                    **Default**: `1e-06`








                ??? json-spec "`/solver/contact/CCD/max_iterations` (`int`)"
                    ```
                    /solver/contact/CCD/max_iterations
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations for continuous collision detection

                    **Default**: `1000000`











            ??? json-spec "`/solver/contact/friction_iterations` (`int`)"
                ```
                /solver/contact/friction_iterations
                ```
                <h2>Description</h2>
                Maximum number of update iterations for lagged friction formulation (see IPC paper).

                **Default**: `1`








            ??? json-spec "`/solver/contact/friction_convergence_tol` (`float`)"
                ```
                /solver/contact/friction_convergence_tol
                ```
                <h2>Description</h2>
                Tolerence for friction convergence

                **Default**: `0.01`






            ??? json-spec "`/solver/contact/barrier_stiffness`"
                ```
                /solver/contact/barrier_stiffness
                ```


                === "`/solver/contact/barrier_stiffness` (`string`)"
                    <h2>Description</h2>
                    How coefficient of clamped log-barrier function for contact is updated

                    **Default**: `'adaptive'`

                    **Options:** `['adaptive']`



                === "`/solver/contact/barrier_stiffness` (`float`)"
                    <h2>Description</h2>
                    The coefficient of clamped log-barrier function value when not adaptive











        ??? json-spec "`/solver/ignore_inertia` (`bool`)"
            ```
            /solver/ignore_inertia
            ```
            <h2>Description</h2>
            Ignore inertia in time dependent. Used for doing incremental load.

            **Default**: `False`








        ??? json-spec "`/solver/advanced` (`object`)"
            ```
            /solver/advanced
            ```
            <h2>Description</h2>
            Advanced settings for the solver

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/solver/advanced/cache_size` (`int`)"
                ```
                /solver/advanced/cache_size
                ```
                <h2>Description</h2>
                Maximum number of elements when the assembly values are cached.

                **Default**: `900000`








            ??? json-spec "`/solver/advanced/lump_mass_matrix` (`bool`)"
                ```
                /solver/advanced/lump_mass_matrix
                ```
                <h2>Description</h2>
                If true, use diagonal mass matrix with entries on the diagonal equal to the sum of entries in each row of the full mass matrix.}

                **Default**: `False`








            ??? json-spec "`/solver/advanced/lagged_regularization_weight` (`float`)"
                ```
                /solver/advanced/lagged_regularization_weight
                ```
                <h2>Description</h2>
                Weight used to regularize singular static problems.

                **Default**: `0`














    ??? json-spec "`/boundary_conditions` (`object`)"
        ```
        /boundary_conditions
        ```
        <h2>Description</h2>
        The settings for boundary conditions.

        **Default**: `None`
        <h2>Optional</h2>



        ??? json-spec "`/boundary_conditions/rhs`"
            ```
            /boundary_conditions/rhs
            ```


            === "`/boundary_conditions/rhs` (`float`)"
                <h2>Description</h2>
                Right-hand side of the system being solved for scalar-valued PDEs



            === "`/boundary_conditions/rhs` (`string`)"
                <h2>Description</h2>
                Right-hand side of the system being solved as a function of $x,y,z,t$.



            === "`/boundary_conditions/rhs` (`list`)"
                <h2>Description</h2>
                Right-hand side of the system being solved for vector-valued PDEs.



                ??? json-spec "`/boundary_conditions/rhs/*`"
                    ```
                    /boundary_conditions/rhs/*
                    ```


                    === "`/boundary_conditions/rhs/*` (`float`)"
                        <h2>Description</h2>
                        Right-hand side of the system being solved, value.

                        **Default**: `0`



                    === "`/boundary_conditions/rhs/*` (`string`)"
                        <h2>Description</h2>
                        Right-hand side of the system being solved as a function of $x,y,z,t$.











        ??? json-spec "`/boundary_conditions/dirichlet_boundary` (`list`)"
            ```
            /boundary_conditions/dirichlet_boundary
            ```
            <h2>Description</h2>
            The list of Dirichlet boundary conditions for the main variable. Elements of the list are assignment pairs (ID, value) where ID is assigned by surface selection.



            ??? json-spec "`/boundary_conditions/dirichlet_boundary/*`"
                ```
                /boundary_conditions/dirichlet_boundary/*
                ```


                === "`/boundary_conditions/dirichlet_boundary/*` (`object`)"
                    <h2>Description</h2>
                    Dirichlet boundary condition.

                    **Default**: `None`
                    <h2>Required</h2>



                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/id`"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/id
                        ```


                        === "`/boundary_conditions/dirichlet_boundary/*/id` (`int`)"
                            <h2>Description</h2>
                            ID of Dirichlet boundary condition from surface selection.



                        === "`/boundary_conditions/dirichlet_boundary/*/id` (`string`)"
                            <h2>Description</h2>
                            select all ids.

                            **Options:** `['all']`








                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value` (`list`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/value
                        ```
                        <h2>Description</h2>
                        Values of Dirichlet boundary condition, length 1 for scalar-valued pde, 2/3 for vector-valued PDEs depending on the dimension.



                        ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value/*`"
                            ```
                            /boundary_conditions/dirichlet_boundary/*/value/*
                            ```


                            === "`/boundary_conditions/dirichlet_boundary/*/value/*` (`string`)"
                                <h2>Description</h2>
                                Values of Dirichlet boundary condition for each dimension as a function of $x,y,z,t$.



                            === "`/boundary_conditions/dirichlet_boundary/*/value/*` (`float`)"
                                <h2>Description</h2>
                                Values of Dirichlet boundary condition for each dimension.






                    <h2>Optional</h2>





                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/dimension` (`list`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/dimension
                        ```
                        <h2>Description</h2>
                        List of 2 (2D) or 3 (3D) boolean values indicating if the Dirichlet boundary condition  is applied for a particular dimension.





                        ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/dimension/*` (`bool`)"
                            ```
                            /boundary_conditions/dirichlet_boundary/*/dimension/*
                            ```
                            <h2>Description</h2>
                            value

                            **Default**: `True`









                === "`/boundary_conditions/dirichlet_boundary/*` (`string`)"
                    <h2>Description</h2>
                    Dirichlet boundary condition loaded from a file, <node_id> <bc values>, 1 for scalar, 2/3 for tensor depending on dimension.











        ??? json-spec "`/boundary_conditions/neumann_boundary` (`list`)"
            ```
            /boundary_conditions/neumann_boundary
            ```
            <h2>Description</h2>
            The list of Neumann boundary conditions for the main variable. Elements of the list are assignment pairs (ID, value) where ID is assigned by surface selection.





            ??? json-spec "`/boundary_conditions/neumann_boundary/*` (`object`)"
                ```
                /boundary_conditions/neumann_boundary/*
                ```
                <h2>Description</h2>
                Neumann boundary condition

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/boundary_conditions/neumann_boundary/*/id` (`int`)"
                    ```
                    /boundary_conditions/neumann_boundary/*/id
                    ```
                    <h2>Description</h2>
                    ID of Neumann boundary condition

                    **Default**: `1`








                ??? json-spec "`/boundary_conditions/neumann_boundary/*/value` (`list`)"
                    ```
                    /boundary_conditions/neumann_boundary/*/value
                    ```
                    <h2>Description</h2>
                    Values of Neumann boundary condition for each dimension



                    ??? json-spec "`/boundary_conditions/neumann_boundary/*/value/*`"
                        ```
                        /boundary_conditions/neumann_boundary/*/value/*
                        ```


                        === "`/boundary_conditions/neumann_boundary/*/value/*` (`string`)"
                            <h2>Description</h2>
                            Values of Neumann boundary condition for each dimension as function of $x,y,z,t$

                            **Default**: `''`



                        === "`/boundary_conditions/neumann_boundary/*/value/*` (`float`)"
                            <h2>Description</h2>
                            Values of Neumann boundary condition for each dimension

                            **Default**: `0`

















        ??? json-spec "`/boundary_conditions/pressure_boundary` (`list`)"
            ```
            /boundary_conditions/pressure_boundary
            ```
            <h2>Description</h2>
            Dirichlet boundary condition for normal * value for vector-valued PDEs.





            ??? json-spec "`/boundary_conditions/pressure_boundary/*` (`object`)"
                ```
                /boundary_conditions/pressure_boundary/*
                ```
                <h2>Description</h2>
                pressure BC entry

                **Default**: `None`
                <h2>Required</h2>





                ??? json-spec "`/boundary_conditions/pressure_boundary/*/id` (`int`)"
                    ```
                    /boundary_conditions/pressure_boundary/*/id
                    ```
                    <h2>Description</h2>
                    ID for the pressure Neumann boundary condition








                ??? json-spec "`/boundary_conditions/pressure_boundary/*/value` (`list`)"
                    ```
                    /boundary_conditions/pressure_boundary/*/value
                    ```
                    <h2>Description</h2>
                    Values of pressure Neumann boundary condition



                    ??? json-spec "`/boundary_conditions/pressure_boundary/*/value/*`"
                        ```
                        /boundary_conditions/pressure_boundary/*/value/*
                        ```


                        === "`/boundary_conditions/pressure_boundary/*/value/*` (`string`)"
                            <h2>Description</h2>
                            Values of pressure Neumann boundary condition as a function of $x,y,z,t$



                        === "`/boundary_conditions/pressure_boundary/*/value/*` (`float`)"
                            <h2>Description</h2>
                            Values of pressure Neumann boundary condition






                <h2>Optional</h2>
















        ??? json-spec "`/boundary_conditions/obstacle_displacements` (`list`)"
            ```
            /boundary_conditions/obstacle_displacements
            ```
            <h2>Description</h2>
            The list of obstacle displacements. Each entry is an (ID, value) pair, where ids are set by selection.





            ??? json-spec "`/boundary_conditions/obstacle_displacements/*` (`object`)"
                ```
                /boundary_conditions/obstacle_displacements/*
                ```
                <h2>Description</h2>
                Obstacle displacements

                **Default**: `None`
                <h2>Required</h2>





                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/id` (`int`)"
                    ```
                    /boundary_conditions/obstacle_displacements/*/id
                    ```
                    <h2>Description</h2>
                    ID of Obstacle displacements








                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/value` (`list`)"
                    ```
                    /boundary_conditions/obstacle_displacements/*/value
                    ```
                    <h2>Description</h2>
                    Values of Obstacle displacements for each dimension



                    ??? json-spec "`/boundary_conditions/obstacle_displacements/*/value/*`"
                        ```
                        /boundary_conditions/obstacle_displacements/*/value/*
                        ```


                        === "`/boundary_conditions/obstacle_displacements/*/value/*` (`string`)"
                            <h2>Description</h2>
                            Values of Obstacle displacements for each dimension as a function of $x,y,z,t$



                        === "`/boundary_conditions/obstacle_displacements/*/value/*` (`float`)"
                            <h2>Description</h2>
                            Values of Obstacle displacements for each dimension




















    ??? json-spec "`/initial_conditions` (`object`)"
        ```
        /initial_conditions
        ```
        <h2>Description</h2>
        Initial conditions for the time-dependent problem, imposed on the main variable, its derivative or second derivative

        **Default**: `None`
        <h2>Optional</h2>





        ??? json-spec "`/initial_conditions/solution` (`list`)"
            ```
            /initial_conditions/solution
            ```
            <h2>Description</h2>
            initial solution





            ??? json-spec "`/initial_conditions/solution/*` (`object`)"
                ```
                /initial_conditions/solution/*
                ```
                <h2>Description</h2>
                A list of (ID, value) pairs defining the initial conditions for the main variable values. Ids are set by selection, and values can be floats or formulas.

                **Default**: `None`
                <h2>Required</h2>





                ??? json-spec "`/initial_conditions/solution/*/id` (`int`)"
                    ```
                    /initial_conditions/solution/*/id
                    ```
                    <h2>Description</h2>
                    ID from volume selections








                ??? json-spec "`/initial_conditions/solution/*/value` (`list`)"
                    ```
                    /initial_conditions/solution/*/value
                    ```
                    <h2>Description</h2>
                    value of the solution



                    ??? json-spec "`/initial_conditions/solution/*/value/*`"
                        ```
                        /initial_conditions/solution/*/value/*
                        ```


                        === "`/initial_conditions/solution/*/value/*` (`float`)"
                            <h2>Description</h2>
                            value



                        === "`/initial_conditions/solution/*/value/*` (`string`)"
                            <h2>Description</h2>
                            as a function of $x,y,z,t$

















        ??? json-spec "`/initial_conditions/velocity` (`list`)"
            ```
            /initial_conditions/velocity
            ```
            <h2>Description</h2>
            initial velocity





            ??? json-spec "`/initial_conditions/velocity/*` (`object`)"
                ```
                /initial_conditions/velocity/*
                ```
                <h2>Description</h2>
                A list of (ID, value) pairs defining the initial conditions for the first derivative of the main variable values. Ids are set by selection, and values can be floats or formulas.

                **Default**: `None`
                <h2>Required</h2>





                ??? json-spec "`/initial_conditions/velocity/*/id` (`int`)"
                    ```
                    /initial_conditions/velocity/*/id
                    ```
                    <h2>Description</h2>
                    ID from volume selections








                ??? json-spec "`/initial_conditions/velocity/*/value` (`list`)"
                    ```
                    /initial_conditions/velocity/*/value
                    ```
                    <h2>Description</h2>
                    value od the initial velocity



                    ??? json-spec "`/initial_conditions/velocity/*/value/*`"
                        ```
                        /initial_conditions/velocity/*/value/*
                        ```


                        === "`/initial_conditions/velocity/*/value/*` (`float`)"
                            <h2>Description</h2>
                            value



                        === "`/initial_conditions/velocity/*/value/*` (`string`)"
                            <h2>Description</h2>
                            value as a function of $x,y,z,t$

















        ??? json-spec "`/initial_conditions/acceleration` (`list`)"
            ```
            /initial_conditions/acceleration
            ```
            <h2>Description</h2>
            initial acceleration





            ??? json-spec "`/initial_conditions/acceleration/*` (`object`)"
                ```
                /initial_conditions/acceleration/*
                ```
                <h2>Description</h2>
                entries

                **Default**: `None`
                <h2>Required</h2>





                ??? json-spec "`/initial_conditions/acceleration/*/id` (`int`)"
                    ```
                    /initial_conditions/acceleration/*/id
                    ```
                    <h2>Description</h2>
                    ID from volume selections








                ??? json-spec "`/initial_conditions/acceleration/*/value` (`list`)"
                    ```
                    /initial_conditions/acceleration/*/value
                    ```
                    <h2>Description</h2>
                    value



                    ??? json-spec "`/initial_conditions/acceleration/*/value/*`"
                        ```
                        /initial_conditions/acceleration/*/value/*
                        ```


                        === "`/initial_conditions/acceleration/*/value/*` (`float`)"
                            <h2>Description</h2>
                            value

                            **Default**: `0`



                        === "`/initial_conditions/acceleration/*/value/*` (`string`)"
                            <h2>Description</h2>
                            value as a function of $x,y,z,t$




















    ??? json-spec "`/output` (`object`)"
        ```
        /output
        ```
        <h2>Description</h2>
        output settings

        **Default**: `None`
        <h2>Optional</h2>





        ??? json-spec "`/output/json` (`string`)"
            ```
            /output/json
            ```
            <h2>Description</h2>
            File name for json output statistics on time/error/etc.

            **Default**: `''`








        ??? json-spec "`/output/paraview` (`object`)"
            ```
            /output/paraview
            ```
            <h2>Description</h2>
            Output in paraview format

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/output/paraview/file_name` (`string`)"
                ```
                /output/paraview/file_name
                ```
                <h2>Description</h2>
                Paraview output file name

                **Default**: `''`








            ??? json-spec "`/output/paraview/vismesh_rel_area` (`float`)"
                ```
                /output/paraview/vismesh_rel_area
                ```
                <h2>Description</h2>
                relative area for the upsampled visualisation mesh

                **Default**: `1e-05`








            ??? json-spec "`/output/paraview/skip_frame` (`int`)"
                ```
                /output/paraview/skip_frame
                ```
                <h2>Description</h2>
                export every skip_frame-th frames for time dependent simulations

                **Default**: `1`








            ??? json-spec "`/output/paraview/high_order_mesh` (`bool`)"
                ```
                /output/paraview/high_order_mesh
                ```
                <h2>Description</h2>
                Enables/disables high-order output for paraview. Supported only for isoparametric or linear meshes with high-odrer solutions.

                **Default**: `True`








            ??? json-spec "`/output/paraview/volume` (`bool`)"
                ```
                /output/paraview/volume
                ```
                <h2>Description</h2>
                Export volumetric mesh

                **Default**: `True`








            ??? json-spec "`/output/paraview/surface` (`bool`)"
                ```
                /output/paraview/surface
                ```
                <h2>Description</h2>
                Export surface mesh (in 2d polygon)

                **Default**: `False`








            ??? json-spec "`/output/paraview/wireframe` (`bool`)"
                ```
                /output/paraview/wireframe
                ```
                <h2>Description</h2>
                Export the wireframe of the mesh

                **Default**: `False`








            ??? json-spec "`/output/paraview/options` (`object`)"
                ```
                /output/paraview/options
                ```
                <h2>Description</h2>
                Optional fields in the output

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/output/paraview/options/material` (`bool`)"
                    ```
                    /output/paraview/options/material
                    ```
                    <h2>Description</h2>
                    If true, write out material values sampled on the vertices of the mesh

                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/body_ids` (`bool`)"
                    ```
                    /output/paraview/options/body_ids
                    ```
                    <h2>Description</h2>
                    Export volumes ids

                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/contact_forces` (`bool`)"
                    ```
                    /output/paraview/options/contact_forces
                    ```
                    <h2>Description</h2>
                    If true, write out contact forces for surface

                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/friction_forces` (`bool`)"
                    ```
                    /output/paraview/options/friction_forces
                    ```
                    <h2>Description</h2>
                    If true, write out friction forces for surface

                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/velocity` (`bool`)"
                    ```
                    /output/paraview/options/velocity
                    ```
                    <h2>Description</h2>
                    If true, write out velocities

                    **Default**: `False`








                ??? json-spec "`/output/paraview/options/acceleration` (`bool`)"
                    ```
                    /output/paraview/options/acceleration
                    ```
                    <h2>Description</h2>
                    If true, write out accelerations

                    **Default**: `False`














        ??? json-spec "`/output/data` (`object`)"
            ```
            /output/data
            ```
            <h2>Description</h2>
            File names to write output data to.

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/output/data/solution` (`string`)"
                ```
                /output/data/solution
                ```
                <h2>Description</h2>
                Main variable solution. Unrolled [xyz, xyz, ...] using PolyFEM ordering. If reorder_nodes exports the solution with the same order the vertices of the input mesh as a #n x d file

                **Default**: `''`








            ??? json-spec "`/output/data/full_mat` (`string`)"
                ```
                /output/data/full_mat
                ```
                <h2>Description</h2>
                System matrix without boundary conditions. Doesn't work for nonlinear problems

                **Default**: `''`








            ??? json-spec "`/output/data/stiffness_mat` (`string`)"
                ```
                /output/data/stiffness_mat
                ```
                <h2>Description</h2>
                System matrix with boundary conditions. Doesn't work for nonlinear problems

                **Default**: `''`








            ??? json-spec "`/output/data/stress_mat` (`string`)"
                ```
                /output/data/stress_mat
                ```
                <h2>Description</h2>
                Exports stress

                **Default**: `''`








            ??? json-spec "`/output/data/u_path` (`string`)"
                ```
                /output/data/u_path
                ```
                <h2>Description</h2>
                Writes the complete solution in PolyFEM format, used to restart the sim

                **Default**: `''`








            ??? json-spec "`/output/data/v_path` (`string`)"
                ```
                /output/data/v_path
                ```
                <h2>Description</h2>
                Writes the complete velocity in PolyFEM format, used to restart the sim

                **Default**: `''`








            ??? json-spec "`/output/data/a_path` (`string`)"
                ```
                /output/data/a_path
                ```
                <h2>Description</h2>
                Writes the complete acceleration in PolyFEM format, used to restart the sim

                **Default**: `''`








            ??? json-spec "`/output/data/mises` (`string`)"
                ```
                /output/data/mises
                ```
                <h2>Description</h2>
                File name to write per-node Von Mises stress values to.

                **Default**: `''`








            ??? json-spec "`/output/data/nodes` (`string`)"
                ```
                /output/data/nodes
                ```
                <h2>Description</h2>
                Writes the FEM nodes

                **Default**: `''`








            ??? json-spec "`/output/data/advanced` (`object`)"
                ```
                /output/data/advanced
                ```
                <h2>Description</h2>
                advanced options

                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/output/data/advanced/reorder_nodes` (`bool`)"
                    ```
                    /output/data/advanced/reorder_nodes
                    ```
                    <h2>Description</h2>
                    Reorder nodes accodring to input

                    **Default**: `False`














        ??? json-spec "`/output/advanced` (`object`)"
            ```
            /output/advanced
            ```
            <h2>Description</h2>
            Additional output options

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/output/advanced/timestep_prefix` (`string`)"
                ```
                /output/advanced/timestep_prefix
                ```
                <h2>Description</h2>
                Prefix for output file names for each time step, the final file is step_i.[vtu|vtm] where i is the time index.

                **Default**: `'step_'`








            ??? json-spec "`/output/advanced/sol_on_grid` (`float`)"
                ```
                /output/advanced/sol_on_grid
                ```
                <h2>Description</h2>
                exports the solution sampled on a grid, specify the grid spacing

                **Default**: `-1`








            ??? json-spec "`/output/advanced/compute_error` (`bool`)"
                ```
                /output/advanced/compute_error
                ```
                <h2>Description</h2>
                Enables the computation of the error. If no reference solution is provided, return the norms of the solution

                **Default**: `True`








            ??? json-spec "`/output/advanced/sol_at_node` (`int`)"
                ```
                /output/advanced/sol_at_node
                ```
                <h2>Description</h2>
                Write out solution values at a specific node. the values will be written in the output json file

                **Default**: `-1`








            ??? json-spec "`/output/advanced/vis_boundary_only` (`bool`)"
                ```
                /output/advanced/vis_boundary_only
                ```
                <h2>Description</h2>
                saves only elements touching the boundaries

                **Default**: `False`








            ??? json-spec "`/output/advanced/curved_mesh_size` (`bool`)"
                ```
                /output/advanced/curved_mesh_size
                ```
                <h2>Description</h2>
                upsample curved edges to compute mesh size

                **Default**: `False`








            ??? json-spec "`/output/advanced/save_solve_sequence_debug` (`bool`)"
                ```
                /output/advanced/save_solve_sequence_debug
                ```
                <h2>Description</h2>
                saves AL internal steps, for debugging

                **Default**: `False`








            ??? json-spec "`/output/advanced/save_time_sequence` (`bool`)"
                ```
                /output/advanced/save_time_sequence
                ```
                <h2>Description</h2>
                saves timesteps

                **Default**: `True`








            ??? json-spec "`/output/advanced/save_nl_solve_sequence` (`bool`)"
                ```
                /output/advanced/save_nl_solve_sequence
                ```
                <h2>Description</h2>
                saves obj after every nonlinear iteration, for debugging

                **Default**: `False`








            ??? json-spec "`/output/advanced/spectrum` (`bool`)"
                ```
                /output/advanced/spectrum
                ```
                <h2>Description</h2>
                exports the spectrum of the matrix in the output json. Works only if POLYSOLVE_WITH_SPECTRA is enabled

                **Default**: `False`











        ??? json-spec "`/output/reference` (`object`)"
            ```
            /output/reference
            ```
            <h2>Description</h2>
            Write out the analytic/numerical ground-truth solution and or its gradient

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/output/reference/solution` (`list`)"
                ```
                /output/reference/solution
                ```
                <h2>Description</h2>
                reference solution used to compute errors





                ??? json-spec "`/output/reference/solution/*` (`string`)"
                    ```
                    /output/reference/solution/*
                    ```
                    <h2>Description</h2>
                    value as a function of $x,y,z,t$

                    **Default**: `''`











            ??? json-spec "`/output/reference/gradient` (`list`)"
                ```
                /output/reference/gradient
                ```
                <h2>Description</h2>
                gradient of the reference solution to compute errors





                ??? json-spec "`/output/reference/gradient/*` (`string`)"
                    ```
                    /output/reference/gradient/*
                    ```
                    <h2>Description</h2>
                    value as a function of $x,y,z,t$

                    **Default**: `''`

















    ??? json-spec "`/input` (`object`)"
        ```
        /input
        ```
        <h2>Description</h2>
        input data

        **Default**: `None`
        <h2>Optional</h2>





        ??? json-spec "`/input/data` (`object`)"
            ```
            /input/data
            ```
            <h2>Description</h2>
            input to restart time dependent sim

            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/input/data/u_path` (`string`)"
                ```
                /input/data/u_path
                ```
                <h2>Description</h2>
                input solution

                **Default**: `''`








            ??? json-spec "`/input/data/v_path` (`string`)"
                ```
                /input/data/v_path
                ```
                <h2>Description</h2>
                input velocity

                **Default**: `''`








            ??? json-spec "`/input/data/a_path` (`string`)"
                ```
                /input/data/a_path
                ```
                <h2>Description</h2>
                input acceleration

                **Default**: `''`














    ??? json-spec "`/tests` (`object`)"
        ```
        /tests
        ```
        <h2>Description</h2>
        Used to test to compare different norms of solutions.

        **Default**: `None`
        <h2>Optional</h2>





        ??? json-spec "`/tests/err_h1` (`float`)"
            ```
            /tests/err_h1
            ```
            <h2>Description</h2>
            Reference h1 solution's norm.

            **Default**: `0`








        ??? json-spec "`/tests/err_h1_semi` (`float`)"
            ```
            /tests/err_h1_semi
            ```
            <h2>Description</h2>
            Reference h1 seminorm solution's norm.

            **Default**: `0`








        ??? json-spec "`/tests/err_l2` (`float`)"
            ```
            /tests/err_l2
            ```
            <h2>Description</h2>
            Reference $L^2$ solution's norm.

            **Default**: `0`








        ??? json-spec "`/tests/err_linf` (`float`)"
            ```
            /tests/err_linf
            ```
            <h2>Description</h2>
            Reference $L^\infty$ solution's norm.

            **Default**: `0`








        ??? json-spec "`/tests/err_linf_grad` (`float`)"
            ```
            /tests/err_linf_grad
            ```
            <h2>Description</h2>
            Reference $L^\infty$ solution's gradient norm.

            **Default**: `0`








        ??? json-spec "`/tests/err_lp` (`float`)"
            ```
            /tests/err_lp
            ```
            <h2>Description</h2>
            Reference $L^8$ solution's gradient norm.

            **Default**: `0`








        ??? json-spec "`/tests/margin` (`float`)"
            ```
            /tests/margin
            ```
            <h2>Description</h2>
            Reference tolerance used in tests.

            **Default**: `1e-05`






        ??? json-spec "`/tests/time_steps`"
            ```
            /tests/time_steps
            ```


            === "`/tests/time_steps` (`int`)"
                <h2>Description</h2>
                Number of time steps to test.

                **Default**: `1`

                **Range:** `[1, inf]`



            === "`/tests/time_steps` (`string`)"
                <h2>Description</h2>
                Number of time steps to test.

                **Options:** `['all', 'static']`








