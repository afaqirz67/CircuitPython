# libraries...
import digitalio
import time

class RGB: # creating a class

    def __init__(self, r, g, b):
        self.r = digitalio.DigitalInOut(r) # setting the direction into output
        self.r.direction = digitalio.Direction.OUTPUT

        #The operating of digital output is done in
        # two modes one is a push-pull mode and another one is an open-drain mode.

        self.r.drive_mode = digitalio.DriveMode.OPEN_DRAIN  # pulls the pin voltage to  ground


        self.g = digitalio.DigitalInOut(g)
        self.g.direction = digitalio.Direction.OUTPUT
        self.g.drive_mode = digitalio.DriveMode.OPEN_DRAIN

        self.b = digitalio.DigitalInOut(b)
        self.b.direction = digitalio.Direction.OUTPUT
        self.b.drive_mode = digitalio.DriveMode.OPEN_DRAIN


    def red(self): # Glow red
        self.r.value = False
        self.g.value = True
        self.b.value = True

    def green(self): # Glow green
        self.r.value = True
        self.g.value = False
        self.b.value = True

    def blue(self): # Glow blue
        self.r.value = True
        self.g.value = True
        self.b.value = False

    def yellow(self): # Glow yellow
        self.r.value = False        # Red and green make yellow
        self.g.value = False
        self.b.value = True

    def magenta(self): # Glow magenta
        self.r.value = False       # Blue and red make magenta
        self.g.value = True
        self.b.value = False

    def cyan(self): # Glow cyan
        self.r.value = True        # Green and blue make cyan
        self.g.value = False
        self.b.value = False


    def rainbow(self, rate: float): # making the colors of the rainbow

        self.yellow()
        time.sleep(1.0/rate)
        self.red()
        time.sleep(1.0/rate)
        self.green()
        time.sleep(1.0/rate)
        self.blue()
        time.sleep(1.0/rate)
        self.cyan()
        time.sleep(1.0/rate)
        self.magenta()
        time.sleep(1.0/rate)





