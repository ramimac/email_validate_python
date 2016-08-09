#!/usr/bin/python
from validate_email import validate_email
import sys
if len(sys.argv) != 2:
    print "Please choose an Email list file"
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
                with open('correct-emails.txt','a') as truemail:
                    truemail.write(line)
            else:
                with open('fake-emails.txt','a') as falseemail:
                    falseemail.write(line)
               # pass
