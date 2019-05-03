# Pushing data from Raspberry Pi to InfluxDB

With [piroommonitor](https://github.com/kangasta/piroommonitor.git) and [fdbk](https://github.com/kangasta/fdbk.git):

```bash
sudo apt-get remove python3-requests

git clone https://github.com/kangasta/piroommonitor.git
cd piroommonitor
sudo python3 setup.py install

piroommonitor --db-connection InfluxConnection 192.168.1.200 piroommonitor "" "" DictConnection "~/.sensors.json" -v -i 5 -n 1
```
