import time
import random
from setup import led, rgb, check

class State:
    def __init__(self):
        self.button_a = False
        self.button_b = False
        self.led = False
        self.rgb = False
        self.color = (255, 255, 255)

    def random_color(self):
        self.color = (
             random.randrange(0, 255),
             random.randrange(0, 255),
             random.randrange(0, 255)
        )

    def update(self):
        self.button_a = check("A")
        self.button_b = check("B")

        if self.button_a:
            print("LED on")
            self.led = True
        else:
            self.led = False

        if self.button_b:
            print("RGB on. Color: {}".format(state.color))
            self.rgb = True
        else:
            self.rgb = False
            self.random_color()

    def __repr__(self):
        return "<Buttons: {}/{}, LED: {}, Color: {}>".format(self.button_a, self.button_b, self.led, self.color)

state = State()

while True:
    # update the state
    state.update()

    # take action - do things that cause side effects
    led.value = state.led

    if state.rgb:
        rgb[0] = state.color
    else:
        rgb[0] = (0, 0, 0)

    time.sleep(0.2)
