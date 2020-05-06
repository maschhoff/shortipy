"""
shortipy

db - Helpers

2020 maschhoff github.com/maschhoff

"""

import json
import os

def loadDB():
        if os.path.isfile('./data/db.json'):
                res={}
                with open('./data/db.json', 'r') as fp:
                        res = json.load(fp)
                return res 
        else:
                dict={}
                dict["shortlinks"]={"1234":"https://github.com/maschhoff/shortipy"}
                writeDB(dict)
                return dict
	  

def writeDB(config):
        with open('./data/db.json', 'w') as fp:
                json.dump(config, fp)
