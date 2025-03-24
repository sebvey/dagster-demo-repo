# WARNINGS

## code location dependencies

Non trivial: we need code location environment with dependencies only
used by managers:
- dagster-postgres if postgres used as storage
- dagster-docker
- and so on...

Good practice - to have a 'dagster_prj' common dependency
- all declared somewhere (prjxxx_dagster_core)
- dagster versions are fixed in one place
-> should fix an unexplored problematic: version mismatch between code location and managers

## docker
when we sync the environment with uv, we use the --frozen option:
=> we use the dependencies in uv.lock => IT MUST BE UP TO DATE 

Use of root account... because some perm denied with a standard user ... to investigate

# TODOs

- Document how the built image is reused to launch jobs
- explore python private repositories (to hold prjxxx_dagster_core)

# Usefull links

## Code location 
- https://dagster.io/blog/dagster-code-locations
- https://docs.dagster.io/guides/deploy/code-locations/
