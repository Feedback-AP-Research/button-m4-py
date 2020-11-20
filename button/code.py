from setup import led, rgb, check

if check("A"):
    print("Button A has been pressed")
else:
    print("Button A has not been pressed")

if check("B"):
    print("Button B has been pressed")
else:
    print("Button B has not been pressed")
