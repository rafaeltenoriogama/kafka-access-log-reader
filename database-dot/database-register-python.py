from kafka import KafkaConsumer
import mysql.connector
import json

# Kafka Consumer configuration
consumer = KafkaConsumer(
    "apachelog",
    bootstrap_servers=["127.0.0.1:9092"],
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    group_id="log-group",
    value_deserializer=lambda x: json.loads(x.decode("utf-8")),
)

# Make a connection with MySQL/MariaDB
db = mysql.connector.connect(
    host="localhost",  # If doesn't work, try 127.0.0.1
    user="your_username",
    password="your_password",
    database="your_database",
)
cursor = db.cursor()

# Proceed write data in kafka and in table of logs on MySQL.
try:
    for message in consumer:
        data = message.value
        sql = """
        INSERT INTO logs (ip, identd, userid, datetime, request, status_code, size, referer, user_agent)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        val = (
            data["ip"],
            data["identd"],
            data["userid"],
            data["datetime"],
            data["request"],
            data["status_code"],
            data["size"],
            data["referer"],
            data["user_agent"],
        )
        cursor.execute(sql, val)
        db.commit()
        print(f"Log entry inserted with ID: {cursor.lastrowid}")
except Exception as e:
    print(f"Error: {str(e)}")
finally:
    # Close connections
    cursor.close()
    db.close()
