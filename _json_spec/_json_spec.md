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



        ??? json-spec "`/geometry/*`"
            ```
            /geometry/*
            ```


            === "`/geometry/*` (`object`)"
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
                
                    **Options:** `['mesh', 'plane', 'ground', 'mesh_sequence', 'mesh_array']`








                ??? json-spec "`/geometry/*/extract` (`string`)"
                    ```
                    /geometry/*/extract
                    ```
                    <h2>Description</h2>
                    Used to extract stuff from the mesh. Eg extract surface extracts the surface from a tet mesh.
                
                    **Default**: `'volume'`
                
                    **Options:** `['volume', 'edges', 'points', 'surface']`








                ??? json-spec "`/geometry/*/unit` (`string`)"
                    ```
                    /geometry/*/unit
                    ```
                    <h2>Description</h2>
                    Units of the geometric model.
                
                    **Default**: `''`








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
                        Assign specified ID to all elements of the geometry.



                    === "`/geometry/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        Load ids from a file; the file is required to have one ID per element of the geometry
                    
                        **Extensions:** `['.txt']`



                    === "`/geometry/*/volume_selection` (`object`)"
                        <h2>Description</h2>
                        Offsets the volume IDs loaded from the mesh.
                    
                        **Default**: `None`
                        <h2>Optional</h2>





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
                                Assign the ID to all elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                            
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
                                Assign the ID to all elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
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
                                Assign the ID to all elements with barycenters inside a cylinder with specified axis (p1, p2) and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
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








                                ??? json-spec "`/geometry/*/volume_selection/*/p1` (`list`)"
                                    ```
                                    /geometry/*/volume_selection/*/p1
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/volume_selection/*/p1/*` (`float`)"
                                        ```
                                        /geometry/*/volume_selection/*/p1/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.











                                ??? json-spec "`/geometry/*/volume_selection/*/p2` (`list`)"
                                    ```
                                    /geometry/*/volume_selection/*/p2
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/volume_selection/*/p2/*` (`float`)"
                                        ```
                                        /geometry/*/volume_selection/*/p2/*
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
                                Assign the ID to all elements with barycenters in a halfspace. The halfspace boundary plane is defined by a point in the plane and the normal, which points to the halfspace. The option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                            
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












                ??? json-spec "`/geometry/*/surface_selection`"
                    ```
                    /geometry/*/surface_selection
                    ```


                    === "`/geometry/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        Assign specified ID to all elements of the geometry.



                    === "`/geometry/*/surface_selection` (`file`)"
                        <h2>Description</h2>
                        Load ids from a file; the file is required to have one ID per element of the geometry
                    
                        **Extensions:** `['.txt']`



                    === "`/geometry/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        List of selection (ID assignment) operations to apply to the geometry; operations can be box, sphere, etc.



                        ??? json-spec "`/geometry/*/surface_selection/*`"
                            ```
                            /geometry/*/surface_selection/*
                            ```


                            === "`/geometry/*/surface_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                            
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
                                Assign the ID to all elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
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
                                Assign the ID to all elements with barycenters inside a cylinder with specified axis (p1, p2) and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
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








                                ??? json-spec "`/geometry/*/surface_selection/*/p1` (`list`)"
                                    ```
                                    /geometry/*/surface_selection/*/p1
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/surface_selection/*/p1/*` (`float`)"
                                        ```
                                        /geometry/*/surface_selection/*/p1/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.











                                ??? json-spec "`/geometry/*/surface_selection/*/p2` (`list`)"
                                    ```
                                    /geometry/*/surface_selection/*/p2
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/surface_selection/*/p2/*` (`float`)"
                                        ```
                                        /geometry/*/surface_selection/*/p2/*
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
                                Assign the ID to all elements with barycenters in a halfspace. The halfspace boundary plane is defined by a point in the plane and the normal, which points to the halfspace. The option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                            
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






                            === "`/geometry/*/surface_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assigns ids to sides touching the bbox of the model using a threshold. Assigns 1+offset to left, 2+offset to bottom, 3+offset to right, 4+offset to top, 5+offset to front, 6+offset to back, 7+offset to everything else.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/surface_selection/*/threshold` (`float`)"
                                    ```
                                    /geometry/*/surface_selection/*/threshold
                                    ```
                                    <h2>Description</h2>
                                    Threshold for box side selection.



                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/surface_selection/*/id_offset` (`int`)"
                                    ```
                                    /geometry/*/surface_selection/*/id_offset
                                    ```
                                    <h2>Description</h2>
                                    ID offset of box side selection.
                                
                                    **Default**: `0`














                ??? json-spec "`/geometry/*/curve_selection` (`object`)"
                    ```
                    /geometry/*/curve_selection
                    ```
                    <h2>Description</h2>
                    Selection of curves
                
                    **Default**: `None`






                ??? json-spec "`/geometry/*/point_selection`"
                    ```
                    /geometry/*/point_selection
                    ```


                    === "`/geometry/*/point_selection` (`int`)"
                        <h2>Description</h2>
                        Assign specified ID to all elements of the geometry.



                    === "`/geometry/*/point_selection` (`file`)"
                        <h2>Description</h2>
                        Load ids from a file; the file is required to have one ID per element of the geometry
                    
                        **Extensions:** `['.txt']`



                    === "`/geometry/*/point_selection` (`list`)"
                        <h2>Description</h2>
                        List of selection (ID assignment) operations to apply to the geometry; operations can be box, sphere, etc.



                        ??? json-spec "`/geometry/*/point_selection/*`"
                            ```
                            /geometry/*/point_selection/*
                            ```


                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/box` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/box
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/box/*` (`list`)"
                                        ```
                                        /geometry/*/point_selection/*/box/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.





                                        ??? json-spec "`/geometry/*/point_selection/*/box/*/*` (`float`)"
                                            ```
                                            /geometry/*/point_selection/*/box/*/*
                                            ```
                                            <h2>Description</h2>
                                            FIXME: Missing documentation in the specification.
                                        
                                            **Default**: `0`









                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/radius` (`float`)"
                                    ```
                                    /geometry/*/point_selection/*/radius
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/center` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/center
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/center/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/center/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.






                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters inside a cylinder with specified axis (p1, p2) and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/radius` (`float`)"
                                    ```
                                    /geometry/*/point_selection/*/radius
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/p1` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/p1
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/p1/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/p1/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.











                                ??? json-spec "`/geometry/*/point_selection/*/p2` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/p2
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/p2/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/p2/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.






                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters in a halfspace. The halfspace boundary plane is defined by a point in the plane and the normal, which points to the halfspace. The option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/point` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/point
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/point/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/point/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.











                                ??? json-spec "`/geometry/*/point_selection/*/normal` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/normal
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/normal/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/normal/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.






                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Same as halfspace, but the boundary plane is axis-aligned. The choice of axis is specified either by a string matching the regexp r"[+-][xyzXYZ]" or an int matching the regular expression [+-]?[123] where the sign is the side of the plane to select and letter or number indicates the axis to which the plane is perpendicular. The offset is the plane offset from the origin. If the relative option is set to true, the offset is with respect to the center of the bounding box.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.






                                ??? json-spec "`/geometry/*/point_selection/*/axis`"
                                    ```
                                    /geometry/*/point_selection/*/axis
                                    ```


                                    === "`/geometry/*/point_selection/*/axis` (`int`)"
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.



                                    === "`/geometry/*/point_selection/*/axis` (`string`)"
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/position` (`float`)"
                                    ```
                                    /geometry/*/point_selection/*/position
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.



                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assigns ids to sides touching the bbox of the model using a threshold. Assigns 1+offset to left, 2+offset to bottom, 3+offset to right, 4+offset to top, 5+offset to front, 6+offset to back, 7+offset to everything else.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/threshold` (`float`)"
                                    ```
                                    /geometry/*/point_selection/*/threshold
                                    ```
                                    <h2>Description</h2>
                                    Threshold for box side selection.



                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id_offset` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id_offset
                                    ```
                                    <h2>Description</h2>
                                    ID offset of box side selection.
                                
                                    **Default**: `0`














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






            === "mesh_array"
            
                **Type**: mesh_array
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








                ??? json-spec "`/geometry/*/array` (`object`)"
                    ```
                    /geometry/*/array
                    ```
                    <h2>Description</h2>
                    Array of meshes
                    <h2>Required</h2>





                    ??? json-spec "`/geometry/*/array/offset` (`float`)"
                        ```
                        /geometry/*/array/offset
                        ```
                        <h2>Description</h2>
                        Offset of the mesh in the array.








                    ??? json-spec "`/geometry/*/array/size` (`list`)"
                        ```
                        /geometry/*/array/size
                        ```
                        <h2>Description</h2>
                        Size of the array (two entries for 2D problems or three entries for 3D problems).





                        ??? json-spec "`/geometry/*/array/size/*` (`int`)"
                            ```
                            /geometry/*/array/size/*
                            ```
                            <h2>Description</h2>
                            Size of the array (two entries for 2D problems or three entries for 3D problems).
                        
                            **Range:** `[1, inf]`






                    <h2>Optional</h2>





                    ??? json-spec "`/geometry/*/array/relative` (`bool`)"
                        ```
                        /geometry/*/array/relative
                        ```
                        <h2>Description</h2>
                        Is the offset value relative to the mesh's dimensions.
                    
                        **Default**: `False`






                <h2>Optional</h2>





                ??? json-spec "`/geometry/*/type` (`string`)"
                    ```
                    /geometry/*/type
                    ```
                    <h2>Description</h2>
                    Type of geometry, currently only one supported. In future we will add stuff like planes, spheres, etc.
                
                    **Default**: `'mesh'`
                
                    **Options:** `['mesh', 'plane', 'ground', 'mesh_sequence', 'mesh_array']`








                ??? json-spec "`/geometry/*/extract` (`string`)"
                    ```
                    /geometry/*/extract
                    ```
                    <h2>Description</h2>
                    Used to extract stuff from the mesh. Eg extract surface extracts the surface from a tet mesh.
                
                    **Default**: `'volume'`
                
                    **Options:** `['volume', 'edges', 'points', 'surface']`








                ??? json-spec "`/geometry/*/unit` (`string`)"
                    ```
                    /geometry/*/unit
                    ```
                    <h2>Description</h2>
                    Units of the geometric model.
                
                    **Default**: `''`








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
                        Assign specified ID to all elements of the geometry.



                    === "`/geometry/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        Load ids from a file; the file is required to have one ID per element of the geometry
                    
                        **Extensions:** `['.txt']`



                    === "`/geometry/*/volume_selection` (`object`)"
                        <h2>Description</h2>
                        Offsets the volume IDs loaded from the mesh.
                    
                        **Default**: `None`
                        <h2>Optional</h2>





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
                                Assign the ID to all elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                            
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
                                Assign the ID to all elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
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
                                Assign the ID to all elements with barycenters inside a cylinder with specified axis (p1, p2) and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
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








                                ??? json-spec "`/geometry/*/volume_selection/*/p1` (`list`)"
                                    ```
                                    /geometry/*/volume_selection/*/p1
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/volume_selection/*/p1/*` (`float`)"
                                        ```
                                        /geometry/*/volume_selection/*/p1/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.











                                ??? json-spec "`/geometry/*/volume_selection/*/p2` (`list`)"
                                    ```
                                    /geometry/*/volume_selection/*/p2
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/volume_selection/*/p2/*` (`float`)"
                                        ```
                                        /geometry/*/volume_selection/*/p2/*
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
                                Assign the ID to all elements with barycenters in a halfspace. The halfspace boundary plane is defined by a point in the plane and the normal, which points to the halfspace. The option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                            
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












                ??? json-spec "`/geometry/*/surface_selection`"
                    ```
                    /geometry/*/surface_selection
                    ```


                    === "`/geometry/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        Assign specified ID to all elements of the geometry.



                    === "`/geometry/*/surface_selection` (`file`)"
                        <h2>Description</h2>
                        Load ids from a file; the file is required to have one ID per element of the geometry
                    
                        **Extensions:** `['.txt']`



                    === "`/geometry/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        List of selection (ID assignment) operations to apply to the geometry; operations can be box, sphere, etc.



                        ??? json-spec "`/geometry/*/surface_selection/*`"
                            ```
                            /geometry/*/surface_selection/*
                            ```


                            === "`/geometry/*/surface_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                            
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
                                Assign the ID to all elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
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
                                Assign the ID to all elements with barycenters inside a cylinder with specified axis (p1, p2) and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
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








                                ??? json-spec "`/geometry/*/surface_selection/*/p1` (`list`)"
                                    ```
                                    /geometry/*/surface_selection/*/p1
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/surface_selection/*/p1/*` (`float`)"
                                        ```
                                        /geometry/*/surface_selection/*/p1/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.











                                ??? json-spec "`/geometry/*/surface_selection/*/p2` (`list`)"
                                    ```
                                    /geometry/*/surface_selection/*/p2
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/surface_selection/*/p2/*` (`float`)"
                                        ```
                                        /geometry/*/surface_selection/*/p2/*
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
                                Assign the ID to all elements with barycenters in a halfspace. The halfspace boundary plane is defined by a point in the plane and the normal, which points to the halfspace. The option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                            
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






                            === "`/geometry/*/surface_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assigns ids to sides touching the bbox of the model using a threshold. Assigns 1+offset to left, 2+offset to bottom, 3+offset to right, 4+offset to top, 5+offset to front, 6+offset to back, 7+offset to everything else.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/surface_selection/*/threshold` (`float`)"
                                    ```
                                    /geometry/*/surface_selection/*/threshold
                                    ```
                                    <h2>Description</h2>
                                    Threshold for box side selection.



                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/surface_selection/*/id_offset` (`int`)"
                                    ```
                                    /geometry/*/surface_selection/*/id_offset
                                    ```
                                    <h2>Description</h2>
                                    ID offset of box side selection.
                                
                                    **Default**: `0`














                ??? json-spec "`/geometry/*/curve_selection` (`object`)"
                    ```
                    /geometry/*/curve_selection
                    ```
                    <h2>Description</h2>
                    Selection of curves
                
                    **Default**: `None`






                ??? json-spec "`/geometry/*/point_selection`"
                    ```
                    /geometry/*/point_selection
                    ```


                    === "`/geometry/*/point_selection` (`int`)"
                        <h2>Description</h2>
                        Assign specified ID to all elements of the geometry.



                    === "`/geometry/*/point_selection` (`file`)"
                        <h2>Description</h2>
                        Load ids from a file; the file is required to have one ID per element of the geometry
                    
                        **Extensions:** `['.txt']`



                    === "`/geometry/*/point_selection` (`list`)"
                        <h2>Description</h2>
                        List of selection (ID assignment) operations to apply to the geometry; operations can be box, sphere, etc.



                        ??? json-spec "`/geometry/*/point_selection/*`"
                            ```
                            /geometry/*/point_selection/*
                            ```


                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters inside an axis-aligned box given by the list of its 2 corners, one with min, the other with max coordinates along all axes.  If relative option is set to true, the coordinates of the box corners are specified in bilinear/trilinear coordinates  with respect to the bounding box of the geometry.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/box` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/box
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/box/*` (`list`)"
                                        ```
                                        /geometry/*/point_selection/*/box/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.





                                        ??? json-spec "`/geometry/*/point_selection/*/box/*/*` (`float`)"
                                            ```
                                            /geometry/*/point_selection/*/box/*/*
                                            ```
                                            <h2>Description</h2>
                                            FIXME: Missing documentation in the specification.
                                        
                                            **Default**: `0`









                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters inside a sphere with specified center and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/radius` (`float`)"
                                    ```
                                    /geometry/*/point_selection/*/radius
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/center` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/center
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/center/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/center/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.






                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters inside a cylinder with specified axis (p1, p2) and radius.  If relative option is set to true, the coordinates of the  center are specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry, and the radius is specified relative to the bounding box diagonal length.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/radius` (`float`)"
                                    ```
                                    /geometry/*/point_selection/*/radius
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/p1` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/p1
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/p1/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/p1/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.











                                ??? json-spec "`/geometry/*/point_selection/*/p2` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/p2
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/p2/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/p2/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.






                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assign the ID to all elements with barycenters in a halfspace. The halfspace boundary plane is defined by a point in the plane and the normal, which points to the halfspace. The option relative set to true indicates that the point position is specified in bilinear/trilinear coordinates with respect to the bounding box of the geometry.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/point` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/point
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/point/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/point/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.











                                ??? json-spec "`/geometry/*/point_selection/*/normal` (`list`)"
                                    ```
                                    /geometry/*/point_selection/*/normal
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.





                                    ??? json-spec "`/geometry/*/point_selection/*/normal/*` (`float`)"
                                        ```
                                        /geometry/*/point_selection/*/normal/*
                                        ```
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.






                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Same as halfspace, but the boundary plane is axis-aligned. The choice of axis is specified either by a string matching the regexp r"[+-][xyzXYZ]" or an int matching the regular expression [+-]?[123] where the sign is the side of the plane to select and letter or number indicates the axis to which the plane is perpendicular. The offset is the plane offset from the origin. If the relative option is set to true, the offset is with respect to the center of the bounding box.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.






                                ??? json-spec "`/geometry/*/point_selection/*/axis`"
                                    ```
                                    /geometry/*/point_selection/*/axis
                                    ```


                                    === "`/geometry/*/point_selection/*/axis` (`int`)"
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.



                                    === "`/geometry/*/point_selection/*/axis` (`string`)"
                                        <h2>Description</h2>
                                        FIXME: Missing documentation in the specification.








                                ??? json-spec "`/geometry/*/point_selection/*/position` (`float`)"
                                    ```
                                    /geometry/*/point_selection/*/position
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.



                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/relative` (`bool`)"
                                    ```
                                    /geometry/*/point_selection/*/relative
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.
                                
                                    **Default**: `False`






                            === "`/geometry/*/point_selection/*` (`object`)"
                                <h2>Description</h2>
                                Assigns ids to sides touching the bbox of the model using a threshold. Assigns 1+offset to left, 2+offset to bottom, 3+offset to right, 4+offset to top, 5+offset to front, 6+offset to back, 7+offset to everything else.
                            
                                **Default**: `None`
                                <h2>Required</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/threshold` (`float`)"
                                    ```
                                    /geometry/*/point_selection/*/threshold
                                    ```
                                    <h2>Description</h2>
                                    Threshold for box side selection.



                                <h2>Optional</h2>





                                ??? json-spec "`/geometry/*/point_selection/*/id_offset` (`int`)"
                                    ```
                                    /geometry/*/point_selection/*/id_offset
                                    ```
                                    <h2>Description</h2>
                                    ID offset of box side selection.
                                
                                    **Default**: `0`














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






            === "plane"
            
                **Type**: plane
                <h2>Description</h2>
                Plane geometry object defined by its origin and normal.
                <h2>Required</h2>





                ??? json-spec "`/geometry/*/point` (`list`)"
                    ```
                    /geometry/*/point
                    ```
                    <h2>Description</h2>
                    Point on plane (two entries for 2D problems or three entries for 3D problems).





                    ??? json-spec "`/geometry/*/point/*` (`float`)"
                        ```
                        /geometry/*/point/*
                        ```
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.











                ??? json-spec "`/geometry/*/normal` (`list`)"
                    ```
                    /geometry/*/normal
                    ```
                    <h2>Description</h2>
                    Normal of plane (two entries for 2D problems or three entries for 3D problems).





                    ??? json-spec "`/geometry/*/normal/*` (`float`)"
                        ```
                        /geometry/*/normal/*
                        ```
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.






                <h2>Optional</h2>





                ??? json-spec "`/geometry/*/type` (`string`)"
                    ```
                    /geometry/*/type
                    ```
                    <h2>Description</h2>
                    Type of geometry, currently only one supported. In future we will add stuff like planes, spheres, etc.
                
                    **Default**: `'mesh'`
                
                    **Options:** `['mesh', 'plane', 'ground', 'mesh_sequence', 'mesh_array']`








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






            === "ground"
            
                **Type**: ground
                <h2>Description</h2>
                Plane orthogonal to gravity defined by its height.
                <h2>Required</h2>





                ??? json-spec "`/geometry/*/height` (`float`)"
                    ```
                    /geometry/*/height
                    ```
                    <h2>Description</h2>
                    Height of ground plane.



                <h2>Optional</h2>





                ??? json-spec "`/geometry/*/type` (`string`)"
                    ```
                    /geometry/*/type
                    ```
                    <h2>Description</h2>
                    Type of geometry, currently only one supported. In future we will add stuff like planes, spheres, etc.
                
                    **Default**: `'mesh'`
                
                    **Options:** `['mesh', 'plane', 'ground', 'mesh_sequence', 'mesh_array']`








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






            === "mesh_sequence"
            
                **Type**: mesh_sequence
                <h2>Description</h2>
                Mesh sequence.
                <h2>Required</h2>



                ??? json-spec "`/geometry/*/mesh_sequence`"
                    ```
                    /geometry/*/mesh_sequence
                    ```


                    === "`/geometry/*/mesh_sequence` (`string`)"
                        <h2>Description</h2>
                        Directory (or GLOB) of meshes for the mesh sequence.



                    === "`/geometry/*/mesh_sequence` (`list`)"
                        <h2>Description</h2>
                        List of mesh files for the mesh sequence.





                        ??? json-spec "`/geometry/*/mesh_sequence/*` (`file`)"
                            ```
                            /geometry/*/mesh_sequence/*
                            ```
                            <h2>Description</h2>
                            Path of the mesh file to load.
                        
                            **Extensions:** `['.obj', '.msh', '.stl', '.ply', '.mesh']`











                ??? json-spec "`/geometry/*/fps` (`int`)"
                    ```
                    /geometry/*/fps
                    ```
                    <h2>Description</h2>
                    Frames of the mesh sequence per second.



                <h2>Optional</h2>





                ??? json-spec "`/geometry/*/type` (`string`)"
                    ```
                    /geometry/*/type
                    ```
                    <h2>Description</h2>
                    Type of geometry, currently only one supported. In future we will add stuff like planes, spheres, etc.
                
                    **Default**: `'mesh'`
                
                    **Options:** `['mesh', 'plane', 'ground', 'mesh_sequence', 'mesh_array']`








                ??? json-spec "`/geometry/*/extract` (`string`)"
                    ```
                    /geometry/*/extract
                    ```
                    <h2>Description</h2>
                    Used to extract stuff from the mesh. Eg extract surface extracts the surface from a tet mesh.
                
                    **Default**: `'volume'`
                
                    **Options:** `['volume', 'edges', 'points', 'surface']`








                ??? json-spec "`/geometry/*/unit` (`string`)"
                    ```
                    /geometry/*/unit
                    ```
                    <h2>Description</h2>
                    Units of the geometric model.
                
                    **Default**: `''`








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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/E`"
                    ```
                    /materials/*/E
                    ```


                    === "`/materials/*/E` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/E` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/E` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/E/value`"
                            ```
                            /materials/*/E/value
                            ```


                            === "`/materials/*/E/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/E/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/E/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/E/unit` (`string`)"
                            ```
                            /materials/*/E/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/nu`"
                    ```
                    /materials/*/nu
                    ```


                    === "`/materials/*/nu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/nu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/nu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/nu/value`"
                            ```
                            /materials/*/nu/value
                            ```


                            === "`/materials/*/nu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/nu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/nu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/nu/unit` (`string`)"
                            ```
                            /materials/*/nu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/phi`"
                    ```
                    /materials/*/phi
                    ```


                    === "`/materials/*/phi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/phi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/phi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/phi/value`"
                            ```
                            /materials/*/phi/value
                            ```


                            === "`/materials/*/phi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/phi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/phi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/phi/unit` (`string`)"
                            ```
                            /materials/*/phi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/psi`"
                    ```
                    /materials/*/psi
                    ```


                    === "`/materials/*/psi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/psi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/psi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/psi/value`"
                            ```
                            /materials/*/psi/value
                            ```


                            === "`/materials/*/psi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/psi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/psi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/psi/unit` (`string`)"
                            ```
                            /materials/*/psi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/lambda`"
                    ```
                    /materials/*/lambda
                    ```


                    === "`/materials/*/lambda` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/lambda` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/lambda` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/lambda/value`"
                            ```
                            /materials/*/lambda/value
                            ```


                            === "`/materials/*/lambda/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/lambda/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/lambda/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/lambda/unit` (`string`)"
                            ```
                            /materials/*/lambda/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/mu`"
                    ```
                    /materials/*/mu
                    ```


                    === "`/materials/*/mu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/mu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/mu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/mu/value`"
                            ```
                            /materials/*/mu/value
                            ```


                            === "`/materials/*/mu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/mu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/mu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/mu/unit` (`string`)"
                            ```
                            /materials/*/mu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/phi`"
                    ```
                    /materials/*/phi
                    ```


                    === "`/materials/*/phi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/phi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/phi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/phi/value`"
                            ```
                            /materials/*/phi/value
                            ```


                            === "`/materials/*/phi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/phi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/phi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/phi/unit` (`string`)"
                            ```
                            /materials/*/phi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/psi`"
                    ```
                    /materials/*/psi
                    ```


                    === "`/materials/*/psi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/psi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/psi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/psi/value`"
                            ```
                            /materials/*/psi/value
                            ```


                            === "`/materials/*/psi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/psi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/psi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/psi/unit` (`string`)"
                            ```
                            /materials/*/psi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









            === "MooneyRivlin"
            
                **Type**: MooneyRivlin
                <h2>Description</h2>
                Material Parameters including ID, for Mooney-Rivlin
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/c1`"
                    ```
                    /materials/*/c1
                    ```


                    === "`/materials/*/c1` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/c1` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/c1` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/c1/value`"
                            ```
                            /materials/*/c1/value
                            ```


                            === "`/materials/*/c1/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/c1/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/c1/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/c1/unit` (`string`)"
                            ```
                            /materials/*/c1/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/c2`"
                    ```
                    /materials/*/c2
                    ```


                    === "`/materials/*/c2` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/c2` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/c2` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/c2/value`"
                            ```
                            /materials/*/c2/value
                            ```


                            === "`/materials/*/c2/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/c2/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/c2/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/c2/unit` (`string`)"
                            ```
                            /materials/*/c2/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/k`"
                    ```
                    /materials/*/k
                    ```


                    === "`/materials/*/k` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/k` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/k` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/k/value`"
                            ```
                            /materials/*/k/value
                            ```


                            === "`/materials/*/k/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/k/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/k/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/k/unit` (`string`)"
                            ```
                            /materials/*/k/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









            === "MooneyRivlin3Param"
            
                **Type**: MooneyRivlin3Param
                <h2>Description</h2>
                Material Parameters including ID, for Mooney-Rivlin
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/c1`"
                    ```
                    /materials/*/c1
                    ```


                    === "`/materials/*/c1` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/c1` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/c1` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/c1/value`"
                            ```
                            /materials/*/c1/value
                            ```


                            === "`/materials/*/c1/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/c1/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/c1/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/c1/unit` (`string`)"
                            ```
                            /materials/*/c1/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/c2`"
                    ```
                    /materials/*/c2
                    ```


                    === "`/materials/*/c2` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/c2` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/c2` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/c2/value`"
                            ```
                            /materials/*/c2/value
                            ```


                            === "`/materials/*/c2/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/c2/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/c2/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/c2/unit` (`string`)"
                            ```
                            /materials/*/c2/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/c3`"
                    ```
                    /materials/*/c3
                    ```


                    === "`/materials/*/c3` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/c3` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/c3` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/c3/value`"
                            ```
                            /materials/*/c3/value
                            ```


                            === "`/materials/*/c3/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/c3/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/c3/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/c3/unit` (`string`)"
                            ```
                            /materials/*/c3/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/d1`"
                    ```
                    /materials/*/d1
                    ```


                    === "`/materials/*/d1` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/d1` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/d1` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/d1/value`"
                            ```
                            /materials/*/d1/value
                            ```


                            === "`/materials/*/d1/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/d1/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/d1/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/d1/unit` (`string`)"
                            ```
                            /materials/*/d1/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









            === "MooneyRivlin3ParamSymbolic"
            
                **Type**: MooneyRivlin3ParamSymbolic
                <h2>Description</h2>
                Material Parameters including ID, for Mooney-Rivlin
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/c1`"
                    ```
                    /materials/*/c1
                    ```


                    === "`/materials/*/c1` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/c1` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/c1` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/c1/value`"
                            ```
                            /materials/*/c1/value
                            ```


                            === "`/materials/*/c1/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/c1/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/c1/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/c1/unit` (`string`)"
                            ```
                            /materials/*/c1/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/c2`"
                    ```
                    /materials/*/c2
                    ```


                    === "`/materials/*/c2` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/c2` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/c2` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/c2/value`"
                            ```
                            /materials/*/c2/value
                            ```


                            === "`/materials/*/c2/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/c2/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/c2/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/c2/unit` (`string`)"
                            ```
                            /materials/*/c2/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/c3`"
                    ```
                    /materials/*/c3
                    ```


                    === "`/materials/*/c3` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/c3` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/c3` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/c3/value`"
                            ```
                            /materials/*/c3/value
                            ```


                            === "`/materials/*/c3/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/c3/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/c3/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/c3/unit` (`string`)"
                            ```
                            /materials/*/c3/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/d1`"
                    ```
                    /materials/*/d1
                    ```


                    === "`/materials/*/d1` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/d1` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/d1` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/d1/value`"
                            ```
                            /materials/*/d1/value
                            ```


                            === "`/materials/*/d1/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/d1/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/d1/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/d1/unit` (`string`)"
                            ```
                            /materials/*/d1/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









            === "UnconstrainedOgden"
            
                **Type**: UnconstrainedOgden
                <h2>Description</h2>
                Material Parameters including ID, for [Ogden](https://en.wikipedia.org/wiki/Ogden_hyperelastic_model).
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/alphas`"
                    ```
                    /materials/*/alphas
                    ```


                    === "`/materials/*/alphas` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/alphas` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/alphas` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/alphas/value`"
                            ```
                            /materials/*/alphas/value
                            ```


                            === "`/materials/*/alphas/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/alphas/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/alphas/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/alphas/unit` (`string`)"
                            ```
                            /materials/*/alphas/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value











                ??? json-spec "`/materials/*/mus` (`list`)"
                    ```
                    /materials/*/mus
                    ```
                    <h2>Description</h2>
                    Ogden mu



                    ??? json-spec "`/materials/*/mus/*`"
                        ```
                        /materials/*/mus/*
                        ```


                        === "`/materials/*/mus/*` (`float`)"
                            <h2>Description</h2>
                            Value as a constant float



                        === "`/materials/*/mus/*` (`string`)"
                            <h2>Description</h2>
                            Value as an expression of $x,y,z,t$ or a file



                        === "`/materials/*/mus/*` (`object`)"
                            <h2>Description</h2>
                            Value with unit
                            <h2>Required</h2>



                            ??? json-spec "`/materials/*/mus/*/value`"
                                ```
                                /materials/*/mus/*/value
                                ```


                                === "`/materials/*/mus/*/value` (`float`)"
                                    <h2>Description</h2>
                                    The value of the constant



                                === "`/materials/*/mus/*/value` (`string`)"
                                    <h2>Description</h2>
                                    The value as an expression



                                === "`/materials/*/mus/*/value` (`file`)"
                                    <h2>Description</h2>
                                    The value as a file








                            ??? json-spec "`/materials/*/mus/*/unit` (`string`)"
                                ```
                                /materials/*/mus/*/unit
                                ```
                                <h2>Description</h2>
                                The unit of the Value














                ??? json-spec "`/materials/*/Ds` (`list`)"
                    ```
                    /materials/*/Ds
                    ```
                    <h2>Description</h2>
                    Ogden D



                    ??? json-spec "`/materials/*/Ds/*`"
                        ```
                        /materials/*/Ds/*
                        ```


                        === "`/materials/*/Ds/*` (`float`)"
                            <h2>Description</h2>
                            Value as a constant float



                        === "`/materials/*/Ds/*` (`string`)"
                            <h2>Description</h2>
                            Value as an expression of $x,y,z,t$ or a file



                        === "`/materials/*/Ds/*` (`object`)"
                            <h2>Description</h2>
                            Value with unit
                            <h2>Required</h2>



                            ??? json-spec "`/materials/*/Ds/*/value`"
                                ```
                                /materials/*/Ds/*/value
                                ```


                                === "`/materials/*/Ds/*/value` (`float`)"
                                    <h2>Description</h2>
                                    The value of the constant



                                === "`/materials/*/Ds/*/value` (`string`)"
                                    <h2>Description</h2>
                                    The value as an expression



                                === "`/materials/*/Ds/*/value` (`file`)"
                                    <h2>Description</h2>
                                    The value as a file








                            ??? json-spec "`/materials/*/Ds/*/unit` (`string`)"
                                ```
                                /materials/*/Ds/*/unit
                                ```
                                <h2>Description</h2>
                                The unit of the Value









                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









            === "IncompressibleOgden"
            
                **Type**: IncompressibleOgden
                <h2>Description</h2>
                Material Parameters including ID, for [Ogden](https://en.wikipedia.org/wiki/Ogden_hyperelastic_model).
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/c`"
                    ```
                    /materials/*/c
                    ```


                    === "`/materials/*/c` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/c` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/c` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/c/value`"
                            ```
                            /materials/*/c/value
                            ```


                            === "`/materials/*/c/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/c/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/c/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/c/unit` (`string`)"
                            ```
                            /materials/*/c/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                    === "`/materials/*/c` (`list`)"
                        <h2>Description</h2>
                        Coefficient(s) of Incompressible Ogden



                        ??? json-spec "`/materials/*/c/*`"
                            ```
                            /materials/*/c/*
                            ```


                            === "`/materials/*/c/*` (`float`)"
                                <h2>Description</h2>
                                Value as a constant float



                            === "`/materials/*/c/*` (`string`)"
                                <h2>Description</h2>
                                Value as an expression of $x,y,z,t$ or a file



                            === "`/materials/*/c/*` (`object`)"
                                <h2>Description</h2>
                                Value with unit
                                <h2>Required</h2>



                                ??? json-spec "`/materials/*/c/*/value`"
                                    ```
                                    /materials/*/c/*/value
                                    ```


                                    === "`/materials/*/c/*/value` (`float`)"
                                        <h2>Description</h2>
                                        The value of the constant



                                    === "`/materials/*/c/*/value` (`string`)"
                                        <h2>Description</h2>
                                        The value as an expression



                                    === "`/materials/*/c/*/value` (`file`)"
                                        <h2>Description</h2>
                                        The value as a file








                                ??? json-spec "`/materials/*/c/*/unit` (`string`)"
                                    ```
                                    /materials/*/c/*/unit
                                    ```
                                    <h2>Description</h2>
                                    The unit of the Value












                ??? json-spec "`/materials/*/m`"
                    ```
                    /materials/*/m
                    ```


                    === "`/materials/*/m` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/m` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/m` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/m/value`"
                            ```
                            /materials/*/m/value
                            ```


                            === "`/materials/*/m/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/m/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/m/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/m/unit` (`string`)"
                            ```
                            /materials/*/m/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                    === "`/materials/*/m` (`list`)"
                        <h2>Description</h2>
                        Exponent(s) of Incompressible Ogden



                        ??? json-spec "`/materials/*/m/*`"
                            ```
                            /materials/*/m/*
                            ```


                            === "`/materials/*/m/*` (`float`)"
                                <h2>Description</h2>
                                Value as a constant float



                            === "`/materials/*/m/*` (`string`)"
                                <h2>Description</h2>
                                Value as an expression of $x,y,z,t$ or a file



                            === "`/materials/*/m/*` (`object`)"
                                <h2>Description</h2>
                                Value with unit
                                <h2>Required</h2>



                                ??? json-spec "`/materials/*/m/*/value`"
                                    ```
                                    /materials/*/m/*/value
                                    ```


                                    === "`/materials/*/m/*/value` (`float`)"
                                        <h2>Description</h2>
                                        The value of the constant



                                    === "`/materials/*/m/*/value` (`string`)"
                                        <h2>Description</h2>
                                        The value as an expression



                                    === "`/materials/*/m/*/value` (`file`)"
                                        <h2>Description</h2>
                                        The value as a file








                                ??? json-spec "`/materials/*/m/*/unit` (`string`)"
                                    ```
                                    /materials/*/m/*/unit
                                    ```
                                    <h2>Description</h2>
                                    The unit of the Value












                ??? json-spec "`/materials/*/k`"
                    ```
                    /materials/*/k
                    ```


                    === "`/materials/*/k` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/k` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/k` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/k/value`"
                            ```
                            /materials/*/k/value
                            ```


                            === "`/materials/*/k/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/k/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/k/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/k/unit` (`string`)"
                            ```
                            /materials/*/k/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/E`"
                    ```
                    /materials/*/E
                    ```


                    === "`/materials/*/E` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/E` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/E` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/E/value`"
                            ```
                            /materials/*/E/value
                            ```


                            === "`/materials/*/E/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/E/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/E/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/E/unit` (`string`)"
                            ```
                            /materials/*/E/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/nu`"
                    ```
                    /materials/*/nu
                    ```


                    === "`/materials/*/nu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/nu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/nu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/nu/value`"
                            ```
                            /materials/*/nu/value
                            ```


                            === "`/materials/*/nu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/nu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/nu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/nu/unit` (`string`)"
                            ```
                            /materials/*/nu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/phi`"
                    ```
                    /materials/*/phi
                    ```


                    === "`/materials/*/phi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/phi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/phi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/phi/value`"
                            ```
                            /materials/*/phi/value
                            ```


                            === "`/materials/*/phi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/phi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/phi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/phi/unit` (`string`)"
                            ```
                            /materials/*/phi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/psi`"
                    ```
                    /materials/*/psi
                    ```


                    === "`/materials/*/psi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/psi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/psi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/psi/value`"
                            ```
                            /materials/*/psi/value
                            ```


                            === "`/materials/*/psi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/psi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/psi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/psi/unit` (`string`)"
                            ```
                            /materials/*/psi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/lambda`"
                    ```
                    /materials/*/lambda
                    ```


                    === "`/materials/*/lambda` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/lambda` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/lambda` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/lambda/value`"
                            ```
                            /materials/*/lambda/value
                            ```


                            === "`/materials/*/lambda/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/lambda/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/lambda/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/lambda/unit` (`string`)"
                            ```
                            /materials/*/lambda/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/mu`"
                    ```
                    /materials/*/mu
                    ```


                    === "`/materials/*/mu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/mu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/mu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/mu/value`"
                            ```
                            /materials/*/mu/value
                            ```


                            === "`/materials/*/mu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/mu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/mu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/mu/unit` (`string`)"
                            ```
                            /materials/*/mu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/E`"
                    ```
                    /materials/*/E
                    ```


                    === "`/materials/*/E` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/E` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/E` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/E/value`"
                            ```
                            /materials/*/E/value
                            ```


                            === "`/materials/*/E/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/E/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/E/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/E/unit` (`string`)"
                            ```
                            /materials/*/E/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/nu`"
                    ```
                    /materials/*/nu
                    ```


                    === "`/materials/*/nu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/nu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/nu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/nu/value`"
                            ```
                            /materials/*/nu/value
                            ```


                            === "`/materials/*/nu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/nu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/nu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/nu/unit` (`string`)"
                            ```
                            /materials/*/nu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`








                ??? json-spec "`/materials/*/elasticity_tensor` (`list`)"
                    ```
                    /materials/*/elasticity_tensor
                    ```
                    <h2>Description</h2>
                    Symmetric elasticity tensor



                    ??? json-spec "`/materials/*/elasticity_tensor/*`"
                        ```
                        /materials/*/elasticity_tensor/*
                        ```


                        === "`/materials/*/elasticity_tensor/*` (`float`)"
                            <h2>Description</h2>
                            Value as a constant float
                        
                            **Default**: `0`



                        === "`/materials/*/elasticity_tensor/*` (`string`)"
                            <h2>Description</h2>
                            Value as an expression of $x,y,z,t$ or a file



                        === "`/materials/*/elasticity_tensor/*` (`object`)"
                            <h2>Description</h2>
                            Value with unit
                            <h2>Required</h2>



                            ??? json-spec "`/materials/*/elasticity_tensor/*/value`"
                                ```
                                /materials/*/elasticity_tensor/*/value
                                ```


                                === "`/materials/*/elasticity_tensor/*/value` (`float`)"
                                    <h2>Description</h2>
                                    The value of the constant



                                === "`/materials/*/elasticity_tensor/*/value` (`string`)"
                                    <h2>Description</h2>
                                    The value as an expression



                                === "`/materials/*/elasticity_tensor/*/value` (`file`)"
                                    <h2>Description</h2>
                                    The value as a file








                            ??? json-spec "`/materials/*/elasticity_tensor/*/unit` (`string`)"
                                ```
                                /materials/*/elasticity_tensor/*/unit
                                ```
                                <h2>Description</h2>
                                The unit of the Value









                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/E`"
                    ```
                    /materials/*/E
                    ```


                    === "`/materials/*/E` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/E` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/E` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/E/value`"
                            ```
                            /materials/*/E/value
                            ```


                            === "`/materials/*/E/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/E/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/E/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/E/unit` (`string`)"
                            ```
                            /materials/*/E/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/nu`"
                    ```
                    /materials/*/nu
                    ```


                    === "`/materials/*/nu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/nu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/nu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/nu/value`"
                            ```
                            /materials/*/nu/value
                            ```


                            === "`/materials/*/nu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/nu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/nu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/nu/unit` (`string`)"
                            ```
                            /materials/*/nu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/phi`"
                    ```
                    /materials/*/phi
                    ```


                    === "`/materials/*/phi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/phi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/phi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/phi/value`"
                            ```
                            /materials/*/phi/value
                            ```


                            === "`/materials/*/phi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/phi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/phi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/phi/unit` (`string`)"
                            ```
                            /materials/*/phi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/psi`"
                    ```
                    /materials/*/psi
                    ```


                    === "`/materials/*/psi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/psi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/psi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/psi/value`"
                            ```
                            /materials/*/psi/value
                            ```


                            === "`/materials/*/psi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/psi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/psi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/psi/unit` (`string`)"
                            ```
                            /materials/*/psi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`








                ??? json-spec "`/materials/*/elasticity_tensor` (`list`)"
                    ```
                    /materials/*/elasticity_tensor
                    ```
                    <h2>Description</h2>
                    Symmetric elasticity tensor



                    ??? json-spec "`/materials/*/elasticity_tensor/*`"
                        ```
                        /materials/*/elasticity_tensor/*
                        ```


                        === "`/materials/*/elasticity_tensor/*` (`float`)"
                            <h2>Description</h2>
                            Value as a constant float
                        
                            **Default**: `0`



                        === "`/materials/*/elasticity_tensor/*` (`string`)"
                            <h2>Description</h2>
                            Value as an expression of $x,y,z,t$ or a file



                        === "`/materials/*/elasticity_tensor/*` (`object`)"
                            <h2>Description</h2>
                            Value with unit
                            <h2>Required</h2>



                            ??? json-spec "`/materials/*/elasticity_tensor/*/value`"
                                ```
                                /materials/*/elasticity_tensor/*/value
                                ```


                                === "`/materials/*/elasticity_tensor/*/value` (`float`)"
                                    <h2>Description</h2>
                                    The value of the constant



                                === "`/materials/*/elasticity_tensor/*/value` (`string`)"
                                    <h2>Description</h2>
                                    The value as an expression



                                === "`/materials/*/elasticity_tensor/*/value` (`file`)"
                                    <h2>Description</h2>
                                    The value as a file








                            ??? json-spec "`/materials/*/elasticity_tensor/*/unit` (`string`)"
                                ```
                                /materials/*/elasticity_tensor/*/unit
                                ```
                                <h2>Description</h2>
                                The unit of the Value









                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/phi`"
                    ```
                    /materials/*/phi
                    ```


                    === "`/materials/*/phi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/phi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/phi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/phi/value`"
                            ```
                            /materials/*/phi/value
                            ```


                            === "`/materials/*/phi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/phi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/phi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/phi/unit` (`string`)"
                            ```
                            /materials/*/phi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/psi`"
                    ```
                    /materials/*/psi
                    ```


                    === "`/materials/*/psi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/psi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/psi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/psi/value`"
                            ```
                            /materials/*/psi/value
                            ```


                            === "`/materials/*/psi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/psi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/psi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/psi/unit` (`string`)"
                            ```
                            /materials/*/psi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/viscosity`"
                    ```
                    /materials/*/viscosity
                    ```


                    === "`/materials/*/viscosity` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/viscosity` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/viscosity` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/viscosity/value`"
                            ```
                            /materials/*/viscosity/value
                            ```


                            === "`/materials/*/viscosity/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/viscosity/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/viscosity/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/viscosity/unit` (`string`)"
                            ```
                            /materials/*/viscosity/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/viscosity`"
                    ```
                    /materials/*/viscosity
                    ```


                    === "`/materials/*/viscosity` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/viscosity` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/viscosity` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/viscosity/value`"
                            ```
                            /materials/*/viscosity/value
                            ```


                            === "`/materials/*/viscosity/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/viscosity/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/viscosity/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/viscosity/unit` (`string`)"
                            ```
                            /materials/*/viscosity/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









            === "OperatorSplitting"
            
                **Type**: OperatorSplitting
                <h2>Description</h2>
                Material Parameters including ID, viscosity, density ($\rho$)
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/viscosity`"
                    ```
                    /materials/*/viscosity
                    ```


                    === "`/materials/*/viscosity` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/viscosity` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/viscosity` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/viscosity/value`"
                            ```
                            /materials/*/viscosity/value
                            ```


                            === "`/materials/*/viscosity/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/viscosity/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/viscosity/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/viscosity/unit` (`string`)"
                            ```
                            /materials/*/viscosity/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/E`"
                    ```
                    /materials/*/E
                    ```


                    === "`/materials/*/E` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/E` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/E` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/E/value`"
                            ```
                            /materials/*/E/value
                            ```


                            === "`/materials/*/E/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/E/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/E/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/E/unit` (`string`)"
                            ```
                            /materials/*/E/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/nu`"
                    ```
                    /materials/*/nu
                    ```


                    === "`/materials/*/nu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/nu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/nu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/nu/value`"
                            ```
                            /materials/*/nu/value
                            ```


                            === "`/materials/*/nu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/nu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/nu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/nu/unit` (`string`)"
                            ```
                            /materials/*/nu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/lambda`"
                    ```
                    /materials/*/lambda
                    ```


                    === "`/materials/*/lambda` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/lambda` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/lambda` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/lambda/value`"
                            ```
                            /materials/*/lambda/value
                            ```


                            === "`/materials/*/lambda/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/lambda/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/lambda/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/lambda/unit` (`string`)"
                            ```
                            /materials/*/lambda/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/mu`"
                    ```
                    /materials/*/mu
                    ```


                    === "`/materials/*/mu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/mu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/mu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/mu/value`"
                            ```
                            /materials/*/mu/value
                            ```


                            === "`/materials/*/mu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/mu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/mu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/mu/unit` (`string`)"
                            ```
                            /materials/*/mu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`



                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/k`"
                    ```
                    /materials/*/k
                    ```


                    === "`/materials/*/k` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/k` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/k` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/k/value`"
                            ```
                            /materials/*/k/value
                            ```


                            === "`/materials/*/k/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/k/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/k/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/k/unit` (`string`)"
                            ```
                            /materials/*/k/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









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
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`



                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









            === "AMIPS"
            
                **Type**: AMIPS
                <h2>Description</h2>
                Material Parameters including ID
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`



                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









            === "FixedCorotational"
            
                **Type**: FixedCorotational
                <h2>Description</h2>
                Material Parameters including ID
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/E`"
                    ```
                    /materials/*/E
                    ```


                    === "`/materials/*/E` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/E` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/E` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/E/value`"
                            ```
                            /materials/*/E/value
                            ```


                            === "`/materials/*/E/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/E/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/E/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/E/unit` (`string`)"
                            ```
                            /materials/*/E/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/nu`"
                    ```
                    /materials/*/nu
                    ```


                    === "`/materials/*/nu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/nu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/nu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/nu/value`"
                            ```
                            /materials/*/nu/value
                            ```


                            === "`/materials/*/nu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/nu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/nu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/nu/unit` (`string`)"
                            ```
                            /materials/*/nu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/phi`"
                    ```
                    /materials/*/phi
                    ```


                    === "`/materials/*/phi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/phi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/phi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/phi/value`"
                            ```
                            /materials/*/phi/value
                            ```


                            === "`/materials/*/phi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/phi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/phi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/phi/unit` (`string`)"
                            ```
                            /materials/*/phi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/psi`"
                    ```
                    /materials/*/psi
                    ```


                    === "`/materials/*/psi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/psi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/psi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/psi/value`"
                            ```
                            /materials/*/psi/value
                            ```


                            === "`/materials/*/psi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/psi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/psi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/psi/unit` (`string`)"
                            ```
                            /materials/*/psi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









            === "FixedCorotational"
            
                **Type**: FixedCorotational
                <h2>Description</h2>
                Material Parameters including ID
                <h2>Required</h2>





                ??? json-spec "`/materials/*/type` (`string`)"
                    ```
                    /materials/*/type
                    ```
                    <h2>Description</h2>
                    Type of material
                
                    **Options:** `['LinearElasticity', 'HookeLinearElasticity', 'SaintVenant', 'NeoHookean', 'MooneyRivlin', 'MooneyRivlin3Param', 'MooneyRivlin3ParamSymbolic', 'UnconstrainedOgden', 'IncompressibleOgden', 'Stokes', 'NavierStokes', 'OperatorSplitting', 'IncompressibleLinearElasticity', 'Laplacian', 'Helmholtz', 'Bilaplacian', 'AMIPS', 'FixedCorotational']`






                ??? json-spec "`/materials/*/lambda`"
                    ```
                    /materials/*/lambda
                    ```


                    === "`/materials/*/lambda` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/lambda` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/lambda` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/lambda/value`"
                            ```
                            /materials/*/lambda/value
                            ```


                            === "`/materials/*/lambda/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/lambda/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/lambda/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/lambda/unit` (`string`)"
                            ```
                            /materials/*/lambda/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/mu`"
                    ```
                    /materials/*/mu
                    ```


                    === "`/materials/*/mu` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/materials/*/mu` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/mu` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/mu/value`"
                            ```
                            /materials/*/mu/value
                            ```


                            === "`/materials/*/mu/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/mu/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/mu/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/mu/unit` (`string`)"
                            ```
                            /materials/*/mu/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/materials/*/id`"
                    ```
                    /materials/*/id
                    ```


                    === "`/materials/*/id` (`int`)"
                        <h2>Description</h2>
                        Volume selection ID
                    
                        **Default**: `0`



                    === "`/materials/*/id` (`list`)"
                        <h2>Description</h2>
                        Volume selection IDs





                        ??? json-spec "`/materials/*/id/*` (`int`)"
                            ```
                            /materials/*/id/*
                            ```
                            <h2>Description</h2>
                            Volume selection ID









                ??? json-spec "`/materials/*/rho`"
                    ```
                    /materials/*/rho
                    ```


                    === "`/materials/*/rho` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `1`



                    === "`/materials/*/rho` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/rho` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/rho/value`"
                            ```
                            /materials/*/rho/value
                            ```


                            === "`/materials/*/rho/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/rho/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/rho/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/rho/unit` (`string`)"
                            ```
                            /materials/*/rho/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/phi`"
                    ```
                    /materials/*/phi
                    ```


                    === "`/materials/*/phi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/phi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/phi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/phi/value`"
                            ```
                            /materials/*/phi/value
                            ```


                            === "`/materials/*/phi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/phi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/phi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/phi/unit` (`string`)"
                            ```
                            /materials/*/phi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value









                ??? json-spec "`/materials/*/psi`"
                    ```
                    /materials/*/psi
                    ```


                    === "`/materials/*/psi` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/materials/*/psi` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/materials/*/psi` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/materials/*/psi/value`"
                            ```
                            /materials/*/psi/value
                            ```


                            === "`/materials/*/psi/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/materials/*/psi/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/materials/*/psi/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/materials/*/psi/unit` (`string`)"
                            ```
                            /materials/*/psi/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value












    <h2>Optional</h2>





    ??? json-spec "`/units` (`object`)"
        ```
        /units
        ```
        <h2>Description</h2>
        Basic units used in the code.
    
        **Default**: `None`
        <h2>Optional</h2>





        ??? json-spec "`/units/length` (`string`)"
            ```
            /units/length
            ```
            <h2>Description</h2>
            Length unit.
        
            **Default**: `'m'`








        ??? json-spec "`/units/mass` (`string`)"
            ```
            /units/mass
            ```
            <h2>Description</h2>
            Mass unit.
        
            **Default**: `'kg'`








        ??? json-spec "`/units/time` (`string`)"
            ```
            /units/time
            ```
            <h2>Description</h2>
            Time unit.
        
            **Default**: `'s'`








        ??? json-spec "`/units/characteristic_length` (`float`)"
            ```
            /units/characteristic_length
            ```
            <h2>Description</h2>
            Characteristic length, used for tolerances.
        
            **Default**: `1`









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










            ??? json-spec "`/preset_problem/viscosity` (`float`)"
                ```
                /preset_problem/viscosity
                ```
                <h2>Description</h2>
                TODO
            
                **Default**: `1`






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





            ??? json-spec "`/preset_problem/viscosity` (`float`)"
                ```
                /preset_problem/viscosity
                ```
                <h2>Description</h2>
                TODO
            
                **Default**: `1`






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








            ??? json-spec "`/preset_problem/viscosity` (`float`)"
                ```
                /preset_problem/viscosity
                ```
                <h2>Description</h2>
                TODO
            
                **Default**: `1`






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





            ??? json-spec "`/preset_problem/viscosity` (`float`)"
                ```
                /preset_problem/viscosity
                ```
                <h2>Description</h2>
                TODO
            
                **Default**: `1`






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
        Path for all relative paths, set automatically to the folder containing this JSON.
    
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








        ??? json-spec "`/space/basis_type` (`string`)"
            ```
            /space/basis_type
            ```
            <h2>Description</h2>
            Type of basis to use for non polygonal element, one of Lagrange, Spline, or Serendipity. Spline or Serendipity work only for quad/hex meshes
        
            **Default**: `'Lagrange'`
        
            **Options:** `['Lagrange', 'Spline', 'Serendipity']`








        ??? json-spec "`/space/poly_basis_type` (`string`)"
            ```
            /space/poly_basis_type
            ```
            <h2>Description</h2>
            Type of basis to use for a polygonal element, one of MFSHarmonic, MeanValue, or Wachspress see 'PolySpline..' paper for details.
        
            **Default**: `'MFSHarmonic'`
        
            **Options:** `['MFSHarmonic', 'MeanValue', 'Wachspress']`








        ??? json-spec "`/space/use_p_ref` (`bool`)"
            ```
            /space/use_p_ref
            ```
            <h2>Description</h2>
            Perform a priori p-refinement based on element shape, as described in 'Decoupling..' paper.
        
            **Default**: `False`








        ??? json-spec "`/space/remesh` (`object`)"
            ```
            /space/remesh
            ```
            <h2>Description</h2>
            Settings for adaptive remeshing
        
            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/space/remesh/enabled` (`bool`)"
                ```
                /space/remesh/enabled
                ```
                <h2>Description</h2>
                Whether to do adaptive remeshing
            
                **Default**: `False`








            ??? json-spec "`/space/remesh/split` (`object`)"
                ```
                /space/remesh/split
                ```
                <h2>Description</h2>
                Settings for adaptive remeshing edge splitting operations
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/space/remesh/split/enabled` (`bool`)"
                    ```
                    /space/remesh/split/enabled
                    ```
                    <h2>Description</h2>
                    Whether to do edge splitting in adaptive remeshing
                
                    **Default**: `True`








                ??? json-spec "`/space/remesh/split/acceptance_tolerance` (`float`)"
                    ```
                    /space/remesh/split/acceptance_tolerance
                    ```
                    <h2>Description</h2>
                    Accept split operation if energy decreased by at least x
                
                    **Default**: `0.001`
                
                    **Range:** `[0, inf]`








                ??? json-spec "`/space/remesh/split/culling_threshold` (`float`)"
                    ```
                    /space/remesh/split/culling_threshold
                    ```
                    <h2>Description</h2>
                    Split operation culling threshold on energy
                
                    **Default**: `0.95`
                
                    **Range:** `[0, 1]`








                ??? json-spec "`/space/remesh/split/max_depth` (`int`)"
                    ```
                    /space/remesh/split/max_depth
                    ```
                    <h2>Description</h2>
                    Maximum depth split per time-step
                
                    **Default**: `3`
                
                    **Range:** `[1, inf]`








                ??? json-spec "`/space/remesh/split/min_edge_length` (`float`)"
                    ```
                    /space/remesh/split/min_edge_length
                    ```
                    <h2>Description</h2>
                    Minimum edge length to split
                
                    **Default**: `1e-06`
                
                    **Range:** `[0, inf]`











            ??? json-spec "`/space/remesh/collapse` (`object`)"
                ```
                /space/remesh/collapse
                ```
                <h2>Description</h2>
                Settings for adaptive remeshing edge collapse operations
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/space/remesh/collapse/enabled` (`bool`)"
                    ```
                    /space/remesh/collapse/enabled
                    ```
                    <h2>Description</h2>
                    Whether to do edge collapse in adaptive remeshing
                
                    **Default**: `True`








                ??? json-spec "`/space/remesh/collapse/acceptance_tolerance` (`float`)"
                    ```
                    /space/remesh/collapse/acceptance_tolerance
                    ```
                    <h2>Description</h2>
                    Accept collapse operation if energy decreased by at least x
                
                    **Default**: `-1e-08`
                
                    **Range:** `[-inf, 0]`








                ??? json-spec "`/space/remesh/collapse/culling_threshold` (`float`)"
                    ```
                    /space/remesh/collapse/culling_threshold
                    ```
                    <h2>Description</h2>
                    Collapse operation culling threshold on energy
                
                    **Default**: `0.01`
                
                    **Range:** `[0, 1]`








                ??? json-spec "`/space/remesh/collapse/max_depth` (`int`)"
                    ```
                    /space/remesh/collapse/max_depth
                    ```
                    <h2>Description</h2>
                    Maximum depth collapse per time-step
                
                    **Default**: `3`
                
                    **Range:** `[1, inf]`








                ??? json-spec "`/space/remesh/collapse/rel_max_edge_length` (`float`)"
                    ```
                    /space/remesh/collapse/rel_max_edge_length
                    ```
                    <h2>Description</h2>
                    Length of maximum edge length to collapse relative to initial minimum edge length
                
                    **Default**: `1`
                
                    **Range:** `[0, inf]`








                ??? json-spec "`/space/remesh/collapse/abs_max_edge_length` (`float`)"
                    ```
                    /space/remesh/collapse/abs_max_edge_length
                    ```
                    <h2>Description</h2>
                    Length of maximum edge length to collapse in absolute units of distance
                
                    **Default**: `1e+100`
                
                    **Range:** `[0, inf]`











            ??? json-spec "`/space/remesh/swap` (`object`)"
                ```
                /space/remesh/swap
                ```
                <h2>Description</h2>
                Settings for adaptive remeshing edge/face swap operations
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/space/remesh/swap/enabled` (`bool`)"
                    ```
                    /space/remesh/swap/enabled
                    ```
                    <h2>Description</h2>
                    Whether to do edge/face swap in adaptive remeshing
                
                    **Default**: `False`








                ??? json-spec "`/space/remesh/swap/acceptance_tolerance` (`float`)"
                    ```
                    /space/remesh/swap/acceptance_tolerance
                    ```
                    <h2>Description</h2>
                    Accept swap operation if energy decreased by at least x
                
                    **Default**: `-1e-08`
                
                    **Range:** `[-inf, 0]`








                ??? json-spec "`/space/remesh/swap/max_depth` (`int`)"
                    ```
                    /space/remesh/swap/max_depth
                    ```
                    <h2>Description</h2>
                    Maximum depth swap per time-step
                
                    **Default**: `3`
                
                    **Range:** `[1, inf]`











            ??? json-spec "`/space/remesh/smooth` (`object`)"
                ```
                /space/remesh/smooth
                ```
                <h2>Description</h2>
                Settings for adaptive remeshing vertex smoothing operations
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/space/remesh/smooth/enabled` (`bool`)"
                    ```
                    /space/remesh/smooth/enabled
                    ```
                    <h2>Description</h2>
                    Whether to do vertex smoothing in adaptive remeshing
                
                    **Default**: `False`








                ??? json-spec "`/space/remesh/smooth/acceptance_tolerance` (`float`)"
                    ```
                    /space/remesh/smooth/acceptance_tolerance
                    ```
                    <h2>Description</h2>
                    Accept smooth operation if energy decreased by at least x
                
                    **Default**: `-1e-08`
                
                    **Range:** `[-inf, 0]`








                ??? json-spec "`/space/remesh/smooth/max_iters` (`int`)"
                    ```
                    /space/remesh/smooth/max_iters
                    ```
                    <h2>Description</h2>
                    Maximum number of smoothing iterations per time-step
                
                    **Default**: `1`
                
                    **Range:** `[1, inf]`











            ??? json-spec "`/space/remesh/local_relaxation` (`object`)"
                ```
                /space/remesh/local_relaxation
                ```
                <h2>Description</h2>
                Settings for adaptive remeshing local relaxation
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/space/remesh/local_relaxation/local_mesh_n_ring` (`int`)"
                    ```
                    /space/remesh/local_relaxation/local_mesh_n_ring
                    ```
                    <h2>Description</h2>
                    Size of n-ring for local relaxation
                
                    **Default**: `2`








                ??? json-spec "`/space/remesh/local_relaxation/local_mesh_rel_area` (`float`)"
                    ```
                    /space/remesh/local_relaxation/local_mesh_rel_area
                    ```
                    <h2>Description</h2>
                    Minimum area for local relaxation
                
                    **Default**: `0.01`








                ??? json-spec "`/space/remesh/local_relaxation/max_nl_iterations` (`int`)"
                    ```
                    /space/remesh/local_relaxation/max_nl_iterations
                    ```
                    <h2>Description</h2>
                    Maximum number of nonlinear solver iterations before acceptance check
                
                    **Default**: `1`











            ??? json-spec "`/space/remesh/type` (`string`)"
                ```
                /space/remesh/type
                ```
                <h2>Description</h2>
                Type of adaptive remeshing to use.
            
                **Default**: `'physics'`
            
                **Options:** `['physics', 'sizing_field']`











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








            ??? json-spec "`/space/advanced/isoparametric` (`bool`)"
                ```
                /space/advanced/isoparametric
                ```
                <h2>Description</h2>
                Forces geometric map basis to be the same degree as the main variable basis, irrespective of the degree associated with the geom. map degrees associated with the elements of the geometry.
            
                **Default**: `False`








            ??? json-spec "`/space/advanced/bc_method` (`string`)"
                ```
                /space/advanced/bc_method
                ```
                <h2>Description</h2>
                Method for imposing analytic Dirichet boundary conditions. If 'lsq' (least-squares fit), then the bc function is sampled at quadrature points, and the FEspace nodal values on the boundary are determined by minimizing L2 norm of the difference. If 'sample', then the analytic bc function is sampled at the boundary nodes.
            
                **Default**: `'sample'`
            
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








            ??? json-spec "`/space/advanced/use_particle_advection` (`bool`)"
                ```
                /space/advanced/use_particle_advection
                ```
                <h2>Description</h2>
                Use particle advection in splitting method for solving NS equation.
            
                **Default**: `False`












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






            ??? json-spec "`/time/integrator`"
                ```
                /time/integrator
                ```


                === "`/time/integrator` (`string`)"
                    <h2>Description</h2>
                    Time integrator
                
                    **Default**: `'ImplicitEuler'`
                
                    **Options:** `['ImplicitEuler', 'BDF1', 'BDF2', 'BDF3', 'BDF4', 'BDF5', 'BDF6', 'ImplicitNewmark']`



                === "ImplicitEuler"
                
                    **Type**: ImplicitEuler
                    <h2>Description</h2>
                    Implicit Euler time integration
                    <h2>Required</h2>





                    ??? json-spec "`/time/integrator/type` (`string`)"
                        ```
                        /time/integrator/type
                        ```
                        <h2>Description</h2>
                        Type of time integrator to use
                    
                        **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`






                === "BDF"
                
                    **Type**: BDF
                    <h2>Description</h2>
                    Backwards differentiation formula time integration
                    <h2>Required</h2>





                    ??? json-spec "`/time/integrator/type` (`string`)"
                        ```
                        /time/integrator/type
                        ```
                        <h2>Description</h2>
                        Type of time integrator to use
                    
                        **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`



                    <h2>Optional</h2>





                    ??? json-spec "`/time/integrator/steps` (`int`)"
                        ```
                        /time/integrator/steps
                        ```
                        <h2>Description</h2>
                        BDF order
                    
                        **Default**: `1`
                    
                        **Range:** `[1, 6]`






                === "ImplicitNewmark"
                
                    **Type**: ImplicitNewmark
                    <h2>Description</h2>
                    Implicit Newmark time integration
                    <h2>Required</h2>





                    ??? json-spec "`/time/integrator/type` (`string`)"
                        ```
                        /time/integrator/type
                        ```
                        <h2>Description</h2>
                        Type of time integrator to use
                    
                        **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`



                    <h2>Optional</h2>





                    ??? json-spec "`/time/integrator/gamma` (`float`)"
                        ```
                        /time/integrator/gamma
                        ```
                        <h2>Description</h2>
                        Newmark gamma
                    
                        **Default**: `0.5`
                    
                        **Range:** `[0, 1]`








                    ??? json-spec "`/time/integrator/beta` (`float`)"
                        ```
                        /time/integrator/beta
                        ```
                        <h2>Description</h2>
                        Newmark beta
                    
                        **Default**: `0.25`
                    
                        **Range:** `[0, 0.5]`











            ??? json-spec "`/time/quasistatic` (`bool`)"
                ```
                /time/quasistatic
                ```
                <h2>Description</h2>
                Ignore inertia in time dependent. Used for doing incremental load.
            
                **Default**: `False`






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






            ??? json-spec "`/time/integrator`"
                ```
                /time/integrator
                ```


                === "`/time/integrator` (`string`)"
                    <h2>Description</h2>
                    Time integrator
                
                    **Default**: `'ImplicitEuler'`
                
                    **Options:** `['ImplicitEuler', 'BDF1', 'BDF2', 'BDF3', 'BDF4', 'BDF5', 'BDF6', 'ImplicitNewmark']`



                === "ImplicitEuler"
                
                    **Type**: ImplicitEuler
                    <h2>Description</h2>
                    Implicit Euler time integration
                    <h2>Required</h2>





                    ??? json-spec "`/time/integrator/type` (`string`)"
                        ```
                        /time/integrator/type
                        ```
                        <h2>Description</h2>
                        Type of time integrator to use
                    
                        **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`






                === "BDF"
                
                    **Type**: BDF
                    <h2>Description</h2>
                    Backwards differentiation formula time integration
                    <h2>Required</h2>





                    ??? json-spec "`/time/integrator/type` (`string`)"
                        ```
                        /time/integrator/type
                        ```
                        <h2>Description</h2>
                        Type of time integrator to use
                    
                        **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`



                    <h2>Optional</h2>





                    ??? json-spec "`/time/integrator/steps` (`int`)"
                        ```
                        /time/integrator/steps
                        ```
                        <h2>Description</h2>
                        BDF order
                    
                        **Default**: `1`
                    
                        **Range:** `[1, 6]`






                === "ImplicitNewmark"
                
                    **Type**: ImplicitNewmark
                    <h2>Description</h2>
                    Implicit Newmark time integration
                    <h2>Required</h2>





                    ??? json-spec "`/time/integrator/type` (`string`)"
                        ```
                        /time/integrator/type
                        ```
                        <h2>Description</h2>
                        Type of time integrator to use
                    
                        **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`



                    <h2>Optional</h2>





                    ??? json-spec "`/time/integrator/gamma` (`float`)"
                        ```
                        /time/integrator/gamma
                        ```
                        <h2>Description</h2>
                        Newmark gamma
                    
                        **Default**: `0.5`
                    
                        **Range:** `[0, 1]`








                    ??? json-spec "`/time/integrator/beta` (`float`)"
                        ```
                        /time/integrator/beta
                        ```
                        <h2>Description</h2>
                        Newmark beta
                    
                        **Default**: `0.25`
                    
                        **Range:** `[0, 0.5]`











            ??? json-spec "`/time/quasistatic` (`bool`)"
                ```
                /time/quasistatic
                ```
                <h2>Description</h2>
                Ignore inertia in time dependent. Used for doing incremental load.
            
                **Default**: `False`






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






            ??? json-spec "`/time/integrator`"
                ```
                /time/integrator
                ```


                === "`/time/integrator` (`string`)"
                    <h2>Description</h2>
                    Time integrator
                
                    **Default**: `'ImplicitEuler'`
                
                    **Options:** `['ImplicitEuler', 'BDF1', 'BDF2', 'BDF3', 'BDF4', 'BDF5', 'BDF6', 'ImplicitNewmark']`



                === "ImplicitEuler"
                
                    **Type**: ImplicitEuler
                    <h2>Description</h2>
                    Implicit Euler time integration
                    <h2>Required</h2>





                    ??? json-spec "`/time/integrator/type` (`string`)"
                        ```
                        /time/integrator/type
                        ```
                        <h2>Description</h2>
                        Type of time integrator to use
                    
                        **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`






                === "BDF"
                
                    **Type**: BDF
                    <h2>Description</h2>
                    Backwards differentiation formula time integration
                    <h2>Required</h2>





                    ??? json-spec "`/time/integrator/type` (`string`)"
                        ```
                        /time/integrator/type
                        ```
                        <h2>Description</h2>
                        Type of time integrator to use
                    
                        **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`



                    <h2>Optional</h2>





                    ??? json-spec "`/time/integrator/steps` (`int`)"
                        ```
                        /time/integrator/steps
                        ```
                        <h2>Description</h2>
                        BDF order
                    
                        **Default**: `1`
                    
                        **Range:** `[1, 6]`






                === "ImplicitNewmark"
                
                    **Type**: ImplicitNewmark
                    <h2>Description</h2>
                    Implicit Newmark time integration
                    <h2>Required</h2>





                    ??? json-spec "`/time/integrator/type` (`string`)"
                        ```
                        /time/integrator/type
                        ```
                        <h2>Description</h2>
                        Type of time integrator to use
                    
                        **Options:** `['ImplicitEuler', 'BDF', 'ImplicitNewmark']`



                    <h2>Optional</h2>





                    ??? json-spec "`/time/integrator/gamma` (`float`)"
                        ```
                        /time/integrator/gamma
                        ```
                        <h2>Description</h2>
                        Newmark gamma
                    
                        **Default**: `0.5`
                    
                        **Range:** `[0, 1]`








                    ??? json-spec "`/time/integrator/beta` (`float`)"
                        ```
                        /time/integrator/beta
                        ```
                        <h2>Description</h2>
                        Newmark beta
                    
                        **Default**: `0.25`
                    
                        **Range:** `[0, 0.5]`











            ??? json-spec "`/time/quasistatic` (`bool`)"
                ```
                /time/quasistatic
                ```
                <h2>Description</h2>
                Ignore inertia in time dependent. Used for doing incremental load.
            
                **Default**: `False`











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








        ??? json-spec "`/contact/use_convergent_formulation` (`bool`)"
            ```
            /contact/use_convergent_formulation
            ```
            <h2>Description</h2>
            Whether to use the convergent (area weighted) formulation of IPC.
        
            **Default**: `False`






        ??? json-spec "`/contact/collision_mesh`"
            ```
            /contact/collision_mesh
            ```


            === "`/contact/collision_mesh` (`object`)"
                <h2>Description</h2>
                Load a preconstructed collision mesh.
            
                **Default**: `'skip'`
                <h2>Required</h2>





                ??? json-spec "`/contact/collision_mesh/mesh` (`string`)"
                    ```
                    /contact/collision_mesh/mesh
                    ```
                    <h2>Description</h2>
                    Path to preconstructed collision mesh.








                ??? json-spec "`/contact/collision_mesh/linear_map` (`string`)"
                    ```
                    /contact/collision_mesh/linear_map
                    ```
                    <h2>Description</h2>
                    HDF file storing the linear mapping of displacements.



                <h2>Optional</h2>





                ??? json-spec "`/contact/collision_mesh/enabled` (`bool`)"
                    ```
                    /contact/collision_mesh/enabled
                    ```
                    <h2>Description</h2>
                    
                
                    **Default**: `True`






            === "`/contact/collision_mesh` (`object`)"
                <h2>Description</h2>
                Construct a collision mesh with a maximum edge length.
                <h2>Required</h2>





                ??? json-spec "`/contact/collision_mesh/max_edge_length` (`float`)"
                    ```
                    /contact/collision_mesh/max_edge_length
                    ```
                    <h2>Description</h2>
                    Maximum edge length to use for building the collision mesh.



                <h2>Optional</h2>





                ??? json-spec "`/contact/collision_mesh/tessellation_type` (`string`)"
                    ```
                    /contact/collision_mesh/tessellation_type
                    ```
                    <h2>Description</h2>
                    Type of tessellation to use for building the collision mesh.
                
                    **Default**: `'regular'`
                
                    **Options:** `['regular', 'irregular']`








                ??? json-spec "`/contact/collision_mesh/enabled` (`bool`)"
                    ```
                    /contact/collision_mesh/enabled
                    ```
                    <h2>Description</h2>
                    
                
                    **Default**: `True`











        ??? json-spec "`/contact/periodic` (`bool`)"
            ```
            /contact/periodic
            ```
            <h2>Description</h2>
            Set to true to check collision between adjacent periodic cells.
        
            **Default**: `False`











    ??? json-spec "`/solver` (`object`)"
        ```
        /solver
        ```
        <h2>Description</h2>
        The settings for the solver including linear solver, nonlinear solver, and some advanced options.
    
        **Default**: `None`
        <h2>Optional</h2>





        ??? json-spec "`/solver/max_threads` (`int`)"
            ```
            /solver/max_threads
            ```
            <h2>Description</h2>
            Maximum number of threads used; 0 is unlimited.
        
            **Default**: `0`
        
            **Range:** `[0, inf]`








        ??? json-spec "`/solver/linear` (`object`)"
            ```
            /solver/linear
            ```
            <h2>Description</h2>
            Settings for the linear solver.
        
            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/solver/linear/enable_overwrite_solver` (`bool`)"
                ```
                /solver/linear/enable_overwrite_solver
                ```
                <h2>Description</h2>
                If solver name is not present, falls back to default
            
                **Default**: `False`








            ??? json-spec "`/solver/linear/solver` (`string`)"
                ```
                /solver/linear/solver
                ```
                <h2>Description</h2>
                Linear solver type.
            
                **Default**: `''`
            
                **Options:** `['Eigen::SimplicialLDLT', 'Eigen::SparseLU', 'Eigen::CholmodSupernodalLLT', 'Eigen::UmfPackLU', 'Eigen::SuperLU', 'Eigen::PardisoLDLT', 'Eigen::PardisoLLT', 'Eigen::PardisoLU', 'Pardiso', 'Hypre', 'AMGCL', 'Eigen::LeastSquaresConjugateGradient', 'Eigen::DGMRES', 'Eigen::ConjugateGradient', 'Eigen::BiCGSTAB', 'Eigen::GMRES', 'Eigen::MINRES']`








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























        ??? json-spec "`/solver/adjoint_linear` (`object`)"
            ```
            /solver/adjoint_linear
            ```
            <h2>Description</h2>
            Settings for the linear solver.
        
            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/solver/adjoint_linear/enable_overwrite_solver` (`bool`)"
                ```
                /solver/adjoint_linear/enable_overwrite_solver
                ```
                <h2>Description</h2>
                If solver name is not present, falls back to default
            
                **Default**: `False`








            ??? json-spec "`/solver/adjoint_linear/solver` (`string`)"
                ```
                /solver/adjoint_linear/solver
                ```
                <h2>Description</h2>
                Linear solver type.
            
                **Default**: `''`
            
                **Options:** `['Eigen::SimplicialLDLT', 'Eigen::SparseLU', 'Eigen::CholmodSupernodalLLT', 'Eigen::UmfPackLU', 'Eigen::SuperLU', 'Eigen::PardisoLDLT', 'Eigen::PardisoLLT', 'Eigen::PardisoLU', 'Pardiso', 'Hypre', 'AMGCL', 'Eigen::LeastSquaresConjugateGradient', 'Eigen::DGMRES', 'Eigen::ConjugateGradient', 'Eigen::BiCGSTAB', 'Eigen::GMRES', 'Eigen::MINRES']`








            ??? json-spec "`/solver/adjoint_linear/precond` (`string`)"
                ```
                /solver/adjoint_linear/precond
                ```
                <h2>Description</h2>
                Preconditioner used if using an iterative linear solver.
            
                **Default**: `''`
            
                **Options:** `['Eigen::IdentityPreconditioner', 'Eigen::DiagonalPreconditioner', 'Eigen::IncompleteCholesky', 'Eigen::LeastSquareDiagonalPreconditioner', 'Eigen::IncompleteLUT']`








            ??? json-spec "`/solver/adjoint_linear/Eigen::LeastSquaresConjugateGradient` (`object`)"
                ```
                /solver/adjoint_linear/Eigen::LeastSquaresConjugateGradient
                ```
                <h2>Description</h2>
                Settings for the Eigen's Least Squares Conjugate Gradient solver.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/adjoint_linear/Eigen::LeastSquaresConjugateGradient/max_iter` (`int`)"
                    ```
                    /solver/adjoint_linear/Eigen::LeastSquaresConjugateGradient/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.
                
                    **Default**: `1000`








                ??? json-spec "`/solver/adjoint_linear/Eigen::LeastSquaresConjugateGradient/tolerance` (`float`)"
                    ```
                    /solver/adjoint_linear/Eigen::LeastSquaresConjugateGradient/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.
                
                    **Default**: `1e-12`











            ??? json-spec "`/solver/adjoint_linear/Eigen::DGMRES` (`object`)"
                ```
                /solver/adjoint_linear/Eigen::DGMRES
                ```
                <h2>Description</h2>
                Settings for the Eigen's DGMRES solver.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/adjoint_linear/Eigen::DGMRES/max_iter` (`int`)"
                    ```
                    /solver/adjoint_linear/Eigen::DGMRES/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.
                
                    **Default**: `1000`








                ??? json-spec "`/solver/adjoint_linear/Eigen::DGMRES/tolerance` (`float`)"
                    ```
                    /solver/adjoint_linear/Eigen::DGMRES/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.
                
                    **Default**: `1e-12`











            ??? json-spec "`/solver/adjoint_linear/Eigen::ConjugateGradient` (`object`)"
                ```
                /solver/adjoint_linear/Eigen::ConjugateGradient
                ```
                <h2>Description</h2>
                Settings for the Eigen's Conjugate Gradient solver.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/adjoint_linear/Eigen::ConjugateGradient/max_iter` (`int`)"
                    ```
                    /solver/adjoint_linear/Eigen::ConjugateGradient/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.
                
                    **Default**: `1000`








                ??? json-spec "`/solver/adjoint_linear/Eigen::ConjugateGradient/tolerance` (`float`)"
                    ```
                    /solver/adjoint_linear/Eigen::ConjugateGradient/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.
                
                    **Default**: `1e-12`











            ??? json-spec "`/solver/adjoint_linear/Eigen::BiCGSTAB` (`object`)"
                ```
                /solver/adjoint_linear/Eigen::BiCGSTAB
                ```
                <h2>Description</h2>
                Settings for the Eigen's BiCGSTAB solver.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/adjoint_linear/Eigen::BiCGSTAB/max_iter` (`int`)"
                    ```
                    /solver/adjoint_linear/Eigen::BiCGSTAB/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.
                
                    **Default**: `1000`








                ??? json-spec "`/solver/adjoint_linear/Eigen::BiCGSTAB/tolerance` (`float`)"
                    ```
                    /solver/adjoint_linear/Eigen::BiCGSTAB/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.
                
                    **Default**: `1e-12`











            ??? json-spec "`/solver/adjoint_linear/Eigen::GMRES` (`object`)"
                ```
                /solver/adjoint_linear/Eigen::GMRES
                ```
                <h2>Description</h2>
                Settings for the Eigen's GMRES solver.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/adjoint_linear/Eigen::GMRES/max_iter` (`int`)"
                    ```
                    /solver/adjoint_linear/Eigen::GMRES/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.
                
                    **Default**: `1000`








                ??? json-spec "`/solver/adjoint_linear/Eigen::GMRES/tolerance` (`float`)"
                    ```
                    /solver/adjoint_linear/Eigen::GMRES/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.
                
                    **Default**: `1e-12`











            ??? json-spec "`/solver/adjoint_linear/Eigen::MINRES` (`object`)"
                ```
                /solver/adjoint_linear/Eigen::MINRES
                ```
                <h2>Description</h2>
                Settings for the Eigen's MINRES solver.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/adjoint_linear/Eigen::MINRES/max_iter` (`int`)"
                    ```
                    /solver/adjoint_linear/Eigen::MINRES/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.
                
                    **Default**: `1000`








                ??? json-spec "`/solver/adjoint_linear/Eigen::MINRES/tolerance` (`float`)"
                    ```
                    /solver/adjoint_linear/Eigen::MINRES/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.
                
                    **Default**: `1e-12`











            ??? json-spec "`/solver/adjoint_linear/Pardiso` (`object`)"
                ```
                /solver/adjoint_linear/Pardiso
                ```
                <h2>Description</h2>
                Settings for the Pardiso solver.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/adjoint_linear/Pardiso/mtype` (`int`)"
                    ```
                    /solver/adjoint_linear/Pardiso/mtype
                    ```
                    <h2>Description</h2>
                    Matrix type.
                
                    **Default**: `11`
                
                    **Options:** `[1, 2, -2, 3, 4, -4, 6, 11, 13]`











            ??? json-spec "`/solver/adjoint_linear/Hypre` (`object`)"
                ```
                /solver/adjoint_linear/Hypre
                ```
                <h2>Description</h2>
                Settings for the Hypre solver.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/adjoint_linear/Hypre/max_iter` (`int`)"
                    ```
                    /solver/adjoint_linear/Hypre/max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations.
                
                    **Default**: `1000`








                ??? json-spec "`/solver/adjoint_linear/Hypre/pre_max_iter` (`int`)"
                    ```
                    /solver/adjoint_linear/Hypre/pre_max_iter
                    ```
                    <h2>Description</h2>
                    Maximum number of pre iterations.
                
                    **Default**: `1`








                ??? json-spec "`/solver/adjoint_linear/Hypre/tolerance` (`float`)"
                    ```
                    /solver/adjoint_linear/Hypre/tolerance
                    ```
                    <h2>Description</h2>
                    Convergence tolerance.
                
                    **Default**: `1e-10`











            ??? json-spec "`/solver/adjoint_linear/AMGCL` (`object`)"
                ```
                /solver/adjoint_linear/AMGCL
                ```
                <h2>Description</h2>
                Settings for the AMGCL solver.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/adjoint_linear/AMGCL/solver` (`object`)"
                    ```
                    /solver/adjoint_linear/AMGCL/solver
                    ```
                    <h2>Description</h2>
                    Solver settings for the AMGCL.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/adjoint_linear/AMGCL/solver/tol` (`float`)"
                        ```
                        /solver/adjoint_linear/AMGCL/solver/tol
                        ```
                        <h2>Description</h2>
                        Convergence tolerance.
                    
                        **Default**: `1e-10`








                    ??? json-spec "`/solver/adjoint_linear/AMGCL/solver/maxiter` (`int`)"
                        ```
                        /solver/adjoint_linear/AMGCL/solver/maxiter
                        ```
                        <h2>Description</h2>
                        Maximum number of iterations.
                    
                        **Default**: `1000`








                    ??? json-spec "`/solver/adjoint_linear/AMGCL/solver/type` (`string`)"
                        ```
                        /solver/adjoint_linear/AMGCL/solver/type
                        ```
                        <h2>Description</h2>
                        Type of solver to use.
                    
                        **Default**: `'cg'`











                ??? json-spec "`/solver/adjoint_linear/AMGCL/precond` (`object`)"
                    ```
                    /solver/adjoint_linear/AMGCL/precond
                    ```
                    <h2>Description</h2>
                    Preconditioner settings for the AMGCL.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/relax` (`object`)"
                        ```
                        /solver/adjoint_linear/AMGCL/precond/relax
                        ```
                        <h2>Description</h2>
                        Preconditioner settings for the AMGCL.
                    
                        **Default**: `None`
                        <h2>Optional</h2>





                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/relax/degree` (`int`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/relax/degree
                            ```
                            <h2>Description</h2>
                            Degree of the polynomial.
                        
                            **Default**: `16`








                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/relax/type` (`string`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/relax/type
                            ```
                            <h2>Description</h2>
                            Type of relaxation to use.
                        
                            **Default**: `'chebyshev'`








                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/relax/power_iters` (`int`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/relax/power_iters
                            ```
                            <h2>Description</h2>
                            Number of power iterations.
                        
                            **Default**: `100`








                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/relax/higher` (`float`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/relax/higher
                            ```
                            <h2>Description</h2>
                            Higher level relaxation.
                        
                            **Default**: `2`








                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/relax/lower` (`float`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/relax/lower
                            ```
                            <h2>Description</h2>
                            Lower level relaxation.
                        
                            **Default**: `0.008333333333`








                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/relax/scale` (`bool`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/relax/scale
                            ```
                            <h2>Description</h2>
                            Scale.
                        
                            **Default**: `True`











                    ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/class` (`string`)"
                        ```
                        /solver/adjoint_linear/AMGCL/precond/class
                        ```
                        <h2>Description</h2>
                        Type of preconditioner to use.
                    
                        **Default**: `'amg'`








                    ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/max_levels` (`int`)"
                        ```
                        /solver/adjoint_linear/AMGCL/precond/max_levels
                        ```
                        <h2>Description</h2>
                        Maximum number of levels.
                    
                        **Default**: `6`








                    ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/direct_coarse` (`bool`)"
                        ```
                        /solver/adjoint_linear/AMGCL/precond/direct_coarse
                        ```
                        <h2>Description</h2>
                        Use direct solver for the coarsest level.
                    
                        **Default**: `False`








                    ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/ncycle` (`int`)"
                        ```
                        /solver/adjoint_linear/AMGCL/precond/ncycle
                        ```
                        <h2>Description</h2>
                        Number of cycles.
                    
                        **Default**: `2`








                    ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/coarsening` (`object`)"
                        ```
                        /solver/adjoint_linear/AMGCL/precond/coarsening
                        ```
                        <h2>Description</h2>
                        Coarsening parameters.
                    
                        **Default**: `None`
                        <h2>Optional</h2>





                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/coarsening/type` (`string`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/coarsening/type
                            ```
                            <h2>Description</h2>
                            Coarsening type.
                        
                            **Default**: `'smoothed_aggregation'`








                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/coarsening/estimate_spectral_radius` (`bool`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/coarsening/estimate_spectral_radius
                            ```
                            <h2>Description</h2>
                            Should the spectral radius be estimated.
                        
                            **Default**: `True`








                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/coarsening/relax` (`float`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/coarsening/relax
                            ```
                            <h2>Description</h2>
                            Coarsening relaxation.
                        
                            **Default**: `1`








                        ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/coarsening/aggr` (`object`)"
                            ```
                            /solver/adjoint_linear/AMGCL/precond/coarsening/aggr
                            ```
                            <h2>Description</h2>
                            Aggregation settings.
                        
                            **Default**: `None`
                            <h2>Optional</h2>





                            ??? json-spec "`/solver/adjoint_linear/AMGCL/precond/coarsening/aggr/eps_strong` (`float`)"
                                ```
                                /solver/adjoint_linear/AMGCL/precond/coarsening/aggr/eps_strong
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



            ??? json-spec "`/solver/nonlinear/solver`"
                ```
                /solver/nonlinear/solver
                ```


                === "`/solver/nonlinear/solver` (`string`)"
                    <h2>Description</h2>
                    Nonlinear solver type
                
                    **Default**: `'Newton'`
                
                    **Options:** `['Newton', 'DenseNewton', 'GradientDescent', 'ADAM', 'StochasticADAM', 'StochasticGradientDescent', 'L-BFGS', 'BFGS', 'L-BFGS-B', 'MMA']`



                === "`/solver/nonlinear/solver` (`list`)"
                    <h2>Description</h2>
                    List of solvers for ballback. Eg, [{'type':'Newton'}, {'type':'L-BFGS'}, {'type':'GradientDescent'}] will solve using Newton, in case of failure will fallback to L-BFGS and eventually to GradientDescent



                    ??? json-spec "`/solver/nonlinear/solver/*`"
                        ```
                        /solver/nonlinear/solver/*
                        ```


                        === "Newton"
                        
                            **Type**: Newton
                            <h2>Description</h2>
                            Options for Newton.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/residual_tolerance` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/residual_tolerance
                                ```
                                <h2>Description</h2>
                                Tolerance of the linear system residual. If residual is above, the direction is rejected.
                            
                                **Default**: `1e-05`






                        === "ProjectedNewton"
                        
                            **Type**: ProjectedNewton
                            <h2>Description</h2>
                            Options for projected Newton.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/residual_tolerance` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/residual_tolerance
                                ```
                                <h2>Description</h2>
                                Tolerance of the linear system residual. If residual is above, the direction is rejected.
                            
                                **Default**: `1e-05`






                        === "RegularizedNewton"
                        
                            **Type**: RegularizedNewton
                            <h2>Description</h2>
                            Options for regularized Newton.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/residual_tolerance` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/residual_tolerance
                                ```
                                <h2>Description</h2>
                                Tolerance of the linear system residual. If residual is above, the direction is rejected.
                            
                                **Default**: `1e-05`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_min` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_min
                                ```
                                <h2>Description</h2>
                                Minimum regulariztion weight.
                            
                                **Default**: `1e-08`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_max` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_max
                                ```
                                <h2>Description</h2>
                                Maximum regulariztion weight.
                            
                                **Default**: `100000000.0`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_inc` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_inc
                                ```
                                <h2>Description</h2>
                                Regulariztion weight increment.
                            
                                **Default**: `10`






                        === "RegularizedProjectedNewton"
                        
                            **Type**: RegularizedProjectedNewton
                            <h2>Description</h2>
                            Options for regularized projected Newton.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/residual_tolerance` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/residual_tolerance
                                ```
                                <h2>Description</h2>
                                Tolerance of the linear system residual. If residual is above, the direction is rejected.
                            
                                **Default**: `1e-05`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_min` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_min
                                ```
                                <h2>Description</h2>
                                Minimum regulariztion weight.
                            
                                **Default**: `1e-08`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_max` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_max
                                ```
                                <h2>Description</h2>
                                Maximum regulariztion weight.
                            
                                **Default**: `100000000.0`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_inc` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_inc
                                ```
                                <h2>Description</h2>
                                Regulariztion weight increment.
                            
                                **Default**: `10`






                        === "DenseNewton"
                        
                            **Type**: DenseNewton
                            <h2>Description</h2>
                            Options for Newton.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/residual_tolerance` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/residual_tolerance
                                ```
                                <h2>Description</h2>
                                Tolerance of the linear system residual. If residual is above, the direction is rejected.
                            
                                **Default**: `1e-05`






                        === "DenseProjectedNewton"
                        
                            **Type**: DenseProjectedNewton
                            <h2>Description</h2>
                            Options for projected Newton.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/residual_tolerance` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/residual_tolerance
                                ```
                                <h2>Description</h2>
                                Tolerance of the linear system residual. If residual is above, the direction is rejected.
                            
                                **Default**: `1e-05`






                        === "DenseRegularizedNewton"
                        
                            **Type**: DenseRegularizedNewton
                            <h2>Description</h2>
                            Options for regularized Newton.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/residual_tolerance` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/residual_tolerance
                                ```
                                <h2>Description</h2>
                                Tolerance of the linear system residual. If residual is above, the direction is rejected.
                            
                                **Default**: `1e-05`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_min` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_min
                                ```
                                <h2>Description</h2>
                                Minimum regulariztion weight.
                            
                                **Default**: `1e-08`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_max` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_max
                                ```
                                <h2>Description</h2>
                                Maximum regulariztion weight.
                            
                                **Default**: `100000000.0`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_inc` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_inc
                                ```
                                <h2>Description</h2>
                                Regulariztion weight increment.
                            
                                **Default**: `10`






                        === "DenseRegularizedProjectedNewton"
                        
                            **Type**: DenseRegularizedProjectedNewton
                            <h2>Description</h2>
                            Options for projected regularized Newton.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/residual_tolerance` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/residual_tolerance
                                ```
                                <h2>Description</h2>
                                Tolerance of the linear system residual. If residual is above, the direction is rejected.
                            
                                **Default**: `1e-05`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_min` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_min
                                ```
                                <h2>Description</h2>
                                Minimum regulariztion weight.
                            
                                **Default**: `1e-08`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_max` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_max
                                ```
                                <h2>Description</h2>
                                Maximum regulariztion weight.
                            
                                **Default**: `100000000.0`








                            ??? json-spec "`/solver/nonlinear/solver/*/reg_weight_inc` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/reg_weight_inc
                                ```
                                <h2>Description</h2>
                                Regulariztion weight increment.
                            
                                **Default**: `10`






                        === "GradientDescent"
                        
                            **Type**: GradientDescent
                            <h2>Description</h2>
                            Options for Gradient Descent.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`






                        === "StochasticGradientDescent"
                        
                            **Type**: StochasticGradientDescent
                            <h2>Description</h2>
                            Options for Stochastic Gradient Descent.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/erase_component_probability` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/erase_component_probability
                                ```
                                <h2>Description</h2>
                                Probability of erasing a component on the gradient for stochastic solvers.
                            
                                **Default**: `0.3`






                        === "L-BFGS"
                        
                            **Type**: L-BFGS
                            <h2>Description</h2>
                            Options for L-BFGS.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/history_size` (`int`)"
                                ```
                                /solver/nonlinear/solver/*/history_size
                                ```
                                <h2>Description</h2>
                                The number of corrections to approximate the inverse Hessian matrix.
                            
                                **Default**: `6`






                        === "BFGS"
                        
                            **Type**: BFGS
                            <h2>Description</h2>
                            Options for BFGS.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`






                        === "ADAM"
                        
                            **Type**: ADAM
                            <h2>Description</h2>
                            Options for ADAM.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/alpha` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/alpha
                                ```
                                <h2>Description</h2>
                                Parameter alpha for ADAM.
                            
                                **Default**: `0.001`








                            ??? json-spec "`/solver/nonlinear/solver/*/beta_1` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/beta_1
                                ```
                                <h2>Description</h2>
                                Parameter beta_1 for ADAM.
                            
                                **Default**: `0.9`








                            ??? json-spec "`/solver/nonlinear/solver/*/beta_2` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/beta_2
                                ```
                                <h2>Description</h2>
                                Parameter beta_2 for ADAM.
                            
                                **Default**: `0.999`








                            ??? json-spec "`/solver/nonlinear/solver/*/epsilon` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/epsilon
                                ```
                                <h2>Description</h2>
                                Parameter epsilon for ADAM.
                            
                                **Default**: `1e-08`






                        === "StochasticADAM"
                        
                            **Type**: StochasticADAM
                            <h2>Description</h2>
                            Options for ADAM.
                            <h2>Required</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/type` (`string`)"
                                ```
                                /solver/nonlinear/solver/*/type
                                ```
                                <h2>Description</h2>
                                Nonlinear solver type
                            
                                **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                            <h2>Optional</h2>





                            ??? json-spec "`/solver/nonlinear/solver/*/alpha` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/alpha
                                ```
                                <h2>Description</h2>
                                Parameter alpha for ADAM.
                            
                                **Default**: `0.001`








                            ??? json-spec "`/solver/nonlinear/solver/*/beta_1` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/beta_1
                                ```
                                <h2>Description</h2>
                                Parameter beta_1 for ADAM.
                            
                                **Default**: `0.9`








                            ??? json-spec "`/solver/nonlinear/solver/*/beta_2` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/beta_2
                                ```
                                <h2>Description</h2>
                                Parameter beta_2 for ADAM.
                            
                                **Default**: `0.999`








                            ??? json-spec "`/solver/nonlinear/solver/*/epsilon` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/epsilon
                                ```
                                <h2>Description</h2>
                                Parameter epsilon for ADAM.
                            
                                **Default**: `1e-08`








                            ??? json-spec "`/solver/nonlinear/solver/*/erase_component_probability` (`float`)"
                                ```
                                /solver/nonlinear/solver/*/erase_component_probability
                                ```
                                <h2>Description</h2>
                                Probability of erasing a component on the gradient for stochastic solvers.
                            
                                **Default**: `0.3`














            ??? json-spec "`/solver/nonlinear/x_delta` (`float`)"
                ```
                /solver/nonlinear/x_delta
                ```
                <h2>Description</h2>
                Stopping criterion: minimal change of the variables x for the iterations to continue. Computed as the L2 norm of x divide by the time step.
            
                **Default**: `0`
            
                **Range:** `[0, inf]`








            ??? json-spec "`/solver/nonlinear/grad_norm` (`float`)"
                ```
                /solver/nonlinear/grad_norm
                ```
                <h2>Description</h2>
                Stopping criterion: Minimal gradient norm for the iterations to continue.
            
                **Default**: `1e-08`
            
                **Range:** `[0, inf]`








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
            
                **Default**: `500`






            ??? json-spec "`/solver/nonlinear/iterations_per_strategy`"
                ```
                /solver/nonlinear/iterations_per_strategy
                ```


                === "`/solver/nonlinear/iterations_per_strategy` (`int`)"
                    <h2>Description</h2>
                    Number of iterations for every substrategy before reset.
                
                    **Default**: `5`



                === "`/solver/nonlinear/iterations_per_strategy` (`list`)"
                    <h2>Description</h2>
                    Number of iterations for every substrategy before reset.





                    ??? json-spec "`/solver/nonlinear/iterations_per_strategy/*` (`int`)"
                        ```
                        /solver/nonlinear/iterations_per_strategy/*
                        ```
                        <h2>Description</h2>
                        Number of iterations for every substrategy before reset.
                    
                        **Default**: `5`











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
                
                    **Default**: `'RobustArmijo'`
                
                    **Options:** `['Armijo', 'RobustArmijo', 'Backtracking', 'None']`








                ??? json-spec "`/solver/nonlinear/line_search/use_grad_norm_tol` (`float`)"
                    ```
                    /solver/nonlinear/line_search/use_grad_norm_tol
                    ```
                    <h2>Description</h2>
                    When the energy is smaller than use_grad_norm_tol, line-search uses norm of gradient instead of energy
                
                    **Default**: `1e-06`








                ??? json-spec "`/solver/nonlinear/line_search/min_step_size` (`float`)"
                    ```
                    /solver/nonlinear/line_search/min_step_size
                    ```
                    <h2>Description</h2>
                    Mimimum step size
                
                    **Default**: `1e-10`








                ??? json-spec "`/solver/nonlinear/line_search/max_step_size_iter` (`int`)"
                    ```
                    /solver/nonlinear/line_search/max_step_size_iter
                    ```
                    <h2>Description</h2>
                    Number of iterations
                
                    **Default**: `30`








                ??? json-spec "`/solver/nonlinear/line_search/min_step_size_final` (`float`)"
                    ```
                    /solver/nonlinear/line_search/min_step_size_final
                    ```
                    <h2>Description</h2>
                    Mimimum step size for last descent strategy
                
                    **Default**: `1e-20`








                ??? json-spec "`/solver/nonlinear/line_search/max_step_size_iter_final` (`int`)"
                    ```
                    /solver/nonlinear/line_search/max_step_size_iter_final
                    ```
                    <h2>Description</h2>
                    Number of iterations for last descent strategy
                
                    **Default**: `100`








                ??? json-spec "`/solver/nonlinear/line_search/default_init_step_size` (`float`)"
                    ```
                    /solver/nonlinear/line_search/default_init_step_size
                    ```
                    <h2>Description</h2>
                    Initial step size
                
                    **Default**: `1`








                ??? json-spec "`/solver/nonlinear/line_search/step_ratio` (`float`)"
                    ```
                    /solver/nonlinear/line_search/step_ratio
                    ```
                    <h2>Description</h2>
                    Ratio used to decrease the step
                
                    **Default**: `0.5`








                ??? json-spec "`/solver/nonlinear/line_search/Armijo` (`object`)"
                    ```
                    /solver/nonlinear/line_search/Armijo
                    ```
                    <h2>Description</h2>
                    Options for Armijo.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/nonlinear/line_search/Armijo/c` (`float`)"
                        ```
                        /solver/nonlinear/line_search/Armijo/c
                        ```
                        <h2>Description</h2>
                        Armijo c parameter.
                    
                        **Default**: `0.0001`











                ??? json-spec "`/solver/nonlinear/line_search/RobustArmijo` (`object`)"
                    ```
                    /solver/nonlinear/line_search/RobustArmijo
                    ```
                    <h2>Description</h2>
                    Options for RobustArmijo.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/nonlinear/line_search/RobustArmijo/delta_relative_tolerance` (`float`)"
                        ```
                        /solver/nonlinear/line_search/RobustArmijo/delta_relative_tolerance
                        ```
                        <h2>Description</h2>
                        Relative tolerance on E to switch to approximate.
                    
                        **Default**: `0.1`














            ??? json-spec "`/solver/nonlinear/allow_out_of_iterations` (`bool`)"
                ```
                /solver/nonlinear/allow_out_of_iterations
                ```
                <h2>Description</h2>
                If false (default), an exception will be thrown when the nonlinear solver reaches the maximum number of iterations.
            
                **Default**: `False`








            ??? json-spec "`/solver/nonlinear/L-BFGS` (`object`)"
                ```
                /solver/nonlinear/L-BFGS
                ```
                <h2>Description</h2>
                Options for LBFGS.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/nonlinear/L-BFGS/history_size` (`int`)"
                    ```
                    /solver/nonlinear/L-BFGS/history_size
                    ```
                    <h2>Description</h2>
                    The number of corrections to approximate the inverse Hessian matrix.
                
                    **Default**: `6`











            ??? json-spec "`/solver/nonlinear/L-BFGS-B` (`object`)"
                ```
                /solver/nonlinear/L-BFGS-B
                ```
                <h2>Description</h2>
                Options for the boxed L-BFGS.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/nonlinear/L-BFGS-B/history_size` (`int`)"
                    ```
                    /solver/nonlinear/L-BFGS-B/history_size
                    ```
                    <h2>Description</h2>
                    The number of corrections to approximate the inverse Hessian matrix.
                
                    **Default**: `6`











            ??? json-spec "`/solver/nonlinear/Newton` (`object`)"
                ```
                /solver/nonlinear/Newton
                ```
                <h2>Description</h2>
                Options for Newton.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/nonlinear/Newton/residual_tolerance` (`float`)"
                    ```
                    /solver/nonlinear/Newton/residual_tolerance
                    ```
                    <h2>Description</h2>
                    Tolerance of the linear system residual. If residual is above, the direction is rejected.
                
                    **Default**: `1e-05`








                ??? json-spec "`/solver/nonlinear/Newton/reg_weight_min` (`float`)"
                    ```
                    /solver/nonlinear/Newton/reg_weight_min
                    ```
                    <h2>Description</h2>
                    Minimum regulariztion weight.
                
                    **Default**: `1e-08`








                ??? json-spec "`/solver/nonlinear/Newton/reg_weight_max` (`float`)"
                    ```
                    /solver/nonlinear/Newton/reg_weight_max
                    ```
                    <h2>Description</h2>
                    Maximum regulariztion weight.
                
                    **Default**: `100000000.0`








                ??? json-spec "`/solver/nonlinear/Newton/reg_weight_inc` (`float`)"
                    ```
                    /solver/nonlinear/Newton/reg_weight_inc
                    ```
                    <h2>Description</h2>
                    Regulariztion weight increment.
                
                    **Default**: `10`








                ??? json-spec "`/solver/nonlinear/Newton/force_psd_projection` (`bool`)"
                    ```
                    /solver/nonlinear/Newton/force_psd_projection
                    ```
                    <h2>Description</h2>
                    Force the Hessian to be PSD when using second order solvers (i.e., Newton's method).
                
                    **Default**: `False`








                ??? json-spec "`/solver/nonlinear/Newton/use_psd_projection` (`bool`)"
                    ```
                    /solver/nonlinear/Newton/use_psd_projection
                    ```
                    <h2>Description</h2>
                    Use PSD as fallback using second order solvers (i.e., Newton's method).
                
                    **Default**: `True`








                ??? json-spec "`/solver/nonlinear/Newton/use_psd_projection_in_regularized` (`bool`)"
                    ```
                    /solver/nonlinear/Newton/use_psd_projection_in_regularized
                    ```
                    <h2>Description</h2>
                    Use PSD in regularized Newton.
                
                    **Default**: `True`











            ??? json-spec "`/solver/nonlinear/ADAM` (`object`)"
                ```
                /solver/nonlinear/ADAM
                ```
                <h2>Description</h2>
                Options for ADAM.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/nonlinear/ADAM/alpha` (`float`)"
                    ```
                    /solver/nonlinear/ADAM/alpha
                    ```
                    <h2>Description</h2>
                    Parameter alpha for ADAM.
                
                    **Default**: `0.001`








                ??? json-spec "`/solver/nonlinear/ADAM/beta_1` (`float`)"
                    ```
                    /solver/nonlinear/ADAM/beta_1
                    ```
                    <h2>Description</h2>
                    Parameter beta_1 for ADAM.
                
                    **Default**: `0.9`








                ??? json-spec "`/solver/nonlinear/ADAM/beta_2` (`float`)"
                    ```
                    /solver/nonlinear/ADAM/beta_2
                    ```
                    <h2>Description</h2>
                    Parameter beta_2 for ADAM.
                
                    **Default**: `0.999`








                ??? json-spec "`/solver/nonlinear/ADAM/epsilon` (`float`)"
                    ```
                    /solver/nonlinear/ADAM/epsilon
                    ```
                    <h2>Description</h2>
                    Parameter epsilon for ADAM.
                
                    **Default**: `1e-08`











            ??? json-spec "`/solver/nonlinear/StochasticADAM` (`object`)"
                ```
                /solver/nonlinear/StochasticADAM
                ```
                <h2>Description</h2>
                Options for ADAM.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/nonlinear/StochasticADAM/alpha` (`float`)"
                    ```
                    /solver/nonlinear/StochasticADAM/alpha
                    ```
                    <h2>Description</h2>
                    Parameter alpha for ADAM.
                
                    **Default**: `0.001`








                ??? json-spec "`/solver/nonlinear/StochasticADAM/beta_1` (`float`)"
                    ```
                    /solver/nonlinear/StochasticADAM/beta_1
                    ```
                    <h2>Description</h2>
                    Parameter beta_1 for ADAM.
                
                    **Default**: `0.9`








                ??? json-spec "`/solver/nonlinear/StochasticADAM/beta_2` (`float`)"
                    ```
                    /solver/nonlinear/StochasticADAM/beta_2
                    ```
                    <h2>Description</h2>
                    Parameter beta_2 for ADAM.
                
                    **Default**: `0.999`








                ??? json-spec "`/solver/nonlinear/StochasticADAM/epsilon` (`float`)"
                    ```
                    /solver/nonlinear/StochasticADAM/epsilon
                    ```
                    <h2>Description</h2>
                    Parameter epsilon for ADAM.
                
                    **Default**: `1e-08`








                ??? json-spec "`/solver/nonlinear/StochasticADAM/erase_component_probability` (`float`)"
                    ```
                    /solver/nonlinear/StochasticADAM/erase_component_probability
                    ```
                    <h2>Description</h2>
                    Probability of erasing a component on the gradient for ADAM.
                
                    **Default**: `0.3`











            ??? json-spec "`/solver/nonlinear/StochasticGradientDescent` (`object`)"
                ```
                /solver/nonlinear/StochasticGradientDescent
                ```
                <h2>Description</h2>
                Options for Stochastic Gradient Descent.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/nonlinear/StochasticGradientDescent/erase_component_probability` (`float`)"
                    ```
                    /solver/nonlinear/StochasticGradientDescent/erase_component_probability
                    ```
                    <h2>Description</h2>
                    Probability of erasing a component on the gradient for StochasticGradientDescent.
                
                    **Default**: `0.3`











            ??? json-spec "`/solver/nonlinear/box_constraints` (`object`)"
                ```
                /solver/nonlinear/box_constraints
                ```
                <h2>Description</h2>
                FIXME: Missing documentation in the specification.
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/nonlinear/box_constraints/bounds` (`list`)"
                    ```
                    /solver/nonlinear/box_constraints/bounds
                    ```
                    <h2>Description</h2>
                    Box constraints on optimization variables.



                    ??? json-spec "`/solver/nonlinear/box_constraints/bounds/*`"
                        ```
                        /solver/nonlinear/box_constraints/bounds/*
                        ```


                        === "`/solver/nonlinear/box_constraints/bounds/*` (`list`)"
                            <h2>Description</h2>
                            Box constraint values on optimization variables.





                            ??? json-spec "`/solver/nonlinear/box_constraints/bounds/*/*` (`float`)"
                                ```
                                /solver/nonlinear/box_constraints/bounds/*/*
                                ```
                                <h2>Description</h2>
                                Box constraint values on optimization variables.






                        === "`/solver/nonlinear/box_constraints/bounds/*` (`float`)"
                            <h2>Description</h2>
                            Box constraint values on optimization variables.









                ??? json-spec "`/solver/nonlinear/box_constraints/max_change`"
                    ```
                    /solver/nonlinear/box_constraints/max_change
                    ```


                    === "`/solver/nonlinear/box_constraints/max_change` (`float`)"
                        <h2>Description</h2>
                        Maximum change of optimization variables in one iteration, only for solvers with box constraints. Negative value to disable this constraint.
                    
                        **Default**: `-1`



                    === "`/solver/nonlinear/box_constraints/max_change` (`list`)"
                        <h2>Description</h2>
                        Maximum change of optimization variables in one iteration, only for solvers with box constraints.





                        ??? json-spec "`/solver/nonlinear/box_constraints/max_change/*` (`float`)"
                            ```
                            /solver/nonlinear/box_constraints/max_change/*
                            ```
                            <h2>Description</h2>
                            Maximum change of every optimization variable in one iteration, only for solvers with box constraints.














            ??? json-spec "`/solver/nonlinear/advanced` (`object`)"
                ```
                /solver/nonlinear/advanced
                ```
                <h2>Description</h2>
                Nonlinear solver advanced options
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/solver/nonlinear/advanced/f_delta` (`float`)"
                    ```
                    /solver/nonlinear/advanced/f_delta
                    ```
                    <h2>Description</h2>
                    Dangerous Option: Quit the optimization if the solver reduces the energy by less than f_delta for consecutive f_delta_step_tol steps.
                
                    **Default**: `0`
                
                    **Range:** `[0, inf]`








                ??? json-spec "`/solver/nonlinear/advanced/f_delta_step_tol` (`int`)"
                    ```
                    /solver/nonlinear/advanced/f_delta_step_tol
                    ```
                    <h2>Description</h2>
                    Dangerous Option: Quit the optimization if the solver reduces the energy by less than f_delta for consecutive f_delta_step_tol steps.
                
                    **Default**: `100`








                ??? json-spec "`/solver/nonlinear/advanced/derivative_along_delta_x_tol` (`float`)"
                    ```
                    /solver/nonlinear/advanced/derivative_along_delta_x_tol
                    ```
                    <h2>Description</h2>
                    Quit the optimization if the directional derivative along the descent direction is smaller than this tolerance.
                
                    **Default**: `0`
                
                    **Range:** `[0, inf]`








                ??? json-spec "`/solver/nonlinear/advanced/apply_gradient_fd` (`string`)"
                    ```
                    /solver/nonlinear/advanced/apply_gradient_fd
                    ```
                    <h2>Description</h2>
                    Expensive Option: For every iteration of the nonlinear solver, run finite difference to verify gradient of energy.
                
                    **Default**: `'None'`
                
                    **Options:** `['None', 'DirectionalDerivative', 'FullFiniteDiff']`








                ??? json-spec "`/solver/nonlinear/advanced/gradient_fd_eps` (`float`)"
                    ```
                    /solver/nonlinear/advanced/gradient_fd_eps
                    ```
                    <h2>Description</h2>
                    Expensive Option: Eps for finite difference to verify gradient of energy.
                
                    **Default**: `1e-07`














        ??? json-spec "`/solver/augmented_lagrangian` (`object`)"
            ```
            /solver/augmented_lagrangian
            ```
            <h2>Description</h2>
            Parameters for the AL for imposing Dirichlet BCs. If the bc are not imposable, we add $w\|u - bc\|^2$ to the energy ($u$ is the solution at the Dirichlet nodes and $bc$ are the Dirichlet values). After convergence, we try to impose bc again. The algorithm computes E + a/2*AL^2 - lambda AL, where E is the current energy (elastic, inertia, contact, etc.) and AL is the augmented Lagrangian energy. a starts at `initial_weight` and, in case DBC cannot be imposed, we update a as `a *= scaling` until `max_weight`. See IPC additional material
        
            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/solver/augmented_lagrangian/initial_weight` (`float`)"
                ```
                /solver/augmented_lagrangian/initial_weight
                ```
                <h2>Description</h2>
                Initial weight for AL
            
                **Default**: `1000000.0`
            
                **Range:** `[0, inf]`








            ??? json-spec "`/solver/augmented_lagrangian/scaling` (`float`)"
                ```
                /solver/augmented_lagrangian/scaling
                ```
                <h2>Description</h2>
                Multiplication factor
            
                **Default**: `2.0`








            ??? json-spec "`/solver/augmented_lagrangian/max_weight` (`float`)"
                ```
                /solver/augmented_lagrangian/max_weight
                ```
                <h2>Description</h2>
                Maximum weight
            
                **Default**: `100000000.0`








            ??? json-spec "`/solver/augmented_lagrangian/eta` (`float`)"
                ```
                /solver/augmented_lagrangian/eta
                ```
                <h2>Description</h2>
                Tolerance for increasing the weight or updating the lagrangian
            
                **Default**: `0.99`
            
                **Range:** `[0, 1]`








            ??? json-spec "`/solver/augmented_lagrangian/nonlinear` (`object`)"
                ```
                /solver/augmented_lagrangian/nonlinear
                ```
                <h2>Description</h2>
                Settings for nonlinear solver. Interior-loop linear solver settings are defined in the solver/linear section.
            
                **Default**: `None`
                <h2>Optional</h2>



                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver`"
                    ```
                    /solver/augmented_lagrangian/nonlinear/solver
                    ```


                    === "`/solver/augmented_lagrangian/nonlinear/solver` (`string`)"
                        <h2>Description</h2>
                        Nonlinear solver type
                    
                        **Default**: `'Newton'`
                    
                        **Options:** `['Newton', 'DenseNewton', 'GradientDescent', 'ADAM', 'StochasticADAM', 'StochasticGradientDescent', 'L-BFGS', 'BFGS', 'L-BFGS-B', 'MMA']`



                    === "`/solver/augmented_lagrangian/nonlinear/solver` (`list`)"
                        <h2>Description</h2>
                        List of solvers for ballback. Eg, [{'type':'Newton'}, {'type':'L-BFGS'}, {'type':'GradientDescent'}] will solve using Newton, in case of failure will fallback to L-BFGS and eventually to GradientDescent



                        ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*`"
                            ```
                            /solver/augmented_lagrangian/nonlinear/solver/*
                            ```


                            === "Newton"
                            
                                **Type**: Newton
                                <h2>Description</h2>
                                Options for Newton.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance
                                    ```
                                    <h2>Description</h2>
                                    Tolerance of the linear system residual. If residual is above, the direction is rejected.
                                
                                    **Default**: `1e-05`






                            === "ProjectedNewton"
                            
                                **Type**: ProjectedNewton
                                <h2>Description</h2>
                                Options for projected Newton.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance
                                    ```
                                    <h2>Description</h2>
                                    Tolerance of the linear system residual. If residual is above, the direction is rejected.
                                
                                    **Default**: `1e-05`






                            === "RegularizedNewton"
                            
                                **Type**: RegularizedNewton
                                <h2>Description</h2>
                                Options for regularized Newton.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance
                                    ```
                                    <h2>Description</h2>
                                    Tolerance of the linear system residual. If residual is above, the direction is rejected.
                                
                                    **Default**: `1e-05`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_min` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_min
                                    ```
                                    <h2>Description</h2>
                                    Minimum regulariztion weight.
                                
                                    **Default**: `1e-08`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_max` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_max
                                    ```
                                    <h2>Description</h2>
                                    Maximum regulariztion weight.
                                
                                    **Default**: `100000000.0`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_inc` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_inc
                                    ```
                                    <h2>Description</h2>
                                    Regulariztion weight increment.
                                
                                    **Default**: `10`






                            === "RegularizedProjectedNewton"
                            
                                **Type**: RegularizedProjectedNewton
                                <h2>Description</h2>
                                Options for regularized projected Newton.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance
                                    ```
                                    <h2>Description</h2>
                                    Tolerance of the linear system residual. If residual is above, the direction is rejected.
                                
                                    **Default**: `1e-05`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_min` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_min
                                    ```
                                    <h2>Description</h2>
                                    Minimum regulariztion weight.
                                
                                    **Default**: `1e-08`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_max` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_max
                                    ```
                                    <h2>Description</h2>
                                    Maximum regulariztion weight.
                                
                                    **Default**: `100000000.0`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_inc` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_inc
                                    ```
                                    <h2>Description</h2>
                                    Regulariztion weight increment.
                                
                                    **Default**: `10`






                            === "DenseNewton"
                            
                                **Type**: DenseNewton
                                <h2>Description</h2>
                                Options for Newton.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance
                                    ```
                                    <h2>Description</h2>
                                    Tolerance of the linear system residual. If residual is above, the direction is rejected.
                                
                                    **Default**: `1e-05`






                            === "DenseProjectedNewton"
                            
                                **Type**: DenseProjectedNewton
                                <h2>Description</h2>
                                Options for projected Newton.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance
                                    ```
                                    <h2>Description</h2>
                                    Tolerance of the linear system residual. If residual is above, the direction is rejected.
                                
                                    **Default**: `1e-05`






                            === "DenseRegularizedNewton"
                            
                                **Type**: DenseRegularizedNewton
                                <h2>Description</h2>
                                Options for regularized Newton.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance
                                    ```
                                    <h2>Description</h2>
                                    Tolerance of the linear system residual. If residual is above, the direction is rejected.
                                
                                    **Default**: `1e-05`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_min` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_min
                                    ```
                                    <h2>Description</h2>
                                    Minimum regulariztion weight.
                                
                                    **Default**: `1e-08`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_max` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_max
                                    ```
                                    <h2>Description</h2>
                                    Maximum regulariztion weight.
                                
                                    **Default**: `100000000.0`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_inc` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_inc
                                    ```
                                    <h2>Description</h2>
                                    Regulariztion weight increment.
                                
                                    **Default**: `10`






                            === "DenseRegularizedProjectedNewton"
                            
                                **Type**: DenseRegularizedProjectedNewton
                                <h2>Description</h2>
                                Options for projected regularized Newton.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/residual_tolerance
                                    ```
                                    <h2>Description</h2>
                                    Tolerance of the linear system residual. If residual is above, the direction is rejected.
                                
                                    **Default**: `1e-05`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_min` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_min
                                    ```
                                    <h2>Description</h2>
                                    Minimum regulariztion weight.
                                
                                    **Default**: `1e-08`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_max` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_max
                                    ```
                                    <h2>Description</h2>
                                    Maximum regulariztion weight.
                                
                                    **Default**: `100000000.0`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_inc` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/reg_weight_inc
                                    ```
                                    <h2>Description</h2>
                                    Regulariztion weight increment.
                                
                                    **Default**: `10`






                            === "GradientDescent"
                            
                                **Type**: GradientDescent
                                <h2>Description</h2>
                                Options for Gradient Descent.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`






                            === "StochasticGradientDescent"
                            
                                **Type**: StochasticGradientDescent
                                <h2>Description</h2>
                                Options for Stochastic Gradient Descent.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/erase_component_probability` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/erase_component_probability
                                    ```
                                    <h2>Description</h2>
                                    Probability of erasing a component on the gradient for stochastic solvers.
                                
                                    **Default**: `0.3`






                            === "L-BFGS"
                            
                                **Type**: L-BFGS
                                <h2>Description</h2>
                                Options for L-BFGS.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/history_size` (`int`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/history_size
                                    ```
                                    <h2>Description</h2>
                                    The number of corrections to approximate the inverse Hessian matrix.
                                
                                    **Default**: `6`






                            === "BFGS"
                            
                                **Type**: BFGS
                                <h2>Description</h2>
                                Options for BFGS.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`






                            === "ADAM"
                            
                                **Type**: ADAM
                                <h2>Description</h2>
                                Options for ADAM.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/alpha` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/alpha
                                    ```
                                    <h2>Description</h2>
                                    Parameter alpha for ADAM.
                                
                                    **Default**: `0.001`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/beta_1` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/beta_1
                                    ```
                                    <h2>Description</h2>
                                    Parameter beta_1 for ADAM.
                                
                                    **Default**: `0.9`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/beta_2` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/beta_2
                                    ```
                                    <h2>Description</h2>
                                    Parameter beta_2 for ADAM.
                                
                                    **Default**: `0.999`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/epsilon` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/epsilon
                                    ```
                                    <h2>Description</h2>
                                    Parameter epsilon for ADAM.
                                
                                    **Default**: `1e-08`






                            === "StochasticADAM"
                            
                                **Type**: StochasticADAM
                                <h2>Description</h2>
                                Options for ADAM.
                                <h2>Required</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/type` (`string`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/type
                                    ```
                                    <h2>Description</h2>
                                    Nonlinear solver type
                                
                                    **Options:** `['Newton', 'DenseNewton', 'ProjectedNewton', 'DenseProjectedNewton', 'RegularizedNewton', 'DenseRegularizedNewton', 'RegularizedProjectedNewton', 'DenseRegularizedProjectedNewton', 'GradientDescent', 'StochasticGradientDescent', 'ADAM', 'StochasticADAM', 'L-BFGS', 'BFGS']`



                                <h2>Optional</h2>





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/alpha` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/alpha
                                    ```
                                    <h2>Description</h2>
                                    Parameter alpha for ADAM.
                                
                                    **Default**: `0.001`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/beta_1` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/beta_1
                                    ```
                                    <h2>Description</h2>
                                    Parameter beta_1 for ADAM.
                                
                                    **Default**: `0.9`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/beta_2` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/beta_2
                                    ```
                                    <h2>Description</h2>
                                    Parameter beta_2 for ADAM.
                                
                                    **Default**: `0.999`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/epsilon` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/epsilon
                                    ```
                                    <h2>Description</h2>
                                    Parameter epsilon for ADAM.
                                
                                    **Default**: `1e-08`








                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/solver/*/erase_component_probability` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/solver/*/erase_component_probability
                                    ```
                                    <h2>Description</h2>
                                    Probability of erasing a component on the gradient for stochastic solvers.
                                
                                    **Default**: `0.3`














                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/x_delta` (`float`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/x_delta
                    ```
                    <h2>Description</h2>
                    Stopping criterion: minimal change of the variables x for the iterations to continue. Computed as the L2 norm of x divide by the time step.
                
                    **Default**: `0`
                
                    **Range:** `[0, inf]`








                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/grad_norm` (`float`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/grad_norm
                    ```
                    <h2>Description</h2>
                    Stopping criterion: Minimal gradient norm for the iterations to continue.
                
                    **Default**: `1e-08`
                
                    **Range:** `[0, inf]`








                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/first_grad_norm_tol` (`float`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/first_grad_norm_tol
                    ```
                    <h2>Description</h2>
                    Minimal gradient norm for the iterations to not start, assume we already are at a minimum.
                
                    **Default**: `1e-10`








                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/max_iterations` (`int`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/max_iterations
                    ```
                    <h2>Description</h2>
                    Maximum number of iterations for a nonlinear solve.
                
                    **Default**: `500`






                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/iterations_per_strategy`"
                    ```
                    /solver/augmented_lagrangian/nonlinear/iterations_per_strategy
                    ```


                    === "`/solver/augmented_lagrangian/nonlinear/iterations_per_strategy` (`int`)"
                        <h2>Description</h2>
                        Number of iterations for every substrategy before reset.
                    
                        **Default**: `5`



                    === "`/solver/augmented_lagrangian/nonlinear/iterations_per_strategy` (`list`)"
                        <h2>Description</h2>
                        Number of iterations for every substrategy before reset.





                        ??? json-spec "`/solver/augmented_lagrangian/nonlinear/iterations_per_strategy/*` (`int`)"
                            ```
                            /solver/augmented_lagrangian/nonlinear/iterations_per_strategy/*
                            ```
                            <h2>Description</h2>
                            Number of iterations for every substrategy before reset.
                        
                            **Default**: `5`











                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search` (`object`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/line_search
                    ```
                    <h2>Description</h2>
                    Settings for line-search in the nonlinear solver
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/method` (`string`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/method
                        ```
                        <h2>Description</h2>
                        Line-search type
                    
                        **Default**: `'RobustArmijo'`
                    
                        **Options:** `['Armijo', 'RobustArmijo', 'Backtracking', 'None']`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/use_grad_norm_tol` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/use_grad_norm_tol
                        ```
                        <h2>Description</h2>
                        When the energy is smaller than use_grad_norm_tol, line-search uses norm of gradient instead of energy
                    
                        **Default**: `1e-06`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/min_step_size` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/min_step_size
                        ```
                        <h2>Description</h2>
                        Mimimum step size
                    
                        **Default**: `1e-10`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/max_step_size_iter` (`int`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/max_step_size_iter
                        ```
                        <h2>Description</h2>
                        Number of iterations
                    
                        **Default**: `30`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/min_step_size_final` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/min_step_size_final
                        ```
                        <h2>Description</h2>
                        Mimimum step size for last descent strategy
                    
                        **Default**: `1e-20`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/max_step_size_iter_final` (`int`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/max_step_size_iter_final
                        ```
                        <h2>Description</h2>
                        Number of iterations for last descent strategy
                    
                        **Default**: `100`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/default_init_step_size` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/default_init_step_size
                        ```
                        <h2>Description</h2>
                        Initial step size
                    
                        **Default**: `1`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/step_ratio` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/step_ratio
                        ```
                        <h2>Description</h2>
                        Ratio used to decrease the step
                    
                        **Default**: `0.5`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/Armijo` (`object`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/Armijo
                        ```
                        <h2>Description</h2>
                        Options for Armijo.
                    
                        **Default**: `None`
                        <h2>Optional</h2>





                        ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/Armijo/c` (`float`)"
                            ```
                            /solver/augmented_lagrangian/nonlinear/line_search/Armijo/c
                            ```
                            <h2>Description</h2>
                            Armijo c parameter.
                        
                            **Default**: `0.0001`











                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/RobustArmijo` (`object`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/line_search/RobustArmijo
                        ```
                        <h2>Description</h2>
                        Options for RobustArmijo.
                    
                        **Default**: `None`
                        <h2>Optional</h2>





                        ??? json-spec "`/solver/augmented_lagrangian/nonlinear/line_search/RobustArmijo/delta_relative_tolerance` (`float`)"
                            ```
                            /solver/augmented_lagrangian/nonlinear/line_search/RobustArmijo/delta_relative_tolerance
                            ```
                            <h2>Description</h2>
                            Relative tolerance on E to switch to approximate.
                        
                            **Default**: `0.1`














                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/allow_out_of_iterations` (`bool`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/allow_out_of_iterations
                    ```
                    <h2>Description</h2>
                    If false (default), an exception will be thrown when the nonlinear solver reaches the maximum number of iterations.
                
                    **Default**: `False`








                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/L-BFGS` (`object`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/L-BFGS
                    ```
                    <h2>Description</h2>
                    Options for LBFGS.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/L-BFGS/history_size` (`int`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/L-BFGS/history_size
                        ```
                        <h2>Description</h2>
                        The number of corrections to approximate the inverse Hessian matrix.
                    
                        **Default**: `6`











                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/L-BFGS-B` (`object`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/L-BFGS-B
                    ```
                    <h2>Description</h2>
                    Options for the boxed L-BFGS.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/L-BFGS-B/history_size` (`int`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/L-BFGS-B/history_size
                        ```
                        <h2>Description</h2>
                        The number of corrections to approximate the inverse Hessian matrix.
                    
                        **Default**: `6`











                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/Newton` (`object`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/Newton
                    ```
                    <h2>Description</h2>
                    Options for Newton.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/Newton/residual_tolerance` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/Newton/residual_tolerance
                        ```
                        <h2>Description</h2>
                        Tolerance of the linear system residual. If residual is above, the direction is rejected.
                    
                        **Default**: `1e-05`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/Newton/reg_weight_min` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/Newton/reg_weight_min
                        ```
                        <h2>Description</h2>
                        Minimum regulariztion weight.
                    
                        **Default**: `1e-08`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/Newton/reg_weight_max` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/Newton/reg_weight_max
                        ```
                        <h2>Description</h2>
                        Maximum regulariztion weight.
                    
                        **Default**: `100000000.0`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/Newton/reg_weight_inc` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/Newton/reg_weight_inc
                        ```
                        <h2>Description</h2>
                        Regulariztion weight increment.
                    
                        **Default**: `10`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/Newton/force_psd_projection` (`bool`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/Newton/force_psd_projection
                        ```
                        <h2>Description</h2>
                        Force the Hessian to be PSD when using second order solvers (i.e., Newton's method).
                    
                        **Default**: `False`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/Newton/use_psd_projection` (`bool`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/Newton/use_psd_projection
                        ```
                        <h2>Description</h2>
                        Use PSD as fallback using second order solvers (i.e., Newton's method).
                    
                        **Default**: `True`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/Newton/use_psd_projection_in_regularized` (`bool`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/Newton/use_psd_projection_in_regularized
                        ```
                        <h2>Description</h2>
                        Use PSD in regularized Newton.
                    
                        **Default**: `True`











                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/ADAM` (`object`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/ADAM
                    ```
                    <h2>Description</h2>
                    Options for ADAM.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/ADAM/alpha` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/ADAM/alpha
                        ```
                        <h2>Description</h2>
                        Parameter alpha for ADAM.
                    
                        **Default**: `0.001`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/ADAM/beta_1` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/ADAM/beta_1
                        ```
                        <h2>Description</h2>
                        Parameter beta_1 for ADAM.
                    
                        **Default**: `0.9`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/ADAM/beta_2` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/ADAM/beta_2
                        ```
                        <h2>Description</h2>
                        Parameter beta_2 for ADAM.
                    
                        **Default**: `0.999`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/ADAM/epsilon` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/ADAM/epsilon
                        ```
                        <h2>Description</h2>
                        Parameter epsilon for ADAM.
                    
                        **Default**: `1e-08`











                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/StochasticADAM` (`object`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/StochasticADAM
                    ```
                    <h2>Description</h2>
                    Options for ADAM.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/StochasticADAM/alpha` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/StochasticADAM/alpha
                        ```
                        <h2>Description</h2>
                        Parameter alpha for ADAM.
                    
                        **Default**: `0.001`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/StochasticADAM/beta_1` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/StochasticADAM/beta_1
                        ```
                        <h2>Description</h2>
                        Parameter beta_1 for ADAM.
                    
                        **Default**: `0.9`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/StochasticADAM/beta_2` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/StochasticADAM/beta_2
                        ```
                        <h2>Description</h2>
                        Parameter beta_2 for ADAM.
                    
                        **Default**: `0.999`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/StochasticADAM/epsilon` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/StochasticADAM/epsilon
                        ```
                        <h2>Description</h2>
                        Parameter epsilon for ADAM.
                    
                        **Default**: `1e-08`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/StochasticADAM/erase_component_probability` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/StochasticADAM/erase_component_probability
                        ```
                        <h2>Description</h2>
                        Probability of erasing a component on the gradient for ADAM.
                    
                        **Default**: `0.3`











                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/StochasticGradientDescent` (`object`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/StochasticGradientDescent
                    ```
                    <h2>Description</h2>
                    Options for Stochastic Gradient Descent.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/StochasticGradientDescent/erase_component_probability` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/StochasticGradientDescent/erase_component_probability
                        ```
                        <h2>Description</h2>
                        Probability of erasing a component on the gradient for StochasticGradientDescent.
                    
                        **Default**: `0.3`











                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/box_constraints` (`object`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/box_constraints
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/box_constraints/bounds` (`list`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/box_constraints/bounds
                        ```
                        <h2>Description</h2>
                        Box constraints on optimization variables.



                        ??? json-spec "`/solver/augmented_lagrangian/nonlinear/box_constraints/bounds/*`"
                            ```
                            /solver/augmented_lagrangian/nonlinear/box_constraints/bounds/*
                            ```


                            === "`/solver/augmented_lagrangian/nonlinear/box_constraints/bounds/*` (`list`)"
                                <h2>Description</h2>
                                Box constraint values on optimization variables.





                                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/box_constraints/bounds/*/*` (`float`)"
                                    ```
                                    /solver/augmented_lagrangian/nonlinear/box_constraints/bounds/*/*
                                    ```
                                    <h2>Description</h2>
                                    Box constraint values on optimization variables.






                            === "`/solver/augmented_lagrangian/nonlinear/box_constraints/bounds/*` (`float`)"
                                <h2>Description</h2>
                                Box constraint values on optimization variables.









                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/box_constraints/max_change`"
                        ```
                        /solver/augmented_lagrangian/nonlinear/box_constraints/max_change
                        ```


                        === "`/solver/augmented_lagrangian/nonlinear/box_constraints/max_change` (`float`)"
                            <h2>Description</h2>
                            Maximum change of optimization variables in one iteration, only for solvers with box constraints. Negative value to disable this constraint.
                        
                            **Default**: `-1`



                        === "`/solver/augmented_lagrangian/nonlinear/box_constraints/max_change` (`list`)"
                            <h2>Description</h2>
                            Maximum change of optimization variables in one iteration, only for solvers with box constraints.





                            ??? json-spec "`/solver/augmented_lagrangian/nonlinear/box_constraints/max_change/*` (`float`)"
                                ```
                                /solver/augmented_lagrangian/nonlinear/box_constraints/max_change/*
                                ```
                                <h2>Description</h2>
                                Maximum change of every optimization variable in one iteration, only for solvers with box constraints.














                ??? json-spec "`/solver/augmented_lagrangian/nonlinear/advanced` (`object`)"
                    ```
                    /solver/augmented_lagrangian/nonlinear/advanced
                    ```
                    <h2>Description</h2>
                    Nonlinear solver advanced options
                
                    **Default**: `None`
                    <h2>Optional</h2>





                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/advanced/f_delta` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/advanced/f_delta
                        ```
                        <h2>Description</h2>
                        Dangerous Option: Quit the optimization if the solver reduces the energy by less than f_delta for consecutive f_delta_step_tol steps.
                    
                        **Default**: `0`
                    
                        **Range:** `[0, inf]`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/advanced/f_delta_step_tol` (`int`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/advanced/f_delta_step_tol
                        ```
                        <h2>Description</h2>
                        Dangerous Option: Quit the optimization if the solver reduces the energy by less than f_delta for consecutive f_delta_step_tol steps.
                    
                        **Default**: `100`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/advanced/derivative_along_delta_x_tol` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/advanced/derivative_along_delta_x_tol
                        ```
                        <h2>Description</h2>
                        Quit the optimization if the directional derivative along the descent direction is smaller than this tolerance.
                    
                        **Default**: `0`
                    
                        **Range:** `[0, inf]`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/advanced/apply_gradient_fd` (`string`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/advanced/apply_gradient_fd
                        ```
                        <h2>Description</h2>
                        Expensive Option: For every iteration of the nonlinear solver, run finite difference to verify gradient of energy.
                    
                        **Default**: `'None'`
                    
                        **Options:** `['None', 'DirectionalDerivative', 'FullFiniteDiff']`








                    ??? json-spec "`/solver/augmented_lagrangian/nonlinear/advanced/gradient_fd_eps` (`float`)"
                        ```
                        /solver/augmented_lagrangian/nonlinear/advanced/gradient_fd_eps
                        ```
                        <h2>Description</h2>
                        Expensive Option: Eps for finite difference to verify gradient of energy.
                    
                        **Default**: `1e-07`

















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
                
                    **Options:** `['hash_grid', 'HG', 'brute_force', 'BF', 'spatial_hash', 'SH', 'bvh', 'BVH', 'sweep_and_prune', 'SAP', 'sweep_and_tiniest_queue', 'STQ']`








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











        ??? json-spec "`/solver/rayleigh_damping` (`list`)"
            ```
            /solver/rayleigh_damping
            ```
            <h2>Description</h2>
            Apply Rayleigh damping.



            ??? json-spec "`/solver/rayleigh_damping/*`"
                ```
                /solver/rayleigh_damping/*
                ```


                === "`/solver/rayleigh_damping/*` (`object`)"
                    <h2>Description</h2>
                    Apply Rayleigh damping to the given Form with a stiffness ratio.
                    <h2>Required</h2>





                    ??? json-spec "`/solver/rayleigh_damping/*/form` (`string`)"
                        ```
                        /solver/rayleigh_damping/*/form
                        ```
                        <h2>Description</h2>
                        Form to damp.
                    
                        **Options:** `['elasticity', 'contact', 'friction']`








                    ??? json-spec "`/solver/rayleigh_damping/*/stiffness_ratio` (`float`)"
                        ```
                        /solver/rayleigh_damping/*/stiffness_ratio
                        ```
                        <h2>Description</h2>
                        Ratio of to damp (stiffness = 0.75 * stiffness_ratio * Δt³).
                    
                        **Range:** `[0, inf]`



                    <h2>Optional</h2>





                    ??? json-spec "`/solver/rayleigh_damping/*/lagging_iterations` (`int`)"
                        ```
                        /solver/rayleigh_damping/*/lagging_iterations
                        ```
                        <h2>Description</h2>
                        Maximum number of update iterations for lagging.
                    
                        **Default**: `1`






                === "`/solver/rayleigh_damping/*` (`object`)"
                    <h2>Description</h2>
                    Apply Rayleigh damping to the given Form with a stiffness.
                    <h2>Required</h2>





                    ??? json-spec "`/solver/rayleigh_damping/*/form` (`string`)"
                        ```
                        /solver/rayleigh_damping/*/form
                        ```
                        <h2>Description</h2>
                        Form to damp.
                    
                        **Options:** `['elasticity', 'contact', 'friction']`








                    ??? json-spec "`/solver/rayleigh_damping/*/stiffness` (`float`)"
                        ```
                        /solver/rayleigh_damping/*/stiffness
                        ```
                        <h2>Description</h2>
                        Ratio of to damp.
                    
                        **Range:** `[0, inf]`



                    <h2>Optional</h2>





                    ??? json-spec "`/solver/rayleigh_damping/*/lagging_iterations` (`int`)"
                        ```
                        /solver/rayleigh_damping/*/lagging_iterations
                        ```
                        <h2>Description</h2>
                        Maximum number of update iterations for lagging.
                    
                        **Default**: `1`














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








            ??? json-spec "`/solver/advanced/lagged_regularization_iterations` (`int`)"
                ```
                /solver/advanced/lagged_regularization_iterations
                ```
                <h2>Description</h2>
                Number of regularize singular static problems.
            
                **Default**: `1`














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
                Value as a constant float



            === "`/boundary_conditions/rhs` (`string`)"
                <h2>Description</h2>
                Value as an expression of $x,y,z,t$ or a file



            === "`/boundary_conditions/rhs` (`object`)"
                <h2>Description</h2>
                Value with unit
                <h2>Required</h2>



                ??? json-spec "`/boundary_conditions/rhs/value`"
                    ```
                    /boundary_conditions/rhs/value
                    ```


                    === "`/boundary_conditions/rhs/value` (`float`)"
                        <h2>Description</h2>
                        The value of the constant



                    === "`/boundary_conditions/rhs/value` (`string`)"
                        <h2>Description</h2>
                        The value as an expression



                    === "`/boundary_conditions/rhs/value` (`file`)"
                        <h2>Description</h2>
                        The value as a file








                ??? json-spec "`/boundary_conditions/rhs/unit` (`string`)"
                    ```
                    /boundary_conditions/rhs/unit
                    ```
                    <h2>Description</h2>
                    The unit of the Value






            === "`/boundary_conditions/rhs` (`list`)"
                <h2>Description</h2>
                Right-hand side of the system being solved for vector-valued PDEs.



                ??? json-spec "`/boundary_conditions/rhs/*`"
                    ```
                    /boundary_conditions/rhs/*
                    ```


                    === "`/boundary_conditions/rhs/*` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float
                    
                        **Default**: `0`



                    === "`/boundary_conditions/rhs/*` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/boundary_conditions/rhs/*` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/boundary_conditions/rhs/*/value`"
                            ```
                            /boundary_conditions/rhs/*/value
                            ```


                            === "`/boundary_conditions/rhs/*/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/boundary_conditions/rhs/*/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/boundary_conditions/rhs/*/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/boundary_conditions/rhs/*/unit` (`string`)"
                            ```
                            /boundary_conditions/rhs/*/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value














        ??? json-spec "`/boundary_conditions/dirichlet_boundary` (`list`)"
            ```
            /boundary_conditions/dirichlet_boundary
            ```
            <h2>Description</h2>
            The list of boundary conditions for the main variable. Elements of the list are assignment pairs (ID, value) where ID is assigned by surface selection.



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
                            ID of boundary condition from surface selection.
                        
                            **Range:** `[0, 2147483646]`



                        === "`/boundary_conditions/dirichlet_boundary/*/id` (`string`)"
                            <h2>Description</h2>
                            select all ids.
                        
                            **Options:** `['all']`








                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value` (`list`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/value
                        ```
                        <h2>Description</h2>
                        Values of boundary condition, length 1 for scalar-valued pde, 2/3 for vector-valued PDEs depending on the dimension.



                        ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value/*`"
                            ```
                            /boundary_conditions/dirichlet_boundary/*/value/*
                            ```


                            === "`/boundary_conditions/dirichlet_boundary/*/value/*` (`float`)"
                                <h2>Description</h2>
                                Value as a constant float



                            === "`/boundary_conditions/dirichlet_boundary/*/value/*` (`string`)"
                                <h2>Description</h2>
                                Value as an expression of $x,y,z,t$ or a file



                            === "`/boundary_conditions/dirichlet_boundary/*/value/*` (`object`)"
                                <h2>Description</h2>
                                Value with unit
                                <h2>Required</h2>



                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value/*/value`"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/value/*/value
                                    ```


                                    === "`/boundary_conditions/dirichlet_boundary/*/value/*/value` (`float`)"
                                        <h2>Description</h2>
                                        The value of the constant



                                    === "`/boundary_conditions/dirichlet_boundary/*/value/*/value` (`string`)"
                                        <h2>Description</h2>
                                        The value as an expression



                                    === "`/boundary_conditions/dirichlet_boundary/*/value/*/value` (`file`)"
                                        <h2>Description</h2>
                                        The value as a file








                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value/*/unit` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/value/*/unit
                                    ```
                                    <h2>Description</h2>
                                    The unit of the Value






                            === "`/boundary_conditions/dirichlet_boundary/*/value/*` (`list`)"
                                <h2>Description</h2>
                                Dirichlet boundary condition specified per timestep.



                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value/*/*`"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/value/*/*
                                    ```


                                    === "`/boundary_conditions/dirichlet_boundary/*/value/*/*` (`float`)"
                                        <h2>Description</h2>
                                        Value as a constant float
                                    
                                        **Default**: `0`



                                    === "`/boundary_conditions/dirichlet_boundary/*/value/*/*` (`string`)"
                                        <h2>Description</h2>
                                        Value as an expression of $x,y,z,t$ or a file



                                    === "`/boundary_conditions/dirichlet_boundary/*/value/*/*` (`object`)"
                                        <h2>Description</h2>
                                        Value with unit
                                        <h2>Required</h2>



                                        ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value/*/*/value`"
                                            ```
                                            /boundary_conditions/dirichlet_boundary/*/value/*/*/value
                                            ```


                                            === "`/boundary_conditions/dirichlet_boundary/*/value/*/*/value` (`float`)"
                                                <h2>Description</h2>
                                                The value of the constant



                                            === "`/boundary_conditions/dirichlet_boundary/*/value/*/*/value` (`string`)"
                                                <h2>Description</h2>
                                                The value as an expression



                                            === "`/boundary_conditions/dirichlet_boundary/*/value/*/*/value` (`file`)"
                                                <h2>Description</h2>
                                                The value as a file








                                        ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/value/*/*/unit` (`string`)"
                                            ```
                                            /boundary_conditions/dirichlet_boundary/*/value/*/*/unit
                                            ```
                                            <h2>Description</h2>
                                            The unit of the Value












                    <h2>Optional</h2>





                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/time_reference` (`list`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/time_reference
                        ```
                        <h2>Description</h2>
                        List of times when the Dirichlet boundary condition is specified





                        ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/time_reference/*` (`float`)"
                            ```
                            /boundary_conditions/dirichlet_boundary/*/time_reference/*
                            ```
                            <h2>Description</h2>
                            Values of Dirichlet boundary condition for timestep











                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation` (`list`)"
                        ```
                        /boundary_conditions/dirichlet_boundary/*/interpolation
                        ```
                        <h2>Description</h2>
                        interpolation of boundary condition



                        ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*`"
                            ```
                            /boundary_conditions/dirichlet_boundary/*/interpolation/*
                            ```


                            === "none"
                            
                                **Type**: none
                                <h2>Description</h2>
                                interpolation of boundary condition
                            
                                **Default**: `{'type': 'none'}`
                                <h2>Required</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/type` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/type
                                    ```
                                    <h2>Description</h2>
                                    type of interpolation of boundary condition
                                
                                    **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`






                            === "linear"
                            
                                **Type**: linear
                                <h2>Description</h2>
                                interpolation of boundary condition
                                <h2>Required</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/type` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/type
                                    ```
                                    <h2>Description</h2>
                                    type of interpolation of boundary condition
                                
                                    **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`






                            === "linear_ramp"
                            
                                **Type**: linear_ramp
                                <h2>Description</h2>
                                interpolation of boundary condition
                                <h2>Required</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/type` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/type
                                    ```
                                    <h2>Description</h2>
                                    type of interpolation of boundary condition
                                
                                    **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/to` (`float`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/to
                                    ```
                                    <h2>Description</h2>
                                    interpolation ending time



                                <h2>Optional</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/from` (`float`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/from
                                    ```
                                    <h2>Description</h2>
                                    interpolation starting time
                                
                                    **Default**: `0`






                            === "piecewise_constant"
                            
                                **Type**: piecewise_constant
                                <h2>Description</h2>
                                interpolation of boundary condition
                                <h2>Required</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/type` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/type
                                    ```
                                    <h2>Description</h2>
                                    type of interpolation of boundary condition
                                
                                    **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/points` (`list`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/points
                                    ```
                                    <h2>Description</h2>
                                    interpolation time points





                                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/points/*` (`float`)"
                                        ```
                                        /boundary_conditions/dirichlet_boundary/*/interpolation/*/points/*
                                        ```
                                        <h2>Description</h2>
                                        interpolation time point











                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/values` (`list`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/values
                                    ```
                                    <h2>Description</h2>
                                    interpolation values





                                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/values/*` (`float`)"
                                        ```
                                        /boundary_conditions/dirichlet_boundary/*/interpolation/*/values/*
                                        ```
                                        <h2>Description</h2>
                                        interpolation value






                                <h2>Optional</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/extend` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/extend
                                    ```
                                    <h2>Description</h2>
                                    how to extend the piecewise interpolation
                                
                                    **Default**: `'constant'`
                                
                                    **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`






                            === "piecewise_linear"
                            
                                **Type**: piecewise_linear
                                <h2>Description</h2>
                                interpolation of boundary condition
                                <h2>Required</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/type` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/type
                                    ```
                                    <h2>Description</h2>
                                    type of interpolation of boundary condition
                                
                                    **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/points` (`list`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/points
                                    ```
                                    <h2>Description</h2>
                                    interpolation time points





                                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/points/*` (`float`)"
                                        ```
                                        /boundary_conditions/dirichlet_boundary/*/interpolation/*/points/*
                                        ```
                                        <h2>Description</h2>
                                        interpolation time point











                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/values` (`list`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/values
                                    ```
                                    <h2>Description</h2>
                                    interpolation values





                                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/values/*` (`float`)"
                                        ```
                                        /boundary_conditions/dirichlet_boundary/*/interpolation/*/values/*
                                        ```
                                        <h2>Description</h2>
                                        interpolation value






                                <h2>Optional</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/extend` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/extend
                                    ```
                                    <h2>Description</h2>
                                    how to extend the piecewise interpolation
                                
                                    **Default**: `'constant'`
                                
                                    **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`






                            === "piecewise_cubic"
                            
                                **Type**: piecewise_cubic
                                <h2>Description</h2>
                                interpolation of boundary condition
                                <h2>Required</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/type` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/type
                                    ```
                                    <h2>Description</h2>
                                    type of interpolation of boundary condition
                                
                                    **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/points` (`list`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/points
                                    ```
                                    <h2>Description</h2>
                                    interpolation time points





                                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/points/*` (`float`)"
                                        ```
                                        /boundary_conditions/dirichlet_boundary/*/interpolation/*/points/*
                                        ```
                                        <h2>Description</h2>
                                        interpolation time point











                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/values` (`list`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/values
                                    ```
                                    <h2>Description</h2>
                                    interpolation values





                                    ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/values/*` (`float`)"
                                        ```
                                        /boundary_conditions/dirichlet_boundary/*/interpolation/*/values/*
                                        ```
                                        <h2>Description</h2>
                                        interpolation value






                                <h2>Optional</h2>





                                ??? json-spec "`/boundary_conditions/dirichlet_boundary/*/interpolation/*/extend` (`string`)"
                                    ```
                                    /boundary_conditions/dirichlet_boundary/*/interpolation/*/extend
                                    ```
                                    <h2>Description</h2>
                                    how to extend the piecewise interpolation
                                
                                    **Default**: `'constant'`
                                
                                    **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`














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
            The list of boundary conditions for the main variable. Elements of the list are assignment pairs (ID, value) where ID is assigned by surface selection.





            ??? json-spec "`/boundary_conditions/neumann_boundary/*` (`object`)"
                ```
                /boundary_conditions/neumann_boundary/*
                ```
                <h2>Description</h2>
                Neumann boundary condition
            
                **Default**: `None`
                <h2>Required</h2>



                ??? json-spec "`/boundary_conditions/neumann_boundary/*/id`"
                    ```
                    /boundary_conditions/neumann_boundary/*/id
                    ```


                    === "`/boundary_conditions/neumann_boundary/*/id` (`int`)"
                        <h2>Description</h2>
                        ID of boundary condition from surface selection.
                    
                        **Range:** `[0, 2147483646]`



                    === "`/boundary_conditions/neumann_boundary/*/id` (`string`)"
                        <h2>Description</h2>
                        select all ids.
                    
                        **Options:** `['all']`








                ??? json-spec "`/boundary_conditions/neumann_boundary/*/value` (`list`)"
                    ```
                    /boundary_conditions/neumann_boundary/*/value
                    ```
                    <h2>Description</h2>
                    Values of boundary condition, length 1 for scalar-valued pde, 2/3 for vector-valued PDEs depending on the dimension.



                    ??? json-spec "`/boundary_conditions/neumann_boundary/*/value/*`"
                        ```
                        /boundary_conditions/neumann_boundary/*/value/*
                        ```


                        === "`/boundary_conditions/neumann_boundary/*/value/*` (`float`)"
                            <h2>Description</h2>
                            Value as a constant float



                        === "`/boundary_conditions/neumann_boundary/*/value/*` (`string`)"
                            <h2>Description</h2>
                            Value as an expression of $x,y,z,t$ or a file



                        === "`/boundary_conditions/neumann_boundary/*/value/*` (`object`)"
                            <h2>Description</h2>
                            Value with unit
                            <h2>Required</h2>



                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/value/*/value`"
                                ```
                                /boundary_conditions/neumann_boundary/*/value/*/value
                                ```


                                === "`/boundary_conditions/neumann_boundary/*/value/*/value` (`float`)"
                                    <h2>Description</h2>
                                    The value of the constant



                                === "`/boundary_conditions/neumann_boundary/*/value/*/value` (`string`)"
                                    <h2>Description</h2>
                                    The value as an expression



                                === "`/boundary_conditions/neumann_boundary/*/value/*/value` (`file`)"
                                    <h2>Description</h2>
                                    The value as a file








                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/value/*/unit` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/value/*/unit
                                ```
                                <h2>Description</h2>
                                The unit of the Value









                <h2>Optional</h2>





                ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation` (`list`)"
                    ```
                    /boundary_conditions/neumann_boundary/*/interpolation
                    ```
                    <h2>Description</h2>
                    interpolation of boundary condition



                    ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*`"
                        ```
                        /boundary_conditions/neumann_boundary/*/interpolation/*
                        ```


                        === "none"
                        
                            **Type**: none
                            <h2>Description</h2>
                            interpolation of boundary condition
                        
                            **Default**: `{'type': 'none'}`
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`






                        === "linear"
                        
                            **Type**: linear
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`






                        === "linear_ramp"
                        
                            **Type**: linear_ramp
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/to` (`float`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/to
                                ```
                                <h2>Description</h2>
                                interpolation ending time



                            <h2>Optional</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/from` (`float`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/from
                                ```
                                <h2>Description</h2>
                                interpolation starting time
                            
                                **Default**: `0`






                        === "piecewise_constant"
                        
                            **Type**: piecewise_constant
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/points` (`list`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/points
                                ```
                                <h2>Description</h2>
                                interpolation time points





                                ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/points/*` (`float`)"
                                    ```
                                    /boundary_conditions/neumann_boundary/*/interpolation/*/points/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation time point











                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/values` (`list`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/values
                                ```
                                <h2>Description</h2>
                                interpolation values





                                ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/values/*` (`float`)"
                                    ```
                                    /boundary_conditions/neumann_boundary/*/interpolation/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation value






                            <h2>Optional</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/extend` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/extend
                                ```
                                <h2>Description</h2>
                                how to extend the piecewise interpolation
                            
                                **Default**: `'constant'`
                            
                                **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`






                        === "piecewise_linear"
                        
                            **Type**: piecewise_linear
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/points` (`list`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/points
                                ```
                                <h2>Description</h2>
                                interpolation time points





                                ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/points/*` (`float`)"
                                    ```
                                    /boundary_conditions/neumann_boundary/*/interpolation/*/points/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation time point











                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/values` (`list`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/values
                                ```
                                <h2>Description</h2>
                                interpolation values





                                ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/values/*` (`float`)"
                                    ```
                                    /boundary_conditions/neumann_boundary/*/interpolation/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation value






                            <h2>Optional</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/extend` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/extend
                                ```
                                <h2>Description</h2>
                                how to extend the piecewise interpolation
                            
                                **Default**: `'constant'`
                            
                                **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`






                        === "piecewise_cubic"
                        
                            **Type**: piecewise_cubic
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/points` (`list`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/points
                                ```
                                <h2>Description</h2>
                                interpolation time points





                                ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/points/*` (`float`)"
                                    ```
                                    /boundary_conditions/neumann_boundary/*/interpolation/*/points/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation time point











                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/values` (`list`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/values
                                ```
                                <h2>Description</h2>
                                interpolation values





                                ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/values/*` (`float`)"
                                    ```
                                    /boundary_conditions/neumann_boundary/*/interpolation/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation value






                            <h2>Optional</h2>





                            ??? json-spec "`/boundary_conditions/neumann_boundary/*/interpolation/*/extend` (`string`)"
                                ```
                                /boundary_conditions/neumann_boundary/*/interpolation/*/extend
                                ```
                                <h2>Description</h2>
                                how to extend the piecewise interpolation
                            
                                **Default**: `'constant'`
                            
                                **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`




















        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary` (`list`)"
            ```
            /boundary_conditions/normal_aligned_neumann_boundary
            ```
            <h2>Description</h2>
            Neumann boundary condition for normal times value for vector-valued PDEs.





            ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*` (`object`)"
                ```
                /boundary_conditions/normal_aligned_neumann_boundary/*
                ```
                <h2>Description</h2>
                pressure BC entry
            
                **Default**: `None`
                <h2>Required</h2>





                ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/id` (`int`)"
                    ```
                    /boundary_conditions/normal_aligned_neumann_boundary/*/id
                    ```
                    <h2>Description</h2>
                    ID for the pressure Neumann boundary condition
                
                    **Range:** `[0, 2147483646]`






                ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/value`"
                    ```
                    /boundary_conditions/normal_aligned_neumann_boundary/*/value
                    ```


                    === "`/boundary_conditions/normal_aligned_neumann_boundary/*/value` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/boundary_conditions/normal_aligned_neumann_boundary/*/value` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/boundary_conditions/normal_aligned_neumann_boundary/*/value` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/value/value`"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/value/value
                            ```


                            === "`/boundary_conditions/normal_aligned_neumann_boundary/*/value/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/boundary_conditions/normal_aligned_neumann_boundary/*/value/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/boundary_conditions/normal_aligned_neumann_boundary/*/value/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/value/unit` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/value/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                <h2>Optional</h2>



                ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation`"
                    ```
                    /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation
                    ```


                    === "none"
                    
                        **Type**: none
                        <h2>Description</h2>
                        interpolation of boundary condition
                    
                        **Default**: `{'type': 'none'}`
                        <h2>Required</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type
                            ```
                            <h2>Description</h2>
                            type of interpolation of boundary condition
                        
                            **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`






                    === "linear"
                    
                        **Type**: linear
                        <h2>Description</h2>
                        interpolation of boundary condition
                        <h2>Required</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type
                            ```
                            <h2>Description</h2>
                            type of interpolation of boundary condition
                        
                            **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`






                    === "linear_ramp"
                    
                        **Type**: linear_ramp
                        <h2>Description</h2>
                        interpolation of boundary condition
                        <h2>Required</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type
                            ```
                            <h2>Description</h2>
                            type of interpolation of boundary condition
                        
                            **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/to` (`float`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/to
                            ```
                            <h2>Description</h2>
                            interpolation ending time



                        <h2>Optional</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/from` (`float`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/from
                            ```
                            <h2>Description</h2>
                            interpolation starting time
                        
                            **Default**: `0`






                    === "piecewise_constant"
                    
                        **Type**: piecewise_constant
                        <h2>Description</h2>
                        interpolation of boundary condition
                        <h2>Required</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type
                            ```
                            <h2>Description</h2>
                            type of interpolation of boundary condition
                        
                            **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points` (`list`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points
                            ```
                            <h2>Description</h2>
                            interpolation time points





                            ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points/*` (`float`)"
                                ```
                                /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points/*
                                ```
                                <h2>Description</h2>
                                interpolation time point











                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values` (`list`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values
                            ```
                            <h2>Description</h2>
                            interpolation values





                            ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values/*` (`float`)"
                                ```
                                /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values/*
                                ```
                                <h2>Description</h2>
                                interpolation value






                        <h2>Optional</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/extend` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/extend
                            ```
                            <h2>Description</h2>
                            how to extend the piecewise interpolation
                        
                            **Default**: `'constant'`
                        
                            **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`






                    === "piecewise_linear"
                    
                        **Type**: piecewise_linear
                        <h2>Description</h2>
                        interpolation of boundary condition
                        <h2>Required</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type
                            ```
                            <h2>Description</h2>
                            type of interpolation of boundary condition
                        
                            **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points` (`list`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points
                            ```
                            <h2>Description</h2>
                            interpolation time points





                            ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points/*` (`float`)"
                                ```
                                /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points/*
                                ```
                                <h2>Description</h2>
                                interpolation time point











                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values` (`list`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values
                            ```
                            <h2>Description</h2>
                            interpolation values





                            ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values/*` (`float`)"
                                ```
                                /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values/*
                                ```
                                <h2>Description</h2>
                                interpolation value






                        <h2>Optional</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/extend` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/extend
                            ```
                            <h2>Description</h2>
                            how to extend the piecewise interpolation
                        
                            **Default**: `'constant'`
                        
                            **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`






                    === "piecewise_cubic"
                    
                        **Type**: piecewise_cubic
                        <h2>Description</h2>
                        interpolation of boundary condition
                        <h2>Required</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/type
                            ```
                            <h2>Description</h2>
                            type of interpolation of boundary condition
                        
                            **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points` (`list`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points
                            ```
                            <h2>Description</h2>
                            interpolation time points





                            ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points/*` (`float`)"
                                ```
                                /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/points/*
                                ```
                                <h2>Description</h2>
                                interpolation time point











                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values` (`list`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values
                            ```
                            <h2>Description</h2>
                            interpolation values





                            ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values/*` (`float`)"
                                ```
                                /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/values/*
                                ```
                                <h2>Description</h2>
                                interpolation value






                        <h2>Optional</h2>





                        ??? json-spec "`/boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/extend` (`string`)"
                            ```
                            /boundary_conditions/normal_aligned_neumann_boundary/*/interpolation/extend
                            ```
                            <h2>Description</h2>
                            how to extend the piecewise interpolation
                        
                            **Default**: `'constant'`
                        
                            **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`

















        ??? json-spec "`/boundary_conditions/pressure_boundary` (`list`)"
            ```
            /boundary_conditions/pressure_boundary
            ```
            <h2>Description</h2>
            Neumann boundary condition for normal times value for vector-valued PDEs.





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
                
                    **Range:** `[0, 2147483646]`






                ??? json-spec "`/boundary_conditions/pressure_boundary/*/value`"
                    ```
                    /boundary_conditions/pressure_boundary/*/value
                    ```


                    === "`/boundary_conditions/pressure_boundary/*/value` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/boundary_conditions/pressure_boundary/*/value` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/boundary_conditions/pressure_boundary/*/value` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/boundary_conditions/pressure_boundary/*/value/value`"
                            ```
                            /boundary_conditions/pressure_boundary/*/value/value
                            ```


                            === "`/boundary_conditions/pressure_boundary/*/value/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/boundary_conditions/pressure_boundary/*/value/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/boundary_conditions/pressure_boundary/*/value/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/boundary_conditions/pressure_boundary/*/value/unit` (`string`)"
                            ```
                            /boundary_conditions/pressure_boundary/*/value/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value






                    === "`/boundary_conditions/pressure_boundary/*/value` (`list`)"
                        <h2>Description</h2>
                        Values of pressure boundary condition specified per timestep



                        ??? json-spec "`/boundary_conditions/pressure_boundary/*/value/*`"
                            ```
                            /boundary_conditions/pressure_boundary/*/value/*
                            ```


                            === "`/boundary_conditions/pressure_boundary/*/value/*` (`float`)"
                                <h2>Description</h2>
                                Value as a constant float
                            
                                **Default**: `0`



                            === "`/boundary_conditions/pressure_boundary/*/value/*` (`string`)"
                                <h2>Description</h2>
                                Value as an expression of $x,y,z,t$ or a file



                            === "`/boundary_conditions/pressure_boundary/*/value/*` (`object`)"
                                <h2>Description</h2>
                                Value with unit
                                <h2>Required</h2>



                                ??? json-spec "`/boundary_conditions/pressure_boundary/*/value/*/value`"
                                    ```
                                    /boundary_conditions/pressure_boundary/*/value/*/value
                                    ```


                                    === "`/boundary_conditions/pressure_boundary/*/value/*/value` (`float`)"
                                        <h2>Description</h2>
                                        The value of the constant



                                    === "`/boundary_conditions/pressure_boundary/*/value/*/value` (`string`)"
                                        <h2>Description</h2>
                                        The value as an expression



                                    === "`/boundary_conditions/pressure_boundary/*/value/*/value` (`file`)"
                                        <h2>Description</h2>
                                        The value as a file








                                ??? json-spec "`/boundary_conditions/pressure_boundary/*/value/*/unit` (`string`)"
                                    ```
                                    /boundary_conditions/pressure_boundary/*/value/*/unit
                                    ```
                                    <h2>Description</h2>
                                    The unit of the Value









                <h2>Optional</h2>





                ??? json-spec "`/boundary_conditions/pressure_boundary/*/time_reference` (`list`)"
                    ```
                    /boundary_conditions/pressure_boundary/*/time_reference
                    ```
                    <h2>Description</h2>
                    List of times when the pressure boundary condition is specified





                    ??? json-spec "`/boundary_conditions/pressure_boundary/*/time_reference/*` (`float`)"
                        ```
                        /boundary_conditions/pressure_boundary/*/time_reference/*
                        ```
                        <h2>Description</h2>
                        Values of pressure boundary condition for timestep

















        ??? json-spec "`/boundary_conditions/pressure_cavity` (`list`)"
            ```
            /boundary_conditions/pressure_cavity
            ```
            <h2>Description</h2>
            Neumann boundary condition for normal times value for vector-valued PDEs.





            ??? json-spec "`/boundary_conditions/pressure_cavity/*` (`object`)"
                ```
                /boundary_conditions/pressure_cavity/*
                ```
                <h2>Description</h2>
                pressure BC entry
            
                **Default**: `None`
                <h2>Required</h2>





                ??? json-spec "`/boundary_conditions/pressure_cavity/*/id` (`int`)"
                    ```
                    /boundary_conditions/pressure_cavity/*/id
                    ```
                    <h2>Description</h2>
                    ID for the pressure Neumann boundary condition
                
                    **Range:** `[0, 2147483646]`






                ??? json-spec "`/boundary_conditions/pressure_cavity/*/value`"
                    ```
                    /boundary_conditions/pressure_cavity/*/value
                    ```


                    === "`/boundary_conditions/pressure_cavity/*/value` (`float`)"
                        <h2>Description</h2>
                        Value as a constant float



                    === "`/boundary_conditions/pressure_cavity/*/value` (`string`)"
                        <h2>Description</h2>
                        Value as an expression of $x,y,z,t$ or a file



                    === "`/boundary_conditions/pressure_cavity/*/value` (`object`)"
                        <h2>Description</h2>
                        Value with unit
                        <h2>Required</h2>



                        ??? json-spec "`/boundary_conditions/pressure_cavity/*/value/value`"
                            ```
                            /boundary_conditions/pressure_cavity/*/value/value
                            ```


                            === "`/boundary_conditions/pressure_cavity/*/value/value` (`float`)"
                                <h2>Description</h2>
                                The value of the constant



                            === "`/boundary_conditions/pressure_cavity/*/value/value` (`string`)"
                                <h2>Description</h2>
                                The value as an expression



                            === "`/boundary_conditions/pressure_cavity/*/value/value` (`file`)"
                                <h2>Description</h2>
                                The value as a file








                        ??? json-spec "`/boundary_conditions/pressure_cavity/*/value/unit` (`string`)"
                            ```
                            /boundary_conditions/pressure_cavity/*/value/unit
                            ```
                            <h2>Description</h2>
                            The unit of the Value

















        ??? json-spec "`/boundary_conditions/obstacle_displacements` (`list`)"
            ```
            /boundary_conditions/obstacle_displacements
            ```
            <h2>Description</h2>
            The list of boundary conditions for the main variable. Elements of the list are assignment pairs (ID, value) where ID is assigned by surface selection.





            ??? json-spec "`/boundary_conditions/obstacle_displacements/*` (`object`)"
                ```
                /boundary_conditions/obstacle_displacements/*
                ```
                <h2>Description</h2>
                Obstacle displacements
            
                **Default**: `None`
                <h2>Required</h2>



                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/id`"
                    ```
                    /boundary_conditions/obstacle_displacements/*/id
                    ```


                    === "`/boundary_conditions/obstacle_displacements/*/id` (`int`)"
                        <h2>Description</h2>
                        ID of boundary condition from surface selection.
                    
                        **Range:** `[0, 2147483646]`



                    === "`/boundary_conditions/obstacle_displacements/*/id` (`string`)"
                        <h2>Description</h2>
                        select all ids.
                    
                        **Options:** `['all']`








                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/value` (`list`)"
                    ```
                    /boundary_conditions/obstacle_displacements/*/value
                    ```
                    <h2>Description</h2>
                    Values of boundary condition, length 1 for scalar-valued pde, 2/3 for vector-valued PDEs depending on the dimension.



                    ??? json-spec "`/boundary_conditions/obstacle_displacements/*/value/*`"
                        ```
                        /boundary_conditions/obstacle_displacements/*/value/*
                        ```


                        === "`/boundary_conditions/obstacle_displacements/*/value/*` (`float`)"
                            <h2>Description</h2>
                            Value as a constant float



                        === "`/boundary_conditions/obstacle_displacements/*/value/*` (`string`)"
                            <h2>Description</h2>
                            Value as an expression of $x,y,z,t$ or a file



                        === "`/boundary_conditions/obstacle_displacements/*/value/*` (`object`)"
                            <h2>Description</h2>
                            Value with unit
                            <h2>Required</h2>



                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/value/*/value`"
                                ```
                                /boundary_conditions/obstacle_displacements/*/value/*/value
                                ```


                                === "`/boundary_conditions/obstacle_displacements/*/value/*/value` (`float`)"
                                    <h2>Description</h2>
                                    The value of the constant



                                === "`/boundary_conditions/obstacle_displacements/*/value/*/value` (`string`)"
                                    <h2>Description</h2>
                                    The value as an expression



                                === "`/boundary_conditions/obstacle_displacements/*/value/*/value` (`file`)"
                                    <h2>Description</h2>
                                    The value as a file








                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/value/*/unit` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/value/*/unit
                                ```
                                <h2>Description</h2>
                                The unit of the Value









                <h2>Optional</h2>





                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation` (`list`)"
                    ```
                    /boundary_conditions/obstacle_displacements/*/interpolation
                    ```
                    <h2>Description</h2>
                    interpolation of boundary condition



                    ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*`"
                        ```
                        /boundary_conditions/obstacle_displacements/*/interpolation/*
                        ```


                        === "none"
                        
                            **Type**: none
                            <h2>Description</h2>
                            interpolation of boundary condition
                        
                            **Default**: `{'type': 'none'}`
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`






                        === "linear"
                        
                            **Type**: linear
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`






                        === "linear_ramp"
                        
                            **Type**: linear_ramp
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/to` (`float`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/to
                                ```
                                <h2>Description</h2>
                                interpolation ending time



                            <h2>Optional</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/from` (`float`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/from
                                ```
                                <h2>Description</h2>
                                interpolation starting time
                            
                                **Default**: `0`






                        === "piecewise_constant"
                        
                            **Type**: piecewise_constant
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/points` (`list`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/points
                                ```
                                <h2>Description</h2>
                                interpolation time points





                                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/points/*` (`float`)"
                                    ```
                                    /boundary_conditions/obstacle_displacements/*/interpolation/*/points/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation time point











                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/values` (`list`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/values
                                ```
                                <h2>Description</h2>
                                interpolation values





                                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/values/*` (`float`)"
                                    ```
                                    /boundary_conditions/obstacle_displacements/*/interpolation/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation value






                            <h2>Optional</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/extend` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/extend
                                ```
                                <h2>Description</h2>
                                how to extend the piecewise interpolation
                            
                                **Default**: `'constant'`
                            
                                **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`






                        === "piecewise_linear"
                        
                            **Type**: piecewise_linear
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/points` (`list`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/points
                                ```
                                <h2>Description</h2>
                                interpolation time points





                                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/points/*` (`float`)"
                                    ```
                                    /boundary_conditions/obstacle_displacements/*/interpolation/*/points/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation time point











                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/values` (`list`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/values
                                ```
                                <h2>Description</h2>
                                interpolation values





                                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/values/*` (`float`)"
                                    ```
                                    /boundary_conditions/obstacle_displacements/*/interpolation/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation value






                            <h2>Optional</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/extend` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/extend
                                ```
                                <h2>Description</h2>
                                how to extend the piecewise interpolation
                            
                                **Default**: `'constant'`
                            
                                **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`






                        === "piecewise_cubic"
                        
                            **Type**: piecewise_cubic
                            <h2>Description</h2>
                            interpolation of boundary condition
                            <h2>Required</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/type` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/type
                                ```
                                <h2>Description</h2>
                                type of interpolation of boundary condition
                            
                                **Options:** `['none', 'linear', 'linear_ramp', 'piecewise_constant', 'piecewise_linear', 'piecewise_cubic']`








                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/points` (`list`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/points
                                ```
                                <h2>Description</h2>
                                interpolation time points





                                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/points/*` (`float`)"
                                    ```
                                    /boundary_conditions/obstacle_displacements/*/interpolation/*/points/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation time point











                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/values` (`list`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/values
                                ```
                                <h2>Description</h2>
                                interpolation values





                                ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/values/*` (`float`)"
                                    ```
                                    /boundary_conditions/obstacle_displacements/*/interpolation/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    interpolation value






                            <h2>Optional</h2>





                            ??? json-spec "`/boundary_conditions/obstacle_displacements/*/interpolation/*/extend` (`string`)"
                                ```
                                /boundary_conditions/obstacle_displacements/*/interpolation/*/extend
                                ```
                                <h2>Description</h2>
                                how to extend the piecewise interpolation
                            
                                **Default**: `'constant'`
                            
                                **Options:** `['constant', 'extrapolate', 'repeat', 'repeat_offset']`




















        ??? json-spec "`/boundary_conditions/periodic_boundary` (`object`)"
            ```
            /boundary_conditions/periodic_boundary
            ```
            <h2>Description</h2>
            Options for periodic boundary conditions.
        
            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/boundary_conditions/periodic_boundary/enabled` (`bool`)"
                ```
                /boundary_conditions/periodic_boundary/enabled
                ```
                <h2>Description</h2>
                
            
                **Default**: `False`








            ??? json-spec "`/boundary_conditions/periodic_boundary/tolerance` (`float`)"
                ```
                /boundary_conditions/periodic_boundary/tolerance
                ```
                <h2>Description</h2>
                Relative tolerance of deciding periodic correspondence
            
                **Default**: `1e-05`








            ??? json-spec "`/boundary_conditions/periodic_boundary/correspondence` (`list`)"
                ```
                /boundary_conditions/periodic_boundary/correspondence
                ```
                <h2>Description</h2>
                Periodic directions for periodic boundary conditions. If not specified, default to axis-aligned directions.





                ??? json-spec "`/boundary_conditions/periodic_boundary/correspondence/*` (`list`)"
                    ```
                    /boundary_conditions/periodic_boundary/correspondence/*
                    ```
                    <h2>Description</h2>
                    One periodic direction.





                    ??? json-spec "`/boundary_conditions/periodic_boundary/correspondence/*/*` (`float`)"
                        ```
                        /boundary_conditions/periodic_boundary/correspondence/*/*
                        ```
                        <h2>Description</h2>
                        One entry of a periodic direction.














            ??? json-spec "`/boundary_conditions/periodic_boundary/linear_displacement_offset` (`list`)"
                ```
                /boundary_conditions/periodic_boundary/linear_displacement_offset
                ```
                <h2>Description</h2>
                





                ??? json-spec "`/boundary_conditions/periodic_boundary/linear_displacement_offset/*` (`list`)"
                    ```
                    /boundary_conditions/periodic_boundary/linear_displacement_offset/*
                    ```
                    <h2>Description</h2>
                    



                    ??? json-spec "`/boundary_conditions/periodic_boundary/linear_displacement_offset/*/*`"
                        ```
                        /boundary_conditions/periodic_boundary/linear_displacement_offset/*/*
                        ```


                        === "`/boundary_conditions/periodic_boundary/linear_displacement_offset/*/*` (`float`)"
                            <h2>Description</h2>
                            



                        === "`/boundary_conditions/periodic_boundary/linear_displacement_offset/*/*` (`string`)"
                            <h2>Description</h2>
                            














            ??? json-spec "`/boundary_conditions/periodic_boundary/fixed_macro_strain` (`list`)"
                ```
                /boundary_conditions/periodic_boundary/fixed_macro_strain
                ```
                <h2>Description</h2>
                





                ??? json-spec "`/boundary_conditions/periodic_boundary/fixed_macro_strain/*` (`int`)"
                    ```
                    /boundary_conditions/periodic_boundary/fixed_macro_strain/*
                    ```
                    <h2>Description</h2>
                    











            ??? json-spec "`/boundary_conditions/periodic_boundary/force_zero_mean` (`bool`)"
                ```
                /boundary_conditions/periodic_boundary/force_zero_mean
                ```
                <h2>Description</h2>
                The periodic solution is not unique, set to true to find the solution with zero mean.
            
                **Default**: `False`














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
                            Value as a constant float



                        === "`/initial_conditions/solution/*/value/*` (`string`)"
                            <h2>Description</h2>
                            Value as an expression of $x,y,z,t$ or a file



                        === "`/initial_conditions/solution/*/value/*` (`object`)"
                            <h2>Description</h2>
                            Value with unit
                            <h2>Required</h2>



                            ??? json-spec "`/initial_conditions/solution/*/value/*/value`"
                                ```
                                /initial_conditions/solution/*/value/*/value
                                ```


                                === "`/initial_conditions/solution/*/value/*/value` (`float`)"
                                    <h2>Description</h2>
                                    The value of the constant



                                === "`/initial_conditions/solution/*/value/*/value` (`string`)"
                                    <h2>Description</h2>
                                    The value as an expression



                                === "`/initial_conditions/solution/*/value/*/value` (`file`)"
                                    <h2>Description</h2>
                                    The value as a file








                            ??? json-spec "`/initial_conditions/solution/*/value/*/unit` (`string`)"
                                ```
                                /initial_conditions/solution/*/value/*/unit
                                ```
                                <h2>Description</h2>
                                The unit of the Value




















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
                            Value as a constant float



                        === "`/initial_conditions/velocity/*/value/*` (`string`)"
                            <h2>Description</h2>
                            Value as an expression of $x,y,z,t$ or a file



                        === "`/initial_conditions/velocity/*/value/*` (`object`)"
                            <h2>Description</h2>
                            Value with unit
                            <h2>Required</h2>



                            ??? json-spec "`/initial_conditions/velocity/*/value/*/value`"
                                ```
                                /initial_conditions/velocity/*/value/*/value
                                ```


                                === "`/initial_conditions/velocity/*/value/*/value` (`float`)"
                                    <h2>Description</h2>
                                    The value of the constant



                                === "`/initial_conditions/velocity/*/value/*/value` (`string`)"
                                    <h2>Description</h2>
                                    The value as an expression



                                === "`/initial_conditions/velocity/*/value/*/value` (`file`)"
                                    <h2>Description</h2>
                                    The value as a file








                            ??? json-spec "`/initial_conditions/velocity/*/value/*/unit` (`string`)"
                                ```
                                /initial_conditions/velocity/*/value/*/unit
                                ```
                                <h2>Description</h2>
                                The unit of the Value




















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
                            Value as a constant float



                        === "`/initial_conditions/acceleration/*/value/*` (`string`)"
                            <h2>Description</h2>
                            Value as an expression of $x,y,z,t$ or a file



                        === "`/initial_conditions/acceleration/*/value/*` (`object`)"
                            <h2>Description</h2>
                            Value with unit
                            <h2>Required</h2>



                            ??? json-spec "`/initial_conditions/acceleration/*/value/*/value`"
                                ```
                                /initial_conditions/acceleration/*/value/*/value
                                ```


                                === "`/initial_conditions/acceleration/*/value/*/value` (`float`)"
                                    <h2>Description</h2>
                                    The value of the constant



                                === "`/initial_conditions/acceleration/*/value/*/value` (`string`)"
                                    <h2>Description</h2>
                                    The value as an expression



                                === "`/initial_conditions/acceleration/*/value/*/value` (`file`)"
                                    <h2>Description</h2>
                                    The value as a file








                            ??? json-spec "`/initial_conditions/acceleration/*/value/*/unit` (`string`)"
                                ```
                                /initial_conditions/acceleration/*/value/*/unit
                                ```
                                <h2>Description</h2>
                                The unit of the Value























    ??? json-spec "`/output` (`object`)"
        ```
        /output
        ```
        <h2>Description</h2>
        output settings
    
        **Default**: `None`
        <h2>Optional</h2>





        ??? json-spec "`/output/directory` (`string`)"
            ```
            /output/directory
            ```
            <h2>Description</h2>
            Directory for output files.
        
            **Default**: `''`








        ??? json-spec "`/output/log` (`object`)"
            ```
            /output/log
            ```
            <h2>Description</h2>
            Setting for the output log.
        
            **Default**: `None`
            <h2>Optional</h2>



            ??? json-spec "`/output/log/level`"
                ```
                /output/log/level
                ```


                === "`/output/log/level` (`int`)"
                    <h2>Description</h2>
                    Level of logging, 0 trace, 1 debug, 2 info, 3 warning, 4 error, 5 critical, and 6 off.
                
                    **Range:** `[0, 6]`



                === "`/output/log/level` (`string`)"
                    <h2>Description</h2>
                    Level of logging.
                
                    **Default**: `'debug'`
                
                    **Options:** `['trace', 'debug', 'info', 'warning', 'error', 'critical', 'off']`






            ??? json-spec "`/output/log/file_level`"
                ```
                /output/log/file_level
                ```


                === "`/output/log/file_level` (`int`)"
                    <h2>Description</h2>
                    Level of logging to a file, 0 trace, 1 debug, 2 info, 3 warning, 4 error, 5 critical, and 6 off.
                
                    **Range:** `[0, 6]`



                === "`/output/log/file_level` (`string`)"
                    <h2>Description</h2>
                    Level of logging.
                
                    **Default**: `'trace'`
                
                    **Options:** `['trace', 'debug', 'info', 'warning', 'error', 'critical', 'off']`








            ??? json-spec "`/output/log/path` (`string`)"
                ```
                /output/log/path
                ```
                <h2>Description</h2>
                File where to save the log; empty string is output to terminal.
            
                **Default**: `''`








            ??? json-spec "`/output/log/quiet` (`bool`)"
                ```
                /output/log/quiet
                ```
                <h2>Description</h2>
                Disable cout for logging.
            
                **Default**: `False`











        ??? json-spec "`/output/json` (`string`)"
            ```
            /output/json
            ```
            <h2>Description</h2>
            File name for JSON output statistics on time/error/etc.
        
            **Default**: `''`








        ??? json-spec "`/output/restart_json` (`string`)"
            ```
            /output/restart_json
            ```
            <h2>Description</h2>
            File name for JSON output to restart the simulation.
        
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
                Enables/disables high-order output for paraview. Supported only for isoparametric or linear meshes with high-order solutions.
            
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








            ??? json-spec "`/output/paraview/points` (`bool`)"
                ```
                /output/paraview/points
                ```
                <h2>Description</h2>
                Export the Dirichlet points
            
                **Default**: `False`








            ??? json-spec "`/output/paraview/options` (`object`)"
                ```
                /output/paraview/options
                ```
                <h2>Description</h2>
                Optional fields in the output
            
                **Default**: `None`
                <h2>Optional</h2>





                ??? json-spec "`/output/paraview/options/use_hdf5` (`bool`)"
                    ```
                    /output/paraview/options/use_hdf5
                    ```
                    <h2>Description</h2>
                    If true, export the data as hdf5, compatible with paraview >5.11
                
                    **Default**: `False`








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








                ??? json-spec "`/output/paraview/options/scalar_values` (`bool`)"
                    ```
                    /output/paraview/options/scalar_values
                    ```
                    <h2>Description</h2>
                    If true, write out scalar values
                
                    **Default**: `True`








                ??? json-spec "`/output/paraview/options/tensor_values` (`bool`)"
                    ```
                    /output/paraview/options/tensor_values
                    ```
                    <h2>Description</h2>
                    If true, write out tensor values
                
                    **Default**: `True`








                ??? json-spec "`/output/paraview/options/discretization_order` (`bool`)"
                    ```
                    /output/paraview/options/discretization_order
                    ```
                    <h2>Description</h2>
                    If true, write out discretization order
                
                    **Default**: `True`








                ??? json-spec "`/output/paraview/options/nodes` (`bool`)"
                    ```
                    /output/paraview/options/nodes
                    ```
                    <h2>Description</h2>
                    If true, write out node order
                
                    **Default**: `True`








                ??? json-spec "`/output/paraview/options/forces` (`bool`)"
                    ```
                    /output/paraview/options/forces
                    ```
                    <h2>Description</h2>
                    If true, write out all variational forces on the FE mesh 
                
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








            ??? json-spec "`/output/data/state` (`string`)"
                ```
                /output/data/state
                ```
                <h2>Description</h2>
                Writes the complete state in PolyFEM hdf5 format, used to restart the sim
            
                **Default**: `''`








            ??? json-spec "`/output/data/rest_mesh` (`string`)"
                ```
                /output/data/rest_mesh
                ```
                <h2>Description</h2>
                Writes the rest mesh in MSH format, used to restart the sim
            
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
                Write out solution values at a specific node. the values will be written in the output JSON file
            
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








            ??? json-spec "`/output/advanced/save_ccd_debug_meshes` (`bool`)"
                ```
                /output/advanced/save_ccd_debug_meshes
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
                exports the spectrum of the matrix in the output JSON. Works only if POLYSOLVE_WITH_SPECTRA is enabled
            
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





            ??? json-spec "`/input/data/state` (`file`)"
                ```
                /input/data/state
                ```
                <h2>Description</h2>
                input state as hdf5
            
                **Default**: `''`








            ??? json-spec "`/input/data/reorder` (`bool`)"
                ```
                /input/data/reorder
                ```
                <h2>Description</h2>
                reorder input data
            
                **Default**: `False`














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








