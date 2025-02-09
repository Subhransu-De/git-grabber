FROM python:3.13-slim-bookworm
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
RUN apt-get update && apt-get install -y git openssh-client ssh

WORKDIR /app

COPY uv.lock .
COPY pyproject.toml .
RUN uv sync --frozen

COPY app/ ./app/

ENTRYPOINT ["uv", "run", "app"]