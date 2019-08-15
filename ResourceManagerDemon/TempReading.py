import Adafruit_DHT                                          
import time
import threading

class TempReading(object):
   DHT11 = Adafruit_DHT.DHT11                                   
   DHT11_PIN = 3 # usa numerazione pin BCM
   temp = []
   humi = []
   reading = False
   
   def temperatureHumidityReading(self):
        if not reading:
           reading = True
           temp = []
           humi = []
           for i in range(0,3,1):
               umi, tem = Adafruit_DHT.read_retry(DHT11, DHT11_PIN, retries=2, delay_seconds=1) 
               if umi is not None and tem is not None:
                   temp.append(tem)
                   humi.append(umi)
           reading = False
   
   def getTemperature(self):
       temperatureHumidityReading()
       if len(temp) > 0:
           sumTemp = 0
           for i in range(0,len(temp),1):
               sumTemp+=temp[i]
           return sumTemp / len(temp)
       else:
           return 0
   
   def getHumidity(self):
       temperatureHumidityReading()
       if len(humi) > 0:
           sumHumi = 0
           for i in range(0,len(humi),1):
               sumHumi+=humi[i]
           return sumHumi / len(humi)
       else:
           return 0