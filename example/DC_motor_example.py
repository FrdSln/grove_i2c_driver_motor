# example pour 2 moteurs à courant continu
from machine import ADC, Pin
from time import *

from esp_grove_driver_moteur import *
dm = mp_driver_moteur()

# 2 moteurs sens 1
dm.vit(1, 50)      # sens 1 moteur 1 à 50%
dm.vit(2, 50)      # sens 1 moteur 2 à 50%
sleep_ms(2000)
# arrêt
dm.vit(1, 0)
dm.vit(2, 0)
sleep_ms(2000)
# 2 moteurs sens 2
dm.vit(1, -50)     # sens 2 moteur 1 à 50%
dm.vit(2, -50)     # sens 2 moteur 2 à 50%
sleep_ms(2000)
# arrêt
dm.vit(1, 0)
dm.vit(2, 0)
sleep_ms(2000)

# démo 1 moteur puis l'autre
dm.vit(1, 30)
sleep_ms(1000)
dm.vit(1, 0)
sleep_ms(1000)
dm.vit(2, 30)
sleep_ms(1000)
dm.vit(2, 0)
