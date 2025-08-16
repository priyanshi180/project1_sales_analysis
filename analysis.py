import pandas as pd
from pyspark.sql import SparkSession

# Initialize Spark
spark = SparkSession.builder.appName("SalesAnalysis").getOrCreate()

# Load CSV data
df = spark.read.csv("data.csv", header=True, inferSchema=True)

# Show data
df.show()

# Group by region and sum sales
region_sales = df.groupBy("region").sum("sales")
region_sales.show()

# Stop Spark
spark.stop()
