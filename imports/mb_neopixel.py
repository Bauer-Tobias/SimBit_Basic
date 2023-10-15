# -*- coding: utf-8 -*-
# Didaktik der Informatik - Universität Bayreuth
# Version 2021-04-29
from neopixel import *
from mb_basic import *
np = None
def prepare_neopixel(pin_nr, n):
    global np
    np = NeoPixel(get_pin(pin_nr), n)
def clear_neopixel():
    global np
    if np == None:
        print("Du musst deinen Neopixel erst initialisieren.")
    else:
        np.clear()
def neopixel_set_pixel(position, r, g, b, show=False):
    global np
    if np == None:
        print("Du musst deinen Neopixel erst initialisieren.")
    else:
        if r > 255:
            r = 255
        if g > 255:
            g = 255
        if b > 255:
            b = 255
        np[position] = (r, g, b)
        if show:
            np.show()
def neopixel_clear_pixel(position, show=False):
    global np
    if np == None:
        print("Du musst deinen Neopixel erst initialisieren.")
    else:
        np[position] = (0, 0, 0)
        if show:
            np.show()
def neopixel_show():
    global np
    if np == None:
        print("Du musst deinen Neopixel erst initialisieren.")
    else:
        np.show()