# Phase A–H Curriculum Expansion

This document maps the repository to a full advanced learning roadmap for PySpark and cloud-native data engineering work.

## Phase A — Getting started

### Module 01: Introduction to Apache Spark and PySpark
Topics:
- Spark architecture and purpose
- PySpark vs Python, Pandas, and SQL
- Spark ecosystem components
- Batch vs stream processing
- When to use PySpark and when not to use it

### Module 02: Environment Setup and First Program
Topics:
- Installing Python, Java, and PySpark
- Virtual environment configuration
- Jupyter, VS Code, and Colab workflows
- SparkSession and SparkContext
- local mode and cluster mode
- common startup and configuration errors

### Module 03: Python Prerequisites for PySpark
Topics:
- data structures and Python functions
- map, filter, zip, enumerate, and comprehensions
- lambdas and higher-order functions
- exception handling and custom errors
- JSON, files, OOP, and date handling

### Module 04: Spark Architecture and Execution Model
Topics:
- driver, executors, and worker nodes
- jobs, stages, tasks, and partitions
- DAG execution and lazy evaluation
- narrow vs wide transformations
- shuffle, lineage, and task retry strategies

## Phase B — DataFrames and essential operations

### Module 05: Creating DataFrames and Understanding Schemas
Topics:
- createDataFrame and Row objects
- reading CSV, JSON, Parquet, and ORC
- explicit and inferred schemas
- StructType, StructField, nested data
- dtypes, schema inspection, show, collect, take

### Module 06: Selecting, Filtering, and Sorting Data
Topics:
- select, selectExpr, filter, where
- col and column expressions
- sort, orderBy, limit, distinct
- when, otherwise, null-safe conditions

### Module 07: Column Expressions and Built-in Functions
Topics:
- col, lit, expr, coalesce, concat, concat_ws
- boolean, arithmetic, and conditional functions
- reusable expression design
- DataFrame API vs SQL expression style

### Module 08: Missing Data, Duplicates, and Data Quality
Topics:
- null detection and handling
- fillna, dropna, replace, coalesce
- deduplicating records and keys
- data quality checks for validity and completeness

## Phase C — Data transformation mastery

### Module 09: String Functions and Text Processing
Topics:
- upper, lower, trim, length, regexp_replace
- split, substring, contains, rlike
- regex parsing and clean-up logic

### Module 10: Date and Time Functions
Topics:
- to_date, to_timestamp, date_format, datediff
- year, month, day extraction
- months_between, add_months, timestamp parsing
- business periods and time-based slicing

### Module 11: Numeric and Mathematical Functions
Topics:
- rounding, abs, sqrt, ceil, floor
- decimal precision and safe division
- averages, variance, and descriptive stats

### Module 12: Arrays, Maps, Structs, and Nested Data
Topics:
- array, map, struct constructors
- get, element_at, explode, posexplode
- flattening nested payloads and event data

### Module 13: Aggregations and Grouping
Topics:
- groupBy and agg
- countDistinct, approx_count_distinct
- conditional aggregation
- pivots, rollups, cube, and grouping sets

## Phase D — Joins, windows, and relational problem-solving

### Module 14: Joins and Set Operations
Topics:
- inner, left, right, full, semi, anti joins
- self-joins and hierarchical joins
- union, unionByName, intersect, exceptAll
- null keys and duplicate multiplication

### Module 15: Window Functions
Topics:
- partitionBy, orderBy, row_number, rank
- lag, lead, running totals, moving averages
- top-N per group and sessionization

### Module 16: Advanced Transformation Patterns
Topics:
- reusable ETL functions
- transformation pipelines and schema evolution
- incremental loads and slowly changing dimensions
- deduplication and change detection

## Phase E — Reading, writing, and data formats

### Module 17: Reading Data from Files and External Sources
Topics:
- CSV, JSON, Parquet, ORC, Avro, text sources
- partitioned reads and malformed records
- JDBC and cloud-object storage patterns

### Module 18: Writing Data and Managing Output
Topics:
- DataFrameWriter, saveAsTable, partitionBy
- output file count and file sizes
- compression, overwrite, append, atomic writes
- idempotent and safe rerun patterns

## Phase F — Spark SQL and performance engineering

### Module 19: Spark SQL and Temporary Views
Topics:
- spark.sql, temp views, UDFs, SQL functions
- joins, subqueries, CTEs, and window SQL
- query plans and debugging SQL errors

### Module 20: Partitioning, Shuffling, and Data Distribution
Topics:
- input vs shuffle vs output partitions
- repartition vs coalesce
- data skew and salting
- broadcast joins, AQE, predicate pushdown

### Module 21: Performance Optimization and Debugging
Topics:
- explain() and Spark UI analysis
- caching and persistence strategy
- avoiding expensive actions and Python UDFs
- benchmarking and systematic performance tuning

## Phase G — Advanced Spark APIs and distributed computing

### Module 22: UDFs, Pandas UDFs, and RDDs
Topics:
- UDF lifecycle and registration
- scalar and iterator Pandas UDFs
- RDD map, filter, reduceByKey, pair RDDs
- when to prefer DataFrames over RDDs

### Module 23: Advanced Spark Configuration and Execution
Topics:
- SparkConf and runtime configuration
- cluster managers, resource sizing, dynamic allocation
- task retries, event logging, and History Server

## Phase H — Streaming and production systems

### Module 24: Structured Streaming
Topics:
- readStream/writeStream
- output modes, triggers, watermarks
- event-time processing and late data
- Kafka integration and consumer semantics

### Module 25: Testing, Code Quality, and Reusable Pipelines
Topics:
- pytest and DataFrame assertions
- data contracts and regression test design
- environment-driven jobs and schema validation

### Module 26: GCP and PySpark
Topics:
- Dataproc and serverless Spark patterns
- GCS read/write and BigQuery connectors
- IAM, ADC, and service account setup
- pipeline orchestration and cost monitoring

### Module 27: Lakehouse, Delta Lake, and Incremental Processing
Topics:
- raw-cleaned-curated layers
- Delta Lake transaction log and schema enforcement
- CDC, SCD, incremental loads, and idempotent merges

### Module 28: Production Deployment, Orchestration, and Monitoring
Topics:
- Airflow or Cloud Composer
- Docker and packaging
- CI/CD, logging, retries, alerting
- job runbooks and operational monitoring

## Suggested roadmap for this repo

- Start with notebooks 00–08
- Revisit the phases in the order above
- Build small projects in `src/` and `jobs/`
- Use `dags/` and `configs/` for orchestration practice
- Validate outputs in local development before cloud deployment

