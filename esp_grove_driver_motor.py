# bibliothèque pour ESP32 flashé micropython
# écrit à partir de la version micro:bit (GcWorks.fr)
# F. SAULIN 2022
from machine import Pin, I2C
import time

i2c = I2C(0,scl=Pin(22), sda=Pin(21), freq=20000)


class mp_driver_motor:
    def __init__(self):
        time.sleep_ms(10)
        self.m1_dir = self.m2_dir = 1
        self.m1_vit = self.m2_vit = 0
        self.set_register(0x84, 0x02, 0x00)  # PWM à 3921 Hz

    def set_register(self, reg, val1, val2):
        val = bytes((reg, val1, val2))
        i2c.writeto(0x0F, val)
        time.sleep_ms(50)

    def vit(self, mot, vit):
        if mot == 1:
            self.m1_vit = vit
        if mot == 2:
            self.m2_vit = vit

        # direction
        if self.m1_vit >= 0 and self.m2_vit >= 0:
            self.set_register(0xAA, 0x0A, 0x00)
        if self.m1_vit >= 0 and self.m2_vit < 0:
            self.set_register(0xAA, 0x06, 0x00)
        if self.m1_vit < 0 and self.m2_vit >= 0:
            self.set_register(0xAA, 0x09, 0x00)
        if self.m1_vit < 0 and self.m2_vit < 0:
            self.set_register(0xAA, 0x05, 0x00)

        # vitesse
        self.set_register(
            0x82, int(abs(self.m1_vit) / 100 * 255), int(abs(self.m2_vit) / 100 * 255)
        )
