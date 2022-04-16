# bibliothèque pour ESP32 flashé micropython
# pilotage d'un moteur pas à pas bipolaire
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

# pilote un moteur pas à pas 2 phases en mode 1
    def step(self, pas):
        if pas > 0:
            direction = 1
        else:
            direction = -1
            pas = - pas

        self.set_register(0x82, 0xff, 0xff)

        cnt = 0
        if direction == 1:
            for i in range(pas):
                if cnt == 0:
                    self.set_register(0xaa, 0x01, 0x01)
                    self.set_register(0xaa, 0x05, 0x01)
                if cnt == 1:
                    self.set_register(0xaa, 0x04, 0x01)
                    self.set_register(0xaa, 0x06, 0x01)
                if cnt == 2:
                    self.set_register(0xaa, 0x02, 0x01)
                    self.set_register(0xaa, 0x0a, 0x01)
                if cnt == 3:
                    self.set_register(0xaa, 0x08, 0x01)
                    self.set_register(0xaa, 0x09, 0x01)
                cnt = (cnt + 1) % 4
        if direction == -1:
            for i in range(pas):
                if cnt == 0:
                    self.set_register(0xaa, 0x08, 0x01)
                    self.set_register(0xaa, 0x0a, 0x01)
                if cnt == 1:
                    self.set_register(0xaa, 0x02, 0x01)
                    self.set_register(0xaa, 0x06, 0x01)
                if cnt == 2:
                    self.set_register(0xaa, 0x04, 0x01)
                    self.set_register(0xaa, 0x05, 0x01)
                if cnt == 3:
                    self.set_register(0xaa, 0x01, 0x01)
                    self.set_register(0xaa, 0x09, 0x01)
                cnt = (cnt + 1) % 4

