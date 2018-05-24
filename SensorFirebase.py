#!/usr/bin/env python

'''
I run this script with python 3.5.2
This scrip simply merges the GrovePi Loundness Sensor example script with Prybase.
It sends the sensor's output to Firebase.
https://github.com/DexterInd/GrovePi/blob/master/Software/Python/grove_loudness_sensor.py
https://github.com/thisbejim/Pyrebase
'''


# GrovePi Example for using the Grove - Temperature&Humidity Sensor (HDC1000)(http://www.seeedstudio.com/depot/Grove-TemperatureHumidity-Sensor-HDC1000-p-2535.html)
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
# This example is derived from the HDC1000 example by control everyhing here: https://github.com/ControlEverythingCommunity/HDC1000/blob/master/Python/HDC1000.py
'''
## License
The MIT License (MIT)
GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''


import pyrebase
from random import randint


config = {
  "apiKey": "apiKey",
  "authDomain": "projectId.firebaseapp.com",
  "databaseURL": "https://databaseName.firebaseio.com",
  "storageBucket": "projectId.appspot.com",
  "serviceAccount": "path/to/serviceAccountCredentials.json"
}


firebase = pyrebase.initialize_app(config)
db = firebase.database()



#from grove_i2c_temp_hum_hdc1000 import HDC1000
import time as t

#hdc = HDC1000()
#hdc.Config()

while 1:
    print('Temp    : %.2f C')
    #         % hdc.Temperature())
    date = t.localtime(t.time())
    time = int(t.time())
    randData1 = randint(0,60)
    print(randData1)

    
    datestamp = "%d-%d-%dT%d:%d:%d"%((date[0] %10000),date[1],date[2],date[3],date[4], date[5]) 
    data = {"time": time, "y": randData1}
    db.child("data").push(data)
    print(str(datestamp))
    #         % hdc.Humidity())
    print('-' * 17)
    t.sleep(3)
