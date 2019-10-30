'''
(C) 2019 dk2jk
Gps -zeit lesen
'''
import serial, time
import datetime

class MyTimeGps:
    _c=""
    def __init__(self):
        try:
            _port = "/dev/ttyS0"    # Raspberry Pi 3
            self._ser = serial.Serial(_port, baudrate = 9600)
            self._ser.flushInput() # sonst läuft input über
        except:
            print( "***kein Raspi***")
        print ("---Time (GPS)----")

    ''' feststellung des letzten sonntags im monat maerz bzw. october
            return: datum als datetime object
            z.b.: datetime.datetime(2019, 3, 31, 2, 0)
    ''' 
    def zeitumstellung(self,jahr):
        stunde=1
        for day in range (31, 20, -1):# start beim letzten tag im monat
            x = datetime.datetime(jahr, 3, day,stunde,0,0) 
            if (x.weekday() == 6): #letzter sonntag im monat
                sommer=x                
        for day in range (31, 20, -1):# start beim letzten tag im monat
            x = datetime.datetime(jahr, 10, day,stunde,0,0) 
            if (x.weekday() == 6): #letzter sonntag im monat
                winter=x                
        return sommer,winter
    
    def toLocal(self, hour,offset):
        # sommer/ winterzeit (grob)             
        y= int(hour)+offset #-------MEZ/ MESZ ------
        if y >=24:
            y=y-24
        return y
    
    def rmc_to_datetime(self,s1):
        # rmc== "$GNRMC,153422.000,V,,,,,3.83,356.90,291019,,,E*58" 
        #s1= rmc.split(',')
        hms= s1[1]
        #print("hms=",hms)
        h= int(hms[0:2])
        m= int(hms[2:4])
        s= int(hms[4:6])
        date=s1[9]
        day= int(date[0:2])
        mon= int(date[2:4])
        year= 2000 + int(date[4:6])
        return datetime.datetime(year,mon, day,h,m,s) #datetime.datetime.now()
    
    def read(self):
        while True:
            time.sleep(.01)
            c= self._ser.readline().decode("utf-8")            
            s2= c.split(',')          
            if s2[0]=="$GNRMC":                
                break
        dt= self.rmc_to_datetime(s2)
        self._c=c
        #print(c)
        self._ser.flushInput() # sonst läuft input über    
        return dt    # datetime: 2019-09-27 13:25:35
    
    def last_sentence(self):
        return self._c

    def dt_to_local(self,dt):
        #print(uhr.last_sentence())
        #print(dt)   # datetime: 2019-09-27 13:25:35
        #y=uhr.sommerWinter(x)    
        termin= self.zeitumstellung(jahr=dt.date().year)
        #print (termin[0],termin[1])
        if ( dt> termin[1] or dt<termin[0]):
            #print( "winterzeit!")
            offset=1
        else:
            #print( "sommerzeit!")
            offset=2
        local_hour= self.toLocal(dt.time().hour,offset)
        #print(local_hour)
        #print(dt)
        return dt.replace(hour=local_hour)       

if __name__ == "__main__":
    uhr = MyTimeGps()
    dt=uhr.read()
    dt_local= uhr.dt_to_local(dt)
    print(dt_local)
