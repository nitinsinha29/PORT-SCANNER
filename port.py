#!/bin/python3
import sys # gives you access to some variables or maintained by the interpreter
import socket # allows to establish the network connection over protocol
from datetime import datetime

#Define our target
if len(sys.argv)==2: #  ( method of length is 2 ) argv = amount of argument we are giving
	target = socket.gethostbyname(sys.argv[1]) #Translate Host Name to IP ( basically convert host name to ip )
else:
	print("Invalid amount of arguments.")
	print("Syntax : python3 port.py <IP>") # here port.py is name of the file 
	
#Adding a banner
print("-"*50)
print("Scanning target " + target )
print("Time Started : " + str(datetime.now()))
print("-"*50)

try:
	for port in range (50,85):
		s=socket.socket(socket.AF_INET,socket.SOCK_STREAM) #trying to connect the port with given ip.  here , AF_INET = IPV4 and SOCK_STREAM is port which are going to connect to.
		socket.setdefaulttimeout(1)
		result=s.connect_ex((target , port )) # ex= error indicator
		if result==0:
			print(f"port{port} is open")
		s.close()

except KeyboardInterrupt:
	print("\n Exiting Program")
	sys.exit()
	
except socket.gaierror:
	print("Hostname could not be resolved") #suppose the hostname couldn't find ip
	sys.exit()
	
except socket.error:
	print("Could not connected to server")
	sys.exit()
		
