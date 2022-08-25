"""
Vorbereitung:
wget https://github.com/joan2937/pigpio/archive/master.zip
unzip master.zip
cd pigpio-master
make
sudo make install
mögliche frequenzen 8000  4000  2000 1600 1000  800  500  400  320

start des 'daemon' im system mit: sudo pigpiod

"""
import pigpio

class Pwm():
    def __init__(self, pin=18, *, fq=320, dc= 0): 
        self.fq=fq
        self.dc=dc
        self.pin=pin
        self.pi = pigpio.pi()
        self.pi.set_PWM_range(self.pin, 100)
        self.frequenz(self.fq)
        self.set(self.dc)

    def frequenz(self,fq):
        self.pi.set_PWM_frequency(self.pin, fq)
        
    def set(self,prozent, run= True):
        if prozent<0:
            prozent=0
        elif prozent>100:
            prozent=100
        self.dc=prozent
        if run:
            self.on()
            
    def off(self):
        self.pi.set_PWM_dutycycle(self.pin, 0)

    def on(self):
        self.pi.set_PWM_dutycycle(self.pin, self.dc)

if __name__ == '__main__':   # test
    pwm= Pwm(pin=23, dc=50)  # rechteck
