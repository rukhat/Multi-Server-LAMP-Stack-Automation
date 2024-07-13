# Setting Up LDAP on Ubuntu

This guide outlines the steps to set up an LDAP server on Ubuntu.

## Prerequisites

- Ubuntu 20.04 installed with sudo privileges
- Internet connectivity

## Installation

1.) Update package index.
 
sudo apt update

2.) Install OpenLDAP.

sudo apt install slapd ldap-utils

3.) Configure OpenLDAP.

Use "dpkg-reconfigure slapd" and follow the setup instructions.
Follow the interactive setup 
Set the LDAP domain (e.g., example.com), as well as the LDAP administrator password.

## **OPTIONAL** - Set up the LDAP Account Manager

Enter "sudo apt install ldap-account-manager"
Verify LDAP is running by entering "sudo systemctl status slapd"


For additional information, official Ubuntu documentation and OpenLDAP can be found at:
https://ubuntu.com/server/docs