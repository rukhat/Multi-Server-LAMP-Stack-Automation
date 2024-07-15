# CS-2080-Team-3-Project-Multi-Server-Automation

A multi-server automation and configuration project using Vagrant, Ansible, Docker for application management, e.g.,  installing and managing the LAMP stack

Group Members:

* Himon Thakur
* Joel Willis
* Brianna Knight 






# LDAP and PAM Authentication Server

## Overview
This section of the project will demonstrate the setup and configuration of an LDAP server, as well as PAM (Pluggable Authentication Module). The server is capable of managing users/groups, implementing lockout policies, time-based access restrictions, and logging of authentication attempts.

## Setup Instructions

### Prerequisites
- Ubuntu 20.04
- VirtualBox
- Basic knowledge of LDAP and PAM (documentation can be found at https://help.ubuntu.com/community/PAMAuthentication and https://ubuntu.com/server/docs/install-and-configure-ldap)

### Step-by-Step Setup

1. **Install Required Packages:**

    sudo apt install apache2 php php-cgi libapache2-mod-php php-mbstring php-common php-pear slapd ldap-utils ldap-account-manager -y
   

3. **Configure LDAP:**
    - Follow the steps in `setup-ldap.md` to configure the LDAP server.
    - 

4. **Configure PAM:**
    - Follow the steps in `setup-pam.md` to integrate PAM with LDAP.
    - 

5. **Run Featured Scripts:**
    - Use the provided `check_time.sh` script for time-based access restrictions.
   
   
   
# Application Management Script

This project contains a script to create and run backup scripts for a database server and an authentication server. The backup scripts use `rsync` to synchronize data from these servers to a local backup directory.

## Prerequisites

- Python 3.x
- Vagrant (if running on a Vagrant VM)
- SSH access to the server or Vagrant VM

## Setup Instructions

- When initially running the backup scripts, you will need to change the address to your
    desired location.
- In the app.py note lines 19-23

        db_backup_content = """#!/bin/bash
        rsync -avz --delete vagrant@192.168.56.10:/path/to/backup/ /home/vagrant/backups/db/
        """

        auth_backup_content = """#!/bin/bash
        rsync -avz --delete vagrant@192.168.56.11:/path/to/backup/ /home/vagrant/backups/auth/
        """
        
        
- DO THE FOLLOWING
    - Change 192.168.56.10 to your database server's IP address. 
    - Change /path/to/backup/ to the actual path you want to back up from the database server.
    - Change 192.168.56.11 to your authentication server's IP address.
    - Change /path/to/backup/ to the actual path you want to back up from the authentication server.


## To utilize the Application management server:

    - To create scripts on your local machine or VM
        python3 app.py create_scripts

    - To run the database backup script
        python3 app.py backup_db

    -To run the authentication backup script
        python3 app.py backup_auth
  
    -To run the Server Performance script: 
        python3 app.py monitor <server name>

