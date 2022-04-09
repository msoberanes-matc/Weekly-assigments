#!/usr/bin/env python3
import argparse
import sys
parser = argparse.ArgumentParser(description="This is <your name her> script")

#parser.add_argument("-h", "--help", dest="helpstring", help="show this help mes#sage and exit")

parser.add_argument("-m", dest="basic", help="Enter some text")

parser.add_argument('-i'
                    ,'--integer'
                    , dest='varInteger'
                    , metavar="[an integer]", default=777, type=int, help='<required> Enter a simple Integer')

parser.add_argument('-d', '--float', dest='varFloat', metavar='[a float]', default=10.6, type=float, help='Enter a simple Float')

parser.add_argument('-s', '--string', dest='varString', metavar='[a string]', default='hello', type=str, help='Enter a simple String')

parser.add_argument('-l'
                    , dest='varlist'
                    , nargs=3
                    , metavar="[strings]", default='[1, 2, 3]', help='Enter a list of strings (space delimited)')

parser.add_argument('-t', '--set-true', dest='varBool', default=False, action='store_true', help='Toggle from default False to True')

parser.add_argument('-f', '--setfalse', dest='varBoolf', default=True, action='store_false', help='Toggle from default True to False')

parser.add_argument('-v', dest='--version', help='show programs version number and exit')

#parser.add_argument('--three', nargs=3)
#parser.add_argument('--optional', nargs='?')
#parser.add_argument('--all', nargs='*', dest='all')
#parser.add_argument('--one-or-more', nargs='+')

#parser = argparse.ArgumentParser(description='Creating a parser to add arguments')
#parser.add_argument('-l', dest='varlist', action='append', help='Specify a list of things')

#if len(sys.argv) == 1:
print(parser.print_help())
#print((parser.parse_args()).varInteger)
#print((parser.parse_args()).varString)
#print((parser.parse_args()).varFloat)
#print((parser.parse_args()).varlist)
results=parser.parse_args()
print(results.varInteger)
print(results.varString)
print(results.varFloat)
print(results.varlist)

#print(results)

