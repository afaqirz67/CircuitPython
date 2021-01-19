from fancyLed import FancyLED
import board

fancy1 = FancyLED(board.D1, board.D2, board.D3)
fancy2 = FancyLED(board.D4, board.D5, board.D7)

while True:
    fancy1.alternate()
    fancy2.blink()
    fancy1.chase()
    fancy2.sparkle()