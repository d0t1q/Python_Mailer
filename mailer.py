#!/usr/bin/python
#Bell and Telus and most likely other gateways have a threshold that will ban 
#you for sending to quickly put in a 45 second wait timer to stop this ban?
#Rogers wont accept mail at this time

import sys
import smtplib
import time
from  email.mime.text import MIMEText


def help():
    print '\nno'

def send_mail(me_, you_, times_repeat_):
    msg = MIMEText("""Youre home is on fire""",)
    msg['Subject'] = ''
    msg['From'] = me_
    msg['To'] = you_
    for x in range(0, times_repeat_):
        s = smtplib.SMTP('localhost')
        s.sendmail(me_,[you_], msg.as_string())
        s.quit()
        print 'Sucessful ', x+1, ' emails sent of ', times_repeat_
        (x)
        if times_repeat_ > 1 :
            time.sleep(45)#sleeps for 45s
try:

    def main():
    #this will catch the system arguments into the args var
        args = sys.argv[1:]
        if not args:
            print """
        Usage: script_name.py [OPTION]

        -h or --help

        -e [you@domain.com] [receipent@domain.com]
        after you type in the required information you will be propmted to
        times to repeat

        """
            sys.exit(1)
      #send to the help function
        if sys.argv[1].lower() == "-h" or sys.argv[1].lower() == "--help":
            help()
      #start email var capture
        if sys.argv[1].lower() == "-e":
            me_ = sys.argv[2]
            you_ = sys.argv[3]
            times_repeat_ = input ("How many times to repeat: ")
            send_mail(me_, you_, times_repeat_)

except KeyboardInterrupt:
    sys.exit()

#call the main function
if __name__=='__main__':
    main()

