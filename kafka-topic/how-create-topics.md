### How to create topics and how many partitions?

By default, the replication factor is 1, but to have efficiency, we should create 3 brokers, to have 3 partitions and replication factor on 3.

You can have 3 brokers on same machine or VM, but have in mind that the zookeeper will make a election and select other broker to assume if you have problems, so, have brokers on different machines should be more relevant.

Anyway, supposed that you are in kafka/bin directory, let's make a topic with default replication:

```bash
./kafka-topic.sh --bootstrap-server 127.0.0.1:9092 --topc apachelog --create --partitions 3 --replication-factor 1
´´´
```
