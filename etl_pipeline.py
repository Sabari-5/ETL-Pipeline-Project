import os
import pandas as pd
from sqlalchemy import create_engine
import boto3
import snowflake.connector
from config import *

os.makedirs("output", exist_ok=True)

print("Step 1 : Connecting MySQL")

engine = create_engine(
    f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}"
)

query = "SELECT * FROM employees"

df = pd.read_sql(query, engine)

print(df.head())

print("Rows Extracted :", len(df))

# --------------------------
# CSV
# --------------------------

csv_file = "output/employees.csv"

df.to_csv(csv_file, index=False)

print("CSV Created")

# --------------------------
# Parquet
# --------------------------

parquet_file = "output/employees.parquet"

df.to_parquet(parquet_file, index=False)

print("Parquet Created")

# --------------------------
# Upload S3
# --------------------------

s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY,
    aws_secret_access_key=AWS_SECRET_KEY
)

s3.upload_file(
    parquet_file,
    AWS_BUCKET,
    'employees/employees.parquet'
)

print("Uploaded to S3")

# --------------------------
# Snowflake
# --------------------------

conn = snowflake.connector.connect(
    user=SNOWFLAKE_USER,
    password=SNOWFLAKE_PASSWORD,
    account=SNOWFLAKE_ACCOUNT,
    warehouse=SNOWFLAKE_WAREHOUSE,
    database=SNOWFLAKE_DATABASE,
    schema=SNOWFLAKE_SCHEMA
)

cursor = conn.cursor()

cursor.execute("""
CREATE OR REPLACE STAGE EMP_STAGE
""")

print("Stage Created")

cursor.execute("""
COPY INTO EMPLOYEES
FROM @EMP_STAGE
FILE_FORMAT = (TYPE = PARQUET)
MATCH_BY_COLUMN_NAME = CASE_INSENSITIVE
""")

print("Data Loaded Snowflake")

cursor.close()
conn.close()

print("ETL Completed Successfully")