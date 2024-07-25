### `setup-pam.md`

```markdown
# Setting Up PAM with LDAP Integration

This guide explains how to configure Pluggable Authentication Modules (PAM) with LDAP integration on Ubuntu.

## Prerequisites

- Ubuntu 20.04 installed with sudo privileges
- LDAP server already configured and running

## Installation

1.) Install libpam-ldap.

Enter "sudo apt-get install libpam-ldap"

2.) Navigate to /etc/pam.d/. 

3.) Modify common-auth.

Add the following lines to the .conf file:

auth [success=1 default=ignore] pam_unix.so nullok_secure
auth required pam_ldap.so use_first_pass

4.) Modify common-account.

Add the following lines to the .conf file.

account required pam_unix.so
account sufficient pam_ldap.so

5.) Modify common-session

Add the following lines to the .conf file.

session required pam_unix.so
session optional pam_ldap.so





For any questions regarding PAM, you can access Ubuntu's official PAM documentation here:
https://help.ubuntu.com/community/PAMAuthentication
