#!/usr/bin/python3
#import RPi.GPIO as gpio
from myOutput import *
import time

class Shift:
    """
    die bits 0:7  werden seriell an pin 'dat' ausgesendet.
    bei der pos. Flanke von 'clk' wird das Datenbit .x geschoben.
    mit der pos. Flanke von 'cs' werden alle Bits übernommen.
    
    dat : |.7---|.6---|.5---|.4---|.3---|.2---|.1---|.0---|
    clk : ____/'\___/'\___/'\___/'\___/'\___/'\___/'\___/'\__
    cs  : \________________________________________________/''''
    """
    def __init__(self, dat, clk, cs, invert=True):
        self._dat = Output( dat)
        self._clk = Output( clk)
        self._cs  = Output(cs)
        self._invert= invert
#        gpio.setwarnings(False) # warnungen abschalten z.b. wenn anderes programm die led schon bedient
#        gpio.setmode(gpio.BCM)

        self._dat.set(0 ^ self._invert)    
        self._clk.set(0 ^ self._invert)  
        self._cs.set (1 ^ self._invert)
       
    
    def _delay(self):
        """ evtll notwendige verzögerung
        """
       ## time.sleep(.0005)
        pass

    
    def _shift1(self,datBit):
        """ ein bit schieben
        """
        self._dat.set( datBit ^ self._invert) ## data
        self._delay()
        self._clk.set( 1 ^ self._invert)   ## clk
        self._delay()
        self._clk.set( 0 ^ self._invert)
    
    """ cs low gibt 595 chip frei """
    def cs_low(self):
        self._cs.set( 0 ^ self._invert)
    
    """ cs high übernimmt daten ins ausgangsregister 595"""
    def cs_high(self):
        self._cs.set( 1 ^ self._invert)                

    """ schiebt ein byte ins schieberegister bei cs = low """
    def _shiftByte( self,byte):
        for i in range (0,8):  ## 7:0
            mask= 1<<i
            if ( (byte & mask ) > 0):    ## true/false 
                self._shift1(True)   ## shift  bit
            else:
                self._shift1(False)   ## shift  bit
    """ schiebt die bytes aus der liste ins Schieberegister
    """
    def shiftList(self,bytes):
        self.cs_low()
        for element in bytes:
            self._shiftByte(element)
            #time.sleep(0.0001)
        self.cs_high()
        
    """ schiebt ein bytes ins Schieberegister
    """   
    def shift(self,data):
        self.cs_low()
        self._shiftByte(data)
        self.cs_high()
        

if __name__ == "__main__" or   __name__ == "builtins":       
    if BOARD==None:
        pass
    if BOARD== "RASPI":
        s= Shift(17,27,22,invert=True) # dat, clk, cs, invert=False):
    elif BORAD=="ESP82":
        s= Shift(12,13,14,invert=True) # dat, clk, cs, invert=False):

    while True:
        s.shiftList([0x01,0x02,0x04])
        time.sleep(0.1)
    #gpio.cleanup()
    print("break")

    
