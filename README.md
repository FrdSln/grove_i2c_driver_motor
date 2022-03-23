# Grove - I2C Motor Driver V1.3

![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)

Bibliothèque et exemple d'utilisation pour [Grove - I2C Motor Driver V1.3](https://wiki.seeedstudio.com/Grove-I2C_Motor_Driver_V1.3/)

## Utilisation

### Matériel nécessaire

- 1 Carte ESP32 flashée avec micropython
- 1 Shield
- 1 Grove - I2C Motor Driver V1.3
- 2 Moteurs CC
- 1 alimentation 6V - 2A
- Logiciel Mu

### Installation

**Copier** la bibliothèque esp_grove_driver_moteur.py avec l'outil _fichiers_ de Mu.

**Lancer** le fichier exemple DC_motor_example.py

Les moteurs fonctionnent à différentes vitesses, dans un sens puis l'autre.

### Fonctions supportées

- Initialisation : dm = mp_driver_moteur()
- Commande d'un moteur CC : dm.vit( _No moteur_ , _vitesse_ )

## Ressources

Ecrit en **micropython** pour ESP32 à partir de la version _micro:bit_ 

[https://gcworks.fr/tutoriel/microbit/Drivermoteur.html](https://gcworks.fr/tutoriel/microbit/Drivermoteur.html)

## Versions

**Dernière version :** 1.0

[Liste des versions](https://github.com/FrdSln/ grove_i2c_driver_motor/tags)

## Auteur

* **F. SAULIN** ([FrdSln](https://github.com/FrdSln))

## Licence

Ce projet est sous licence ``GNU General Public License v3.0`` - voir le fichier [LICENSE.md](LICENSE.md) pour plus d'informations
