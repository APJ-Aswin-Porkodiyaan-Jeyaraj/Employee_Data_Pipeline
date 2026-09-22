from pyspark.sql import SparkSession

# Start Spark
spark = (
    SparkSession.builder
    .appName("EmployeeData")
    .master("local[*]")
    .getOrCreate()
)

# Create sample data
data = [
    (1, "Alice", "IT", 60000),
    (2, "Bob", "IT", 75000),
    (3, "Charlie", "HR", 50000),
    (4, "David", "HR", 55000),
    (5, "Emma", "Finance", 80000),
]

# Set column names
columns = ["employee_id", "name", "department", "salary"]

# Create the DataFrame
df = spark.createDataFrame(data, columns)

# Display the data
df.show()

# Stop Spark
spark.stop()