<!--Automatically generated using JSON Spec Engine-->








!!! json-spec "`/` (`object`)"
    ```
    /
    ```
    <h2>Description</h2>
    Root of the configuration file.
    <h2>Required</h2>





    ??? json-spec "`/parameters` (`list`)"
        ```
        /parameters
        ```
        <h2>Description</h2>
        TODO





        ??? json-spec "`/parameters/*` (`object`)"
            ```
            /parameters/*
            ```
            <h2>Description</h2>
            TODO
            <h2>Optional</h2>



            ??? json-spec "`/parameters/*/number`"
                ```
                /parameters/*/number
                ```


                === "`/parameters/*/number` (`int`)"
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.



                === "`/parameters/*/number` (`object`)"
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `None`
                    <h2>Required</h2>













                === "`/parameters/*/number` (`object`)"
                    <h2>Description</h2>
                    TODO
                    <h2>Required</h2>





















            ??? json-spec "`/parameters/*/initial`"
                ```
                /parameters/*/initial
                ```


                === "`/parameters/*/initial` (`list`)"
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.





                    ??? json-spec "`/parameters/*/initial/*` (`float`)"
                        ```
                        /parameters/*/initial/*
                        ```
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.






                === "`/parameters/*/initial` (`float`)"
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.














    ??? json-spec "`/variable_to_simulation` (`list`)"
        ```
        /variable_to_simulation
        ```
        <h2>Description</h2>
        A list of mappings from the raw optimization variable to parameters in states.



        ??? json-spec "`/variable_to_simulation/*`"
            ```
            /variable_to_simulation/*
            ```


            === "shape"
            
                **Type**: shape
                <h2>Description</h2>
                FIXME: Missing documentation in the specification.
                <h2>Required</h2>



                ??? json-spec "`/variable_to_simulation/*/state`"
                    ```
                    /variable_to_simulation/*/state
                    ```


                    === "`/variable_to_simulation/*/state` (`int`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/state` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/state/*` (`int`)"
                            ```
                            /variable_to_simulation/*/state/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.











                ??? json-spec "`/variable_to_simulation/*/type` (`string`)"
                    ```
                    /variable_to_simulation/*/type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Options:** `['shape', 'elastic', 'friction', 'damping', 'macro-strain', 'initial', 'dirichlet', 'pressure']`








                ??? json-spec "`/variable_to_simulation/*/composition` (`list`)"
                    ```
                    /variable_to_simulation/*/composition
                    ```
                    <h2>Description</h2>
                    list of parametrizations that maps raw optimization variables to parameters in simulations



                    ??? json-spec "`/variable_to_simulation/*/composition/*`"
                        ```
                        /variable_to_simulation/*/composition/*
                        ```


                        === "bounded-biharmonic-weights"
                        
                            **Type**: bounded-biharmonic-weights
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>


















                        === "scalar-velocity-parametrization"
                        
                            **Type**: scalar-velocity-parametrization
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>













                        === "append-const"
                        
                            **Type**: append-const
                            <h2>Description</h2>
                            Append repeated constant at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/size` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/size
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/start` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/start
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "append-values"
                        
                            **Type**: append-values
                            <h2>Description</h2>
                            Append a list of constants at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/values` (`list`)"
                                ```
                                /variable_to_simulation/*/composition/*/values
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/variable_to_simulation/*/composition/*/values/*` (`float`)"
                                    ```
                                    /variable_to_simulation/*/composition/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "slice"
                        
                            **Type**: slice
                            <h2>Description</h2>
                            Ouputs x[from:to], where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/parameter_index` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/parameter_index
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/last` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/last
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "power"
                        
                            **Type**: power
                            <h2>Description</h2>
                            Ouputs x ^ power, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/power` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/power
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "exp"
                        
                            **Type**: exp
                            <h2>Description</h2>
                            Ouputs exp(x), where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "scale"
                        
                            **Type**: scale
                            <h2>Description</h2>
                            Ouputs x * value, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-elem"
                        
                            **Type**: per-body-to-per-elem
                            <h2>Description</h2>
                            From per volume selection to per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-node"
                        
                            **Type**: per-body-to-per-node
                            <h2>Description</h2>
                            From per volume selection to per FE node.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "E-nu-to-lambda-mu"
                        
                            **Type**: E-nu-to-lambda-mu
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/is_volume` (`bool`)"
                                ```
                                /variable_to_simulation/*/composition/*/is_volume
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "linear-filter"
                        
                            **Type**: linear-filter
                            <h2>Description</h2>
                            Apply linear smoothing filter on a field per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.













                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`









                <h2>Optional</h2>





                ??? json-spec "`/variable_to_simulation/*/composite_map_type` (`string`)"
                    ```
                    /variable_to_simulation/*/composite_map_type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Default**: `'none'`






                ??? json-spec "`/variable_to_simulation/*/composite_map_indices`"
                    ```
                    /variable_to_simulation/*/composite_map_indices
                    ```


                    === "`/variable_to_simulation/*/composite_map_indices` (`file`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/composite_map_indices` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/composite_map_indices/*` (`int`)"
                            ```
                            /variable_to_simulation/*/composite_map_indices/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.









            === "elastic"
            
                **Type**: elastic
                <h2>Description</h2>
                FIXME: Missing documentation in the specification.
                <h2>Required</h2>



                ??? json-spec "`/variable_to_simulation/*/state`"
                    ```
                    /variable_to_simulation/*/state
                    ```


                    === "`/variable_to_simulation/*/state` (`int`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/state` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/state/*` (`int`)"
                            ```
                            /variable_to_simulation/*/state/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.











                ??? json-spec "`/variable_to_simulation/*/type` (`string`)"
                    ```
                    /variable_to_simulation/*/type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Options:** `['shape', 'elastic', 'friction', 'damping', 'macro-strain', 'initial', 'dirichlet', 'pressure']`








                ??? json-spec "`/variable_to_simulation/*/composition` (`list`)"
                    ```
                    /variable_to_simulation/*/composition
                    ```
                    <h2>Description</h2>
                    list of parametrizations that maps raw optimization variables to parameters in simulations



                    ??? json-spec "`/variable_to_simulation/*/composition/*`"
                        ```
                        /variable_to_simulation/*/composition/*
                        ```


                        === "bounded-biharmonic-weights"
                        
                            **Type**: bounded-biharmonic-weights
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>


















                        === "scalar-velocity-parametrization"
                        
                            **Type**: scalar-velocity-parametrization
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>













                        === "append-const"
                        
                            **Type**: append-const
                            <h2>Description</h2>
                            Append repeated constant at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/size` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/size
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/start` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/start
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "append-values"
                        
                            **Type**: append-values
                            <h2>Description</h2>
                            Append a list of constants at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/values` (`list`)"
                                ```
                                /variable_to_simulation/*/composition/*/values
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/variable_to_simulation/*/composition/*/values/*` (`float`)"
                                    ```
                                    /variable_to_simulation/*/composition/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "slice"
                        
                            **Type**: slice
                            <h2>Description</h2>
                            Ouputs x[from:to], where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/parameter_index` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/parameter_index
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/last` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/last
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "power"
                        
                            **Type**: power
                            <h2>Description</h2>
                            Ouputs x ^ power, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/power` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/power
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "exp"
                        
                            **Type**: exp
                            <h2>Description</h2>
                            Ouputs exp(x), where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "scale"
                        
                            **Type**: scale
                            <h2>Description</h2>
                            Ouputs x * value, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-elem"
                        
                            **Type**: per-body-to-per-elem
                            <h2>Description</h2>
                            From per volume selection to per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-node"
                        
                            **Type**: per-body-to-per-node
                            <h2>Description</h2>
                            From per volume selection to per FE node.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "E-nu-to-lambda-mu"
                        
                            **Type**: E-nu-to-lambda-mu
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/is_volume` (`bool`)"
                                ```
                                /variable_to_simulation/*/composition/*/is_volume
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "linear-filter"
                        
                            **Type**: linear-filter
                            <h2>Description</h2>
                            Apply linear smoothing filter on a field per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.













                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`









                <h2>Optional</h2>





                ??? json-spec "`/variable_to_simulation/*/composite_map_type` (`string`)"
                    ```
                    /variable_to_simulation/*/composite_map_type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Default**: `'none'`






                ??? json-spec "`/variable_to_simulation/*/composite_map_indices`"
                    ```
                    /variable_to_simulation/*/composite_map_indices
                    ```


                    === "`/variable_to_simulation/*/composite_map_indices` (`file`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/composite_map_indices` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/composite_map_indices/*` (`int`)"
                            ```
                            /variable_to_simulation/*/composite_map_indices/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.









            === "friction"
            
                **Type**: friction
                <h2>Description</h2>
                FIXME: Missing documentation in the specification.
                <h2>Required</h2>



                ??? json-spec "`/variable_to_simulation/*/state`"
                    ```
                    /variable_to_simulation/*/state
                    ```


                    === "`/variable_to_simulation/*/state` (`int`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/state` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/state/*` (`int`)"
                            ```
                            /variable_to_simulation/*/state/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.











                ??? json-spec "`/variable_to_simulation/*/type` (`string`)"
                    ```
                    /variable_to_simulation/*/type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Options:** `['shape', 'elastic', 'friction', 'damping', 'macro-strain', 'initial', 'dirichlet', 'pressure']`








                ??? json-spec "`/variable_to_simulation/*/composition` (`list`)"
                    ```
                    /variable_to_simulation/*/composition
                    ```
                    <h2>Description</h2>
                    list of parametrizations that maps raw optimization variables to parameters in simulations



                    ??? json-spec "`/variable_to_simulation/*/composition/*`"
                        ```
                        /variable_to_simulation/*/composition/*
                        ```


                        === "bounded-biharmonic-weights"
                        
                            **Type**: bounded-biharmonic-weights
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>


















                        === "scalar-velocity-parametrization"
                        
                            **Type**: scalar-velocity-parametrization
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>













                        === "append-const"
                        
                            **Type**: append-const
                            <h2>Description</h2>
                            Append repeated constant at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/size` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/size
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/start` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/start
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "append-values"
                        
                            **Type**: append-values
                            <h2>Description</h2>
                            Append a list of constants at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/values` (`list`)"
                                ```
                                /variable_to_simulation/*/composition/*/values
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/variable_to_simulation/*/composition/*/values/*` (`float`)"
                                    ```
                                    /variable_to_simulation/*/composition/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "slice"
                        
                            **Type**: slice
                            <h2>Description</h2>
                            Ouputs x[from:to], where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/parameter_index` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/parameter_index
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/last` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/last
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "power"
                        
                            **Type**: power
                            <h2>Description</h2>
                            Ouputs x ^ power, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/power` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/power
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "exp"
                        
                            **Type**: exp
                            <h2>Description</h2>
                            Ouputs exp(x), where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "scale"
                        
                            **Type**: scale
                            <h2>Description</h2>
                            Ouputs x * value, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-elem"
                        
                            **Type**: per-body-to-per-elem
                            <h2>Description</h2>
                            From per volume selection to per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-node"
                        
                            **Type**: per-body-to-per-node
                            <h2>Description</h2>
                            From per volume selection to per FE node.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "E-nu-to-lambda-mu"
                        
                            **Type**: E-nu-to-lambda-mu
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/is_volume` (`bool`)"
                                ```
                                /variable_to_simulation/*/composition/*/is_volume
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "linear-filter"
                        
                            **Type**: linear-filter
                            <h2>Description</h2>
                            Apply linear smoothing filter on a field per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.













                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`









                <h2>Optional</h2>





                ??? json-spec "`/variable_to_simulation/*/composite_map_type` (`string`)"
                    ```
                    /variable_to_simulation/*/composite_map_type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Default**: `'none'`






                ??? json-spec "`/variable_to_simulation/*/composite_map_indices`"
                    ```
                    /variable_to_simulation/*/composite_map_indices
                    ```


                    === "`/variable_to_simulation/*/composite_map_indices` (`file`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/composite_map_indices` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/composite_map_indices/*` (`int`)"
                            ```
                            /variable_to_simulation/*/composite_map_indices/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.









            === "initial"
            
                **Type**: initial
                <h2>Description</h2>
                FIXME: Missing documentation in the specification.
                <h2>Required</h2>



                ??? json-spec "`/variable_to_simulation/*/state`"
                    ```
                    /variable_to_simulation/*/state
                    ```


                    === "`/variable_to_simulation/*/state` (`int`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/state` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/state/*` (`int`)"
                            ```
                            /variable_to_simulation/*/state/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.











                ??? json-spec "`/variable_to_simulation/*/type` (`string`)"
                    ```
                    /variable_to_simulation/*/type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Options:** `['shape', 'elastic', 'friction', 'damping', 'macro-strain', 'initial', 'dirichlet', 'pressure']`








                ??? json-spec "`/variable_to_simulation/*/composition` (`list`)"
                    ```
                    /variable_to_simulation/*/composition
                    ```
                    <h2>Description</h2>
                    list of parametrizations that maps raw optimization variables to parameters in simulations



                    ??? json-spec "`/variable_to_simulation/*/composition/*`"
                        ```
                        /variable_to_simulation/*/composition/*
                        ```


                        === "bounded-biharmonic-weights"
                        
                            **Type**: bounded-biharmonic-weights
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>


















                        === "scalar-velocity-parametrization"
                        
                            **Type**: scalar-velocity-parametrization
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>













                        === "append-const"
                        
                            **Type**: append-const
                            <h2>Description</h2>
                            Append repeated constant at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/size` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/size
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/start` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/start
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "append-values"
                        
                            **Type**: append-values
                            <h2>Description</h2>
                            Append a list of constants at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/values` (`list`)"
                                ```
                                /variable_to_simulation/*/composition/*/values
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/variable_to_simulation/*/composition/*/values/*` (`float`)"
                                    ```
                                    /variable_to_simulation/*/composition/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "slice"
                        
                            **Type**: slice
                            <h2>Description</h2>
                            Ouputs x[from:to], where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/parameter_index` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/parameter_index
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/last` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/last
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "power"
                        
                            **Type**: power
                            <h2>Description</h2>
                            Ouputs x ^ power, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/power` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/power
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "exp"
                        
                            **Type**: exp
                            <h2>Description</h2>
                            Ouputs exp(x), where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "scale"
                        
                            **Type**: scale
                            <h2>Description</h2>
                            Ouputs x * value, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-elem"
                        
                            **Type**: per-body-to-per-elem
                            <h2>Description</h2>
                            From per volume selection to per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-node"
                        
                            **Type**: per-body-to-per-node
                            <h2>Description</h2>
                            From per volume selection to per FE node.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "E-nu-to-lambda-mu"
                        
                            **Type**: E-nu-to-lambda-mu
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/is_volume` (`bool`)"
                                ```
                                /variable_to_simulation/*/composition/*/is_volume
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "linear-filter"
                        
                            **Type**: linear-filter
                            <h2>Description</h2>
                            Apply linear smoothing filter on a field per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.













                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`









                <h2>Optional</h2>





                ??? json-spec "`/variable_to_simulation/*/composite_map_type` (`string`)"
                    ```
                    /variable_to_simulation/*/composite_map_type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Default**: `'none'`






                ??? json-spec "`/variable_to_simulation/*/composite_map_indices`"
                    ```
                    /variable_to_simulation/*/composite_map_indices
                    ```


                    === "`/variable_to_simulation/*/composite_map_indices` (`file`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/composite_map_indices` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/composite_map_indices/*` (`int`)"
                            ```
                            /variable_to_simulation/*/composite_map_indices/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.









            === "dirichlet"
            
                **Type**: dirichlet
                <h2>Description</h2>
                FIXME: Missing documentation in the specification.
                <h2>Required</h2>



                ??? json-spec "`/variable_to_simulation/*/state`"
                    ```
                    /variable_to_simulation/*/state
                    ```


                    === "`/variable_to_simulation/*/state` (`int`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/state` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/state/*` (`int`)"
                            ```
                            /variable_to_simulation/*/state/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.











                ??? json-spec "`/variable_to_simulation/*/type` (`string`)"
                    ```
                    /variable_to_simulation/*/type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Options:** `['shape', 'elastic', 'friction', 'damping', 'macro-strain', 'initial', 'dirichlet', 'pressure']`








                ??? json-spec "`/variable_to_simulation/*/composition` (`list`)"
                    ```
                    /variable_to_simulation/*/composition
                    ```
                    <h2>Description</h2>
                    list of parametrizations that maps raw optimization variables to parameters in simulations



                    ??? json-spec "`/variable_to_simulation/*/composition/*`"
                        ```
                        /variable_to_simulation/*/composition/*
                        ```


                        === "bounded-biharmonic-weights"
                        
                            **Type**: bounded-biharmonic-weights
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>


















                        === "scalar-velocity-parametrization"
                        
                            **Type**: scalar-velocity-parametrization
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>













                        === "append-const"
                        
                            **Type**: append-const
                            <h2>Description</h2>
                            Append repeated constant at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/size` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/size
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/start` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/start
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "append-values"
                        
                            **Type**: append-values
                            <h2>Description</h2>
                            Append a list of constants at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/values` (`list`)"
                                ```
                                /variable_to_simulation/*/composition/*/values
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/variable_to_simulation/*/composition/*/values/*` (`float`)"
                                    ```
                                    /variable_to_simulation/*/composition/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "slice"
                        
                            **Type**: slice
                            <h2>Description</h2>
                            Ouputs x[from:to], where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/parameter_index` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/parameter_index
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/last` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/last
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "power"
                        
                            **Type**: power
                            <h2>Description</h2>
                            Ouputs x ^ power, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/power` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/power
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "exp"
                        
                            **Type**: exp
                            <h2>Description</h2>
                            Ouputs exp(x), where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "scale"
                        
                            **Type**: scale
                            <h2>Description</h2>
                            Ouputs x * value, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-elem"
                        
                            **Type**: per-body-to-per-elem
                            <h2>Description</h2>
                            From per volume selection to per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-node"
                        
                            **Type**: per-body-to-per-node
                            <h2>Description</h2>
                            From per volume selection to per FE node.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "E-nu-to-lambda-mu"
                        
                            **Type**: E-nu-to-lambda-mu
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/is_volume` (`bool`)"
                                ```
                                /variable_to_simulation/*/composition/*/is_volume
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "linear-filter"
                        
                            **Type**: linear-filter
                            <h2>Description</h2>
                            Apply linear smoothing filter on a field per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.













                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`














                <h2>Optional</h2>





                ??? json-spec "`/variable_to_simulation/*/composite_map_type` (`string`)"
                    ```
                    /variable_to_simulation/*/composite_map_type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Default**: `'none'`






                ??? json-spec "`/variable_to_simulation/*/composite_map_indices`"
                    ```
                    /variable_to_simulation/*/composite_map_indices
                    ```


                    === "`/variable_to_simulation/*/composite_map_indices` (`file`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/composite_map_indices` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/composite_map_indices/*` (`int`)"
                            ```
                            /variable_to_simulation/*/composite_map_indices/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.









            === "pressure"
            
                **Type**: pressure
                <h2>Description</h2>
                FIXME: Missing documentation in the specification.
                <h2>Required</h2>



                ??? json-spec "`/variable_to_simulation/*/state`"
                    ```
                    /variable_to_simulation/*/state
                    ```


                    === "`/variable_to_simulation/*/state` (`int`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/state` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/state/*` (`int`)"
                            ```
                            /variable_to_simulation/*/state/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.











                ??? json-spec "`/variable_to_simulation/*/type` (`string`)"
                    ```
                    /variable_to_simulation/*/type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Options:** `['shape', 'elastic', 'friction', 'damping', 'macro-strain', 'initial', 'dirichlet', 'pressure']`








                ??? json-spec "`/variable_to_simulation/*/composition` (`list`)"
                    ```
                    /variable_to_simulation/*/composition
                    ```
                    <h2>Description</h2>
                    list of parametrizations that maps raw optimization variables to parameters in simulations



                    ??? json-spec "`/variable_to_simulation/*/composition/*`"
                        ```
                        /variable_to_simulation/*/composition/*
                        ```


                        === "bounded-biharmonic-weights"
                        
                            **Type**: bounded-biharmonic-weights
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>


















                        === "scalar-velocity-parametrization"
                        
                            **Type**: scalar-velocity-parametrization
                            <h2>Description</h2>
                            TODO
                            <h2>Required</h2>













                        === "append-const"
                        
                            **Type**: append-const
                            <h2>Description</h2>
                            Append repeated constant at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/size` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/size
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/start` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/start
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "append-values"
                        
                            **Type**: append-values
                            <h2>Description</h2>
                            Append a list of constants at the end of the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/values` (`list`)"
                                ```
                                /variable_to_simulation/*/composition/*/values
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.





                                ??? json-spec "`/variable_to_simulation/*/composition/*/values/*` (`float`)"
                                    ```
                                    /variable_to_simulation/*/composition/*/values/*
                                    ```
                                    <h2>Description</h2>
                                    FIXME: Missing documentation in the specification.











                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "slice"
                        
                            **Type**: slice
                            <h2>Description</h2>
                            Ouputs x[from:to], where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/parameter_index` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/parameter_index
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/last` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/last
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "power"
                        
                            **Type**: power
                            <h2>Description</h2>
                            Ouputs x ^ power, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/power` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/power
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "exp"
                        
                            **Type**: exp
                            <h2>Description</h2>
                            Ouputs exp(x), where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`



                            <h2>Optional</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/from` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/from
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/to` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/to
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Default**: `-1`






                        === "scale"
                        
                            **Type**: scale
                            <h2>Description</h2>
                            Ouputs x * value, where x is the input vector
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`








                            ??? json-spec "`/variable_to_simulation/*/composition/*/value` (`float`)"
                                ```
                                /variable_to_simulation/*/composition/*/value
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-elem"
                        
                            **Type**: per-body-to-per-elem
                            <h2>Description</h2>
                            From per volume selection to per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "per-body-to-per-node"
                        
                            **Type**: per-body-to-per-node
                            <h2>Description</h2>
                            From per volume selection to per FE node.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "E-nu-to-lambda-mu"
                        
                            **Type**: E-nu-to-lambda-mu
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/is_volume` (`bool`)"
                                ```
                                /variable_to_simulation/*/composition/*/is_volume
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.








                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`






                        === "linear-filter"
                        
                            **Type**: linear-filter
                            <h2>Description</h2>
                            Apply linear smoothing filter on a field per element.
                            <h2>Required</h2>





                            ??? json-spec "`/variable_to_simulation/*/composition/*/state` (`int`)"
                                ```
                                /variable_to_simulation/*/composition/*/state
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.













                            ??? json-spec "`/variable_to_simulation/*/composition/*/type` (`string`)"
                                ```
                                /variable_to_simulation/*/composition/*/type
                                ```
                                <h2>Description</h2>
                                FIXME: Missing documentation in the specification.
                            
                                **Options:** `['per-body-to-per-elem', 'per-body-to-per-node', 'E-nu-to-lambda-mu', 'slice', 'exp', 'scale', 'power', 'append-values', 'append-const', 'linear-filter', 'bounded-biharmonic-weights', 'scalar-velocity-parametrization']`














                <h2>Optional</h2>





                ??? json-spec "`/variable_to_simulation/*/composite_map_type` (`string`)"
                    ```
                    /variable_to_simulation/*/composite_map_type
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.
                
                    **Default**: `'none'`






                ??? json-spec "`/variable_to_simulation/*/composite_map_indices`"
                    ```
                    /variable_to_simulation/*/composite_map_indices
                    ```


                    === "`/variable_to_simulation/*/composite_map_indices` (`file`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.



                    === "`/variable_to_simulation/*/composite_map_indices` (`list`)"
                        <h2>Description</h2>
                        FIXME: Missing documentation in the specification.





                        ??? json-spec "`/variable_to_simulation/*/composite_map_indices/*` (`int`)"
                            ```
                            /variable_to_simulation/*/composite_map_indices/*
                            ```
                            <h2>Description</h2>
                            FIXME: Missing documentation in the specification.

















    ??? json-spec "`/states` (`list`)"
        ```
        /states
        ```
        <h2>Description</h2>
        Specify a numebr of simulations used in the optimization.





        ??? json-spec "`/states/*` (`object`)"
            ```
            /states/*
            ```
            <h2>Description</h2>
            FIXME: Missing documentation in the specification.
            <h2>Required</h2>





            ??? json-spec "`/states/*/path` (`file`)"
                ```
                /states/*/path
                ```
                <h2>Description</h2>
                The json file path for this state.



            <h2>Optional</h2>





            ??? json-spec "`/states/*/initial_guess` (`int`)"
                ```
                /states/*/initial_guess
                ```
                <h2>Description</h2>
                Specify the state ID, whose solution is used to initialize the solve in this state.
            
                **Default**: `-1`









    <h2>Optional</h2>





    ??? json-spec "`/output` (`object`)"
        ```
        /output
        ```
        <h2>Description</h2>
        Optimization output options
    
        **Default**: `None`
        <h2>Optional</h2>





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











        ??? json-spec "`/output/save_frequency` (`int`)"
            ```
            /output/save_frequency
            ```
            <h2>Description</h2>
            Optimization output frequency
        
            **Default**: `1`








        ??? json-spec "`/output/directory` (`string`)"
            ```
            /output/directory
            ```
            <h2>Description</h2>
            Directory for output files.
        
            **Default**: `''`








        ??? json-spec "`/output/solution` (`file`)"
            ```
            /output/solution
            ```
            <h2>Description</h2>
            Export optimization variables to file at every iteration.
        
            **Default**: `''`











    ??? json-spec "`/solver` (`object`)"
        ```
        /solver
        ```
        <h2>Description</h2>
        Optimization solver parameters.
    
        **Default**: `None`
        <h2>Optional</h2>










        ??? json-spec "`/solver/advanced` (`object`)"
            ```
            /solver/advanced
            ```
            <h2>Description</h2>
            Advanced settings for arranging forward simulations
        
            **Default**: `None`
            <h2>Optional</h2>





            ??? json-spec "`/solver/advanced/solve_in_parallel` (`bool`)"
                ```
                /solver/advanced/solve_in_parallel
                ```
                <h2>Description</h2>
                Run forward simulations in parallel.
            
                **Default**: `False`








            ??? json-spec "`/solver/advanced/solve_in_order` (`list`)"
                ```
                /solver/advanced/solve_in_order
                ```
                <h2>Description</h2>
                Run forward simulations in order.





                ??? json-spec "`/solver/advanced/solve_in_order/*` (`int`)"
                    ```
                    /solver/advanced/solve_in_order/*
                    ```
                    <h2>Description</h2>
                    Id of forward simulations.











            ??? json-spec "`/solver/advanced/characteristic_length` (`float`)"
                ```
                /solver/advanced/characteristic_length
                ```
                <h2>Description</h2>
                A scaling on the nonlinear problem for better stability.
            
                **Default**: `1`








            ??? json-spec "`/solver/advanced/enable_slim` (`bool`)"
                ```
                /solver/advanced/enable_slim
                ```
                <h2>Description</h2>
                Whether to apply slim smoothing to the optimization when step is accepted.
            
                **Default**: `False`








            ??? json-spec "`/solver/advanced/smooth_line_search` (`bool`)"
                ```
                /solver/advanced/smooth_line_search
                ```
                <h2>Description</h2>
                Whether to apply slim smoothing to the optimization line search.
            
                **Default**: `False`











        ??? json-spec "`/solver/max_threads` (`int`)"
            ```
            /solver/max_threads
            ```
            <h2>Description</h2>
            Maximum number of threads used; 0 is unlimited.
        
            **Default**: `0`
        
            **Range:** `[0, inf]`











    ??? json-spec "`/stopping_conditions` (`list`)"
        ```
        /stopping_conditions
        ```
        <h2>Description</h2>
        A list of functionals. The optimization stops if these functionals are all negative, even if the objective gradient norm is not small enough.













    ??? json-spec "`/functionals` (`list`)"
        ```
        /functionals
        ```
        <h2>Description</h2>
        A list of functionals. Their sum is the functional being optimized.













    ??? json-spec "`/compute_objective` (`bool`)"
        ```
        /compute_objective
        ```
        <h2>Description</h2>
        Evaluate the functionals and exit.
    
        **Default**: `False`





