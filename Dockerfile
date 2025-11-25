# Use Python 3.13 slim image
FROM python:3.13-slim

# Set working directory
WORKDIR /app/

# Prepare UV
COPY --from=ghcr.io/astral-sh/uv:0.5.11 /uv /uvx /bin/
ENV PATH="/app/.venv/bin:$PATH"
ENV PYTHONPATH=/app
ENV UV_COMPILE_BYTECODE=1
ENV UV_LINK_MODE=copy

# Copy project files
COPY pyproject.toml uv.lock alembic.ini /app/
COPY Makefile Makefile
COPY alembic ./alembic
COPY app ./app
COPY data ./data
COPY domain ./domain
COPY services ./services

# Install Python dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen --no-install-project

# Sync the project
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync

# Expose port
EXPOSE 8000

# Run the application
CMD ["fastapi", "run", "--workers", "4", "app/src/http_api/main.py"]
