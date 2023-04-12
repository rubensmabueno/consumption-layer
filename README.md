# Data Platform Consumption Layer
This repository provides a Docker Compose-based implementation of the Data Platform consumption layer as described in the article [Data Platform - Solution for Consumption (Part 2)](https://rubensminoru.medium.com/data-platform-solution-for-consumption-part-2-3019c5832266).

The consumption layer includes components for data persistence, storage, cataloging, and processing, which together address the challenges faced by traditional commercial Data Warehouse solutions, such as limited scalability and tightly coupled architecture as mentioned in this article [Data Platform — The Challenges (Part 1)](https://medium.com/@rubensminoru/data-platform-the-challenges-part-1-7bd86657e273).

## Architecture
The architecture of this Data Platform consumption layer consists of the following components:

- Permanent Memory: Object Storage (S3)
- Storage Engine: Parquet columnar format
- Catalog Manager: Hive Metastore
- Computation Engine: PrestoDB and Hive

These components are decoupled and highly scalable, providing an efficient and flexible solution for various data consumption needs.

## Getting Started
### Prerequisites
- Docker
- Docker Compose

### Setup
1. Clone this repository to your local machine.
2. Navigate to the root directory of the project.
3. Run `docker-compose up -d` to start all the services.

The Docker Compose configuration includes the following services:

1. Hive Server
2. Metastore
3. PostgreSQL
4. LocalStack
5. PrestoDB Coordinator
6. PrestoDB Workers
7. Hue
For detailed information on each service, please refer to the [technical documentation](https://github.com/rubensmabueno/consumption-layer/edit/main/TECHNICAL.md).

### Usage
Once all services are up and running, you can access the different components of the Data Platform consumption layer using their respective ports and tools:

- Hive: Connect to HiveServer2 on port 10000
- Metastore: Connect to the Hive metastore on port 9083
- PostgreSQL: Connect to the PostgreSQL database on port 5432
- LocalStack: Access S3 storage on port 4566
- Coordinator: Access the PrestoDB coordinator on port 8081
- Hue: Access the Hue web interface on port 8888

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License
This project is licensed under the MIT License - see the [LICENSE](https://github.com/rubensmabueno/consumption-layer/edit/main/LICENSE) file for details.
