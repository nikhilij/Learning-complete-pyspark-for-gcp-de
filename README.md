# Learning Complete PySpark for GCP Data Engineering

This repository is a structured, hands-on learning path for mastering Apache Spark with PySpark, focused on real-world GCP data engineering workflows.

It is designed for a complete beginner to intermediate learner who wants to go from Python basics and Spark fundamentals to advanced optimization, streaming, ML, and cloud integration.

## What you will learn

- Spark architecture and execution model
- RDDs, DataFrames, and Datasets
- Data transformations, actions, and lazy evaluation
- Spark SQL, window functions, and aggregations
- Joins, schema design, and debugging patterns
- Performance tuning and optimization
- Reading/writing from CSV, JSON, Parquet, Delta, GCS, and BigQuery
- Structured streaming
- PySpark MLlib and feature engineering
- Building end-to-end GCP data pipelines

## Repository structure

- `README.md` — roadmap and navigation
- `requirements.txt` — Python dependency list
- `notebooks/` — Jupyter notebooks for each learning stage
- `.gitignore` — common file exclusions

## Recommended learning path

1. Start with environment setup and Python/Spark basics
2. Learn RDDs and DataFrames
3. Master transformations, actions, and DataFrame operations
4. Practice aggregations, joins, and SQL
5. Learn performance optimization and debugging
6. Move into GCP integration with GCS and BigQuery
7. Learn streaming and modern data engineering patterns
8. Practice MLlib and complete a capstone project

## Notebook roadmap

### Level 0: Setup and foundations
- `notebooks/00_Environment_Setup.ipynb` — Install Spark, configure Jupyter, validate your environment
- `notebooks/01_PySpark_Fundamentals.ipynb` — SparkSession, architecture, lazy evaluation, basic APIs

### Level 1: Core Spark data processing
- `notebooks/02_RDDs_and_DataFrames.ipynb` — RDDs, DataFrame creation, schema inference
- `notebooks/03_Transformations_Actions_and_Schemas.ipynb` — select/filter/withColumn/groupBy and column logic
- `notebooks/04_Aggregations_Joins_and_Window_Functions.ipynb` — aggregations, joins, window functions
- `notebooks/05_Spark_SQL_and_Optimization.ipynb` — SQL, catalog, caching, explain plans, performance basics

### Level 2: Real-world engineering and GCP
- `notebooks/06_GCP_Integration.ipynb` — GCS, BigQuery, external tables, ETL pipeline patterns
- `notebooks/07_Streaming_and_MLlib.ipynb` — Structured Streaming and MLlib workflows
- `notebooks/08_Capstone_Project.ipynb` — end-to-end data pipeline project

## Environment setup

### Prerequisites

- Python 3.9+
- Java 11 or 17
- Jupyter Notebook or VS Code with notebook support
- Git
- A GCP account for cloud-related exercises (optional but recommended)

### Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Start Jupyter

```bash
jupyter notebook
```

## Local Spark quick check

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

## Suggested study methodology

- Read the markdown cells first, then run the code cells
- Rewrite examples in your own words and try variations
- Try to predict output before execution
- Create your own mini datasets and edge cases
- Practice one new concept per notebook
- Keep a personal notes file for tricky concepts

## Core concepts to master

### Spark conceptual model
- Cluster manager
- Driver program
- Executors
- Tasks
- Transformations vs actions
- Lazy execution

### Data engineering patterns
- partitioning
- bucketing
- caching
- broadcasting joins
- skew handling
- file formats and schemas

### GCP ecosystem patterns
- Cloud Storage as raw landing zone
- BigQuery as warehouse
- Dataproc or EMR for Spark jobs
- Pub/Sub + Structured Streaming for event ingestion
- Airflow or Cloud Composer for orchestration

## Practice exercises

After each notebook, practice with:

- 3 questions from the notebook
- 1 real-world scenario
- 1 dataset variation
- 1 optimization idea

## Learning outcomes

By the end of this repo, you should be able to:

- build data transformation pipelines in PySpark
- debug and optimize Spark jobs
- read and write many file formats
- work with datasets in a distributed environment
- design production-minded Spark workflows for GCP
- build interview-ready and portfolio-ready PySpark projects

## Additional resources

- Apache Spark official docs
- Databricks learning resources
- GCP BigQuery and Cloud Storage docs
- PySpark API documentation

## Notes

This repository is intended for practical learning. It emphasizes understanding the why and how behind each concept, not just memorizing syntax.

You are encouraged to modify, extend, and experiment with the notebooks to deepen understanding.

## Next step

Open the notebooks in order and work through them sequentially. Start with `00_Environment_Setup.ipynb` and finish with the capstone project.

Happy learning!
