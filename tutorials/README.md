# Data Platform Consumption Layer Tutorial
This tutorial demonstrates how to use the Data Platform consumption layer to store, retrieve, and process data using
PrestoDB and the Parquet format. We will use a Python script to create a sample dataset, store it in the S3 object storage,
and then query the data using PrestoDB and Hive Server.

## Prerequisites
1. Set up the Data Platform consumption layer using the provided Docker Compose configuration. Follow steps described [here](https://github.com/rubensmabueno/consumption-layer/blob/main/README.md#setup).
2. Install Python 3
3. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Step 1: Save sample data to S3 in Parquet format
First, we will create a sample dataset using Pandas. This dataset includes information about four individuals, with columns for id, name, and age. Next, we will save the dataframe in the Parquet format and then upload it to the S3 object storage.

```python
import boto3
from io import BytesIO
import pandas as pd

data = {
    'id': [1, 2, 3, 4],
    'name': ['John', 'Jane', 'Bob', 'Alice'],
    'age': [25, 30, 20, 35]
}
df = pd.DataFrame(data)

# Save dataframe to buffer in Parquet format
df.to_parquet("s3://datalake/example/records.parquet", storage_options={'endpoint_url': 'http://localhost:4566'})
```

## Step 2: Create new table on Hive Metastore
We will now connect to the Hive metastore to create an external table for the Parquet file stored in S3.

```python
from pyhive import hive

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
```

## Step 3: Query data using Hive Server
Now, we will execute a SELECT statement using Hive Server to retrieve the data from the external table and print the results.

```python
with hive_conn.cursor() as cursor:
    cursor.execute("""
        SELECT * FROM example
    """)
    results = cursor.fetchall()
    print("Results from Hive Server:")
    for row in results:
        print(row)
```

## Step 4: Query data using PrestoDB
Finally, we will execute a SELECT statement using PrestoDB to retrieve the data from the external table and print the results.

```python
from pyhive import presto

conn_presto = presto.connect(host='localhost', port=8081, username='presto', catalog='hive', schema='default')

# Query data using PrestoDB
cursor_presto = conn_presto.cursor()
cursor_presto.execute("""
    SELECT * FROM example
""")
results = cursor_presto.fetchall()
for row in results:
    print(row)
```

The complete Python script for this tutorial can be found [here](https://github.com/rubensmabueno/consumption-layer/blob/main/tutorials/consumption-layer-tutorial.py).

This tutorial shows how the consumption layer of the Data Platform allows for the flexible storage and retrieval of data, allowing users to take advantage of the benefits of the Parquet format and powerful querying capabilities of PrestoDB and Hive Server.