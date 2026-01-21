"""Simple entrypoint and helpers for the template project."""

from __future__ import annotations

import os
from typing import Mapping

DEFAULT_PORT = 8000


def parse_port(value: str) -> int:
    """Parse a port value and validate its range."""
    try:
        port = int(value)
    except (TypeError, ValueError) as exc:
        raise ValueError("port must be an integer") from exc

    if not 1 <= port <= 65535:
        raise ValueError("port must be between 1 and 65535")

    return port


def get_port(env: Mapping[str, str] | None = None) -> int:
    """Return the configured port, defaulting when unset."""
    environ = env if env is not None else os.environ
    value = environ.get("APP_PORT")
    if value is None:
        return DEFAULT_PORT
    return parse_port(value)


def build_welcome_message(name: str, port: int) -> str:
    """Build a welcome message for the CLI."""
    normalized = name.strip() or "World"
    return f"Hello, {normalized}! Listening on {port}."


def main() -> None:
    """Entrypoint for `make run`."""
    port = get_port()
    app_name = os.environ.get("APP_NAME", "")
    print(build_welcome_message(app_name, port))


if __name__ == "__main__":
    main()
