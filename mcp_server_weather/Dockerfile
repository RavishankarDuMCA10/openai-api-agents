# Stage 1: Build with uv
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim AS build

WORKDIR /app

ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy lockfile and pyproject metadata
COPY uv.lock pyproject.toml ./

# Install dependencies (excluding dev + project code)
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project --no-dev --no-editable

# Copy source code
COPY . .

# Create a virtual environment and install the project using standard pip
RUN uv venv .venv && \
    .venv/bin/python -m ensurepip && \
    .venv/bin/python -m pip install --upgrade pip setuptools && \
    .venv/bin/python -m pip install .


# Stage 2: Runtime
FROM python:3.12-slim-bookworm

WORKDIR /app

# Copy app and venv from build stage
COPY --from=build /app /app

ENV PATH="/app/.venv/bin:$PATH"

ENTRYPOINT ["mcp-server-weather"]
