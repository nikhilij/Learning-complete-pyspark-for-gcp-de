from __future__ import annotations

from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator


def extract_data():
    print("[extract] reading raw files from GCS or local storage")


def transform_data():
    print("[transform] cleaning, validating, and normalizing data")


def load_data():
    print("[load] writing curated data to Parquet or BigQuery")


def validate_data():
    print("[validate] checking data quality and counts")


with DAG(
    dag_id="pyspark_gcp_pipeline",
    description="Example PySpark + GCP orchestration DAG",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False,
    default_args={
        "retries": 2,
        "retry_delay": timedelta(minutes=5),
    },
) as dag:

    task_extract = PythonOperator(
        task_id="extract_data",
        python_callable=extract_data,
    )

    task_transform = PythonOperator(
        task_id="transform_data",
        python_callable=transform_data,
    )

    task_load = PythonOperator(
        task_id="load_data",
        python_callable=load_data,
    )

    task_validate = PythonOperator(
        task_id="validate_data",
        python_callable=validate_data,
    )

    task_extract >> task_transform >> task_load >> task_validate
