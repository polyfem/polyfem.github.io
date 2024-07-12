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



        ??? json-spec "`/functionals/*`"
            ```
            /functionals/*
            ```


            === "divide"
            
                **Type**: divide
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`






                ??? json-spec "`/functionals/*/objective`"
                    ```
                    /functionals/*/objective
                    ```


                    === "`/functionals/*/objective` (`object`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/objective` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/objective/*` (`object`)"
                            ```
                            /functionals/*/objective/*
                            ```
                            <h2>Description</h2>
                            TODO






                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "plus-const"
            
                **Type**: plus-const
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`






                ??? json-spec "`/functionals/*/objective`"
                    ```
                    /functionals/*/objective
                    ```


                    === "`/functionals/*/objective` (`object`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/objective` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/objective/*` (`object`)"
                            ```
                            /functionals/*/objective/*
                            ```
                            <h2>Description</h2>
                            TODO











                ??? json-spec "`/functionals/*/value` (`float`)"
                    ```
                    /functionals/*/value
                    ```
                    <h2>Description</h2>
                    TODO



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "power"
            
                **Type**: power
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`






                ??? json-spec "`/functionals/*/objective`"
                    ```
                    /functionals/*/objective
                    ```


                    === "`/functionals/*/objective` (`object`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/objective` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/objective/*` (`object`)"
                            ```
                            /functionals/*/objective/*
                            ```
                            <h2>Description</h2>
                            TODO






                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/power` (`float`)"
                    ```
                    /functionals/*/power
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `2`








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "sdf-target"
            
                **Type**: sdf-target
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/control_points` (`list`)"
                    ```
                    /functionals/*/control_points
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/control_points/*` (`list`)"
                        ```
                        /functionals/*/control_points/*
                        ```
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/control_points/*/*` (`float`)"
                            ```
                            /functionals/*/control_points/*/*
                            ```
                            <h2>Description</h2>
                            TODO














                ??? json-spec "`/functionals/*/control_points_grid` (`list`)"
                    ```
                    /functionals/*/control_points_grid
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/control_points_grid/*` (`list`)"
                        ```
                        /functionals/*/control_points_grid/*
                        ```
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/control_points_grid/*/*` (`float`)"
                            ```
                            /functionals/*/control_points_grid/*/*
                            ```
                            <h2>Description</h2>
                            TODO














                ??? json-spec "`/functionals/*/knots` (`list`)"
                    ```
                    /functionals/*/knots
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/knots/*` (`float`)"
                        ```
                        /functionals/*/knots/*
                        ```
                        <h2>Description</h2>
                        TODO











                ??? json-spec "`/functionals/*/knots_u` (`list`)"
                    ```
                    /functionals/*/knots_u
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/knots_u/*` (`float`)"
                        ```
                        /functionals/*/knots_u/*
                        ```
                        <h2>Description</h2>
                        TODO











                ??? json-spec "`/functionals/*/knots_v` (`list`)"
                    ```
                    /functionals/*/knots_v
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/knots_v/*` (`float`)"
                        ```
                        /functionals/*/knots_v/*
                        ```
                        <h2>Description</h2>
                        TODO











                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/surface_selection`"
                    ```
                    /functionals/*/surface_selection
                    ```


                    === "`/functionals/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/surface_selection/*` (`int`)"
                            ```
                            /functionals/*/surface_selection/*
                            ```
                            <h2>Description</h2>
                            TODO









            === "mesh-target"
            
                **Type**: mesh-target
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`













                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/surface_selection`"
                    ```
                    /functionals/*/surface_selection
                    ```


                    === "`/functionals/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/surface_selection/*` (`int`)"
                            ```
                            /functionals/*/surface_selection/*
                            ```
                            <h2>Description</h2>
                            TODO









            === "node-target"
            
                **Type**: node-target
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`













                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "function-target"
            
                **Type**: function-target
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/target_function` (`string`)"
                    ```
                    /functionals/*/target_function
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `'0'`








                ??? json-spec "`/functionals/*/target_function_gradient` (`list`)"
                    ```
                    /functionals/*/target_function_gradient
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/target_function_gradient/*` (`string`)"
                        ```
                        /functionals/*/target_function_gradient/*
                        ```
                        <h2>Description</h2>
                        TODO









                ??? json-spec "`/functionals/*/surface_selection`"
                    ```
                    /functionals/*/surface_selection
                    ```


                    === "`/functionals/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/surface_selection/*` (`int`)"
                            ```
                            /functionals/*/surface_selection/*
                            ```
                            <h2>Description</h2>
                            TODO









            === "target"
            
                **Type**: target
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/surface_selection`"
                    ```
                    /functionals/*/surface_selection
                    ```


                    === "`/functionals/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/surface_selection/*` (`int`)"
                            ```
                            /functionals/*/surface_selection/*
                            ```
                            <h2>Description</h2>
                            TODO











                ??? json-spec "`/functionals/*/reference_cached_body_ids` (`list`)"
                    ```
                    /functionals/*/reference_cached_body_ids
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/reference_cached_body_ids/*` (`int`)"
                        ```
                        /functionals/*/reference_cached_body_ids/*
                        ```
                        <h2>Description</h2>
                        TODO











                ??? json-spec "`/functionals/*/target_state` (`int`)"
                    ```
                    /functionals/*/target_state
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `-1`






            === "displacement-target"
            
                **Type**: displacement-target
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/target_displacement` (`list`)"
                    ```
                    /functionals/*/target_displacement
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/target_displacement/*` (`float`)"
                        ```
                        /functionals/*/target_displacement/*
                        ```
                        <h2>Description</h2>
                        TODO











                ??? json-spec "`/functionals/*/active_dimension` (`list`)"
                    ```
                    /functionals/*/active_dimension
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/active_dimension/*` (`bool`)"
                        ```
                        /functionals/*/active_dimension/*
                        ```
                        <h2>Description</h2>
                        TODO









                ??? json-spec "`/functionals/*/surface_selection`"
                    ```
                    /functionals/*/surface_selection
                    ```


                    === "`/functionals/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/surface_selection/*` (`int`)"
                            ```
                            /functionals/*/surface_selection/*
                            ```
                            <h2>Description</h2>
                            TODO









            === "center-target"
            
                **Type**: center-target
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO








                ??? json-spec "`/functionals/*/target_state` (`int`)"
                    ```
                    /functionals/*/target_state
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `-1`






            === "position"
            
                **Type**: position
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO






            === "parametrized_product"
            
                **Type**: parametrized_product
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/power` (`float`)"
                    ```
                    /functionals/*/power
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `2`






            === "soft_constraint"
            
                **Type**: soft_constraint
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`






                ??? json-spec "`/functionals/*/objective`"
                    ```
                    /functionals/*/objective
                    ```


                    === "`/functionals/*/objective` (`object`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/objective` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/objective/*` (`object`)"
                            ```
                            /functionals/*/objective/*
                            ```
                            <h2>Description</h2>
                            TODO











                ??? json-spec "`/functionals/*/soft_bound` (`list`)"
                    ```
                    /functionals/*/soft_bound
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/soft_bound/*` (`float`)"
                        ```
                        /functionals/*/soft_bound/*
                        ```
                        <h2>Description</h2>
                        TODO






                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/power` (`float`)"
                    ```
                    /functionals/*/power
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `2`






            === "transient_integral"
            
                **Type**: transient_integral
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                ??? json-spec "`/functionals/*/static_objective` (`object`)"
                    ```
                    /functionals/*/static_objective
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/integral_type` (`string`)"
                    ```
                    /functionals/*/integral_type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `'uniform'`
                
                    **Options:** `['simpson', 'uniform', 'final', 'steps']`








                ??? json-spec "`/functionals/*/steps` (`list`)"
                    ```
                    /functionals/*/steps
                    ```
                    <h2>Description</h2>
                    TODO











            === "acceleration"
            
                **Type**: acceleration
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO






            === "kinetic"
            
                **Type**: kinetic
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO






            === "disp_grad"
            
                **Type**: disp_grad
                <h2>Description</h2>
                One entry of displacement gradient matrix
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/dimensions` (`list`)"
                    ```
                    /functionals/*/dimensions
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.











            === "homo_disp_grad"
            
                **Type**: homo_disp_grad
                <h2>Description</h2>
                One entry of macro displacement gradient matrix, only work for homogenization
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/dimensions` (`list`)"
                    ```
                    /functionals/*/dimensions
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.











            === "stress"
            
                **Type**: stress
                <h2>Description</h2>
                One entry of elastic stress matrix
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/dimensions` (`list`)"
                    ```
                    /functionals/*/dimensions
                    ```
                    <h2>Description</h2>
                    FIXME: Missing documentation in the specification.











            === "elastic_energy"
            
                **Type**: elastic_energy
                <h2>Description</h2>
                Elastic energy over the volume selection
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "stress_norm"
            
                **Type**: stress_norm
                <h2>Description</h2>
                Lp Norm of elastic stress over the volume selection
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO








                ??? json-spec "`/functionals/*/power` (`float`)"
                    ```
                    /functionals/*/power
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `2`








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "quadratic_contact_force_norm"
            
                **Type**: quadratic_contact_force_norm
                <h2>Description</h2>
                Lp Norm of elastic stress over the volume selection
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/surface_selection`"
                    ```
                    /functionals/*/surface_selection
                    ```


                    === "`/functionals/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/surface_selection/*` (`int`)"
                            ```
                            /functionals/*/surface_selection/*
                            ```
                            <h2>Description</h2>
                            TODO











                ??? json-spec "`/functionals/*/dhat` (`float`)"
                    ```
                    /functionals/*/dhat
                    ```
                    <h2>Description</h2>
                    The support size of barrier function
                
                    **Default**: `0.001`








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "log_contact_force_norm"
            
                **Type**: log_contact_force_norm
                <h2>Description</h2>
                Lp Norm of elastic stress over the volume selection
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/surface_selection`"
                    ```
                    /functionals/*/surface_selection
                    ```


                    === "`/functionals/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/surface_selection/*` (`int`)"
                            ```
                            /functionals/*/surface_selection/*
                            ```
                            <h2>Description</h2>
                            TODO











                ??? json-spec "`/functionals/*/dhat` (`float`)"
                    ```
                    /functionals/*/dhat
                    ```
                    <h2>Description</h2>
                    The support size of barrier function
                
                    **Default**: `0.001`








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "max_stress"
            
                **Type**: max_stress
                <h2>Description</h2>
                Pointwise max stress over the volume selection
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "compliance"
            
                **Type**: compliance
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "strain_norm"
            
                **Type**: strain_norm
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "boundary_smoothing"
            
                **Type**: boundary_smoothing
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/scale_invariant` (`bool`)"
                    ```
                    /functionals/*/scale_invariant
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `True`








                ??? json-spec "`/functionals/*/power` (`float`)"
                    ```
                    /functionals/*/power
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `2`








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/surface_selection`"
                    ```
                    /functionals/*/surface_selection
                    ```


                    === "`/functionals/*/surface_selection` (`int`)"
                        <h2>Description</h2>
                        TODO



                    === "`/functionals/*/surface_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/surface_selection/*` (`int`)"
                            ```
                            /functionals/*/surface_selection/*
                            ```
                            <h2>Description</h2>
                            TODO









            === "material_smoothing"
            
                **Type**: material_smoothing
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO






            === "control_smoothing"
            
                **Type**: control_smoothing
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "collision_barrier"
            
                **Type**: collision_barrier
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/dhat` (`float`)"
                    ```
                    /functionals/*/dhat
                    ```
                    <h2>Description</h2>
                    The support size of barrier function
                
                    **Default**: `0.001`






            === "deformed_collision_barrier"
            
                **Type**: deformed_collision_barrier
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`








                ??? json-spec "`/functionals/*/dhat` (`float`)"
                    ```
                    /functionals/*/dhat
                    ```
                    <h2>Description</h2>
                    The support size of barrier function
                
                    **Default**: `0.001`






            === "layer_thickness"
            
                **Type**: layer_thickness
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/boundary_ids` (`list`)"
                    ```
                    /functionals/*/boundary_ids
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/boundary_ids/*` (`int`)"
                        ```
                        /functionals/*/boundary_ids/*
                        ```
                        <h2>Description</h2>
                        TODO











                ??? json-spec "`/functionals/*/dhat` (`float`)"
                    ```
                    /functionals/*/dhat
                    ```
                    <h2>Description</h2>
                    The support size of barrier function
                
                    **Default**: `0.001`








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "layer_thickness_log"
            
                **Type**: layer_thickness_log
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO








                ??? json-spec "`/functionals/*/dmin` (`float`)"
                    ```
                    /functionals/*/dmin
                    ```
                    <h2>Description</h2>
                    The min distance of barrier function



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/boundary_ids` (`list`)"
                    ```
                    /functionals/*/boundary_ids
                    ```
                    <h2>Description</h2>
                    TODO





                    ??? json-spec "`/functionals/*/boundary_ids/*` (`int`)"
                        ```
                        /functionals/*/boundary_ids/*
                        ```
                        <h2>Description</h2>
                        TODO











                ??? json-spec "`/functionals/*/dhat` (`float`)"
                    ```
                    /functionals/*/dhat
                    ```
                    <h2>Description</h2>
                    The support size of barrier function
                
                    **Default**: `0.001`








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "weighted_solution"
            
                **Type**: weighted_solution
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






            === "volume"
            
                **Type**: volume
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO



                <h2>Optional</h2>





                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`






                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO






            === "AMIPS"
            
                **Type**: AMIPS
                <h2>Description</h2>
                TODO
                <h2>Required</h2>





                ??? json-spec "`/functionals/*/type` (`string`)"
                    ```
                    /functionals/*/type
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Options:** `['transient_integral', 'power', 'divide', 'plus-const', 'target', 'sdf-target', 'mesh-target', 'center-target', 'function-target', 'displacement-target', 'node-target', 'position', 'acceleration', 'kinetic', 'disp_grad', 'homo_disp_grad', 'stress', 'stress_norm', 'elastic_energy', 'quadratic_contact_force_norm', 'log_contact_force_norm', 'max_stress', 'compliance', 'weighted_solution', 'strain_norm', 'boundary_smoothing', 'collision_barrier', 'deformed_collision_barrier', 'control_smoothing', 'material_smoothing', 'volume', 'soft_constraint', 'layer_thickness', 'layer_thickness_log', 'AMIPS', 'parametrized_product']`








                ??? json-spec "`/functionals/*/state` (`int`)"
                    ```
                    /functionals/*/state
                    ```
                    <h2>Description</h2>
                    TODO



                <h2>Optional</h2>



                ??? json-spec "`/functionals/*/volume_selection`"
                    ```
                    /functionals/*/volume_selection
                    ```


                    === "`/functionals/*/volume_selection` (`list`)"
                        <h2>Description</h2>
                        TODO





                        ??? json-spec "`/functionals/*/volume_selection/*` (`int`)"
                            ```
                            /functionals/*/volume_selection/*
                            ```
                            <h2>Description</h2>
                            TODO






                    === "`/functionals/*/volume_selection` (`file`)"
                        <h2>Description</h2>
                        TODO








                ??? json-spec "`/functionals/*/weight` (`float`)"
                    ```
                    /functionals/*/weight
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `1`








                ??? json-spec "`/functionals/*/print_energy` (`string`)"
                    ```
                    /functionals/*/print_energy
                    ```
                    <h2>Description</h2>
                    TODO
                
                    **Default**: `''`














    ??? json-spec "`/compute_objective` (`bool`)"
        ```
        /compute_objective
        ```
        <h2>Description</h2>
        Evaluate the functionals and exit.
    
        **Default**: `False`





