# shortipy
URL Shortener in python based on flask

# preview

![shortipy](https://i.ibb.co/WFtD0nc/sp.jpg)

# info

* volume mount container path /shortipy/data to persist your DB.
* shortipy runs on port 4321: map the port 4321 to any port you like
* use /start.sh as entrypoint

# run

   docker run -d --name='shortipy' -v '/home/user/shortipy':'/shortipy/data':'rw' 'knex666/shortipy' /start.sh


# donate
Buy me a Pizza -> https://www.buymeacoffee.com/maschhoff
