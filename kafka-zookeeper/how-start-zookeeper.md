#### How start zookeeper

I will shared only relevants information for the project, but if you want understand deeply about zookeeper, just check the documentation on kafka.

It is important to know that you have to start the zookeeper **before** start the kafka server.

The zookeeper once started, have to be follow by the file **zookeeper.properties**, which is the one who has de proper configuration to initialize zookeeper and have the changes like different ports connection to connect with.

So, once on the _bin_ folder of kafka, the command on CLI will be look like this:

```bash
./zookeeper-server-start.sh ../config/zookeeper.properties
```

You can overwrite the files on original **bin** and **config** folder of kafka.
