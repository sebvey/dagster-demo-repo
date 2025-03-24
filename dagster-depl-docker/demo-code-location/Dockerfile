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

# UV SYNC / LIBRARY
ADD . /src
WORKDIR /src
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-editable


## FINAL IMAGE ############################################################

FROM python:3.12-slim
SHELL ["sh", "-exc"]

ENV PATH=/app/bin:$PATH

# RUN groupadd -r app && useradd -r -d /app -g app -N app
# COPY --from=build --chown=app:app /app /app
# USER app
COPY --from=build /app /app
WORKDIR /app

# Run dagster gRPC server on port 4000
EXPOSE 4000
CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-m", "demo_code_location"]



# WE NOW HAVE:
# - python venv installed and in PATH
# - code location library installed
#
# => image usable for code location server (default cmd)
# => image usable for job runs for the code location (dagster will override cmd)
