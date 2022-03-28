#!/usr/bin/env
cel = "celsius"
far = "fahrenheit"
def ask_measure_type():
    degrees_type = input("Please enter fahrenheit or celsius as measure for conversion: ")
    return degrees_type
    
type_degrees = ask_measure_type()
if cel == type_degrees: 
    import c2f
if far == type_degrees:            
    import f2c
