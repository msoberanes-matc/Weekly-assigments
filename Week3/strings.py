#!/usr/bin/env python3
import sys

varRed = "Red"
varGreen = "Green"
varBlue = "Blue"
varName = "Timmy"
varLoot = 10.4516295

#1. Hello Timmy 
print(f"Hello {varName}")
#Hello Timmy

#2. Red-Green-Blue
print(f"{varRed}-{varGreen}-{varBlue}")
#Red-Green-Blue

#3. Is this green or blue?
print(f"Is this {varGreen.lower()} or {varBlue.lower()}?")
#Is this green or blue

#4. My name is TIMMY
print(f"My name is {varName.upper()}")
#My name is TIMMY

#5. [++Red++]
print(f"[{varRed:+^7s}]")
#[++Red++]

#6. [green==]
print(f"[{varGreen.lower():=<7s}]")
#[green==]

#7. [*****blue]
print(f"[{varBlue.lower():*>9s}]")
#[*****blue]

#8. BlueBlueBlueBlueBlueBlueBlueBlueBlueBlue
print(f"{varBlue*10}")
#BlueBlueBlueBlueBlueBlueBlueBlueBlueBlue

#9. 10.4516295
print(f"{varLoot}")
#10.4516295

#10. 10.5
print(f"{varLoot:0.1f}")
#10.5

#11. I have $10.45
print(f"I have {varLoot:0.2f}")
#I have 10.45

#12. [$$$Red$$$$][$$Green$$$][$$$Blue$$$]
print(f"[{varRed:$^10s}] [{varGreen:$^10s}] [{varBlue:$^10s}]")
#[$$$Red$$$$] [$$Green$$$] [$$$Blue$$$]

#13. [ deR  ][ Green  ][ eulB ]
print(f"[{varRed[::-1]: ^8s}] [{varGreen: ^8s}] [{varBlue[::-1]: ^8s}]")
#[  deR   ] [ Green  ] [  eulB  ]

#14. First Color:[Red]Second Color:[Green] Third Color:[Blue]
print(f"First Color:[{varRed}] Second Color:[{varGreen}] Third Color:[{varBlue}]")
#First Color:[Red] Second Color:[Green] Third Color:[Blue]


