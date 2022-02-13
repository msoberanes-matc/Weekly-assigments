#!/usr/bin/env python3
import sys

#1. - Create the following variables in your script:

varString = "Here is a nice string to slice"
varList = [ "Here", "is", "a", "nice", "list", "to", "slice" ]  

#2.- Using slicing on varString create the following output using one line of code:
# a) 'e is a nice string to slice'

print(varString[3:30])

# b) 'Her'

print(varString[0:3])

# c) 'e is a ni'

print(varString[3:12])

# d) 'Hr sanc tigt lc'	

print(varString[0:30:2])
# e) 'ecils ot gnirts ecin a si ereH'

print(varString[::-1])

#3,-Using slicing on varList create the following output using one line of code:

# a) ['slice', 'to', 'list', 'nice', 'a', 'is', 'Here']

print(varList[::-1])

# b) ['a', 'is', 'Here']

print(varList[2::-1])

# c)['a', 'nice']

print(varList[2:4])

# d)['Here', 'nice', 'slice']

print(varList[0:7:3])

# e) ['is', 'a', 'nice', 'list', 'to', 'slice']

print(varList[1:7])

#4.- Using a for loop, print out each element of varString one line at a time.

for x in varString:
     print(x)
     
#5.- Using a for loop, print out each element of varList one line at a time.

for x in varList:
     print(x)




