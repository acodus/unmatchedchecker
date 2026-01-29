"""Pytest configuration and fixtures."""

import pytest
from pyspark.sql import SparkSession


@pytest.fixture(scope="session")
def spark():
    """Create a SparkSession for testing."""
    spark = (
        SparkSession.builder
        .master("local[2]")
        .appName("unmatchedchecker-tests")
        .config("spark.sql.shuffle.partitions", "2")
        .config("spark.default.parallelism", "2")
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config(
            "spark.sql.catalog.spark_catalog",
            "org.apache.spark.sql.delta.catalog.DeltaCatalog",
        )
        .getOrCreate()
    )
    yield spark
    spark.stop()


@pytest.fixture
def sample_dataframe(spark):
    """Create a sample DataFrame for testing."""
    data = [
        (1, "Alice", 100),
        (2, "Bob", 200),
        (3, "Charlie", 150),
    ]
    return spark.createDataFrame(data, ["id", "name", "value"])
