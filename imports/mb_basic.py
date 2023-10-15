# -*- coding: utf-8 -*-
# Didaktik der Informatik - Universität Bayreuth
# Version 2021-04-29
from microbit import *
from random import randint
import time
def is_button_a_pressed():
    return button_a.is_pressed()
def is_button_b_pressed():
    return button_b.is_pressed()
def was_button_a_pressed():
    return button_a.was_pressed()
def was_button_b_pressed():
    return button_b.was_pressed()
def get_presses_on_button_a():
    return button_a.get_presses()
def get_presses_on_button_b():
    return button_b.get_presses()
def set_display_pixel(x, y, brightness=9):
    display.set_pixel(x, y, brightness)
def get_display_pixel(x, y):
    return display.get_pixel(x, y)
def clear_display():
    display.clear()
def show_display_text(str):
    display.show(str)
def scroll_display_text(str):
    display.scroll(str)
def scroll_display_text_advanced(str, delay=150, loop=False, wait=True, monospace=False):
    display.scroll(str, delay, loop, wait, monospace)
def get_pin(pin_nr):
    pin = 'pin' + str(pin_nr)
    if pin_nr == 5 or pin_nr == 11:
        print("Dieser Pin ist für einen Button reserviert. Benutze bitte einen anderen.")
        return None
    elif pin_nr < 0 or pin_nr == 17 or pin_nr == 18 or pin_nr > 20:
        return None
    return globals()[pin]
def read_digital(pin_nr):
    pin = get_pin(pin_nr)
    if pin == None:
        print("Falscher Pin.")
        return 0
    else:
        return pin.read_digital()
def write_digital(pin_nr, value):
    pin = get_pin(pin_nr)
    if pin == None:
        print("Falscher Pin.")
    else:
        pin.write_digital(value)
def read_analog(pin_nr):
    pin = get_pin(pin_nr)
    if pin == None:
        print("Falscher Pin.")
        return 0
    else:
        return pin.read_analog()
def write_analog(pin_nr, value, modulo=True):
    pin = get_pin(pin_nr)
    if pin == None:
        print("Falscher Pin.")
        return
    if modulo == True:
        value = value % 1024
        pin.write_analog(value)
    elif value < 0 or value > 1023:
        print("Falscher Wert.")
    else:
        pin.write_analog(value)
def use_pins_with_breadboard():
    display.off()
def print_slowly(text, delay=1000):
    print(text)
    time.sleep(delay/1000)