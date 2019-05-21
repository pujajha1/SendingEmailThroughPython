''' This is a Python Program which
will send email to recipient address'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendmail(htmltext, subject, from_address, to_address):

    print("I AM INSIDE sendmail method")

    msg = MIMEMultipart('related')
    msg['Subject'] = subject
    msg['From'] = from_address
    msg['To'] = (', ').join(to_address.split(','))
    # msg['To'] = to_address
    # Define alternative plaintext
    ptmsg = MIMEMultipart('alternative')
    msg.attach(ptmsg)
    ptmsg.attach(
        MIMEText(
            "nYou are seeing this message because your E-mail client has e-mail rendering set to Plain Text. "
            , 'text'))
    # Define HTML Message
    HTMLText = MIMEText(htmltext, 'html')
    # Attach HTML
    ptmsg.attach(HTMLText)
    s = smtplib.SMTP('localhost')
    s.sendmail(from_address, to_address, msg.as_string())
    
text="IT is working fine"
htmltext = "<tr><td class='r'>{0}</tr>".format(text)
from_address = "pujajha5912@gmail.com"
to_address = "pujajha5912@gmail.com"
subject = "Sending Email"
sendmail(htmltext, subject, from_address, to_address)
