#!/bin/bash

export WAS_PATH=/opt/IBM/WebSphere/AppServer/bin
user=admin
psword=fit2cloud

processesNum=`bash $WAS_PATH/wsadmin.sh -port 8880 -user $user -password $psword -lang jython -c "print len(AdminControl.queryNames('type=Application,name=websphere-demo,*'))"|tail -1`

if [ "$processesNum" -gt "0" ];then
    exit 0
else 
    exit 1
fi
