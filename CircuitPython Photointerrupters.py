# libraries
import board
import time
import busio
import neopixel
import adafruit_hcsr04

from lcd.lcd import LCD
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D9, echo_pin=board.D10)




while True:
    print((sonar.distance,))