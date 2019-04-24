import datetime
from collections import deque
import csv
from csv import writer


# Open a csv/txt file and append new data
class CsvExport:

    def __init__(self):
        with open('dataFile.csv', 'w') as data_file:
            data_writer = writer(data_file)
            data_writer.writerow(['Date_Time,Temp,Pressure,Humidity,Temp_from_pressure,Temp_from_humidity'])
            data_file.close()

    def writeData(self,dt_log, input1, input2, input3, input4, input5):
        with open('dataFile.csv', 'a') as data_file:
            data_writer = writer(data_file)
            data_writer.writerow([str(dt_log)+','+str(input1)+','+str(input2)+','+str(input3)+','+str(input4)+','+str(input5)])
            data_file.close()
