#!/usr/bin/env python3r

#1. Make a dictionary containing the following FQDN to IP address mappings:

#server1.testlab.com -> 192.168.1.10
#server2.testlab.com -> 192.168.1.11
#server3.testlab.com -> 192.168.1.12
#server4.testlab.com -> 192.168.1.13
#server5.testlab.com -> 192.168.1.14
#server6.testlab.com -> 192.168.1.15

servers = dict()

server1 = dict()
server1["fqdName"] = "server1.testlab.com"
server1["ipAddress"] = "192.168.1.10" 

server2 = dict()
server2["fqdName"] = "server2.testlab.com"
server2["ipAddress"] = "192.168.1.11" 

server3 = dict()
server3["fqdName"] = "server3.testlab.com"
server3["ipAddress"] = "192.168.1.12" 

server4 = dict()
server4["fqdName"] = "server4.testlab.com"
server4["ipAddress"] = "192.168.1.13" 

server5 = dict()
server5["fqdName"] = "server5.testlab.com"
server5["ipAddress"] = "192.168.1.14" 

server6 = dict()
server6["fqdName"] = "server6.testlab.com"
server6["ipAddress"] = "192.168.1.15" 

#5. Add a few more names to address mappings. Continue the ip address sequence above for their values.

#server7.testlab.com
#server8.testlab.com

server7 = dict()
server7["fqdName"] = "server7.testlab.com"
server7["ipAddress"] = "192.168.1.16" 

server8 = dict()
server8["fqdName"] = "server8.testlab.com"
server8["ipAddress"] = "192.168.1.17"

servers["server1"] = server1
servers["server2"] = server2
servers["server3"] = server3
servers["server4"] = server4
servers["server5"] = server5
servers["server6"] = server6
servers["server7"] = server7
servers["server8"] = server8

#servers["server2.testlab.com"] = server2

#2.- List all of the FQDN’s in your dictionary

print("List of all the Fully Qualified Domanin Names in the Servers Dictionary")
print(" ")
for servidor in servers.keys():
    temp1 = servers[servidor]
    print(f"{servidor} : {temp1['fqdName']}")
print(" ")

#3.- List all of the IP Addresses in your dictionary

print("List of all IP Addresses in the Servers Dictionary")
print(" ")
for servidor in servers.keys():
    temp2 = servers[servidor]
    print(f"{servidor} : {temp2['ipAddress']}")
print(" ")

#4.- List all of the full records (key/value pairs)

print("List of all the full records (key/value pairs)")
print(" ")
print(servers.items())
print(" ")

while True:

    search = input("Type FQDN or Server# to search. Type quit to exit ")

#Test if server2.testlab.com is contained in your dictionary. 

    for servidor in servers:
        temp3 = servers[servidor]
        if search == (f"{temp3['fqdName']}"):
           if search == "server2.testlab.com":
               print(f"{temp3['fqdName']}" in server2.values())
               print("This FDQN name was found in the Servers Dictionary!")

#Test if server10.testlab.com is contained is your dictionary.

    if search == "server10.testlab.com":
        print(f"{temp3['fqdName']}" in servers)
        print("This FDQN name has not been added yet to the Servers Dictionary!")

    if search == "quit":
        print("Your search was completed Good Bye!!")
        break
    for server in servers:
        if server == search:
            print("==============================================")
            print(f"Found it: {search}")
            print(f" Fully Qualified Domain Name   : {servers[server]['fqdName']}")
            print(f" IP Address   : {servers[server]['ipAddress']}")
