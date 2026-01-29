# Databricks notebook source
# MAGIC %md
# MAGIC # Sample Exploration Notebook
# MAGIC
# MAGIC This notebook demonstrates the basic structure for data exploration in Databricks.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Setup

# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Load Data
# MAGIC
# MAGIC Replace with your actual data source.

# COMMAND ----------

# Example: Load a sample DataFrame
# df = spark.read.format("delta").load("/path/to/your/data")

# For demonstration, create a sample DataFrame
data = [
    (1, "Alice", 100),
    (2, "Bob", 200),
    (3, "Charlie", 150),
]
df = spark.createDataFrame(data, ["id", "name", "value"])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Explore Data

# COMMAND ----------

df.show()

# COMMAND ----------

df.printSchema()

# COMMAND ----------

df.describe().show()
