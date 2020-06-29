#      _       _        
#  ___ (_) __ _| | _____  sjaks@github
# / __|| |/ _` | |/ / __| jaks.fi
# \__ \| | (_| |   <\__ \ ------------
# |___// |\__,_|_|\_\___/ pitemp
#    |__/                
#
# BRIEF:
# Saves temperature readings to a db

import threading
from influxdb import InfluxDBClient


data = [
    {
        "measurement": "temperature",
        "tags": {
            "sensor": "inside01",
            "location": "Hervanta"
        },
        "fields": {
            "temp": 20.0
        }
    },
    {
        "measurement": "humidity",
        "tags": {
            "sensor": "inside01",
            "location": "Hervanta"
        },
        "fields": {
            "hum": 45.0
        }
    }
]


def setInterval(func,time):
    e = threading.Event()
    while not e.wait(time):
        func()


def value_to_db():
    client.write_points(data)


client = InfluxDBClient(host="influxdb", port=8086)
client.switch_database("db0")
setInterval(value_to_db, 5)
