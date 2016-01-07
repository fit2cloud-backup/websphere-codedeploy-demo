#!/bin/bash

echo configure after deploy code

export WAS_PATH=/opt/IBM/WebSphere/AppServer/bin
user=admin
psword=Calong2015

bash $WAS_PATH/wsadmin.sh -port 8880 -user $user -password $psword -lang jython -f /opt/websphere-demo/scripts/deploy.py


