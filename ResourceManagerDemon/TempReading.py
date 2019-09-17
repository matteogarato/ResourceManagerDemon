import Adafruit_DHT                                          

class TempReading(object):
   DHT11 = Adafruit_DHT.DHT11                                   
   DHT11_PIN = 3 # usa numerazione pin BCM
   temp = []
   humi = []
   reading = False
  
   def temperatureHumidityReading(self):
        if not self.reading:
           self.reading = True
           self.temp = []
           self.humi = []
           print('temperatureHumidityReading')
           umi, tem = Adafruit_DHT.read_retry(DHT11, DHT11_PIN) 
           print('after reading')
           if umi is not None and tem is not None:
                print('umi:{}'.format(umi))
                print('tem:{}'.format(tem))
                self.temp.append(tem)
                self.humi.append(umi)
           reading = False
   
   def getTemperature(self):
       self.temperatureHumidityReading()
       if self.temp:
           sumTemp = 0
           for i in range(0,len(self.temp),1):
               sumTemp+=self.temp[i]
           return sumTemp / len(self.temp)
       else:
           return 0
   
   def getHumidity(self):
       self.temperatureHumidityReading()
       if self.humi:
           sumHumi = 0
           for i in range(0,len(self.humi),1):
               sumHumi+=self.humi[i]
           return sumHumi / len(self.humi)
       else:
           return 0