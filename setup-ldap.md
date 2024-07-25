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

Use "sudo dpkg-reconfigure slapd" and follow the setup instructions.
Follow the interactive setup 
Set the LDAP domain (e.g., authentication.local), as well as the LDAP administrator password.

4.) Enter the LDAP Account Manager

Navigate to http:// IP of your Server/lam

Select LAM configuration, and select edit server profiles. The default login for lam is also lam.

Navigate to server settings and modify list of valid users. Should read "cn=admin,dc=authentication,dc=local". Ensure LAM is set to the correct timezone, and modify tree view under tool settings to say "dc=authentication,dc=local".

Change the default password under profile password. This will be the password for the lam account, and the password set in step 3 is the admin password account. Ensure you save all changes.

Now you should be able to log in to the admin account and create groups/users.




## **OPTIONAL** - Set up the LDAP Account Manager

Enter "sudo apt install ldap-account-manager"
Verify LDAP is running by entering "sudo systemctl status slapd"


For additional information, official Ubuntu documentation and OpenLDAP can be found at:
https://ubuntu.com/server/docs
