# CircuitPython

## TABLE OF CONTENTS
* [Led Blink](#Led-Blink)
* [Servo Capacitive touch](#Servo-Capacitive-touch)
* [CircuitPython LCD](#CircuitPython-LCD)

# Led Blink
## Description
  I used a breadboard, a Metro Express board, an led, and a couple wires with a 220 ohm risistor to wire up the circuit, and run the code to make the led blink. ISN"T THAT COOL?!! This is was our first assignment of the year with circuitpython. At first it seemed to be a little difficult than I thougth, but once I actually started working on it, it felt good. I used [this](https://learn.adafruit.com/adafruit-metro-m4-express-featuring-atsamd51/creating-and-editing-code) website to get a little help with the code.  
## Image
 ![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/main/images/Led-Blink.jpg?raw=true)

### Code
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

### Reflection 
I learned a lot of new things by doing this assignment. First of all, pushing the work from local device to github account is just getting easier and smoother. I learned some basic knowledge of how the circuitpython looks. I learned how to code a metro express to make an led blink.


# Servo Capacitive touch
## Description
  This is assignment we were supposed to have a 180° micro servo to slowly sweep back and forth between 0 and 180°. This would have usually been done with a potentiometer, but what that is done here, I have used to wires to use it instead of a potentiometer. This works totally the same as a potentiometer, and serves the same purpose. The only hardwares that was needed for this besides a micro servo and a microcontroller, was a couple of wires. Servo as always would be hooked up to 5v, ground, and the remaining wire to a digital pin. After that the two wires for the capacitive touch would be attached to two analog pins, and that would be all for the wiring. I also have an image to down below to make it more clear and show a visual of how it should look. After working on the circuit and uploding the code, by touching on wire the servo would sweep in one dirrection and by touching the other wire it would sweep the other direction.

## Image 
![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/master/images/Servo.png?raw=true)



### Code
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
CircuitPython LCD is ...


## Image


## Code
```C

```


### Reflection 
