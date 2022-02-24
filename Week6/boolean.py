#!/usr/bin/env python3
import sys
# This script test different expressions:

#1,-
print("1.- Expression "" True and True " ", gives a result of:")
print(True and True)
print(" ")
#2.-
print("2.- Expression "" False and True " ", gives a result of:")
print(False and True)
print(" ")
#3.-
print("3.- Expression "" 1 == 1 and 2 == 1" ", gives a result of:")
print(1 == 1 and 2 == 1)
print(" ")
#4,-
print("4.- Expression "" 0" ", gives a result of:")
print(0)
print(" ")
#5.-
print("5.- Expression "" “”" ", gives a result of:")
print("“”")
print(" ")
#6.-
print("6.- Expression 0.0" ", gives a result of:")
print(0.0)
print(" ")
#7.-
print("7.- Expression not 0" ", gives a result of:")
print(not 0)
print(" ")
#8.-
print("8.- Expression test == test , gives a result of:")
print("test" == "test")
print(" ")
#9.-
print("9.- Expression 1 == 1 or 2 != 1" ", gives a result of:")
print(1 == 1 or 2 != 1)
print(" ")
#10._
print("10.- Expression True and 1 == 1" ", gives a result of:")
print(True and 1 == 1)
print(" ")
#11.-
print("11.- Expression False and 0 != 0" ", gives a result of:")
print(False and 0 != 0)
print(" ")
#12._
print("12.- Expression True or 1 == 1" ", gives a result of:")
print(True or 1 == 1)
print(" ")
#13.-
print("13.- Expression test == testing, gives a result of:")
print("test" == "testing")
print(" ")
#14,-
print("14.- Expression  != 0 and 2 == 1" ", gives a result of:")
print(1 != 0 and 2 == 1)
print(" ")
#15.-
print("15.- Expression test != testing, gives a result of:")
print("test" != "testing")
print(" ")
#16.-
print("16.- Expression test == 1" ", gives a result of:")
print("test" == 1)
print(" ")
#17.-
print("17.- 1 == 1 and not (testing == 1 or 1 == 0))" ", results in:")
print(1 == 1 and not ("testing" == 1 or 1 == 0))
print(" ")
#18.-
print("18.- chunky == bacon and not (3 == 4 or 3 == 3))" ", results in:")
print("chunky" == "bacon" and not (3 == 4 or 3 == 3))
print(" ")
#19.-
print("19.-  3 == 3 and not (testing == testing or Python == Fun) gives:")
print(3 == 3 and not ("testing" == "testing" or "Python" == "Fun"))
