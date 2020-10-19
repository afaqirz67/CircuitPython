# CircuitPython

## TABLE OF CONTENTS
* [Led Blink](#Led_Blink)'

# Led Blink
## Description
...
## Image
 ![Tux, the Linux mascot](https://github.com/afaqirz67/CircuitPython---III/blob/main/Led_Blink.jpg?raw=true)

### Code
```C
import board
import neopixel
import time

# make a neopixel object
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

#this will run forever
while True:
    print("Make it green!")
    dot.fill((0,255,0))
    time.sleep(.5)
    print("Make it red!")
    dot.fill((255,0,0))
    time.sleep(.5)
```
### Reflection 
...
