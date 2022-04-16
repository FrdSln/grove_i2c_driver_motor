# exemple pour un moteur pas à pas bipolaire
from machine import ADC, Pin
from time import *

from esp_grove_driver_stepper_motor import *
crouzet = mp_driver_motor()

crouzet.step(48)
sleep_ms(2000)
crouzet.step(-24)
sleep_ms(2000)
