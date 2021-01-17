import rojoMCRcon
import threading 
import ServerInfo

mcr = rojoMCRcon.MCRcon(ServerInfo.ip, ServerInfo.password, port=ServerInfo.port)
allowed = 0

def sendCommand(command):
 mcr.connect()
 result = (mcr.command(command))
 mcr.disconnect()
 return(result)


def parseChat(input, allowedFrom):
 global allowed  
 if(allowedFrom != allowed): return
 print(input)