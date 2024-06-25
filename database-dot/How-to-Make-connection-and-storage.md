# Integrating Kafka Consumer with MySQL/MariaDB Using Python

This document outlines the setup of a MySQL/MariaDB database table and the usage of a Python script to consume messages from a Kafka topic and insert them into the database.

## Database Table Setup

First, create a table in your MySQL/MariaDB database to store the log data. Use the following SQL query to create the table:

```sql
CREATE TABLE logs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    ip VARCHAR(255),
    identd VARCHAR(255),
    userid VARCHAR(255),
    datetime VARCHAR(255),
    request VARCHAR(255),
    status_code INT,
    size VARCHAR(255),
    referer VARCHAR(255),
    user_agent VARCHAR(255)
);
```

### Python Kafka Consumer Script

Utilize the kafka-python library to create a Kafka consumer that subscribes to a specific topic (apachelog). Messages from this topic are deserialized from JSON and inserted into the MySQL/MariaDB database using mysql-connector-python.

### Running the Script

Ensure that both your Kafka broker and MySQL/MariaDB server are active. Execute the script using Python to continuously listen for new messages on the apachelog topic and insert them into the logs table.
Example Command to Run the Script:

```bash
python kafka_consumer.py
```

Be sure to replace the placeholders in the script with your actual database credentials and Kafka settings as necessary.

This setup is excellent for scenarios requiring real-time log analysis or effective monitoring of web traffic through Apache logs, with data efficiently stored in a relational database.
