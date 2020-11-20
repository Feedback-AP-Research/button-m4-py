# save as setup.py
import board
import neopixel
from digitalio import DigitalInOut, Direction, Pull

led = DigitalInOut(board.D13)
led.direction = Direction.OUTPUT

rgb = neopixel.NeoPixel(board.NEOPIXEL, 1)
rgb.brightness = 0.3

a_button = DigitalInOut(board.D4)
a_button.direction = Direction.INPUT
a_button.pull = Pull.DOWN

b_button = DigitalInOut(board.D5)
b_button.direction = Direction.INPUT
b_button.pull = Pull.DOWN

def check(token):
    if token == "A":
        return a_button.value
    if token == "B":
        return b_button.value
