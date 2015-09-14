#what this script will do

-will create a file "correct-emails.txt" with valid email  in same location where the script is.

-will create a file "fake-email.txt" with fake emails  in same location where the script is.

#how to run the script 

./email_validate.py <your email file>

eg. 

./email_validate.py  emailcollection.txt


#Reference

validate emails using python library
https://pypi.python.org/pypi/validate_email

#INSTALLATION

First, you must do:

pip install validate_email

pip install pyDNS

Extra

#For check the domain mx and verify email exits you must have the pyDNS package installed:

USAGE

#Basic usage:

from validate_email import validate_email
is_valid = validate_email('example@example.com')

#Checking domain has SMTP Server

Check if the host has SMTP Server:

from validate_email import validate_email
is_valid = validate_email('example@example.com',check_mx=True)

#Verify email exists

Check if the host has SMTP Server and the email really exists:

from validate_email import validate_email
is_valid = validate_email('example@example.com',verify=True)


