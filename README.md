# reciprocal

This repo serves a test model for MOC runtime features and functionalities.

## Tests to run using this model

**Batch Scoring Jobs** with inputs:

1. `input_div_by_zero.json`
    - schema checking **enabled**
    - Expect `UserWarning("Bad Input: DivisionByZero Expected!")` (2x)
    - Protion of job logs:
    ```
        2021/11/19 17:41:05 [info] state changes to RUNNING
        2021/11/19 17:41:05 [info] init succeeded
        2021/11/19 17:41:05 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'input': 1}
        2021/11/19 17:41:05 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'input': 0}
        2021/11/19 17:41:05 [info] MODEL-CONSOLE: An error occured when processing the model: Bad Input: DivisionByZero Expected!
        2021/11/19 17:41:05 [info] MODEL-CONSOLE: UserWarning: Bad Input: DivisionByZero Expected!
        2021/11/19 17:41:05 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'input': 0}
        2021/11/19 17:41:05 [info] MODEL-CONSOLE: UserWarning: Bad Input: DivisionByZero Expected!
        2021/11/19 17:41:05 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'input': 2}
        2021/11/19 17:41:05 [info] state changes to FINISHING
        2021/11/19 17:41:05 [warning] jobResult set to failure: "An output error occurred during model execution, please check the engine logs for details"
        2021/11/19 17:41:05 [info] (post) MODEL-CONSOLE: Model runner exits
        2021/11/19 17:41:06 batch job complete
      ```

2. `input_bad_data_types.json`
    - schema checking **disabled**
    - Expect `UserWarning("Bad Input: input data should be a dictionary")` (2x)
    - Portion of job logs
    ```
        2021/11/19 18:06:32 [info] state changes to RUNNING
        2021/11/19 18:06:32 [info] init succeeded
        2021/11/19 18:06:32 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'input': 1}
        2021/11/19 18:06:32 [info] MODEL-CONSOLE: INFO:model:Input to action(): [{'input': 0}]
        2021/11/19 18:06:32 [info] MODEL-CONSOLE: An error occured when processing the model: Bad Input: input data should be a dictionary
        2021/11/19 18:06:32 [info] MODEL-CONSOLE: UserWarning: Bad Input: input data should be a dictionary
        2021/11/19 18:06:32 [info] MODEL-CONSOLE: INFO:model:Input to action(): 3
        2021/11/19 18:06:32 [info] MODEL-CONSOLE: An error occured when processing the model: Bad Input: input data should be a dictionary
        2021/11/19 18:06:32 [info] MODEL-CONSOLE: UserWarning: Bad Input: input data should be a dictionary
        2021/11/19 18:06:32 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'input': 2}
        2021/11/19 18:06:32 [info] state changes to FINISHING
        2021/11/19 18:06:32 [warning] jobResult set to failure: "An output error occurred during model execution, please check the engine logs for details"
        2021/11/19 18:06:32 [info] (post) MODEL-CONSOLE: Model runner exits
        2021/11/19 18:06:34 batch job complete
    ```

3. `input_bad_keys.json`
    - schema checking **disabled**
    - Expect `warnings.warn("Key 'input' missing from input data", category=UserWarning)` (2x)
    - Portion of job logs
    ```
        2021/11/19 18:24:50 [info] state changes to RUNNING
        2021/11/19 18:24:50 [info] init succeeded
        2021/11/19 18:24:50 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'input': 1}
        2021/11/19 18:24:50 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'inputs': 1}
        2021/11/19 18:24:50 [info] MODEL-CONSOLE: An error occured when processing the model: Key 'input' missing from input data
        2021/11/19 18:24:50 [info] MODEL-CONSOLE: UserWarning: Key 'input' missing from input data
        2021/11/19 18:24:50 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'data': 1}
        2021/11/19 18:24:50 [info] MODEL-CONSOLE: An error occured when processing the model: Key 'input' missing from input data
        2021/11/19 18:24:50 [info] MODEL-CONSOLE: UserWarning: Key 'input' missing from input data
        2021/11/19 18:24:50 [info] MODEL-CONSOLE: INFO:model:Input to action(): {'input': 2}
        2021/11/19 18:24:50 [info] state changes to FINISHING
        2021/11/19 18:24:50 [warning] jobResult set to failure: "An output error occurred during model execution, please check the engine logs for details"
        2021/11/19 18:24:50 [info] (post) MODEL-CONSOLE: Model runner exits
        2021/11/19 18:24:51 batch job complete
    ```

In each of the cases above, the job should **complete** (`"jobStatus": "COMPLETE"`) with **failure** (`"jobResult": "FAILURE"`)
```
  "jobStatus" : "COMPLETE",
  "jobResult" : "FAILURE",
```

**Roundtrip REST**

* Set up an runtime with a roundtrip REST input endpoint, and set the encoding to **JSON**
* POST requests to `<MOC_URL>/<engine-name>/api/roundtrip/0/1`
* Request bodies to try:
    - `{"input": 1}`: expected output: `{"reciprocal": 1.0}`
    - `{"input": 0}`: expected output: ```An error has occurred: An output error occurred during model execution, please check the engine logs for details```
    - `{"inputs": 1}`: expected output: ```An error has occurred: input record rejected by schema```