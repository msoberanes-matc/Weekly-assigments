#!/usr/bin/env python3
import json
import requests
import argparse

parser = argparse.ArgumentParser(description='Enter IP Address')
parser.add_argument('-ip', metavar='ip', type=str, required=True, help='Enter an ip address')

args = parser.parse_args()
ip = args.ip
varString1 = "https://ipinfo.io/"
varString2 = args.ip
varString3 = "/json"

url = varString1 + varString2 + varString3
response = requests.get(url)
myDict = json.loads(response.text)

for key in myDict:
    print(f"{key} : {myDict[key]}")     
  
