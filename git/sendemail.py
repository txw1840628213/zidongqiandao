import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import time
import os
def send_email(i,ips,subject):
    ips=str(ips)
    Email = os.getenv('EMAILS').split('\r\n')
    # Change to your own account information
    # Account Information
    to            = Email[i]          # Email to send to.
    mail_user     = os.getenv('MAIL_USER')           # Email to send from.
    mail_password = os.getenv('MAIL_PASSWORD')          # Email password.
    smtpserver    = smtplib.SMTP('smtp.qq.com') # Server to use.

    smtpserver.ehlo()                            # Says 'hello' to the server
    smtpserver.starttls()                        # Start TLS encryption
    smtpserver.ehlo()
    smtpserver.login(mail_user, mail_password)   # Log in to server
    today = datetime.date.today()                # Get current time/date
    

    # Creates the text, subject, 'from', and 'to' of the message.
    msg = MIMEText(ips)
    msg['Subject'] = subject+'—%s' % today.strftime('%b %d %Y')
    msg['From'] = mail_user
    msg['To'] = to
    print('邮件发送'+str(i))
    # Sends the message
    smtpserver.sendmail(mail_user, [to], msg.as_string())

    # Closes the smtp server.
    smtpserver.quit()
    print('邮件发送成功')
