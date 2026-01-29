"""Configuration management utilities."""

import os
from pathlib import Path
from typing import Any, Dict, Optional

import yaml


def get_project_root() -> Path:
    """Get the project root directory."""
    return Path(__file__).parent.parent.parent


def load_config(environment: Optional[str] = None) -> Dict[str, Any]:
    """Load configuration for the specified environment.

    Args:
        environment: The environment to load config for (dev, staging, prod).
                    Defaults to the ENV environment variable or 'dev'.

    Returns:
        Dictionary containing the configuration.
    """
    if environment is None:
        environment = os.getenv("ENV", "dev")

    config_path = get_project_root() / "config" / environment / "config.yaml"

    if not config_path.exists():
        raise FileNotFoundError(f"Configuration file not found: {config_path}")

    with open(config_path, "r") as f:
        return yaml.safe_load(f)


def get_storage_path(config: Dict[str, Any], path_type: str) -> str:
    """Get a storage path from configuration.

    Args:
        config: The loaded configuration dictionary.
        path_type: The type of path (input_path, output_path, checkpoint_path).

    Returns:
        The requested storage path.
    """
    return config.get("storage", {}).get(path_type, "")
