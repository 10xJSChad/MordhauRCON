import listenScript
import threading 
import time
import parseScript
import ServerInfo

listen = listenScript.Listen(ServerInfo.ip, ServerInfo.password, ServerInfo.port)
allowed = 0

def newListen():
 global listen, allowed
 threading.Timer(60.0, newListen).start()
 if(listen.connected() != None): listen.disconnect()
 listen = listenScript.Listen(ServerInfo.ip, ServerInfo.password, ServerInfo.port)
 allowed += 1; parseScript.allowed = allowed
 listen.startListen(allowed)

newListen()

while True:
 print(parseScript.sendCommand(input()))