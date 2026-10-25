from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main() -> None:
    spark = SparkSession.builder \
        .appName("LocalPySparkPipeline") \
        .master("local[*]") \
        .config("spark.sql.shuffle.partitions", "4") \
        .getOrCreate()

    data = [
        (1, "Alice", "2024-01-01", 2500),
        (2, "Bob", "2024-01-02", 3200),
        (3, "Charlie", "2024-01-03", 2800),
    ]

    df = spark.createDataFrame(data, ["id", "name", "date", "salary"])
    result = df.withColumn("salary", F.col("salary").cast("double"))
    result.show()

    spark.stop()


if __name__ == "__main__":
    main()
