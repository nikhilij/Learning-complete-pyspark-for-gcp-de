# Project Structure and Workflow Blueprint

This repository follows a production-minded project layout for PySpark, Airflow, Dataproc, and GCS workflows.

## Root structure

```text
.
├── README.md
├── CURRICULUM.md
├── requirements.txt
├── .gitignore
├── notebooks/
│   ├── 00_Environment_Setup.ipynb
│   ├── 01_PySpark_Fundamentals.ipynb
│   ├── 02_RDDs_and_DataFrames.ipynb
│   ├── 03_Transformations_Actions_and_Schemas.ipynb
│   ├── 04_Aggregations_Joins_and_Window_Functions.ipynb
│   ├── 05_Spark_SQL_and_Optimization.ipynb
│   ├── 06_GCP_Integration.ipynb
│   ├── 07_Streaming_and_MLlib.ipynb
│   └── 08_Capstone_Project.ipynb
├── data/
│   ├── raw/
│   ├── cleaned/
│   ├── curated/
│   └── output/
├── src/
│   └── pyspark_pipeline/
│       ├── __init__.py
│       ├── config.py
│       ├── utils.py
│       ├── etl.py
│       └── jobs/
│           ├── __init__.py
│           └── sales_pipeline.py
├── jobs/
│   ├── dataproc/
│   │   ├── submit_job.sh
│   │   └── spark_job.py
│   └── local/
│       └── run_local_pipeline.py
├── dags/
│   └── airflow_pyspark_gcp_dag.py
├── configs/
│   ├── .env.example
│   ├── gcp_config.yaml
│   └── spark_defaults.conf
├── tests/
│   ├── test_transformations.py
│   ├── test_data_quality.py
│   └── test_sql_pipeline.py
├── docs/
│   └── project-structure.md
└── scripts/
    ├── setup_env.sh
    └── validate_spark.sh
```

## Workflow architecture

1. Raw data lands in GCS or local raw folder.
2. Spark jobs clean and normalize the raw layer.
3. Curated outputs are written to Parquet or Delta files.
4. BigQuery or downstream warehouses consume curated tables.
5. Airflow orchestrates tasks and monitors schedule, retries, and failures.

## Example pipeline stages

- `extract` — read raw files from GCS local inputs
- `transform` — schema validation, deduplication, conversions
- `load` — write cleaned and curated outputs
- `validate` — run quality checks and record metrics
- `notify` — emit alerts when failures or anomalies occur

## Recommended execution flow

- local development: `python jobs/local/run_local_pipeline.py`
- Dataproc submission: `gcloud dataproc jobs submit pyspark ...`
- Airflow deployment: upload `dags/` into Cloud Composer or local Airflow

## Key engineering principles

- separate raw, cleaned, curated layers
- prefer Parquet for analytical datasets
- validate schema before writing output
- use caching only when repeated reads justify it
- batch and streaming pipelines should share quality checks

