# how-to :: DEPLOY A FLASK APP ON APACHE2
---
## Overview
Flask is not built to serve -- on its own -- persistent or high-traffic sites. Apache, on the other hand, is. Luckily, Apache can be configured to use its industrial-grade machinery to serve Flask and other apps. Deploying your Flask app to an Apache2 server will allow anyone on the web to access your app at any time.

### Estimated Time Cost: 30 minutes

### Prerequisites:

- Please have your server properly setup with apache2 and everything from K24.
- We're going to create a very simple flask app from scratch and run it.

##### 1. Getting Ready
* In the terminal, type
  ```
  sudo apt-get install libapache2-mod-wsgi-py3 python-dev  
  ```
* Then  
  ```
  sudo a2enmod wsgi
  ```
* Then  
  ```
  cd /var/www/
  ```
* Then  
  ```
  sudo mkdir FirstApp
  ```
* Then  
  ```
  sudo chown -R $<USER>:$<USER> FirstApp
  ```
* Then  
  ```
  sudo chmod -R 777 FirstApp
  ```
Make your directory look something like this:  
FirstApp  
├── FirstApp  
--------├── __init__.py  
--------├── static  
--------└── templates  
* Then  
  ```
  sudo apt-get install python3-pip
  ```
* Then  
  ```
  sudo pip install virtualenv
  ```  
* Then (it doesn't matter where)
  ```
  python3.8 -m venv env
  ```
* Then  
  ```
  . env/bin/activate
  ```
* Then  
  ```
  pip install Flask
  ```

##### Setting up config files.
* In the terminal, type
  ```
  sudo nano /etc/apache2/sites-available/FirstApp.conf
  ```
  * Inside it, copy and paste this (with the appropriate substitutions)
  ```
  <VirtualHost *:80>
  	ServerName <IP Address>
  	ServerAdmin user@ip_address
  	WSGIScriptAlias / /var/www/FirstApp/FirstApp.wsgi
  	<Directory /var/www/FirstApp/FirstApp/>
  		Order allow,deny
  		Allow from all
  	</Directory>
  	Alias /static /var/www/FirstApp/FirstApp/static
  	<Directory /var/www/FirstApp/FirstApp/static>
  		Order allow,deny
  		Allow from all
  	</Directory>
  	ErrorLog ${APACHE_LOG_DIR}/error.log
  	LogLevel warn
  	CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
  ```
* Then
  ```
  sudo a2ensite FirstApp.conf
  ```
* Then
  ```
  sudo a2dissite 000-default.conf
  ```
##### Setting up WSGI
* In the terminal, type
  ```
  sudo nano /var/www/FirstApp/FirstApp.wsgi
  ```
  * Inside it, type:
  ```
  #!/usr/bin/python
  import sys
  import logging
  import os
  logging.basicConfig(stream=sys.stderr)
  sys.path.insert(0,"/var/www/FirstApp/")
  sys.path.append("/var/www/FirstApp/FirstApp/")

  from FirstApp import app as application
  application.secret_key = os.urandom(32)
  ```
* Lastly,
  ```
  sudo service apache2 restart
  ```

Check it at your droplet ip.

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-deploy-a-flask-application-on-an-ubuntu-vps
---

Accurate as of (last update): 2022-01-19

#### Contributors:  
Jonathan Wu, pd2  
Thomas Yu, pd2  
Mark Zhu, pd2  
