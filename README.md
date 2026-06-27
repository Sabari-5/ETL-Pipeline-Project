# ETL-Pipeline-Project

# 🚀 End-to-End ETL Pipeline using Python, MySQL, AWS S3, and Snowflake

## 📌 Project Overview

This project demonstrates an end-to-end ETL (Extract, Transform, Load) pipeline built using Python.

The pipeline extracts employee data from a MySQL database, converts it into CSV and Parquet formats, uploads the Parquet file to Amazon S3, and finally loads the data into Snowflake for analytics.

This project simulates a real-world data engineering workflow used in modern cloud-based data platforms.

---

## 🛠️ Technologies Used

- Python
- Pandas
- SQLAlchemy
- MySQL
- AWS S3
- Snowflake
- Boto3
- PyMySQL

---

## 📂 Project Structure

```
ETL-Pipeline/
│
├── output/
│   ├── employees.csv
│   └── employees.parquet
│
├── config.py
├── etl_pipeline.py
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🔄 ETL Workflow

### Step 1 - Extract

- Connect to the MySQL database using SQLAlchemy.
- Read employee data from the `employees` table.
- Load the data into a Pandas DataFrame.

```python
SELECT * FROM employees;
```

---

### Step 2 - Transform

The extracted data is converted into:

- CSV format
- Parquet format

Parquet is used because it is a compressed columnar file format that provides better storage efficiency and faster query performance.

---

### Step 3 - Upload to AWS S3

The generated Parquet file is uploaded to an Amazon S3 bucket using Boto3.

```
employees/
    employees.parquet
```

---

### Step 4 - Load into Snowflake

The pipeline connects to Snowflake and performs the following actions:

- Creates a Snowflake Stage.
- Reads the Parquet file from the stage.
- Loads the data into the `EMPLOYEES` table using the COPY INTO command.

---

## 📊 ETL Architecture

```
             MySQL Database
                    │
                    ▼
             Python ETL Script
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
   employees.csv         employees.parquet
                                │
                                ▼
                           Amazon S3
                                │
                                ▼
                        Snowflake Stage
                                │
                                ▼
                      Snowflake EMPLOYEES Table
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone https://github.com/yourusername/ETL-Pipeline.git
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure credentials

Update the `config.py` file with your credentials:

- MySQL
- AWS
- Snowflake

Example:

```python
MYSQL_HOST=
MYSQL_USER=
MYSQL_PASSWORD=

AWS_ACCESS_KEY=
AWS_SECRET_KEY=
AWS_BUCKET=

SNOWFLAKE_USER=
SNOWFLAKE_PASSWORD=
SNOWFLAKE_ACCOUNT=
```

### Run the pipeline

```bash
python etl_pipeline.py
```

---

## ✅ Expected Output

```
Step 1 : Connecting MySQL

Rows Extracted : 1000

CSV Created

Parquet Created

Uploaded to S3

Stage Created

Data Loaded Snowflake

ETL Completed Successfully
```

---

## 📈 Key Features

- Automated ETL workflow
- Extracts data from MySQL
- Converts data into CSV and Parquet formats
- Uploads files to AWS S3
- Loads data into Snowflake
- Uses SQLAlchemy for database connectivity
- Uses Pandas for data processing
- Uses Boto3 for cloud integration
- Modular configuration using `config.py`

---

## 📌 Future Enhancements

- Add data validation checks
- Implement logging using Python logging module
- Add exception handling
- Schedule the pipeline using Apache Airflow or Cron
- Integrate dbt for data transformations
- Add CI/CD with GitHub Actions
- Build dashboards using Power BI

---

## 👨‍💻 Author

**Sabari R**

Aspiring Data Engineer | Python | SQL | AWS | Snowflake | ETL | Power BI
