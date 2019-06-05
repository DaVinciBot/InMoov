#!/bin/bash

if [ "$(id -u)" != "0" ]; then
   echo "This script must be run as root" 1>&2
   exit 1
fi

useradd -r "ros" -s "/usr/sbin/nologin" > /dev/null
mkdir /home/ros
mkdir /home/ros/log
mkdir /home/ros/web_log
chown ros:ros /home/ros
chown ros:ros /home/ros/log
chown ros:ros /home/ros/web_log
useradd -r "www-data" -s "/usr/sbin/nologin" > /dev/null
useradd -r "mongod" -s "/usr/sbin/nologin" > /dev/null

rm -r "/inmoov"
mkdir "/inmoov"

#Setup nginx
rm "/etc/nginx/sites-enabled/default"
mkdir "/inmoov/config"
cp "./config/" "/inmoov/" -r
ln -s "/inmoov/config/nginx_inmoov-local.conf" "/etc/nginx/sites-enabled/inmoov_nginx.conf"

#Create database
mkdir "/inmoov/databases/"
mongod --dbpath "/inmoov/databases" > /dev/null &
sleep 5
mongo < "/inmoov/config/mongo_config.js"
kill %1
chown mongod:mongod "/inmoov/databases" -R

#Import Web datas
cp "./internal_modules/admin_web_ui/" "/inmoov/www/" -r
chown www-data:www-data "/inmoov/www" -R

#Import ros package
cp "./inmoov_catkin_ws/" "/inmoov/catkin_ws" -r
chown ros:ros "/inmoov/catkin_ws" -R

#Import services
rm /etc/systemd/system/inmoov* -r
cp -r "./services" "/inmoov/services"
cp "/inmoov/services/inmoov_nginx.service" "/etc/systemd/system/inmoov_nginx.service"
cp "/inmoov/services/inmoov_mongod.service" "/etc/systemd/system/inmoov_mongod.service"
cp "/inmoov/services/inmoov_main.service" "/etc/systemd/system/inmoov_main.service"
cp "/inmoov/services/inmoov_gunicorn.service" "/etc/systemd/system/inmoov_gunicorn.service"
cp "/inmoov/services/inmoov_ros.service" "/etc/systemd/system/inmoov_ros.service"
systemctl daemon-reload
systemctl enable inmoov_nginx inmoov_mongod inmoov_main inmoov_gunicorn inmoov_ros

#Mount ROS
cd "/inmoov/catkin_ws"
source "/opt/ros/kinetic/setup.bash"
catkin_make

#And finally reboot
reboot now
