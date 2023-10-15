# -*- coding: utf-8 -*-
# Didaktik der Informatik - Universität Bayreuth
# Version 2021-04-29
from music import *
from mb_basic import *
def play_tone(frequency, duration, pin_nr, wait=True):
    pitch(frequency, duration, get_pin(pin_nr), wait);