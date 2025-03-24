Configuration of code locations are kept in the workspace.yaml file.  
This file is packaged with webserver(s) and dagster daemon.  
It's provided as argument when launching the webserver and daemon.

# WORKSPACE.YAML

Holds the configuration of the code locations, from where to load them + name:
- from file (in the current environment (server/daemon))
- from module (in the current environment (server/daemon))
- from gRPC server

https://docs.dagster.io/guides/deploy/code-locations/workspace-yaml
https://docs.dagster.io/guides/deploy/code-locations/managing-code-locations-with-definitions
