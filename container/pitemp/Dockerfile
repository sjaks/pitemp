FROM python:3
ADD pitemp.py /
RUN pip install influxdb
RUN pip install w1thermsensor
CMD [ "python", "./pitemp.py" ]
