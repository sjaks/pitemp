#      _       _        
#  ___ (_) __ _| | _____  sjaks@github
# / __|| |/ _` | |/ / __| jaks.fi
# \__ \| | (_| |   <\__ \ ------------
# |___// |\__,_|_|\_\___/ pitemp
#    |__/                
#
# BRIEF:
# Saves temperature readings to a db

from influxdb import InfluxDBClient

client = InfluxDBClient(host="influxdb", port=8086)
client.switch_database("db0")

data = [
    {
        "measurement": "measurement",
        "tags": {
            "host": "server01",
            "region": "us-west"
        },
        "time": "2009-11-10T23:00:00Z",
        "fields": {
            "value": 0.64
        }
    }
]

client.write_points(data)
