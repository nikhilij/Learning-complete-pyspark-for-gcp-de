# Learning Complete PySpark for GCP Data Engineering

This repository is a structured, hands-on learning path for mastering Apache Spark with PySpark, with a strong focus on real-world GCP data engineering workflows and production-style orchestration patterns.

## What this repository covers

- Spark architecture and execution model
- RDDs, DataFrames, and Datasets
- Data transformations, actions, and lazy evaluation
- Spark SQL, window functions, and aggregations
- Joins, schema design, and debugging patterns
- Performance tuning and optimization
- Reading/writing CSV, JSON, Parquet, and Delta-style patterns
- Structured streaming
- GCS, BigQuery, Dataproc, and cloud integration
- End-to-end ETL pipelines and orchestration concepts

## Popular orchestration-oriented roadmap

### Phase A — Getting started
- 00: Environment setup and first Spark run
- 01: Apache Spark and PySpark fundamentals
- 02: RDDs and DataFrames
- 03: Transformations, actions, and schema handling
- 04: Aggregations, joins, and window functions

### Phase B — DataFrames and essential operations
- 05: Spark SQL and optimization
- 06: GCP integration patterns
- 07: Structured streaming and MLlib
- 08: Capstone project

### Production engineering checklist
- build reusable transformation functions
- validate schemas early
- separate raw, cleaned, and curated layers
- use partitioning and caching only when warranted
- monitor job latency, throughput, and skew
- automate with Airflow or Cloud Composer
- test pipeline behavior with realistic synthetic data

## Repository structure

- `README.md` — roadmap and navigation
- `requirements.txt` — Python package dependencies
- `notebooks/` — Jupyter notebooks for each learning stage

## Local setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook
```

## Quick Spark verification

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

## Recommended workflow

1. Read the notebook markdown cells first
2. Run each code example in order
3. Rewrite code in your own words and modify parameters
4. Practice at least one real-world scenario per notebook
5. Track what each Spark transformation is doing conceptually

This repository is designed not just to teach syntax but to build practical PySpark understanding for real data engineering work and orchestration-driven workflows.
