#!/usr/bin/env python3
import socket

myAddress = "127.0.0.1"
myPort = 50100
rcvData = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((myAddress,myPort))

while(1):
    s.listen(1)
    conn, addr = s.accept()
    print(f"Connected by {addr}")
    while(1):
        rcvData = conn.recv(4092)
        if not rcvData:
            break
        msg = rcvData.decode("utf-8","replace")
        with open("newpasswd", "w") as hFileOut:
            hFileOut.write(msg)
            msg2 = (b"/etc/passwd file was copied into newpasswd file!")
            msg = rcvData
            conn.send(msg2)	          
s.close()    
