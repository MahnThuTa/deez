# Imports go at the top
from microbit import *


# Code in a 'while True:' loop repeats forever
while True:
    if button_a.was_pressed():
        display.show(Image(
            "13579:"
            "13579:"
            "13579:"
            "13579:"
            "13579:"
            "13579:"
        ))
        sleep(2000)
        display.scroll("GO")
   
    