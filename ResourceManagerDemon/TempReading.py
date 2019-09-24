import Adafruit_DHT                                          
import threading

class TempReading(object):
   DHT11 = Adafruit_DHT.DHT11                                   
   DHT11_PIN = 3 # usa numerazione pin BCM
   reading = False

   def __init__(self, interval=1):
        self.interval = interval
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

   def run(self):
       try:
        if not self.reading:
           self.reading = True
           print('temperatureHumidityReading')
           umi, tem = Adafruit_DHT.read_retry(DHT11, DHT11_PIN) 
           print('after reading')
           if umi is not None and tem is not None:
                print('umi:{}'.format(umi))
                print('tem:{}'.format(tem))
                self.temp.append(tem)
                self.humi.append(umi)
           reading = False
           return umi,temp
       except Exception as e:
        print(e)        
