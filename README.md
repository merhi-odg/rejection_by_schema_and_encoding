# Rejection by Schema and Encoding

This repo serves a test model for MOC runtime features and functionalities.

## Tests to run using this model

**Batch Scoring Jobs** with inputs:

1. `input_causes_input_rejection_by_encoding.json`
    - schema checking **optional**
    - Relevant portion of job logs:
    ```
        2021/11/19 20:19:14 [error] Record rejected by encoding with reason {12,invalid_string}: **********
        2021/11/19 20:19:14 [error] Record rejected by encoding with reason {13,invalid_string}: **********
        2021/11/19 20:19:14 [error] 2 input record(s) rejected by encoding
        2021/11/19 20:19:14 [warning] jobResult set to failure: "input record rejected by encoding"
      ```

2. `input_causes_output_rejection_by_encoding.json`
    - schema checking **optional**
    - Relevant portion of job logs
    ```
        2021/11/19 20:24:48 [error] Record rejected by encoding with reason {16,invalid_json}: **********
        2021/11/19 20:24:49 [error] 1 output record(s) rejected by encoding
        2021/11/19 20:24:49 [error] Record rejected by encoding with reason {16,invalid_json}: **********
        2021/11/19 20:24:49 [error] 1 output record(s) rejected by encoding
        2021/11/19 20:24:49 [warning] jobResult set to failure: "output record rejected by encoding"
    ```

3. `input_causes_input_schema_rejection.json`
    - schema checking **enabled**
    - Relevant Portion of job logs
    ```
        2021/11/30 15:56:29 [error] Record rejected by schema: Field 'input' missing for record 'input_schema': **********
        2021/11/30 15:56:29 [error] Record rejected by schema: Record expected, not **********: **********
        2021/11/30 15:56:29 [error] 2 input record(s) rejected by schema
        2021/11/30 15:56:29 [warning] jobResult set to failure: "input record rejected by schema"
    ```

4. `input_causes_output_schema_rejection.json`
    - schema checking **enabled**
    - Relevant Portion of job logs
    ```
        2021/11/30 15:58:37 [error] Record rejected by schema: Double expected, not **********: **********
        2021/11/30 15:58:37 [error] 1 output record(s) rejected by schema
        2021/11/30 15:58:37 [error] Record rejected by schema: Record expected, not **********: **********
        2021/11/30 15:58:37 [error] 1 output record(s) rejected by schema
        2021/11/30 15:58:37 [warning] jobResult set to failure: "output record rejected by schema"
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
    - {"input": 1}: **expected output**: {"reciprocal": 1.0}
    - {"input": 0}: **expected output**: An error has occurred: **output** record rejected by **schema**
    - {"inputs": 1}: **expected output**: An error has occurred: **input** record rejected by **schema**
    - {"input": 42}: **expected output**: An error has occurred: **output** record rejected by **schema**
    - {"input': 1}: **expected output**: An error has occurred: **input** record rejected by **encoding**
    - {"input": 3.14}: **expected output**: An error has occurred: **output** record rejected by **encoding**