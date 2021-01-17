import rojoMCRcon
import socket
import parseScript
import threading 
import time

class Listen():
    def __init__(self, ip, password, port):
        self.mcr = rojoMCRcon.MCRcon(ip, password, port=port) 
        self.stopListen = False
        self.th = threading.Thread(target=self.listenLoop)

    def sendCommand(self, command):
        return(self.mcr.command(command))

    def disconnect(self):
        print("Reconnecting...")
        self.stopListen = True

    def connected(self):
        return(self.mcr.socket)

    def listenLoop(self):
        while self.stopListen == False:
            response = (self.mcr._listen(2))
            parseScript.parseChat(response, self.allowed)

    def startListen(self, allowed):
        self.mcr.connect()
        self.allowed = allowed
        self.sendCommand("Listen allon")
        if(not self.th.isAlive()): self.th.start()