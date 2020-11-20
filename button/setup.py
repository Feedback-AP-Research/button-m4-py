import time
from setup import led, rgb, check

# review of what the setup module does for us:
#
#   - led is our digital pin object connected to pin 13
#   - rgb is our DotStar or NeoPixel
#   - check() is a function that handles differences between button wiring

# these state variables need specific names
led_state = False
button_a_state = False
button_b_state = False
rgb_state = False
rgb_color = (255, 255, 255)

while True:
    button_a_state = check("A")
    button_b_state = check("B")

    if button_a_state:
        led_state = True
    else:
        led_state = False

    if button_b_state:
        rgb_state = True
    else:
        rgb_state = False

    led.value = led_state

    if rgb_state:
        rgb.fill(rgb_color)
    else:
        rgb.fill((0, 0, 0))

    time.sleep(0.2)
