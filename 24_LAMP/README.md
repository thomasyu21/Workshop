# how-to :: A COMPREHENSIVE GUIDE TO CREATING A DIGITAL OCEAN DROPLET WITH UBUNTU, FLASK, AND APACHE ON LINUX MACHINES
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it, as well as being able to serve Flask applications on linux-based machines.

### Estimated Time Cost: 30 Minutes

### Prerequisites:

- These instructions assume that you're creating your droplet from the school's CS Lab machines.
- You should have your DigitalOcean account have a balance of $100 already.
- To get into the school's CS labs, just
  ```
    ssh <stuy user>@149.89.160.1XX <XX being a number from 01-30>
  ```

### Instructions

#### 1.  Create Your SSH Keys  
* In your terminal, type
    ```
    ssh-keygen
    ```
    * Make sure that when prompted for a ```file in which to save the key```, you just press ENTER so it defaults to ```id_rsa```. If there is already an ```id_rsa```, then save it as something else (use a creative name or something).
* Then
    ```
    cd /home/students/2022/<stuy user>/.ssh/
    ```
* Then
    ```
    cat id_rsa.pub
    ```
* Copy the contents of it from ```ssh-rsa``` to (and including) ```<stuy user>@cslab<number>```.
* Navigate to DigitalOcean and login.
    * Go to ```Settings``` >> ```Security``` >> ```Add SSH Key``` >> and paste your public SSH Key into the field. Name it something descriptive and save.
    * Click the green ```Create``` >> ```Droplets``` >> with the settings of
        * Ubuntu
        * Basic
        * Regular Intel with SSD, $5/mo
        * NY datacenter region
        * SSH Key Authentication
        * Use a creative hostname
    * Create Droplet

#### 2.  Setting Up SSH Into Your Droplets  
* In your terminal, start by SSHing into the created droplet.
    ```
    ssh root@<your_server_ip>
    ```
* Then  
    ```
    adduser <your_username>
    ```
    * <your_username> can be any username you want, just make sure it's something you remember and it's consistent.
* Then  
    ```
    usermod -aG sudo <your_username>
    ```
* Then  
    ```
    ufw allow OpenSSH
    ```
* Then  
    ```
    ufw enable
    ```
* Then  
    ```   
    rsync --archive --chown=<your_username>:<your_username> ~/.ssh /home/<your_username>
    ```

#### As root user, try to ```ssh <your_username>@<your_server_ip>``` into your user account. 
#### Oh no! I get a ```Permission denied (publickey)``` when I ```ssh <your_username>@<your_server_ip>```, what do I do?
* If you get this issue, try to follow these steps, otherwise, skip to the next step.  
* Open a new terminal session and SSH into a CS Lab (if you aren't in there already).  
* Try  
    ```
    ssh-copy-id -f <your_username>@<your_server_ip>
    ```
    * If it says that the ```Number of key(s) added: 1```, or something similar, then you're in the clear.
* And THEN  
* Go back into the first terminal (the one with root access) and type  
    ```
    sudo nano /etc/ssh/sshd_config
    ```
* Then, search for ```PasswordAuthentication```  
    ```
    PasswordAuthentication no
    ```
    * Should be rewritten as:
    ```
    PasswordAuthentication yes
    ```
    * Save and exit.
* Then  
    ```
    sudo service sshd reload
    ```
* Then   
    ```
    ssh <your_username>@<your_server_ip>
    ```
    * It should prompt you for your password, which you should've remembered, so time that in and it should let you in.
* LAST, BUT NOT LEAST. Exit your user account back into your root account. We're going to disable root access from the user account.
    ```
    sudo nano /etc/ssh/sshd_config
    ```
* Then  
    ```
    PermitRootLogin yes
    ```
    * Should be rewritten as:
    ```
    PermitRootLogin no
    ```   
    * Save and exit.
* Then  
    ```
    sudo service ssh restart
    ```
* If that's successful, exit all connections until you are back into your CS Lab terminal.  

#### 3. Installing Apache2; First, SSH back into your user account.  
    ```
    ssh <your_username>@<your_server_ip>
    ```
* Then   
    ```
    sudo apt update
    ```
    * You will often need to update and upgrade, so run those commands often!
* Then   
    ```
    sudo apt install apache2
    ```
* Then   
    ```
    sudo ufw allow 'Apache'
    ```
* Then   
    ```
    sudo ufw allow 5000
    ```
* If you do ```sudo ufw status```, you SHOULD see this:
    ```
    Status: active
    To                         Action      From
    --                         ------      ----
    OpenSSH                    ALLOW       Anywhere
    Apache                     ALLOW       Anywhere
    5000                       ALLOW       Anywhere
    OpenSSH (v6)               ALLOW       Anywhere (v6)
    Apache (v6)                ALLOW       Anywhere (v6)
    5000 (v6)                  ALLOW       Anywhere (v6)
    ```
* Open your web browser and paste your server ip into the URL bar. It should display the Ubuntu web page telling you that it works! Congratulations. We're not quite done yet, however.

#### 4. Installing Flask and Deploying Flask
* In your terminal, type
    ```
    cd /var/www/
    ```
* Then  
    ```
    sudo apt-get update
    ```
* Then  
    ```
    sudo apt-get upgrade
    ```
* Then  
    ```
    sudo apt-get install libapache2-mod-wsgi python3-dev
    ```
* Then  
    ```
    sudo apt-get install python3-pip
    ```
* Then  
    ```
    sudo apt-get install python3-venv
    ```
* Then
    ```
    sudo pip install virtualenv
    ```
* Then  
    ```
    sudo a2enmod wsgi
    ```
* Then  
    ``` 
    sudo mkdir <directory_name>
    ```
* Then  
    ```
    cd <directory_name>
    ```
* Then  
    ```
    python3.8 -m venv env
    ```
* Then  
    ``` 
    source env/bin/activate
    ```
* Then  
    ``` 
    sudo pip3 install flask
    ```
* Then  
    ```
    sudo nano __init__.py
    ```
* The sample code to run:
    ```python
    from flask import Flask
    app = Flask(__name__)

    @app.route("/")
    def index():
        return "<h1>Hi there!</h1>"

    if __name__ == "__main__":
        app.run(host='0.0.0.0')
    ```  
* Run it!
    ```
    python3 __init__.py
    ```
* You should see:
    ```
     * Serving Flask app '__init__' (lazy loading)
     * Environment: production
       WARNING: This is a development server. Do not use it in a production deployment.
       Use a production WSGI server instead.
     * Debug mode: off
     * Running on all addresses.
       WARNING: This is a development server. Do not use it in a production deployment.
     * Running on http://<your_server_ip>:5000/ (Press CTRL+C to quit)
    ```
* Paste that address into your URL bar and you should see that it has successfully run.

#### Congratulations! You have successfully setup your droplet!

### Resources
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh
* https://www.digitalocean.com/community/questions/secure-ubuntu-server-for-non-root-user-using-only-ssh-keys?answer=22286
* https://www.digitalocean.com/docs/droplets/how-to/
* https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh?answer=44730
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/putty/
* https://www.digitalocean.com/docs/droplets/how-to/add-ssh-keys/create-with-openssh/
* https://www.digitalocean.com/docs/droplets/how-to/connect-with-ssh/openssh/
* https://pythonforundergradengineers.com/flask-app-on-digital-ocean.html
---

Accurate as of (last update): 2022-01-17

#### Contributors:  
Jonathan Wu, pd2  
Thomas Yu, pd2  
Mark Zhu, pd2  
