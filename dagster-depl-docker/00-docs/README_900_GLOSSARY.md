op:
- core unit of computation in dagster, performing a simple task

op graph:
- set of interconnected ops

asset:
- represent an object in persistent storage
- many properties, including the computational core = op (or op graph for complex use cases)

job:
 - asset job - materialization of an selection of assets
 - op job - execution of a graph of ops

run = single execution of a job

standard usage of dagster is based on assets and asset jobs.  
ops and op graphs can be used more complex or task centered use cases.  
