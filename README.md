![big-clock](https://user-images.githubusercontent.com/50828453/71590415-9c593680-2b28-11ea-9261-22b783d1ca86.JPG)

# big_digital_clock
A big digital clock giving new life to an old 7-segment displays from a petrol station. 

Description:

A 7-segment-display from a petrol station has been revived. This is an experiment with the language Python.
The controller is a RaspberryPi Zero ( PyBoard or ESP32/ ESP8266-Boards with Micropython will work too). Time date comes from a GPS module.
A 3.3V to 5V level converter is not essential, as the 3.3V CMOS outputs can also drive TTL.
The display works with TPIC6B595 shift registers (similar to 74hc595), which has an SPI Bus (Serial Peripheral Interface);
this can be controlled with 3 lines: data, clock and chipselect. The outputs of the 595 directly drive the LEDs.
The brightness may be controlled via PWM via the gate signal (G) of the 595. This is done here with a squarewace signal from an
555-timer, because the PWM of the Raspi has too much jitter ( but real hardware -PWM will work correctly).

Bill of material:
  - RaspberyPi
  - GPS receiver Modul
  - 4 7-segment-displays with SPI-Interface
  - power supply 5V for Raspi, 12V for Display ( depends on the display )


Install and Run:

The main python script is "grossuhr_gps.py".
You need Python 3.x.
Put all files in one directory eg. "/home/pi/clock". Start your Python-IDE ( I use Thonny) and 
select the  file "grossuhr_gps.py", then select "Run". 

For implementing an autostart of the Raspi, edit the following file:

sudo nano /etc/rc.local

      ...
      python3 /home/pi/clock/grossuhr_gps.py &
      exit 0



