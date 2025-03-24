Python environment allows to run the code location gRPC server:
https://docs.dagster.io/api/python-api/cli#dagster-api-grpc

# locally
`uv run dagster api grpc -h 0.0.0.0 -p 1234`

# docker
```bash
docker build -t demo_code_location:ooo .
docker run -it demo_code_location:ooo sh
dagster api grpc -h 0.0.0.0 -p 1234
```
