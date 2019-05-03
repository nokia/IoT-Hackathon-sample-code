# Pushing data from Raspberry Pi to InfluxDB

This setup is configured to the Raspberry pi with IP 192.168.1.189. With [piroommonitor](https://github.com/kangasta/piroommonitor.git) and [fdbk](https://github.com/kangasta/fdbk.git), the data pushing can be setup with:

```bash
sudo apt-get remove python3-requests

git clone https://github.com/kangasta/piroommonitor.git
cd piroommonitor
sudo python3 setup.py install

piroommonitor --db-connection InfluxConnection 192.168.1.200 piroommonitor "" "" DictConnection "~/.sensors.json" -v -i 5 -n 1
```

To launch the data pushing on start up add

```cron
@reboot /usr/local/bin/piroommonitor --db-connection InfluxConnection 192.168.1.200 piroommonitor "" "" DictConnection "~/.sensors.json" -v -i 5 -n 1
```

to the cron file with `crontab -e`.