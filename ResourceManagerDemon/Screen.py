import Adafruit_CharLCD as LCD #this thing must go, i need to use a new library, not a discontinued one
import time as timeExec
import subprocess
import os
import psutil
import datetime
import time

class Screen(object):
   # Raspberry Pi pin setup
   lcd_rs = 18
   lcd_en = 23
   lcd_d4 = 24
   lcd_d5 = 16
   lcd_d6 = 20
   lcd_d7 = 21
   lcd_backlight = 2
   display = False
   
   # Define LCD column and row size for 16x2 LCD.
   lcd_columns = 16
   lcd_rows = 2
   
   lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight)
   
   def textmessagerecieved(self,line1,line2):
       self.display = True
       chardiffLine1 = len(line1) - 16
       if chardiffLine1 > 0:
           raise NotImplementedError('Line scroll on multiple line not supported yet')
       chardiffLine2 = len(line2) - 16
       if chardiffLine2 > 0:
           for i in range(0, chardiffLine2 + 1):
               self.lcd.clear()
               self.lcd.message("{}\n{}".format((line1).center(16),line2[i:16 + i]))
               timeExec.sleep(0.6)
       else:
           self.lcd.clear()
           self.lcd.message("{}\n{}".format((line1).center(16),(line2).center(16)))
       timeExec.sleep(20)
       self.display = False
