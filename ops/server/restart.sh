#!/bin/bash

echo "stopping plurl ..."
sudo service rabbitmq-server stop
sudo initctl emit plurl-stop
sleep 1s
echo "starting plurl ..."
sudo service rabbitmq-server start
sudo initctl emit plurl-start
touch /tmp/django-restart
echo "restart complete!"