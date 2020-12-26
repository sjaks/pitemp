# pitemp
Raspberry Pi temperature station that
- uses a DHT11 temperature sensor
- saves data into a Influx Database
- uses Grafana to graph the temperature history
- is written in Python
- is deployed using Docker-compose

## Installation
Clone the repository with
```
git clone https://github.com/sjaks/pitemp/
cd pitemp/container
```
and run
```
docker-compose up
```
in the root directory of the project.

## About this project
This is a Raspberry Pi temperature station project that tracks the temperature history of, let's say your home and saves the data into a time series InfluxDB database.
The data is visualized using Grafana.

All the components are deployed using Docker and the whole project can easilly be set up on a Rasberry Pi with Docker Compose.
