# ------- Getting Started ------- 
import numpy as np
import pandas as pd
# Import SparkSession from pyspark.sql
from pyspark.sql import SparkSession
# Import pyspark.sql.functions as F
import pyspark.sql.functions as F
# Create my_spark
my_spark = SparkSession.builder.getOrCreate()
# Print the tables in the catalog
print(spark.catalog.listTables())

# ------- Querying dataframes with SQL commands ------- 
query = "SELECT origin, dest, COUNT(*) as N FROM flights GROUP BY origin, dest"
# Run the query
flight_counts = spark.sql(query)
# Convert the results to a pandas DataFrame
pd_counts = flight_counts.toPandas()

# ------- Moving from Pandas to PySpark ------- 
pd_temp = pd.DataFrame(np.random.random(10))
spark_temp = spark.createDataFrame(pd_temp)
# Examine the tables in the catalog
print(spark.catalog.listTables())
# Add spark_temp to the catalog
spark_temp.createOrReplaceTempView('temp')

# ------- From a file path -------
# Don't change this file path
file_path = "/usr/local/share/datasets/airports.csv"
# Read in the airports data
airports = spark.read.csv(file_path, header=True)

# Show the data
airports.show()

# ------- SQL with PySpark -------
# Filter flights with a SQL string
long_flights1 = flights.filter("air_time > 120").show()
# Filter flights with a boolean column
long_flights2 = flights.filter(flights.air_time > 120).show()

# Select the first set of columns
selected1 = flights.select("tailnum", "origin", "dest")
# Select the second set of columns
temp = flights.select(flights.origin, flights.dest, flights.carrier)
# Define first filter
filterA = flights.origin == "SEA"
# Define second filter
filterB = flights.dest == "PDX"
# Filter the data, first by filterA then by filterB
selected2 = temp.filter(filterA).filter(filterB)

# Define avg_speed
avg_speed = (flights.distance/(flights.air_time/60)).alias("avg_speed")
# Select the correct columns
speed1 = flights.select("origin", "dest", "tailnum", avg_speed)
# Create the same table using a SQL expression
speed2 = flights.selectExpr("origin", "dest", "tailnum", "distance/(air_time/60) as avg_speed")

# Find the shortest flight from PDX in terms of distance
flights.filter(flights.origin == "PDX").groupBy().min("distance").show()
# Average duration of Delta flights
flights.filter(flights.carrier == "DL").filter(flights.origin == "SEA").groupBy().avg("air_time").show()
# Total hours in the air
flights.withColumn("duration_hrs", flights.air_time/60).groupBy().sum("duration_hrs").show()

# Group by month and dest
by_month_dest = flights.groupBy("month", "dest")
# Average departure delay by month and destination
by_month_dest.avg("dep_delay").show()
# Standard deviation
by_month_dest.agg(F.stddev("dep_delay")).show()