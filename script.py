import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os.path


def send_email():

    email_sender = input("Enter From Address  : ")
    email_recipient = input("Enter To Address :  ")
    email_subject = input("Enter Subject :  ")
    attachment_location = input("Enter File Location  :  ")
    email_message = input("Enter Message  :")
    cc = input("Enter CC  :")
    bcc = input("Enter BCC  :")
    
    recp = cc.split(",")+bcc.split(",")+[email_recipient]
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = recp
    msg['Subject'] = email_subject


    msg.attach(MIMEText(email_message, 'plain'))

    if attachment_location != '':
        filename = os.path.basename(attachment_location)
        attachment = open(attachment_location, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition',
                        "attachment; filename= %s" % filename)
        msg.attach(part)

    try:
        server = smtplib.SMTP('mail.smtp2go.com', 587)
        server.ehlo()
        server.starttls()
        server.login('username', 'password')      ## SMTP UserName and Password
        text = msg.as_string()
        server.sendmail(email_sender,recp,text)
        print('email sent')
        server.quit()
    except:
        print("SMPT server connection error")
    return True  
send_email()
