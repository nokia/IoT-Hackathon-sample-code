# How to access an InfluxDB 

The sensors in the Hackathon write their measurement results in an InfluxDB. InfluxDB differs slightly from a normal database, although many of the same commands also work. In the hackathon the InfluxDB runs at address 192.168.1.200, but these examples use a local InfluxDB as an example.

Easiest way to get started with InfluxDB is to run it in a container:

```
docker run -p 8086:8086 --name influx influxdb
```

InfluxDB has a command line interface called influx. Here is a sample session:

```
% influx
Connected to http://localhost:8086 version 1.7.5
InfluxDB shell version: 1.7.3
Enter an InfluxQL query
> show databases;
name: databases
name
----
_internal

> create database test1
> show databases
name: databases
name
----
_internal
test1
> use test1
Using database test1
> show measurements
```

We created a database called test1. Inside the database there are measurements. 

There is also a REST interface. We create another database and put some data in it:

```
% curl -i -XPOST http://localhost:8086/query --data-urlencode q="CREATE DATABASE test2"                                  
HTTP/1.1 200 OK
Content-Type: application/json
Request-Id: 5f5740b9-6c36-11e9-8033-0242ac110002
X-Influxdb-Build: OSS
X-Influxdb-Version: 1.7.5
X-Request-Id: 5f5740b9-6c36-11e9-8033-0242ac110002
Date: Wed, 01 May 2019 17:27:19 GMT
Transfer-Encoding: chunked

{"results":[{"statement_id":0}]}
 
% curl -i -XPOST http://localhost:8086/write\?db=test2 --data-binary "measurements,tag1=good,tag2=bad value1=123,value2=234"
% curl -i -XPOST http://localhost:8086/write\?db=test2 --data-binary "measurements,tag1=good,tag2=bad value1=123,value2=234"
% curl -i -XPOST http://localhost:8086/write\?db=test2 --data-binary "measurements,tag1=good value1=123,value3=345" 
```

The result is as follows. InfluxDB put the time by itself and allows any number of tags and values.

```
% influx
Connected to http://localhost:8086 version 1.7.5
InfluxDB shell version: 1.7.3
Enter an InfluxQL query
> use test2
Using database test2
> show measurements
name: measurements
name
----
measurements

> select * from "measurements"
name: measurements
time                tag1 tag2 value1 value2 value3
----                ---- ---- ------ ------ ------
1556731662530416587 good bad  123    234    
1556731664990461520 good bad  123    234    
1556731682561055307 good      123           345

> select * from "measurements" where "tag2" = 'bad'
name: measurements
time                tag1 tag2 value1 value2 value3
----                ---- ---- ------ ------ ------
1556731662530416587 good bad  123    234    
1556731664990461520 good bad  123    234    


> select * from "measurements" where "time" > now() - 10m
name: measurements
time                tag1 tag2 value1 value2 value3
----                ---- ---- ------ ------ ------
1556731662530416587 good bad  123    234    
1556731664990461520 good bad  123    234    
1556731682561055307 good      123           345
```

The key to understanding the REST interface is that it encapsulates the InfluxDB query language which is explained in https://docs.influxdata.com/influxdb/v1.7/query_language/data_exploration/ with examples.

The REST interface works well for shell scripts. There are bindings to different programming languages, like Python (https://pypi.org/project/influxdb/).

