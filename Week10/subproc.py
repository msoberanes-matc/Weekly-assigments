#!/usr/bin/env python3

import subprocess

def getProcString():
	myProc = subprocess.run(['ps','-axco','command'],
                              stdout=subprocess.PIPE)
	return myProc.stdout.decode()
	
def getProcList():
	myProc = subprocess.run(['ps','-axco','command'],
                              stdout=subprocess.PIPE)
	return myProc.stdout.decode().split('\n')
		
myProcString = getProcString()
myProcList = getProcList()
for line in myProcList[1:]:
    print(line)
    count = len(myProcList)
print(f"The number of processes of this list is: {count}")          
