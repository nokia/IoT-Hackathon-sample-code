import time
import os
import glob
import datetime
from openalpr import Alpr
from influxdb import InfluxDBClient

print ("Starting to record the car plates...")
args = []

client = InfluxDBClient('192.168.1.200', 8086, 'root', 'root', '_internal')
client.create_database('alpr')
client.switch_database('alpr')

alpr = Alpr("eu","/etc/openalpr/openalpr.conf","/usr/share/openalpr/runtime_data")
alpr.set_top_n(3)

while True:
    for image_file in sorted(glob.iglob('./images/*.jpg')):
#    for image_file in glob.iglob('./pictures/*.jpg'):
        res=alpr.recognize_file(image_file)
        if len(res["results"])>0:
            now = datetime.datetime.now()
            plate=res["results"][0]["candidates"][0]["plate"]
            print ("========== PLATE ========")
            print ("Image file %s", image_file)
            timestamp=str(now.strftime("%Y-%m-%d %H:%M:%S"))
            print (plate)
            json_body = [
                {
                    "measurement": "car-plate",
                    "tags": {
                        "region": "eu"
                    },
                    "time": timestamp,
                    "fields": {
                       "value": plate
                    }
                }
            ]
            print(json_body)
            client.write_points(json_body)
#        else:
#            print("No plate")
        os.remove(image_file)
    time.sleep(1)
alpr.unload()
