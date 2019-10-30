#!/usr/bin/python3

from myShift import Shift
#from Pwm import Pwm
_tabelle7segment=(  # bit 0 ist immer 0
    0b00000010,  #0
    0b10011110,  #1
    0b00100100,  #2
    0b00001100,  #3
    0b10011000,  #4
    0b01001000,  #5
    0b01000000,  #6
    0b00011110,  #7
    0b00000000,  #8
    0b00001000,  #9
)


class Display(Shift):

    def __init__( self, datPin, clkPin, csPin):
        self.spi= Shift(datPin,clkPin,csPin,invert=True)
        #invertieren
        self.tabelle7segment=[]
        for i in _tabelle7segment:
            self.tabelle7segment.append(~i)

    def write(self, text, dp=':'):
        y = list(text) #buffer
        c = ' '
        if  len(text) ==4:
            pass #ok, 4 zeichen
        else:
            print("fehler byteanzahl ungleich 4")

        # ziffern in 7-segment code umwandeln
        for i in range (0,4):
            c =text[i]
            c = ord(c) - 0x30
            y[i]= self.tabelle7segment[c]

        # dezimalpunkt oder doppelpunkt
        if dp==':':
            y[1] = y[1] | 0x01
            y[2] = y[2] | 0x01
        elif dp=='.':
            y[1] = y[1] | 0x01
            y[2] = y[2] & ~0x01
        else:
            y[1] = y[1] & ~0x01
            y[2] = y[2] & ~0x01

        #print(hex(y[3]))

        #for i in y:
            #print (hex(i) , end=' ')

        # spi funktion
        self.spi.shiftList(y)

