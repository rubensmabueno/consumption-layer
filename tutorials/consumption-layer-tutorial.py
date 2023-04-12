import pandas as pd
from pyhive import hive, presto

# Create sample data
data = {
    'id': [1, 2, 3, 4],
    'name': ['John', 'Jane', 'Bob', 'Alice'],
    'age': [25, 30, 20, 35]
}
df = pd.DataFrame(data)

# Save dataframe to buffer in Parquet format
df.to_parquet("s3://datalake/example/records.parquet", storage_options={'endpoint_url': 'http://localhost:4566'})

# Connect to Hive server
hive_conn = hive.Connection(host='localhost', port=10000, username='hive', database='default')

# Create an external table for the Parquet file
with hive_conn.cursor() as cursor:
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

# Query data using Hive Server
with hive_conn.cursor() as cursor:
    cursor.execute("""
        SELECT * FROM example
    """)
    results = cursor.fetchall()
    print("Results from Hive Server:")
    for row in results:
        print(row)

# Connect to PrestoDB
conn_presto = presto.connect(host='localhost', port=8081, username='presto', catalog='hive', schema='default')

# Query data using PrestoDB
cursor_presto = conn_presto.cursor()
cursor_presto.execute("""
    SELECT * FROM example
""")
results = cursor_presto.fetchall()
print("Results from PrestoDB:")
for row in results:
    print(row)

print("Finished")