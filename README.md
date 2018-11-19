# Video InMoov

### 1. InMoov : 

- Expliquer le robot (robot open-source, ...). `photo du InMoov + logo + montrer que c'est open-source`
- Montrer les fonctionnalitées déjà présentes (lever les bras, ...). `montrer videos`
- Expliquer le système informatique actuel (arduino, ...). `à réfléchir`

### 2. Projet : 

Problèmes: 
- Système d'alimentation: limité, pas de séparation data/alim.
- Système de contrôle des servos: trop faible capacité, problème si on augmente le nombre de modules à gérer.
- MyRobotLab: trop haut niveau d'interprétation, donc les nouvelles technologie sont difficilement implémentable.

Solutions: 
- Séparation alim et data, carte d'alimentation. 
- Carte de contrôle: on va produire les cartes sur la base d'une arduino avec nos propres conditions (microcontroleur puissant, ethernet, ...).
- ROS outils open-source qui permet la com entre hardware et software (montrer Pepper car utilise ROS).
- Webserver avec API pour contrôler le robot.

### 3. Conclusion :

Résoudre ces problèmes nous permettra d'avoir le contrôle total du robot, de savoir comment il fonctionne et de l'améliorer à l'infini.

### 4. QUI/QUAND :

Qui : Florian Quibel, Florian Prigent, Lucas Bichet, Charles d'Antouard, Ge Qiu, Pierre Le Lay
Quand : Projet Année 2018/2019
- Système d'alimentation + carte embarquée : Janvier 2019 
- Midleware ROS et webserver : Avril 2019
