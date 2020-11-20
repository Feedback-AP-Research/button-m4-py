import time
from setup import led, rgb, check

class State:
    def __init__(self):
        self.led = False
        self.button_a = False
        self.button_b = False
        self.rgb = False
        self.color = (255, 255, 255)

    def __repr__(self):
        return "<Buttons: {}/{}, LED: {}, RGB: {}, Color: {}>".format(self.button_a, self.button_b, self.led, self.rgb, self.color)

state = State()

while True:
    # first pass: check real life
    state.button_a = check("A")
    state.button_b = check("B")

    # second pass: assess state
    if state.button_a:
        state.led = True
    else:
        state.led = False

    if state.button_b:
        state.rgb = True
    else:
        state.rgb = False

    # third pass: reconcile state
    led.value = state.led

    if state.rgb:
        rgb.fill(state.color)
    else:
        rgb.fill((0, 0, 0))

    time.sleep(0.2)
