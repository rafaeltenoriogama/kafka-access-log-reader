### How create a consumer on Kafka?

I assuming that ou already have a topic created, if not, start by there.

So, you have to create a consumer to read data on that topic, make sure to have same name, bootstrap-server and port.

To following this project and you are in **bin folder** of Kafka, your consumer can be created using this:

```bash
./kafka-console-consumer.sh --bootstrap-server 127.0.0.1:9092 --topic apachelog
```
