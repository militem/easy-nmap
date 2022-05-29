import os

class Nmap:

    def __init__(self):
        self.ip = ""
        self.command = ""

    def set_ip_command(self, ip, command):
        self.ip = ip
        self.command = command

    def getCommand(self):
        os.system("sudo nmap " + str(self.ip) + " " + str(self.command))