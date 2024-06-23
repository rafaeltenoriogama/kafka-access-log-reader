import time
import re
import datetime
from kafka import KafkaProducer as kp

log_file = open(r"/var/log/apache2/access.log", "r")
regexp = r'^([\d.]+) (\S+) (\S+) \[([\w:/]+)\s[+\-]\d{4}\] "(.+?)" (\d{3}) (\d+|-) "([^"]+)" "([^"]+)"'
my_producer = kp(bootstrap_servers="127.0.0.1:9092")

while 1:
    log_line = log_file.readline()
    if not log_line:
        time.sleep(5)
    else:
        x = re.match(regexp, log_line).groups()
        msg = bytes(str(x), encoding="acii")
        my_producer.send("apachelog", msg)
        print("Message was sent on: ", datetime.datetime.now())
