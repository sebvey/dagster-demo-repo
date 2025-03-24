The different aspects of the dagster instance are set in the dagster.yaml file.  
This file is packaged with webserver(s) and dagster daemon (in $DAGSTER_HOME)

- run coordinator
- run launcher

- run storage
- schedule storage
- event log storage - event and logs from a run
- compute log storage - raw stdout / errout from compute
- local artifact storage - used by FileSystem I/O manager

- sensor evaluation
- schedule evaluation
- concurrency
- data retention
- gRPC servers (if not our own gRPC servers but dealt by daemon or webserver)

COMPLETE DESC:
https://docs.dagster.io/guides/deploy/dagster-instance-configuration

# Run Coordinator

- https://docs.dagster.io/guides/deploy/execution/run-coordinators

Controls the policy used to manage the set of runs:
- applies limits and priorizations
- sends runs to the run launcher

Available coordinators:
- **DefaultRunCoordinator** - No limit nor prioritization
- **QueuedRunCoordinator** - maintains a queue, daemon pulls from it


# Run Launcher

- https://docs.dagster.io/guides/deploy/execution/run-launchers

A launch operation allocates computational resources
(e.g. a process, a container, a Kubernetes pod, etc) 
to carry out a run execution and then instigates the execution.

Run launcher = interface to the computational resources that will be used. Can be:
- K8sRunLauncher - allocates a kubernetes job per run
- ecs.EcsRunLauncher - launches an Amz ECS task per run
- DockerRunLauncher - launches a Docker container per run
- custom ...


# Compute log storage

controls the capture and persistence of raw stdout and stderr text logs. Among:
- LocalComputeLogManager -> to disk
- NoOpComputeLogManager -> no storage
- AzureBlob / GCP / S3 ComputeLogManager -> to cloud
