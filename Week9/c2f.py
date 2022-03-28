#!/usr/bin/env

def convert_cel_to_far():
    cdegrees =  input(f"Please enter the temperature you want convert to farenheit degrees: ")
    celdegrees = int(cdegrees)
    return celdegrees
    
celsdegrees = convert_cel_to_far()

fdegrees = ((celsdegrees * 9/5) + 32)
print(fdegrees)
