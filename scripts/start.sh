echo start app

export WAS_PATH=/opt/IBM/WebSphere/AppServer/bin
user=admin
psword=Calong2015
processesNum=`bash $WAS_PATH/wsadmin.sh -port 8880 -user $user -password $psword -lang jython -c "print len(AdminControl.queryNames('type=Application,name=websphere-demo,*'))"|tail -1`

if [ "$processesNum" -gt "0" ];then
    exit 0
else 
	bash $WAS_PATH/wsadmin.sh -port 8880 -user $user -password $psword -lang jython -f /opt/websphere-demo/scripts/start.py
fi



