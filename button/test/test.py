
import time
from setup import led, rgb, check

while True:
    led.value = check("A")

    if check("B"):
        rgb[0] = (255, 255, 255)
    else:
        rgb[0] = (0, 0, 0)

    time.sleep(0.2)
