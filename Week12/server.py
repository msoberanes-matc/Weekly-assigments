#!/usr/bin/env python3
import socket

myAddress = "127.0.0.1"
myPort = 44444
rcvData = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((myAddress,myPort))

while(1):
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while(1):
        rcvData = conn.recv(1024)
        if not rcvData:
            break
        msg = rcvData
        conn.sendall(msg)	          
s.close()    
