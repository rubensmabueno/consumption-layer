# Data Platform Consumption Layer - Technical Documentation
This document provides a more in-depth technical explanation of the services used in the Data Platform's consumption layer, their configurations, and how to customize them.

## Table of Contents
- [Services](#Services)
  - [Hive Metastore](#Hive Metastore)
  - [Hive Server](#Hive Server)
  - [PrestoDB](#PrestoDB)
    - [Coordinator](#Coordinator)
    - [Worker](#Worker)
  - [LocalStack](#LocalStack)

## Services
### Hive Metastore
Hive Metastore is a metadata repository for Hive tables. It stores table definitions, schema information, and other metadata, allowing for centralized data and table management. In this implementation, a PostgreSQL database is used for metadata storage.

For more detailed documentation, please refer to the [Hive Metastore documentation](https://cwiki.apache.org/confluence/display/Hive/AdminManual+MetastoreAdmin).

### Hive Server
Hive Server is a service that enables remote clients to execute queries against Hive. It provides a JDBC interface for easy integration with various data tools and platforms.

#### Configuration
The Hive Server service is configured using a mapped volume containing the `core-site.xml` file. The following properties can be customized:

- `hadoop.http.staticuser.user`: Sets the user for the HTTP static web user interface.
- `hadoop.proxyuser.hue.hosts`: Specifies the hosts from which the specified proxy user can submit requests.
- `hadoop.proxyuser.hue.groups`: Specifies the groups to which the specified proxy user belongs.
- `fs.defaultFS`: The default FileSystem implementation. Leave it empty if not required.
- `fs.s3a.impl`: Sets the FileSystem implementation for S3.
- `fs.s3a.endpoint`: Sets the S3 endpoint URL for the S3A connector. Set it to http://localstack:4566 for connecting to LocalStack.
- `fs.s3a.access.key`: Sets the S3 access key.
- `fs.s3a.secret.key`: Sets the S3 secret key.
- `fs.s3a.path.style.access`: Enables or disables path-style access for the S3A connector. Set it to true for compatibility with LocalStack.

For more detailed documentation, please refer to the [Hive documentation](https://hive.apache.org/documentation.html).

### PrestoDB
PrestoDB is a distributed SQL query engine designed for low-latency and interactive data analysis. It supports various data sources, including Hive Metastore, and can be easily integrated with other tools in the data platform.

#### Coordinator
The PrestoDB coordinator is responsible for managing worker nodes and coordinating query execution.

##### Configuration
The coordinator.properties file contains the following properties:

- `coordinator`: Set to true for the coordinator node.
- `node-scheduler.include-coordinator`: Determines if the coordinator should also act as a worker. Set to false to disable.
- `http-server.http.port`: The HTTP port for the coordinator.
- `discovery-server.enabled`: Enables the discovery server.
- `discovery.uri`: The URI for the discovery server.

For more detailed documentation, please refer to the [PrestoDB documentation](https://prestodb.io/docs/current/).

#### Worker
PrestoDB workers are responsible for executing tasks and processing data.

##### Configuration
The `worker.properties` file contains the following properties:

- `coordinator`: Set to false for worker nodes.
- `http-server.http.port`: The HTTP port for the worker.
- `discovery.uri`: The URI for the discovery server.

The `catalog/hive.properties` file contains configuration to connect to Hive Metastore (e.g., hive-hadoop2).

- `hive.metastore.uri`: The URI for the Hive Metastore service (e.g., thrift://metastore:9083).
- `hive.s3.aws-access-key`: Sets the AWS access key for S3.
- `hive.s3.aws-secret-key`: Sets the AWS secret key for S3.
- `hive.s3.endpoint`: Sets the S3 endpoint URL for the connector. Set it to http://localstack:4566 for connecting to LocalStack.
- `hive.s3.path-style-access`: Enables or disables path-style access for the connector. Set it to true for compatibility with LocalStack.
- `hive.parquet.use-column-names`: Determines whether to use column names when accessing Parquet files.

For more detailed documentation, please refer to the [PrestoDB Hive Connector documentation](https://prestodb.io/docs/current/connector/hive.html).

### LocalStack
LocalStack is a fully functional local AWS cloud stack, allowing you to develop and test your cloud and serverless apps offline. In this implementation, LocalStack is used to emulate an S3 service.

For more detailed documentation, please refer to the [LocalStack documentation](https://github.com/localstack/localstack).

## Configuration
To customize the configurations, you can edit the corresponding configuration files and map the edited files to the appropriate container volumes. The main configuration files for each service are as follows:

- *Hive Server*: core-site.xml
- *PrestoDB Coordinator*: coordinator.properties
- *PrestoDB Worker*: worker.properties
- *PrestoDB Hive Connector*: hive.properties

Remember to restart the services after making changes to the configuration files for the changes to take effect.

With these configurations, you can set up and customize the Data Platform consumption layer according to your specific needs and requirements.
