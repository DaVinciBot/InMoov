#!/bin/bash

#Le github de base est dans /home
#Data : placer les données des db pour MongoDB dans /inmoov/databases/
#Data : placer le fichier de config de nginx dans /inmoov/nginx/ + symlink
#Placer les données des serveurs web dans /inmoov/admin_web_ui/
#Créer le workspace ROS dans /inmoov/inmoov_ros

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

CURRENT_DIR="$(pwd)"
rm -r /inmoov
mkdir /inmoov
mkdir /inmoov/databases/

cp "$CURRENT_DIR/config"
source /opt/ros/kinetic/setup.bash && source /home/pi/DaVinciBot-InMoov/inmoov_catkin_ws/devel/setup.bash
mongod --dbpath /home/pi/DaVinciBot-InMoov/db --auth &
mongod --dbpath /inmoov/data/db --auth
export FLASK_ENV = "production"
gunicorn -b 127.0.0.1:5000 InMoov_WebServer:app -w 1 -k eventlet --chdir /home/InMoov/internal_modules/admin_web_ui/

