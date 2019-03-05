import urllib.request
import os
import time
from sense_hat import SenseHat
import json
from datetime import datetime



sense = SenseHat()
sense.clear()
# get CPU temperature
def get_cpu_temp():
    res = os.popen("vcgencmd measure_temp").readline()
    t = float(res.replace("temp=","").replace("'C\n",""))
    return(t)

# use moving average to smooth readings
"""def get_smooth(x):
    if not hasattr(get_smooth, "t"):
        get_smooth.t = [x,x,x]
        get_smooth.t[2] = get_smooth.t[1]
        get_smooth.t[1] = get_smooth.t[0]
        get_smooth.t[0] = x
        xs = (get_smooth.t[0]+get_smooth.t[1]+get_smooth.t[2])/3
    return(xs)

    sense = SenseHat()
    sense.clear()
while True:
    req = urllib.request.Request('http://localhost:3000/sensehat&#8217')
    req.add_header('Content-Type', 'application/json')
"""#Temperature
t1 = sense.get_temperature_from_humidity()
t2 = sense.get_temperature_from_pressure()
t_cpu = get_cpu_temp()
t = (t1+t2)/2
#t_corr = t - ((t_cpu-t)/1.5)
#t_corr = get_smooth(t_corr)
print(json.dumps(t))
"""
    timestamp = int(time.time()*1000)
    result_json_temperature = {"sensor":"temperature" ,"value" : t , 'timestamp' : timestamp }
    response = urllib.request.urlopen(req, json.dumps(result_json_temperature))
    print (response)

#Humidity
    req = urllib.request.Request('http://localhost:3000/sensehat&#8217')
    req.add_header('Content-Type', 'application/json')
    humidity = sense.get_humidity()
    timestamp = int(time.time()*1000)
    result_json_humidity = {"sensor":"humidity" ,"value" : humidity , 'timestamp' : timestamp }
    response = urllib.request.urlopen(req, json.dumps(result_json_humidity))
    print (response)

#Pressure
    req = urllib.request.Request('http://localhost:3000/sensehat&#8217')
    req.add_header('Content-Type', 'application/json')
    pressure = sense.get_pressure()
    timestamp = int(time.time()*1000)
    result_json_pressure = {"sensor":"pressure" ,"value" : pressure , 'timestamp' : timestamp }
    response = urllib.request.urlopen(req, json.dumps(result_json_pressure))
    print (response)

# Sleep for 2 minutes
    time.sleep(120)
    """
