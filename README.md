# CircuitPython

## TABLE OF CONTENTS
* [Led Blink](#Led-Blink)
* [Servo Capacitive touch](#Servo-Capacitive-touch)

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
In this assignment we were supposed to wire up a servo with to other two wires coming out of the analog pins, so if you had to touch one of the wires with your finger, the servo would move in one direction, and if you were to touch the other wire coming out of another anolog pin, the servo would move in other direction. We had to use a Metro Express board and circuitpython to run the code to the servo. The only things beside a Metro Express needed was a servo, a couple wires, and a breadboard. The library I used beside the library for servo was the touchio library for the capacitive touch.    

## Image 

 ![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/main/images/Servo.png?raw=true)

### Code
```C
import time
import board
import touchio
import digitalio
import pulseio
import servo

# create a PWMOut object on Pin A2.
pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)
# This creats a servo object.
my_servo = servo.Servo(pwm)
my_servo.angle = 90

touch_pad1 = board.A0
touch1 = touchio.TouchIn(touch_pad1)

touch_pad2 = board.A1
touch2 = touchio.TouchIn(touch_pad2)

while True:
    if touch1.value:
        print("touch1")
        # it moves from 0 to 180, 5 steps at a time.
        for angle in range(0, 180, 5):
            my_servo.angle = angle
    if touch2.value:
        print("touch2")
        # it moves from 180 to 0, 5 steps at a time.
        for angle in range(180, 0, -5):
            my_servo.angle = angle

```

### Reflection
I pretty much already knew the the actual concept of how servos work before, but the new thing I learned in this assignment is the capacitive touch. The word capacitive itself means sensing when something that conducts electricity, such as a fingertip, is in contact with the screen, which in this case here it would contact with the wires. Capacitive touch sensing is a way of human touch sensing, that requires little or no force to activate. It may be used to sense human touch through more than a quarter of an inch of plastic, wood, ceramic or other insulating material (not any kind of metal though), enabling the sensor to be completely visually concealed. I learned some basic knowledge about capacitive touch in [this](https://www.instructables.com/How-To-Use-Touch-Sensors-With-Arduino/#:~:text=Capacitive%20touch%20sensing%20is%20a%20way%20of%20human,enabling%20the%20sensor%20to%20be%20completely%20visually%20concealed.) website. 
