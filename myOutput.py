#!/usr/bin/python3
import time

try:
    import RPi.GPIO as gpio
    print ( "HARDWARE= RASPI")
    BOARD = "RASPI"
except:
    print ("kein raspberry !")
    try:
        from machine import Pin
        print ( "HARDWARE= MicropPython")
        import sys
        print ("platform=",sys.platform)
        BOARD="ESP82"
    except:
        print ("kein esp8266 !")
        BOARD = None
    #raise  ImportError ("nur fuer ESP8266-Micropython ode RaspberryPi")
    
class Output:
    def __init__(self, pin, invert=False ):
        self.pin = pin
        self._invert= invert
        self.board= BOARD
        self.level= 0 ^ self._invert
        if BOARD == "RASPI":            
            gpio.setwarnings(False)
            gpio.setmode(gpio.BCM)     
            gpio.setup(self.pin,gpio.OUT)
            gpio.output(self.pin,self.level)
        elif BOARD == "ESP82":
            self.pinObj = Pin(self.pin,Pin.OUT)
            self.pinObj.value(self.level)
        
    def set(self, newLevel):
        self.level= newLevel ^ self._invert
        if BOARD == "RASPI":            
             gpio.output(self.pin,self.level)
        elif BOARD == "ESP82":
            self.pinObj.value(self.level)
        
if __name__ == "__main__" or   __name__ == "builtins":       
    if BOARD==None:
        pass
    else:
        x= Output(18,True)
        for i in range(0,2):
            x.set(1)
            time.sleep(.01)
            x.set(0)
            time.sleep(.01)
