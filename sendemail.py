import subprocess
import smtplib
from email.mime.text import MIMEText
import datetime
import time
import os
def send_email(i,n):
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

    ips='流量签到失败，马上联系我over\n'+n+'手动签到:\nhttps://cdn.v2free.net/user/\n\n签到日志：\nhttps://jsd.cdn.zzko.cn/gh/txw1840628213/zidongqiandao@main/log.txt'

    # Creates the text, subject, 'from', and 'to' of the message.
    msg = MIMEText(ips)
    msg['Subject'] = '流量签到失败—%s' % today.strftime('%b %d %Y')
    msg['From'] = mail_user
    msg['To'] = to
    print('邮件发送'+str(i))
    # Sends the message
    smtpserver.sendmail(mail_user, [to], msg.as_string())

    # Closes the smtp server.
    smtpserver.quit()
