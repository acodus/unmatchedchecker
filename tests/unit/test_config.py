"""Unit tests for configuration module."""

import pytest
from pathlib import Path


def test_get_project_root():
    """Test that project root is correctly identified."""
    from src.common.config import get_project_root

    root = get_project_root()
    assert root.exists()
    assert (root / "src").exists()


def test_load_config_dev():
    """Test loading dev configuration."""
    from src.common.config import load_config

    config = load_config("dev")
    assert config["environment"] == "dev"
    assert "databricks" in config
    assert "storage" in config


def test_load_config_invalid_env():
    """Test that invalid environment raises error."""
    from src.common.config import load_config

    with pytest.raises(FileNotFoundError):
        load_config("nonexistent")
