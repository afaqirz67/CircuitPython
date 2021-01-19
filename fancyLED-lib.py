# Libraries
import digitalio
import time
import board

class FancyLED: # FancyLED class is created

    # __init__ is short for initialization. It is a constructor
    # which gets called when you make an instance of the class
    # and it is not necessary. But usually it our practice to
    # write init method for setting default state of the object.


    # The self parameter refers to the instance of the object
    def __init__(self, led1, led2, led3):


        self.l = digitalio.DigitalInOut(led1)
        self.l.direction = digitalio.Direction.OUTPUT

        self.l2 = digitalio.DigitalInOut(led2)
        self.l2.direction = digitalio.Direction.OUTPUT

        self.l3 = digitalio.DigitalInOut(led3)
        self.l3.direction = digitalio.Direction.OUTPUT





    # defining methods ...

    def alternate(self):

        t = 0.3 # sets the time value as a vairable
        self.l.value = True
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)
        self.l.value = True
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)
        self.l.value = True
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)


        self.l.value = True
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)
        self.l.value = True
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)
        self.l.value = True
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)
        self.l3.value = False


    def blink(self):
        t = 0.3
        self.l.value = True
        self.l2.value = True
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)

        self.l.value = True
        self.l2.value = True
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)

        self.l.value = True
        self.l3.value = True
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)

    def chase(self):
        t = 0.3
        self.l.value = True
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)



        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)
        self.l.value = True
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)


        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)
        self.l.value = True
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)


        self.l.value = False
        self.l2.value = True
        self.l3.value = False
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)


    def sparkle(self):
        t = 3
        self.l.value = True
        self.l2.value = True
        self.l3.value = True
        time.sleep(t)
        self.l.value = False
        self.l2.value = False
        self.l3.value = False
        time.sleep(t)





