import sys
import os
from java.lang import System
import sys
import os
from java.lang import System
#Python Script to manage Servers in weblogic server.
#This script takes input from command line and executes it.
#It can be used to check status,stop,start of applications in weblogic server using weblogic wlst tool.
#Company: TechPaste Solutions
import getopt
#========================
#Usage Section
#========================
def usage():
	print "Usage:"
	print "java weblogic.WLST manageServers.py -u username -p password -a adminUrl [:] -n ServerName -c [stop:start:restart:status:stopall:startall:statusall]\n"
	sys.exit(2)
#========================
#Connect To Domain
#======================== 
def connectToDomain():
	try:
		if username != "":
			connect(username, password, adminUrl)
			print 'Successfully connected to the domain\n'
		else:
			connect(userConfigFile=UCF, userKeyFile=UKF, url=admurl)
			print 'Successfully connected to the domain\n' 
	except:
		print 'The domain is unreacheable. Please try again\n'
	exit() 
#==============================================
#Checking Server Status
#==============================================
def _serverstatus(ServerName):
	try:
		print 'Server reached:'+ServerName
		cd('domainRuntime:/ServerLifeCycleRuntimes/'+ServerName);
		print 'Cd successful';
		ls();
		serverState = cmo.getState()
		print 'Server State'+serverState;
		if serverState == "RUNNING":
			print 'Server ' + ServerName + ' is :\033[1;32m' + serverState + '\033[0m';
		elif serverState == "STARTING":
			print 'Server ' + ServerName + ' is :\033[1;33m' + serverState + '\033[0m';
		elif serverState == "UNKNOWN":
			print 'Server ' + ServerName + ' is :\033[1;34m' + serverState + '\033[0m';
		else:
			print 'Server ' + ServerName + ' is :\033[1;31m' + serverState + '\033[0m';
		return serverState
	except:
		print 'Not able to get the' + serverState +'server status. Please try again\n';
		print 'Please check logged in user has full access to complete the requested operation on ' ServerName '\n';
	exit() 
#==============================================
#Start Server Block
#============================================== 
def _startServer(ServerName): 
	try:
		cd('domainRuntime:/ServerLifeCycleRuntimes/'+ServerName);
		cmo.start();
		state=_serverstatus(ServerName);
		while (state!='RUNNING'):
			state=_serverstatus(ServerName);
			java.lang.Thread.sleep(5000);
	except:
		print 'Error in getting current status of ' ServerName '\n';
		print 'Please check logged in user has full access to complete the start operation on ' ServerName '\n';
	exit()
#==============================================
#Stop Server Block
#============================================== 
def _stopServer(ServerName): 
	try:
		cd('domainRuntime:/ServerLifeCycleRuntimes/'+ServerName);
		cmo.forceShutdown();
		state=_serverstatus(ServerName);
		while (state!='SHUTDOWN'):
			state=_serverstatus(ServerName);
			java.lang.Thread.sleep(5000);
	except:
		print 'Error in getting current status of ' ServerName '\n';
		print 'Please check logged in user has full access to complete the stop operation on ' ServerName '\n';
		exit() 
#===============================
#Input Values Validation Section
#=============================== 
	if _name=='main' or __name_== 'main': 
		try:
			opts, args = getopt.getopt(sys.argv[1:], "u(tongue):a:n:c:", ["username=", "password=", "adminUrl=", "ServerName=", "command="]) 
		except getopt.GetoptError, err:
			print str(err)
	usage() 
	username = ''
	password = ''
	adminUrl = ''
	ServerName = ''
	command = '' 
	for opt, arg in opts:
		if opt == "-u":
			username = arg
		elif opt == "-p":
			password = arg
		elif opt == "-a":
			adminUrl = arg
		elif opt == "-n":
			ServerName = arg
		elif opt == "-c":
			command = arg 
		if username == "":
			print "Missing \"-u username\" parameter.\n"
			usage()
		elif password == "":
			print "Missing \"-p password\" parameter.\n"
			usage()
		elif adminUrl == "":
			print "Missing \"-a adminUrl\" parameter.\n"
			usage()
		elif ServerName == "":
			print "Missing \"-n ServerName\" parameter.\n"
			usage()
		elif command == "":
			print "Missing \"-c command\" parameter.\n"
			usage()
#========================
#Main Control Block For Operations
#========================
balancer = 'Balancer'
cl1 = 'cl1'
cl2 = 'cl2'
cl3 = 'cl3'

def tryRun(server):
	try:
		shutdown(server);
		java.lang.Thread.sleep(10000);
		start(server);
		if server == balancer:
			stateBal = _serverstatus(server);
		elif server == cl1:
			state1 = _serverstatus(server)
		elif server == cl2:
			state2 = _serverstatus(server)
		elif server == cl3:
			state3 = _serverstatus(server)
	except:
		print 'waiting...';
		start('Balancer');
		stateBal = _serverstatus('Balancer');

