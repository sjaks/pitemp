#      _       _        
#  ___ (_) __ _| | _____  sjaks@github
# / __|| |/ _` | |/ / __| jaks.fi
# \__ \| | (_| |   <\__ \ ------------
# |___// |\__,_|_|\_\___/ pitemp
#    |__/                
#
# BRIEF:
# Saves temperature readings to a db

import os
import threading
from influxdb import InfluxDBClient
from w1thermsensor import W1ThermSensor


sensor = W1ThermSensor()
data = [
    {
        "measurement": "temperature",
        "tags": {
            "sensor": os.environ["PT_SENSOR"],
            "location": os.environ["PT_LOCATION"]
        },
        "fields": {
            "temp": -99.9
        }
    }
]


def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()


def value_to_db():
    temperature = sensor.get_temperature()
    print("Read a temperature value of " + str(temperature) + "C")
    data[0]["fields"]["temp"] = temperature
    client.write_points(data)


client = InfluxDBClient(host="influxdb", port=8086)
client.switch_database(os.environ["PT_DATABASE"])
setInterval(value_to_db, int(os.environ["PT_INTERVAL"]))
