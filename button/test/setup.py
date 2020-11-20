import time
from setup import led, rgb, check

import random

class State:
    _debounce = 0.2

    def __init__(self):
        self.button_a = False
        self.button_b = False
        self.led = False
        self.rgb = False
        self.color = (255, 255, 255)
        self.last_color = (255, 255, 255)
        self.checkin = time.monotonic()

    def random_color(self):
        print("Generating random color")
        self.color = (
             random.randrange(0, 255),
             random.randrange(0, 255),
             random.randrange(0, 255)
        )

    def update(self):
        if time.monotonic() - self.checkin > self._debounce:
            self.button_a = check("A")

            # b button was pressed
            if not self.button_b and check("B"):
                print("B button pressed")
                self.random_color()
                self.button_b = True
            else:
                self.button_b = False

            self.checkin = time.monotonic()

            if self.button_a:
                print("LED on")
                self.led = True
            else:
                self.led = False

            if self.button_b:
                print("RGB on. Color: {}".format(self.color))
                self.rgb = True
            else:
                self.rgb = False

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
