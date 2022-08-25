![big-clock](https://user-images.githubusercontent.com/50828453/71590415-9c593680-2b28-11ea-9261-22b783d1ca86.JPG)

# big_digital_clock
A big digital clock giving new life to an old 7-segment displays from a petrol station. 

Description:

A 7-segment-display from a petrol station has been revived. This is an experiment with the language Python.
The controller is a RaspberryPi Zero ; [pyboard](https://pyboard.org/wp-content/uploads/2019/01/PYBv1_1-1024x768.jpg)
or ESP32 /esp8266-Boards with Micropython will work with some modifications.
Time date comes from a GPS module.  The timestamp in UTC ist extracted from GPS-sentence. The communication with the GPS-receiver has readable ASCII-format, so ![software](doc/gps_decoder.py) is very simple.
A 3.3V to 5V level converter is not essential, as the 3.3V CMOS outputs can also drive TTL.
The display works with TPIC6B595 shift registers (similar to 74hc595), which has an SPI Bus (Serial Peripheral Interface);
this can be controlled with 3 lines: data, clock and chipselect. The outputs of the 595 directly drive the LEDs.
### Brightness control
- The brightness may be controlled via PWM via the gate signal (G) of the 595. This is done here with a squarewave signal from an
555-Timer, because the PWM of the Raspi has too much jitter.
- We can use hardware-pwm of raspi. This is don via pigpio daeman. This implemented in version of 25.08.22. The Brightness is set from the command line as integer parameter , see below.  

Bill of material:
  - RaspberyPi
  - GPS receiver Modul
  - 4 Seven-segment-displays with SPI-Interface
  - Power supply 5V for Raspi, 12V for Display ( depends on the display )
### Install and Run
The main python script is "grossuhr_gps.py".
You need Python 3.x.
Put all files in one directory eg. "/home/pi/clock". Start your Python-IDE ( I use Thonny) and 
select the  file "grossuhr_gps.py", then select "Run". 

For implementing an autostart of the Raspi, edit the following file:

sudo nano /etc/rc.local

      ...
      #start pigpio daeman
      sudo pigpiod
      #start clock with 15% brightness
      python3 /home/pi/clock/grossuhr_gps.py 15 &
      exit 0



