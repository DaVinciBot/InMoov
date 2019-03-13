#!/bin/bash

source /opt/ros/kinetic/setup.bash && source /home/pi/DaVinciBot-InMoov/inmoov_catkin_ws/devel/setup.bash
mongod --dbpath /home/pi/DaVinciBot-InMoov/db --auth &
export FLASK_ENV = "production"

#Setup reverse proxy nginx avec SSL + config web serveur sans SSL
#Bouger le robot
#finir l'autostart (boote ROS via launcher, boot serveur web + nginx, boote websocket api)
#dev un client de base
#Comment marche le inmoov_controller_client  ?? a joindre au API websocket
#ajout de la vérif des tokens + mise en place des tokens depuis interfacce web
