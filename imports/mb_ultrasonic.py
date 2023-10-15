# -*- coding: utf-8 -*-
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
        return sonar.distance_cm()