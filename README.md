# Learning Complete PySpark for GCP Data Engineering

This repository is a complete, production-oriented PySpark learning path for data engineering work on Google Cloud Platform. It combines theory, notebook practice, and real-world orchestration patterns used in enterprise pipelines.

## Full curriculum structure

### Phase A — Getting started
Module 01: Introduction to Apache Spark and PySpark
- Spark concepts and motivation
- PySpark vs Python and Pandas
- Spark ecosystem overview
- Batch vs streaming and distributed computing

Module 02: Environment setup and first program
- Python, Java, and PySpark installation
- VS Code, Jupyter, and Colab setup
- venv and dependency management
- SparkSession and SparkContext
- local mode vs cluster mode

Module 03: Python prerequisites for PySpark
- Python data structures and functions
- lambda, map, filter, reduce patterns
- exception handling and OOP basics
- working with JSON, files, and date objects

Module 04: Spark architecture and execution model
- driver, executors, cluster manager, workers
- DAG, stages, tasks, and partitions
- transformations vs actions
- lazy evaluation and optimization

### Phase B — DataFrames and essential operations
Module 05: Creating DataFrames and understanding schemas
- createDataFrame, Row objects, schema inference
- CSV, JSON, Parquet, and ORC basics
- StructType, StructField, nested data
- df.show(), df.printSchema(), and inspection methods

Module 06: Selecting, filtering, and sorting data
- select, selectExpr, withColumn, filter, where
- aliases, comparisons, and conditional logic
- sorting and null handling strategies

Module 07: Column expressions and built-in functions
- col, lit, expr, when, otherwise, coalesce
- string, numeric, and conditional functions
- SQL-like expressions and reusable transforms

Module 08: Missing data, duplicates, and data quality
- null detection and cleaning
- fillna, dropna, replace
- duplicate detection and deduplication
- data quality checks and quarantine workflows

### Phase C — Data transformation mastery
Module 09: String functions and text processing
- regex, split, concat, trim, replace
- text normalization and parsing patterns

Module 10: Date and time functions
- to_date, to_timestamp, date_format, datediff
- timezone, age, SLA, and calendar logic

Module 11: Numeric and math functions
- round, abs, sqrt, sign, floor, ceil
- safe division, null-safe math, aggregates

Module 12: Arrays, maps, structs, and nested data
- explode, array functions, nested schema access
- flattening and JSON payload parsing

Module 13: Aggregations and grouping
- groupBy, agg, count, sum, avg, min, max
- conditional aggregations and pivot patterns

### Phase D — Joins, windows, and relational problem-solving
Module 14: Joins and set operations
- inner, left, right, full, semi, anti joins
- union, unionByName, intersect, exceptAll
- broadcast joins and join optimization

Module 15: Window functions
- row_number, rank, dense_rank, lag, lead
- cumulative metrics and top-N analysis
- partitioning and ordering strategies

Module 16: Advanced DataFrame transformation patterns
- reusable transformation pipelines
- schema evolution and conditional logic
- SCD patterns and incremental ETL design

### Phase E — Reading, writing, and data formats
Module 17: Reading data from files and external sources
- CSV, JSON, Parquet, ORC, Avro, text files
- folders and glob patterns
- malformed record handling and partitioned reads

Module 18: Writing data and managing output
- DataFrameWriter, partitionBy, bucketing
- write modes, compression, small-file management
- atomic writes and safe reruns

### Phase F — Spark SQL and advanced performance engineering
Module 19: Spark SQL and temporary views
- SQL queries and temp/global views
- window SQL, CTEs, subqueries, joins
- Catalyst optimizer interaction

Module 20: Partitioning, shuffling, and data distribution
- repartition vs coalesce
- shuffle partitions and skew handling
- AQE and adaptive optimization

Module 21: Performance optimization and debugging
- explain(), Spark UI, metrics, stages
- cache/persist, checkpointing, broadcast joins
- profiling and tuning based on evidence

### Phase G — Advanced Spark APIs and distributed computing
Module 22: UDFs, Pandas UDFs, and RDDs
- Python UDFs and vectorized Pandas UDFs
- RDD transformations and pair RDDs
- when to avoid UDFs and when they are justified

Module 23: Advanced Spark configuration and execution
- SparkConf, runtime SQL configs
- cluster managers and deployment modes
- resource tuning and execution safety

### Phase H — Streaming and production systems
Module 24: Structured Streaming
- readStream, writeStream, output modes, triggers
- event-time, watermarks, late data
- Kafka sources and streaming sinks

Module 25: Testing, quality, and reusable pipelines
- unit testing with pytest
- schema validation and regression checks
- production-ready data contracts

Module 26: Google Cloud Platform and PySpark
- Dataproc, GCS, BigQuery, and IAM
- service account auth and ADC
- workload sizing and cost optimization

Module 27: Lakehouse, Delta Lake, and incremental processing
- raw, curated, and trusted layers
- Delta Lake basics and streaming replication patterns
- CDC, SCD, and idempotent merges

Module 28: Deployment, orchestration, and monitoring
- Airflow and workflow orchestration
- CI/CD and environment management
- monitoring, alerting, and job runbooks

## Repository layout

- `README.md` — curriculum overview and quick start
- `CURRICULUM.md` — detailed phase-by-phase learning guide
- `docs/project-structure.md` — project architecture and folder map
- `dags/` — Airflow job definitions
- `jobs/` — Dataproc and Spark job submissions
- `src/` — reusable PySpark pipeline code
- `configs/` — environment and project configuration files
- `tests/` — unit and integration testing examples
- `data/` — sample datasets and local output folders
- `notebooks/` — Jupyter notebooks for hands-on learning

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Local Spark smoke test

```python
from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("PySpark-Check") \
    .master("local[*]") \
    .getOrCreate()

print(spark.version)
print(spark.range(5).collect())
spark.stop()
```

## Production mindset

This repo is not only about syntax. It is structured around the engineering realities of:
- building reusable ETL transforms
- validating schemas and data quality
- orchestrating workloads with Airflow or Composer
- running on GCP with GCS, BigQuery, and Dataproc
- handling failures, retries, and monitoring in production

The goal is to help you move from notebook exercises to real-world data engineering work.

## Recommended order

1. Complete notebooks 00–08
2. Study `CURRICULUM.md` by phase
3. Review `docs/project-structure.md`
4. Build the sample Airflow + Dataproc project skeleton
5. Practice your own ETL pipeline with synthetic and real data

Happy learning and building production-grade Spark pipelines.

---

This repository is designed for end-to-end PySpark knowledge, from fundamentals to orchestration and cloud deployment.

