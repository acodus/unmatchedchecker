"""Spark utilities for Databricks applications."""

from typing import Optional

from pyspark.sql import DataFrame, SparkSession


def get_spark_session(app_name: str = "unmatchedchecker") -> SparkSession:
    """Get or create a SparkSession.

    Args:
        app_name: The name of the Spark application.

    Returns:
        SparkSession instance.
    """
    return SparkSession.builder.appName(app_name).getOrCreate()


def read_delta_table(
    spark: SparkSession,
    path: Optional[str] = None,
    table_name: Optional[str] = None,
) -> DataFrame:
    """Read a Delta table.

    Args:
        spark: SparkSession instance.
        path: Path to the Delta table (for path-based access).
        table_name: Name of the table (for catalog-based access).

    Returns:
        DataFrame containing the table data.
    """
    if table_name:
        return spark.table(table_name)
    elif path:
        return spark.read.format("delta").load(path)
    else:
        raise ValueError("Either path or table_name must be provided")


def write_delta_table(
    df: DataFrame,
    path: Optional[str] = None,
    table_name: Optional[str] = None,
    mode: str = "overwrite",
    partition_by: Optional[list] = None,
) -> None:
    """Write a DataFrame to a Delta table.

    Args:
        df: DataFrame to write.
        path: Path to write the Delta table (for path-based access).
        table_name: Name of the table (for catalog-based access).
        mode: Write mode (overwrite, append, etc.).
        partition_by: List of columns to partition by.
    """
    writer = df.write.format("delta").mode(mode)

    if partition_by:
        writer = writer.partitionBy(*partition_by)

    if table_name:
        writer.saveAsTable(table_name)
    elif path:
        writer.save(path)
    else:
        raise ValueError("Either path or table_name must be provided")
