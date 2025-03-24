Python environment allowing to run dagster 'managers': 
- webserver
- daemon

# docker local build / run
```bash
docker build -t dagster_manager:ooo .
docker run -it dagster_manager:ooo sh
dagster-webserver -h 0.0.0.0 -p 3000 # webserver (we should 'open' ports locally)
dagster-daemon run # daemon (idem)
```

# webserver
local:  
`uv run dagster-webserver -h 0.0.0.0 -p 3000`

docker:  
```bash
docker build -t dagster_manager:ooo .
docker run -it dagster_manager:ooo sh
dagster api grpc -h 0.0.0.0 -p 1234
```

# daemon
`uv run dagster-daemon run`
