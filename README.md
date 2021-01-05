# CircuitPython

## TABLE OF CONTENTS
* [Led Blink](#Led-Blink)
* [Servo Capacitive touch](#Servo-Capacitive-touch)
* [CircuitPython LCD](#CircuitPython-LCD)
* [CircuitPython Photointerrupters](#CircuitPython-Photointerrupters)
* [CircuitPython Distance Sensor](#CircuitPython-Distance-Sensor)
* [Classes, Objects, and Modules](#Classes,-Objects,-and-Modules)


# Led Blink
## Description
  I used a breadboard, a Metro Express board, an led, and a couple wires with a 220 ohm risistor to wire up the circuit, and run the code to make the led blink. ISN"T THAT COOL?!! This is was our first assignment of the year with circuitpython. At first it seemed to be a little difficult than I thougth, but once I actually started working on it, it felt good. I used [this](https://learn.adafruit.com/adafruit-metro-m4-express-featuring-atsamd51/creating-and-editing-code) website to get a little help with the code.  
## Image
 ![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/main/images/Led-Blink.jpg?raw=true)

## Code
```C
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    led.value = True
    time.sleep(0.5)
    led.value = False
    time.sleep(0.5)
```

## Reflection 
I learned a lot of new things by doing this assignment. First of all, pushing the work from local device to github account is just getting easier and smoother. I learned some basic knowledge of how the circuitpython looks. I learned how to code a metro express to make an led blink.


# Servo Capacitive touch
## Description
  This is assignment we were supposed to have a 180° micro servo to slowly sweep back and forth between 0 and 180°. This would have usually been done with a potentiometer, but what that is done here, I have used to wires to use it instead of a potentiometer. This works totally the same as a potentiometer, and serves the same purpose. The only hardwares that was needed for this besides a micro servo and a microcontroller, was a couple of wires. Servo as always would be hooked up to 5v, ground, and the remaining wire to a digital pin. After that the two wires for the capacitive touch would be attached to two analog pins, and that would be all for the wiring. I also have an image to down below to make it more clear and show a visual of how it should look. After working on the circuit and uploding the code, by touching on wire the servo would sweep in one dirrection and by touching the other wire it would sweep the other direction.

## Image 
![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/master/images/Servo.png?raw=true)



## Code
```C
import time
import board
import touchio
import digitalio
import pulseio
import servo


pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
my_servo = servo.Servo(pwm)
my_servo.angle = 90

touch_pad1 = board.A0
touch1 = touchio.TouchIn(touch_pad1)

touch_pad2 = board.A1
touch2 = touchio.TouchIn(touch_pad2)

while True:
    if touch1.value:
        print("touch1")
        for angle in range(0, 180, 5):
            my_servo.angle = angle
    if touch2.value:
        print("touch2")
        for angle in range(180, 0, -5):
            my_servo.angle = angle
```

### Reflection
Servo Capacitive touch was my first experience using capacitive touch, so first thing that I did was I looked up the definition for the capacitive. Capacitive means "denoting or relating to a touchscreen that works by sensing when something that conducts electricity, such as a fingertip, is in contact with the screen". Based on that, capacitive touch screen is a device display screen that relies on finger pressure for interaction. I learned each board has at least one pin that works as an input when you touch it! The capacitive touch is done completely in hardware, so no external resistors, capacitors or ICs required. Which is really nice! 

# CircuitPython LCD
## Description
The Circuit Python LCD would count in any directions up or down. Just like the Capacitive Touch Servo, which we used wires instead of a potentiometer, we have used wires for the CircuitPython LCD instead a button as well. 


## Image
![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/master/images/CircuitPython%20LCD-img.png?raw=true)

## Code
```C

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
```


## Reflection
The Metro only count once per touch. If I touch and hold the count wire, it would only count as one touch. The LCD would count whenever the wires are pressed. You can toggle
whether your Metro is counting up or down when pressing one wire, and you can count using the other wire. One important thing that I want to point out here is the libraries I
used in my code. I used 3 libraries. [i2c_device.mpy](https://github.com/DoctorShields/CircuitPythonRepo/blob/master/micropython/adafruit_bus_device_mpy/i2c_device.mpy) which I
placed in a separate folder called "adafruit_bus_device" in lib folder on my metro. Also 
[i2c_pcf8574_interface.mpy](https://github.com/DoctorShields/CircuitPythonRepo/blob/master/micropython/lcd_mpy/i2c_pcf8574_interface.mpy) and 
[lcd.mpy](https://github.com/DoctorShields/CircuitPythonRepo/blob/master/micropython/lcd_mpy/lcd.mpy), which I placed in another seperate folder called lcd in my lib folder on
my metero.


# CircuitPython Photointerrupters
## Description
A photo interrupter is a devise that is made up of a infrared led and a photo transistor with a gap between the two of them, When something is placed between the gap the light 
is cut and the current flow through the photo transistor is reduced or stopped. This is assignment had us to Wire up a photointerrupter and have it keep track of how many times 
it has been interrupted. The program should output the count using a full sentence, and output the sentence every 4 seconds without using the syntax sleep().

## Image
![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/master/images/CircuitPython%20photointerrupter.png?raw=true)

## Code
```C
# libraries
from digitalio import DigitalInOut, Direction, Pull
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface


# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)



count = 0

interrupt = DigitalInOut(board.D13) # sets the digital input pin
interrupt.direction = Direction.INPUT # sets the direction as an input
interrupt.pull = Pull.UP 
# defines the pull of the digital input pin as up so when the
# input line isn't being run the pull-up values the state of 
# the line high so it reads as true

lastRefresh = 0
previous = False

while True:
    now = time.time() # now = time in seconds since epoch 
    if now - lastRefresh > 4: 
        lastRefresh = now
        lcd.clear()
        lcd.print("The number of interrupts is: " + str(count))

    if interrupt.value and not previous: # only takes the current value of the interruption
        count = count + 1
    previous = interrupt.value
    
  ```
    

## Reflection
I mostly used the codes I used for the last assignment which was the CircuitPython LCD, so all the codes for the LCD were the same. The only struggle I had in this assignment 
was the code part which required the output statement to appear after every 4 seconds. I went through [this](https://docs.python.org/3/library/time.html) website and found out 
that time.time was what would fit the best in this condition.




# CircuitPython Distance Sensor
## Description
This assignment we had to get a distance sensor calculating the distance and at the same time, having the neopixel on the Metro Express board LED express specific colors 
according to what the calculated distance is. And there is an HC-SR04 distance sensor used to calculate the distance. For example, in this case we had to have the LED be 
red if the distance is 5, and fade out as the distance is getting bigger. Onceit reaches close to 20, it starts going to blue and once it's 20, it should be a solid 
green. As it crosses that point at gets closer to 35. It should go from a green to a blue. Right when the distance is 35, it should be a solid blue. For a better 
picture, take a look at the visuale below. 

![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/master/images/color%20spectrum.png?raw=true)


## Image
![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/master/images/CircuitPython%20Distance%20Sensor%20%20-%20circuit.png?raw=true)
## Code 
```C
# Libraries
import time
import board
import adafruit_hcsr04
import neopixel

pixel_pin = board.NEOPIXEL # pin used to drive the neopixel
num_pixels = 1  # number of pixels being used | in this case (1)

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.3, auto_write=False,) # defines pixels
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D9, echo_pin=board.D10) # calculates the distance


# This function calculates the distance and sets up the color according to distance
def color(distance, target, range): 
    return int( max(255 - 255 * abs(((distance - target) / range)), 0))

# distance varitables
# it assigns a specific distance number for each color to take effect
redTarget = 5 
blueTarget = 20
greenTarget = 35
colorRange = 15

while True:
    time.sleep(0.1)
    try:
        distance = sonar.distance
        print((distance,))
    except RuntimeError: # handles errors occuring while the code is being executed
        print("Retrying!")
        continue # this keeps the program running, without this command any runtime errors can cause the program to stop functioning.


    pixels.fill((color(distance,redTarget,colorRange),
        color(distance, greenTarget, colorRange),
        color(distance,blueTarget,colorRange)))

    pixels.show()    
    # auto_write is set to False, so data can't be sent straight to the pixels, therefore
    # pixel.show() is there to actually send the data to the pixels since it's not set in default
	# it makes the code a little more complicated, but it makes the LED animation faster as well 
```

## Reflection
This assignment was a little challenging, specially having the color of the onboard neopixel on the Metro Express correspond to the distance. I used this website to get
some information about the defining the neopixel. 
[this](https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py)
is the library I used in this assignment. I learned that an HC-SR04 measures the distance to an object roughly 10 times per second. I did not use an LCD screen to see
the distance measure by that, istead I just used my serial moniter for observating the distance. 



# Classes, Objects, and Modules
## Description



## Image 
![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/master/images/Classes,%20Objects,%20and%20Modules.png?raw=true)
## Code
```C

```

## Reflection
