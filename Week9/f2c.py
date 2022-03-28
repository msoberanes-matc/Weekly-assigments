#!/usr/bin/env python3

def convert_far_to_cel():
    fdegrees =  input("Please enter the temperature you want convert to celsius degrees: ")
    fardegrees = int(fdegrees)
    return fardegrees
    
farhdegrees = convert_far_to_cel()

cdegrees = ((farhdegrees - 32) * 5/9)
print(cdegrees)
