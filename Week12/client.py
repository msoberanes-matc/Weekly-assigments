#!/usr/bin/env python3
import socket
rAddress = "127.0.0.1"
rPort = 44444
msg = "Good morning welcome to Python!"
data = ""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((rAddress,rPort))

while True:

    mensaje = input("Type message to the server or exit to quit: ") 

    if mensaje != "exit":
        msg = mensaje
        
    if mensaje == "exit":
        print("See you later Good Bye!!")
        break

    for i in range(1):
        #s.send(msg)
        s.send(msg.encode("utf-8"))
        data = s.recv(1024).decode("utf-8")
        print(data)
s.close()    
