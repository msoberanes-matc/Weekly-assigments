#!/usr/bin/env python3
import requests

response = requests.get("https://notpurple.com")

if response.ok:
    with open("my_web_file.html", "w") as hFile:
        hFile.write(response.text)
else:
    print(f"There was an error")
