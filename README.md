# CS 2080 Team-3 Project: Multi-Server LAMP Stack Automation

This project automates the setup of a multi-server LAMP (Linux, Apache, MySQL, PHP) stack using Vagrant and Ansible. It creates and configures three separate servers: one for the MySQL database, one for authentication, and one for the application.

Group Members:

* Himon Thakur
* Joel Willis
* Brianna Knight 


## Project Structure

- `Vagrantfile`: Defines the virtual machines using Vagrant.
- `playbook.yml`: Ansible playbook for provisioning the servers.
- `inventory.ini`: Inventory file for Ansible (dynamically generated by Vagrant).
- `/scripts`: Directory containing shell scripts used in the project.


## Prerequisites

- [Vagrant](https://www.vagrantup.com/downloads)
- [libvirt](https://libvirt.org/) (KVM) or [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (If you want to)
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)

## Setup

1. Clone this repository

```bash
git clone https://github.com/rukhat/Multi-Server-LAMP-Stack-Automation.git
cd multi-server-lamp-automation
```

2. Start the virtual machine

```bash
vagrant up
```

3. The Ansible playbook will run automatically to provision the servers.

## Server Details

### Database Server (db)
- Runs MySQL server
- Stores scripts table with file paths

### Authentication Server (auth)
- Runs OpenLDAP
- Contains a Python script to fetch and execute scripts from the DB server

### Application Server (app)
- Runs Apache and PHP
- Hosts a simple PHP info page

## Usage

### Accessing the Servers

You can SSH into any of the servers using:

```bash
vagrant ssh <server-name>
```

Replace `<server-name>` with `db`, `auth`, or `app`.

### Running the Script Fetcher

On the auth server, you can run the script that fetches and executes scripts from the database:

```bash
sudo python3 /usr/local/bin/fetch_and_execute_scripts.py
```

## Customization

- Modify the `Vagrantfile` to change VM configurations.
- Update `playbook.yml` to alter server setups or add new features.
- Edit the Python script on the auth server to change how scripts are fetched and executed.

## Troubleshooting

If you encounter issues:
1. Ensure all prerequisites are correctly installed.
2. Check that the IP addresses in the Vagrantfile match those in your virtual network.
3. Verify that the MySQL server is configured to accept remote connections.
4. Check firewall settings to ensure necessary ports are open.

## Contributing

Contributions to improve the project are welcome. Please follow these steps:
1. Fork the repository.
2. Create a new branch for your feature.
3. Commit your changes.
4. Push to the branch.
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/rukhat/Multi-Server-LAMP-Stack-Automation/blob/main/LICENSE) file for details.


# Some Details about the Protocols and Scripts Are Below


# LDAP and PAM Authentication Server

## Overview
This section of the project will demonstrate the setup and configuration of an LDAP server, as well as PAM (Pluggable Authentication Module). The server is capable of managing users/groups, implementing lockout policies, time-based access restrictions, and logging of authentication attempts.

## Setup Instructions

### Prerequisites
- Ubuntu 20.04
- VirtualBox/KVM
- Basic knowledge of LDAP and PAM (documentation can be found at https://help.ubuntu.com/community/PAMAuthentication and https://ubuntu.com/server/docs/install-and-configure-ldap)

### Step-by-Step Setup

1. **Install Required Packages:**

    sudo apt install apache2 php php-cgi libapache2-mod-php php-mbstring php-common php-pear slapd ldap-utils ldap-account-manager -y
   

3. **Configure LDAP:**
    - Follow the steps in `setup-ldap.md` to configure the LDAP server.

4. **Configure PAM:**
    - Follow the steps in `setup-pam.md` to integrate PAM with LDAP.

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

