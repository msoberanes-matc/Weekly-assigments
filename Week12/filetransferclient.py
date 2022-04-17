#!/usr/bin/env python3
import socket
import sys

rAddress = "127.0.0.1"
rPort = 50100

with open("/etc/passwd", "r") as hFile:
    msg = hFile.read()
    
data = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((rAddress,rPort))

for i in range(1):
    s.send(msg.encode("utf-8"))
    data = s.recv(4092).decode("utf-8")
    print(data)
    
s.close()    
