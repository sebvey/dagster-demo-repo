# MORE TO DO FOR PROD READY -> https://hynek.me/articles/docker-uv/
# - environment built in /app -> copied to final image

## BUILD IMAGE ############################################################

FROM python:3.12-slim AS build
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/


ENV UV_LINK_MODE=copy \
    UV_COMPILE_BYTECODE=1 \
    UV_PYTHON_DOWNLOADS=never \
    UV_PYTHON=python3.12 \
    UV_PROJECT_ENVIRONMENT=/app

# UV SYNC / DEPENDENCIES ONLY
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-dev --no-install-project


## FINAL IMAGE ############################################################

FROM python:3.12-slim
SHELL ["sh", "-exc"]

ENV PATH=/app/bin:$PATH \
    DAGSTER_HOME=/app/dagster_home

# RUN groupadd -r app && useradd -r -d /app -g app -N app
# COPY --from=build --chown=app:app /app /app
# USER app
COPY --from=build /app /app

RUN mkdir $DAGSTER_HOME
WORKDIR $DAGSTER_HOME
COPY dagster.yaml workspace.yaml ./

# WE NOW HAVE:
# - python venv installed and in PATH -> dagit + daemon can be launched
# - DAGSTER_HOME defined with dagster.yaml and workspace.yaml in it
#   - dagster.yaml: deployment config
#   - workspace.yaml: code locations config

# We will use this image to run the webserver and the daemon containers
