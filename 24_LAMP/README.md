# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 1 Hour

### Prerequisites:

- Verfied DigitalOcean Account
  - Requires a credit card or paypal account to be link to the account

### 1. Create a Droplet ###


    1. Choose an Image/OS: Ubuntu 20.04 LTS
    2. Choose a Plan: Basic
    3. CPU Options: Regular Intel with SSD; $5/mo plan
    4. Datacenter Region: Somewhere Close (New York)
    5. Authentication: Preferably SSH keys, but can start with password and then transition
    6. Additional Options: None
    7. Hostname: Something Portending Greatness

### 2. Connect to Droplet: ###

  Go to droplet in browser and use the console  

  or in the terminal:
  ```
  $ ssh root@<ipv4>
  ```
  Replace `ipv4` with that of your droplet.

### 3. Creating a New User ###
  ```
  # adduser <username>
  ```
  Replace `username` with your desired username.  
  It will prompt you to create a password linked to your username to ssh into the droplet.  
  It will then prompt you to add information associated to that account. You can choose to leave it blank (just hit Enter for each prompt)

  Now to give the account the power to use the sudo command
  ```
  # usermod -aG sudo <username>
  ```
  Now logout of root and connect through the new user you created.  
  ```
  # logout
  $ ssh <username>@<ipv4>
  ```

### 4. Disabling Root SSH ###
  ```
  $ sudo nano /etc/ssh/sshd_config
  ```
  Within the file, changed `PermitRootLogin` from `yes` to `no`
  ```
  $ sudo service ssh restart
  ```

###5. Enabling the Firewall ###
  ```
  $ sudo ufw allow ssh
  $ sudo ufw enable
  ```
  To check that the firewall enabled use:
  ```
  $ sudo ufw status
  ```

### 6. Install Apache2 ###

  To Install Apache2:
  ```
  $ sudo apt update
  $ sudo apt install apache2
  $ sudo ufw allow in "Apache"
  ```
  To make sure that everything is working:
  ```
  $ sudo ufw status
  ```
  Which should return:
  ```
  Status: active

  To                         Action      From
  --                         ------      ----
  22/tcp                     ALLOW       Anywhere
  Apache                     ALLOW       Anywhere
  22/tcp (v6)                ALLOW       Anywhere (v6)
  Apache (v6)                ALLOW       Anywhere (v6)
  ```

### 7. Virtual Host Setup ###

  ```
  $ sudo mkdir /var/www/<domain_name>
  $ sudo chown -R $USER:$USER /var/www/<domain_name>
  ```
  Replace <domain_name> with your domain name
  ```
  $ sudo nano /etc/apache2/sites-available/<domain_name>.conf
  ```
  In the `<domain_name>.conf` file:
  ```
  <VirtualHost *:80>
    ServerName <domain_name>
    ServerAlias www.<domain_name>
    ServerAdmin webmaster@localhost
    DocumentRoot /var/www/<domain_name>
    ErrorLog ${APACHE_LOG_DIR}/error.log
    CustomLog ${APACHE_LOG_DIR}/access.log combined
  </VirtualHost>
  ```
  Once again replaing <domain_name> with your domain name  
  To activate the host:
  ```
  $ sudo a2ensite <domain_name>
  ```
  You may need to disable the default virtual host
  ```
  $ sudo a2dissite 000-default
  ```
  Then check for syntax errors and reload apache2:
  ```
  $ sudo apachectl configtest
  $ sudo systemctl reload apache2
  ```

### 8. Create a temporary HTML file for the site ###
  ```
  $ nano /var/www/<domain_name>/index.html
  ```
  Fill the HTML file with what you want as a standin.  
  Example:
  ```
  <html>
    <head>
      <title>Temporary Page</title>
    </head>
    <body>
      <h1>Hello!</h1>
    </body>
  </html>
  ```
  Visit the site at:
  `http://<domain_name>` or `http://<ipv4>`

### 9. Some Packages and SQLite3 ###
  To install SQLite3:
  ```
  $ sudo apt install sqlite3
  ```
  Some Python packages you will need:
  ```
  $ sudo apt install python3-pip
  $ sudo apt install python-venv
  ```

### Resources
* https://www.digitalocean.com/community/tutorials/how-to-install-linux-apache-mysql-php-lamp-stack-on-ubuntu-20-04
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://www.digitalocean.com/community/questions/secure-ubuntu-server-for-non-root-user-using-only-ssh-keys?answer=22286
* https://www.digitalocean.com/community/tutorials/how-to-create-a-new-sudo-enabled-user-on-ubuntu-20-04-quickstart
* https://www.digitalocean.com/docs/droplets/how-to/
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh?answer=44730
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/
* https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/
* https://www.digitalocean.com/community/questions/how-can-i-disable-ssh-login-for-a-root-user-i-am-the-account-owner

---

Accurate as of (last update): 2022-01-16

#### Contributors:  
Clyde "Thluffy" Sinclair  
Topher Mykolyk, pd0  
Thomas Yu, pd1  

_Note: the two spaces after each name are important! ( <--burn after reading)  _
