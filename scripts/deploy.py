deploymode = "update"
appname = "websphere-demo"
cell = "cell1"
node = "node1"
server = "server1"
package_path = "/opt/websphere-demo/websphere-demo-1.0.war"
context = "/hello"
web_moudle = "websphere-demo-1.0.war"
web_moudle_config = "websphere-demo-1.0.war,WEB-INF/web.xml"
vhost = "default_host"
pre_compile_jsp = "true"
reload_enabled = "false"

apps = AdminApp.list()
index = apps.find(appname)
if index == -1:
    deploymode = "install"

if deploymode == "install" :

    print("Install application:"+appname)
    options = ['-appname',appname,'-cell',cell,'-node', node, '-server', server ,'-contextroot', context, '-MapWebModToVH',[[ web_moudle, web_moudle_config, vhost ]]]
    if pre_compile_jsp == "true" :
        options.append("-preCompileJSPs")
    if reload_enabled == "false" :
        options.append("-reloadEnabled")
    AdminApp.install(package_path,options)
    AdminConfig.save()

else :
    print("Update application:"+appname)
    options = ['-operation','update','-contents', package_path, '-contextroot',context ,'-nodeployejb','-MapWebModToVH',[[ web_moudle,web_moudle_config,vhost]]]
    if pre_compile_jsp == "true":
        options.append("-preCompileJSPs")
    if reload_enabled == "false" :
        options.append("-reloadEnabled")
    AdminApp.update(appname, 'app', options)

deployid = "/Deployment:"+appname+"/"
dep = AdminConfig.getid(deployid)
depObject = AdminConfig.showAttribute(dep, 'deployedObject')
classldr = AdminConfig.showAttribute(depObject, 'classloader')
AdminConfig.modify(classldr, [['mode', 'PARENT_LAST']])

AdminConfig.save()