#!/usr/bin/python3

from timeGps2 import MyTimeGps
from display import Display


# 4stelliges 7segment- tankstellen display
# fuer raspberry pi

# display mit spi / belegung der pins



def blink(sec):
    if sec & 1:
        dpx = ':'
        if sec >= 55:
            dpx = '.'
    else:
        dpx = ' '
    return dpx

uhr = MyTimeGps()
display = Display(datPin=17, clkPin=27, csPin=22)
while True:
    try:   
        dt=uhr.read()
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






