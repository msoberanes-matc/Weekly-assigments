#!/usr/bin/env python3
import sys

hFile = open("/etc/passwd", "r")

#1,-

fileContent = hFile.read()
#print(fileContent)
#print(type(fileContent))
print("This is the total size of this file in bytes:")
print(len(fileContent))
print("The len function gives the size of the file in bytes, including the new line.")
print("Use read() function when you want to read the entire contents of a file and put into a single string.")
hFile.close()

#2,-

hFile = open("/etc/passwd", "r")

fileContent = hFile.readlines()
#print(fileContent)
#print(type(fileContent))
print("This is the total number of items in this list contained in this file:")
print(len(fileContent))
print("The len function gives the number of items in this list.")
print("Use readlines() function when you want to read the entire contents of a file and put into a list.")
hFile.close()

#3._

 #!/usr/bin/env python3
count = 0 
with open("/etc/passwd", "rb") as hFile:
    line = hFile.read(20)
    
    while line:
        
        lineInfo = f"{count:03d}) [Length:{len(line):03d}] [Index: {hFile.tell():04d}] {line}"
#        print(lineInfo.strip())
        for line in hFile: pass  
        print("This is the total length of this file:")
        print(hFile.tell())
        count += 1
        line = hFile.readline()        
print("Use readline() function when you want to return one line at a time and store it during each iteration of the loop.")
       

