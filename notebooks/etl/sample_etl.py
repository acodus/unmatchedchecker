# Databricks notebook source
# MAGIC %md
# MAGIC # Sample ETL Notebook
# MAGIC
# MAGIC This notebook demonstrates the basic structure for ETL pipelines in Databricks.

# COMMAND ----------

# MAGIC %md
# MAGIC ## Setup

# COMMAND ----------

from pyspark.sql import SparkSession
from pyspark.sql import functions as F

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Configuration

# COMMAND ----------

# Widget parameters for notebook
dbutils.widgets.text("input_path", "", "Input Path")
dbutils.widgets.text("output_path", "", "Output Path")

input_path = dbutils.widgets.get("input_path")
output_path = dbutils.widgets.get("output_path")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Extract

# COMMAND ----------

# df_raw = spark.read.format("delta").load(input_path)

# For demonstration
data = [(1, "raw_data_1"), (2, "raw_data_2")]
df_raw = spark.createDataFrame(data, ["id", "data"])

# COMMAND ----------

# MAGIC %md
# MAGIC ## Transform

# COMMAND ----------

df_transformed = df_raw.withColumn(
    "processed_at", F.current_timestamp()
).withColumn(
    "data_upper", F.upper(F.col("data"))
)

# COMMAND ----------

# MAGIC %md
# MAGIC ## Load

# COMMAND ----------

# df_transformed.write.format("delta").mode("overwrite").save(output_path)

df_transformed.show()
