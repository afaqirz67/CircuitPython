
import touchio
import analogio
import digitalio
import board
import time

from lcd.lcd import LCD
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)



touch_pad1 = board.A0
touch1 = touchio.TouchIn(touch_pad1)

touch_pad2 = board.A1
touch2 = touchio.TouchIn(touch_pad2)


count_direction = "up"
count = 0
needs_refresh = True

while True:
    if needs_refresh:
        lcd.clear()
        lcd.print("Direction: " + count_direction) # toggles the direction
        lcd.print("   Count: " + str(count)) # counts the numbers
        needs_refresh = False

    if touch1.value: # if touchpad1 is touched, execute the following code
        needs_refresh = True # refreshes the lcd
        if count_direction == "up":
            count_direction = "down"
        else:
            count_direction = "up"
        while touch1.value:  #when tachpad1 is being touched, the following code will be executed
            time.sleep(0.25) # wait for .25 seconds from when touchpad1 is touched
            if not touch1.value: #if touchpad1 is not being touched anymore
                break # stop
        continue #if it's still being touched than continue 

    if touch2.value:	
        needs_refresh = True
        if count_direction == "up":
            count = count + 1
        else:
            count = count - 1
        while touch2.value:
            time.sleep(0.25)
            if not touch2.value:
                break
        continue