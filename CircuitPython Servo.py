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
