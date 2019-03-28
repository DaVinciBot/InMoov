#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

CURRENT_DIR="$(pwd)"
rm -r /inmoov
mkdir /inmoov

#Setup nginx
rm /etc/nginx/sites-enabled/default
mkdir /inmoov/config
cp "$CURRENT_DIR/config/*" "/inmoov/config" -r
ln -s "/inmoov/config/nginx_inmoov-local.conf" "/etc/nginx/sites-enabled/inmoov_nginx.conf"

#Create database
mkdir "/inmoov/databases/"
mongod --dbpath "/inmoov/databases" > /dev/null &
mongo --eval "use inmoov; db.users"
kill %1

#Import Web datas
cp "$CURRENT_DIR/internal_modules/admin_web_ui/" "/inmoov/www/" -r

#Import ros package
cp "$CURRENT_DIR/inmoov_catkin_ws/" "/inmoov/catkin_ws" -r

#Import services
cp "$CURRENT_DIR/services/*" "/etc/systemd/system/"

cd "/inmoov/catkin_ws"
catkin_make

#source /opt/ros/kinetic/setup.bash && source /home/pi/DaVinciBot-InMoov/inmoov_catkin_ws/devel/setup.bash
#mongod --dbpath /inmoov/data/db --auth

#And finally reboot
reboot now
