# Imports go at the top
from microbit import *
import neopixel

Red = (255,0,0)
Green = (0,255,17)
Orange = (255,162,0)

np = neopixel.NeoPixel(pin12, 4)

while True:
    np[1] = Green
    np.show()
    sleep(5000)
    np.clear()

    np[2] = Orange
    np.show()
    sleep(2000)
    np.clear()

    np[3] = Red
    np.show()
    sleep(5000)
    np.clear()