#!/usr/bin/python3
# 4stelliges 7segment- tankstellen display
# fuer raspberry pi
# display mit spi 
'''
1. start des 'daemon' im system mit: sudo pigpiod

2. autostart in /etc/rc.local
    python3 /home/pi/app/python/gps/grossuhr_gps.py 15 &
    # 15 % helligkeit
'''

from timeGps2 import MyTimeGps
from display import Display
from pwm import Pwm      
import sys

#helligkeit in prozent als ersten parameter
# default =20 %
try:
    x= sys.argv[1]
    x= int(x)
except Exception as e:
    print(e)
    x=20
helligkeit_prozent=x

def blink(sec):
    if sec & 1:
        dpx = ':'
        if sec >= 55:
            dpx = '.'
    else:
        dpx = ' '
    return dpx

pwm= Pwm(pin=23, dc=15)  # pin23, pwm dutycycle= 15 %
pwm.set(helligkeit_prozent)   # update 240822
display = Display(datPin=17, clkPin=27, csPin=22)
uhr = MyTimeGps()
while True:
    try:   
        dt=uhr.read()
        #print ("UTC=",dt)
        dt_local= uhr.dt_to_local(dt)  #utc nach me(s)z
        #print(dt_local)
        sec=dt_local.time().second
        hStr = '{:02}{:02}'.format(dt_local.time().hour, dt_local.time().minute)  # stunde + minute, als string
        dpx = blink(sec)            # blinkender punkt
        display.write(hStr, dpx)    # display als string mit blinkendem punkt
                                    #  anzeige auf terminal..
        print('\n' + hStr) if sec == 0 else print(sec, end=" ")
    except Exception as e:
        print(e)
        display.spi.shiftList([2,2,2,2])






