#!/bin/python
from validate_email import validate_email
import sys
if len(sys.argv) != 2:
    print "Missing Email List File"
    exit()
else:
    email_listfile=sys.argv[1]
    with open(email_listfile,'r') as email:
        for line in email.readlines():
            print "checking: ",line
            #status_mx=validate_email(line.strip(),check=True)
            #print status_mx
            status_email=validate_email(line.strip(),verify=True)
            print status_email
            if status_email == True:
                with open('corrected-emails.txt','a') as truemail:
                    truemail.write(line)
            else:
                with open('fake-emails.txt','a') as falseemail:
                    falseemail.write(line)
               # pass
