# Databricks notebook source
# MAGIC %md
# MAGIC # Hello World - Databricks Application
# MAGIC
# MAGIC A simple demonstration of Databricks and PySpark capabilities.

# COMMAND ----------

# MAGIC %md
# MAGIC ## 1. Hello World - Basic Output

# COMMAND ----------

print("Hello, Databricks!")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 2. Hello World - With Spark

# COMMAND ----------

from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("HelloWorld").getOrCreate()

# Display Spark version
print(f"Spark Version: {spark.version}")

# COMMAND ----------

# MAGIC %md
# MAGIC ## 3. Hello World - Create a DataFrame

# COMMAND ----------

# Create a simple DataFrame with greetings
greetings = [
    ("English", "Hello, World!"),
    ("Spanish", "¡Hola, Mundo!"),
    ("French", "Bonjour, le Monde!"),
    ("German", "Hallo, Welt!"),
    ("Japanese", "こんにちは、世界！"),
    ("Python", "print('Hello, World!')"),
]

df = spark.createDataFrame(greetings, ["language", "greeting"])
df.show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 4. Hello World - Basic Transformations

# COMMAND ----------

from pyspark.sql.functions import length, upper

# Add columns showing greeting length and uppercase version
df_transformed = df.withColumn("length", length("greeting")).withColumn(
    "greeting_upper", upper("greeting")
)

df_transformed.show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 5. Hello World - SQL Query

# COMMAND ----------

# Register as a temporary view
df.createOrReplaceTempView("greetings")

# Query using Spark SQL
result = spark.sql("""
    SELECT
        language,
        greeting,
        LENGTH(greeting) as greeting_length
    FROM greetings
    WHERE LENGTH(greeting) > 15
    ORDER BY greeting_length DESC
""")

result.show(truncate=False)

# COMMAND ----------

# MAGIC %md
# MAGIC ## 6. Hello World - Summary Statistics

# COMMAND ----------

from pyspark.sql.functions import avg, max, min, count

# Calculate statistics on greeting lengths
stats = df.withColumn("length", length("greeting")).agg(
    count("*").alias("total_greetings"),
    avg("length").alias("avg_length"),
    min("length").alias("min_length"),
    max("length").alias("max_length"),
)

stats.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ## Complete!
# MAGIC
# MAGIC This notebook demonstrated:
# MAGIC - Basic print statements
# MAGIC - Creating Spark DataFrames
# MAGIC - DataFrame transformations
# MAGIC - Spark SQL queries
# MAGIC - Aggregations and statistics
