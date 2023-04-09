import pandas as pd
import boto3
from io import BytesIO
from pyhive import hive

# generate sample data
data = {
    'id': [1, 2, 3, 4],
    'name': ['John', 'Jane', 'Bob', 'Alice'],
    'age': [25, 30, 20, 35]
}
df = pd.DataFrame(data)

# save dataframe to buffer in parquet format
df.to_parquet("s3://datalake/example/records.parquet", engine='pyarrow', compression='snappy', storage_options={'endpoint_url': 'http://localhost:4566'})

# connect to hive metastore
conn = hive.Connection(host='localhost', port=10000, username='hive', database='default')

# create external table for parquet file
with conn.cursor() as cursor:
    cursor.execute("""DROP TABLE example""")
    cursor.execute("""
        CREATE EXTERNAL TABLE IF NOT EXISTS example (
            id BIGINT,
            name STRING,
            age BIGINT
        )
        STORED AS PARQUET
        LOCATION 's3a://datalake/example/'
    """)

with conn.cursor() as cursor:
    cursor.execute("""
        SELECT * FROM example
    """)
    results = cursor.fetchall()
    for row in results:
        print(row)

print("Finished")
