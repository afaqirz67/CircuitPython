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
        continue


    pixels.fill((color(distance,redTarget,colorRange),
        color(distance, greenTarget, colorRange),
        color(distance,blueTarget,colorRange)))

    pixels.show()    
    # auto_write is set to False, so data can't be sent straight to the pixels, therefore
    # pixel.show() is there to actually send the data to the pixels since it's not set in default
	# it makes the code a little more complicated, but it makes the LED animation faster as well 