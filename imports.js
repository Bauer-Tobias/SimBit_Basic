const impArr = [];
impArr.push(["mb_basic.py",`# -*- coding: utf-8 -*-
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
    time.sleep(delay/1000)`]);
impArr.push(["mb_hello.py",`from microbit import *
import speech
def scream(text):
	return speech.say(text)`]);
impArr.push(["mb_music.py",`# -*- coding: utf-8 -*-
# Didaktik der Informatik - Universität Bayreuth
# Version 2021-04-29
from music import *
from mb_basic import *
def play_tone(frequency, duration, pin_nr, wait=True):
    pitch(frequency, duration, get_pin(pin_nr), wait);`]);
impArr.push(["mb_neopixel.py",`# -*- coding: utf-8 -*-
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
        np.show()`]);
impArr.push(["mb_ultrasonic.py",`# -*- coding: utf-8 -*-
# Didaktik der Informatik - Universität Bayreuth
# Version 2021-04-29
from mb_basic import *
from machine import time_pulse_us
class HCSR04:
    def __init__(self, triggerPin, echoPin):
        self.triggerPin = triggerPin
        self.echoPin = echoPin
        self.triggerPin.write_digital(0)
        self.echoPin.read_digital()
    def distance_mm(self):
        self.triggerPin.write_digital(1)
        self.triggerPin.write_digital(0)
        micro = time_pulse_us(self.echoPin, 1)
        return (micro / 2) * 0.34    
    def distance_cm(self):
        return int(self.distance_mm() / 10)
sonar = None
def prepare_ultrasonic_sensor(trigger_pin_nr, echo_pin_nr):
    global sonar
    triggerPin = get_pin(trigger_pin_nr)
    echoPin = get_pin(echo_pin_nr)
    sonar = HCSR04(triggerPin, echoPin)
def ultrasonic_distance_cm():
    global sonar
    if sonar == None:
        print("Du musst den Ultraschallsensor zuerst initialisieren.")
    else:
        return sonar.distance_cm()`]);