"""

Shortipy

2020 maschhoff github.com/maschhoff

"""

from flask import Flask, redirect, render_template, request
import logging
import jdb
import random

app = Flask(__name__)


@app.route('/')
def shorti():
	return render_template('layout.html')

@app.route('/', methods=['POST'])
def shorti_save():
	short=request.form['short']
	db=jdb.loadDB()
	if short.isdigit():
		return redirectit(short)
	else:
		if "http" not in short:
			short="https://"+short
		dbdict=db["shortlinks"]
		r = random.randint(1111,9999)
		logging.info("adding "+str(r)+" with "+short+" to db")
		dbdict[r]=short
		jdb.writeDB(db)
		return render_template('layout.html', message="Link saved: "+str(r), shorturl=str(r))

@app.route('/<string:short>')
def shorts(short):
	return redirectit(short)
	

def redirectit(short):
	#loadDB
	logging.info("load DB")
	db=jdb.loadDB()

	if short in db["shortlinks"].keys():
		logging.info("redirect to "+db["shortlinks"].get(short))
		return redirect(db["shortlinks"].get(short), code=302)
	else:
		logging.error("no url for that short")
		return render_template('layout.html', message="no url saved for that shortcode")
	


if __name__ == '__main__':
	logging.basicConfig(filename='server.log',level=logging.INFO)

	#Server start
	logging.info("start Shortipy server...")
	print("start Shortipy server...")
	print(""" 
	
 _|_  _  __|_. _   
_\| |(_)|  | ||_)\/
              |  / 

	""")

	app.run(host='0.0.0.0',port=4321,debug=False)
