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
   
