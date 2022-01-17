# how-to :: CREATE A DIGITAL OCEAN DROPLET WITH UBUNTU AND APACHE
---
## Overview
Guide to creating an ubuntu 20.04 virtual machine ("droplet") and installing Apache2 web server on it.

### Estimated Time Cost: 1 Hour

### Prerequisites:

- Verfied DigitalOcean Account
  - Requires a credit card or paypal account to be link to the account

1. Create a Droplet
    1. Choose an Image/OS: Ubuntu 20.04 LTS
    2. Choose a Plan: Basic
    3. CPU Options: Regular Intel with SSD; $5/mo plan
    4. Datacenter Region: Somewhere Close (New York)
    5. Authentication: Preferably SSH keys, but can start with password and then transition
    6. Additional Options: None
    7. Hostname: Something Portending Greatness

2. Connect to Droplet:  
  Go to droplet in browser and use the console  

  or in the terminal:
  ```
  $ ssh root@<ipv4>
  ```
  Replace `ipv4` with that of your droplet.

3. Creating a New User
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

4. Disabling Root SSH
  ```
  $ sudo nano /etc/ssh/sshd_config
  ```
  Within the file, changed `PermitRootLogin` from `yes` to `no`
  ```
  $ sudo service ssh restart
  ```

5. Enabling the Firewall
  ```
  $ sudo ufw allow ssh
  $ sudo ufw enable
  ```
  To check that the firewall enabled use:
  ```
  $ sudo ufw status
  ```
  
6. Install Apache2


Step, with
    ```
    generic code block or terminal command
    ```
   and/or...
    ```javascript
    var foo = "this that JS tho";
    ```
   and/or...
    ```python
    print("this that Python tho")
    ```
   and/or...
1. Step, with [hyperlink](https://xkcd.com)s...


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

Accurate as of (last update): 2022-01-11

#### Contributors:  
Clyde "Thluffy" Sinclair  
Topher Mykolyk, pd0  
Thomas Yu, pd1  

_Note: the two spaces after each name are important! ( <--burn after reading)  _