def lifecycleMain():
	try:
		if command =='standby' :
			stateBal=_serverstatus('Balancer');
			state1=_serverstatus('cl1');
			state2=_serverstatus('cl2');
			state3=_serverstatus('cl3');
			while (stateBal!='RUNNING') :
				try:
					shutdown('Balancer');
					java.lang.Thread.sleep(10000);
					start('Balancer');
					stateBal=_serverstatus('Balancer');
				except:
					print 'waiting...';
					start('Balancer');
					stateBal=_serverstatus('Balancer');
			while (state1!='RUNNING') :
				try:
					shutdown('cl1');
					java.lang.Thread.sleep(10000);
					start('cl1');
					state1=_serverstatus('cl1');
				except:
					print 'waiting...';
					start('cl1');
					state1=_serverstatus('cl1');
			while (state2!='RUNNING') :
				try:
					shutdown('cl2');
					java.lang.Thread.sleep(10000);
					start('cl2');
					state2=_serverstatus('cl2');
				except:
					print 'waiting...';
					start('cl2');
					state2=_serverstatus('cl2');
			while (state3!='STANDBY'):
				try:
					shutdown('cl3');
					java.lang.Thread.sleep(10000);
					start('cl3');
					state3=_serverstatus('cl3');
				except:
					print 'waiting...';
					start('cl3');
					state3=_serverstatus('cl3');
			while True:
				while (state1=='RUNNING' and state2=='RUNNING'):
					state1=_serverstatus('cl1');
					state2=_serverstatus('cl2');
					resume('cl3');
				while (state1!='RUNNING' or state2!='RUNNING') :
					state1=_serverstatus('cl1');
					state2=_serverstatus('cl2');
					shutdown('cl3');
					java.lang.Thread.sleep(10000);
					start('cl3');
		elif command =='status' :
			_serverstatus(ServerName);
		elif command =='stop':
			state=_serverstatus(ServerName);
			if state!='SHUTDOWN' :
				print 'Trying To Shutdown Server:' + ServerName + '...';
				_stopServer(ServerName);
		elif command =='start':
			state=_serverstatus(ServerName);
			if state!='RUNNING' :
				print 'Trying To Start Server:' + ServerName + '...';
				_startServer(ServerName);
		elif command =='restart':
			state=_serverstatus(ServerName);
			if state!='SHUTDOWN' :
				print 'Trying To Shutdown Server:' + ServerName + '...';
				_stopServer(ServerName);
				state=_serverstatus(ServerName);
			if state!='RUNNING' :
				print 'Trying To Start Server:' + ServerName + '...';
				_startServer(ServerName);
		elif command == "stopall":
			try:
				cd('/Servers')
				allServers=ls('/Servers', returnMap='true')
				for p_server in allServers:
					if p_server == 'AdminServer':
						continue
					else:
						_stopServer(p_server);
			except Exception, e:
				print "Error Occured"
		elif command == "startall":
			try:
				cd('/Servers')
				allServers=ls('/Servers', returnMap='true')
				for p_server in allServers:
					if p_server == 'AdminServer':
						continue
					else:
						_startServer(p_server);
			except Exception, e:
				print "Error Occured"
		elif command == "statusall":
			try:
				cd('/Servers')
				allServers=ls('/Servers', returnMap='true')
				for p_server in allServers:
					_serverstatus(p_server);
			except Exception, e:
				print "Error Occured"
		else:
			print 'Not able to understand the command supplied.'
			usage();
	except:
		print 'Error during lifecycle operation of ' ServerName '\n'
		exit();
#========================
#Execute Block
#======================== 
connectToDomain();
lifecycleMain();
disconnect();
exit();
##______________________________________________________________________________________
##Сам скрипт написан на python 2 (отличае по синтаксису от python 3) и содержит в себе определение шести функций, управляющих жизненным циклом серверов : usage(), connectToDomain(), serverstatus(ServerName), startServer(ServerName), stopServer(ServerName), lifecycleMain(). Сначала вызывается функция connectToDomain(), которая осуществляет коннект посредством WLST (WebLogic Scripting Tool) к Админ Серверу на административный порт, далее вызывается функция lifecycleMain() , которая в зависимости от поступившей на неё команды, выполняет описанные действия. После того как lifecycleMain() отработает, вызывается disconnect() (думаю, понятно по смыслу), и затем exit() – выход из WLST.
##Сам скрипт я скопипастил с просторов интернета: http://www.techpaste.com/2013/09/simple-wlst-script-start-stop-monitor-check-status-managed-servers-progress-bar-weblogic-server/
##И добавил в следующий блок кода в lifecycleMain():
##______________________________________________________________________________________