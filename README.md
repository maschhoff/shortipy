# shortipy
URL Shortener in python based on flask

# preview

![shortipy](https://i.ibb.co/WFtD0nc/sp.jpg)

# features

* create shortlink by enter a domain to the input field. and you will get a 4 digit number
* use shortlink by enter this shortlink to the input field or
* use shortlink yourdomain.com/1234

# run as docker

## info

* pull from dockerhub knex666/shortipy 
* volume mount container path /shortipy/data to persist your DB.
* shortipy runs on port 4321: map the port 4321 to any port you like
* or use a reverse proxy
* use /start.sh as entrypoint


## run

   docker run -d --name='shortipy' -v '/home/user/shortipy':'/shortipy/data':'rw' 'knex666/shortipy' /start.sh

# run on system

* install python >3
* pull from github
* python -m pip install -r requirements.txt
* python shorti.py or run uwsgi app.ini

# donate
Buy me a Pizza -> https://www.buymeacoffee.com/maschhoff
