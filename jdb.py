"""
shortipy

db - Helpers

2020 maschhoff github.com/maschhoff

"""

import json

def loadDB():
    #print("loadDB()")
    res={}
    with open('./data/db.json', 'r') as fp:
        res = json.load(fp)
    return res  

def writeDB(config):
    with open('./data/db.json', 'w') as fp:
	    json.dump(config, fp)