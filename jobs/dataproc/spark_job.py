from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def build_session(app_name: str = "RetailPipeline") -> SparkSession:
    return (
        SparkSession.builder
        .appName(app_name)
        .config("spark.sql.shuffle.partitions", "8")
        .config("spark.sql.adaptive.enabled", "true")
        .getOrCreate()
    )


def main() -> None:
    spark = build_session()

    raw = spark.createDataFrame(
        [
            ("2024-01-01", "A", 1200),
            ("2024-01-02", "A", 1500),
            ("2024-01-01", "B", 900),
            ("2024-01-03", "B", 1700),
            ("2024-01-02", "C", 800),
        ],
        ["date", "region", "sales"],
    )

    cleaned = raw.withColumn("sales", F.col("sales").cast("double"))
    summary = cleaned.groupBy("region").agg(
        F.sum("sales").alias("total_sales"),
        F.avg("sales").alias("avg_sales"),
        F.count("sales").alias("sales_records"),
    )

    summary.show(truncate=False)
    cleaned.write.mode("overwrite").parquet("data/output/retail_cleaned.parquet")
    summary.write.mode("overwrite").parquet("data/output/retail_summary.parquet")

    spark.stop()


if __name__ == "__main__":
    main()
