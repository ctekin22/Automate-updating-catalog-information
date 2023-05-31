#! /usr/bin/env python3
import os
import requests
import json

fdict = {}
url="http://localhost/fruits/"
dir="./supplier-data/descriptions/"

for file in os.listdir(dir):
    with open(dir + file, "r") as f:
        fdict["name"]=f.readline().strip()
        fdict["weight"]=int(f.readline().strip().split(" ")[0])
        fdict["description"]=f.readline().strip()
        fdict["image_name"]=file.split(".")[0] +".jpeg"

        #print(fdict)
        res = requests.post(url,data=fdict)
        #res = requests.post(url,json=json.dumps(fdict))
    
        if not res.status_code == 201:
            print(f"error: {response.status_code}")
