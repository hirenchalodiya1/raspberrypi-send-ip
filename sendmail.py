import smtplib
from email.mime.text import MIMEText
from ip import get_ip
from datetime import datetime as dt
from decouple import config

print("[ " + dt.strftime(dt.now(), "%d-%m-%Y %H:%M:%S") + " ] IP in process..")

ethernet_interface = config("ETHNET_INTERFACE", cast=str)
wifi_interface = config("WIFI_INTERFACE", cast=str)

smtp_ssl_host = config("HOST", cast=str)  # smtp.mail.yahoo.com
smtp_ssl_port = config("PORT", cast=int)
username = config("SMTP_USERNAME", cast=str)
password = config("PASSWORD", cast=str)
sender = config("SENDER", cast=str)
targets = [config("RECEIVER", cast=str)]

text = "Raspberry PI information:\n\tEthernet(eth0): " + \
    get_ip(ethernet_interface) + "\n\tWIFI(wlan0): " + get_ip(wifi_interface)
msg = MIMEText(text)
msg['Subject'] = 'RaspBerry PI IP Address at ' \
    + dt.strftime(dt.now(), "%d-%m-%Y %H:%M:%S")
msg['From'] = sender
msg['To'] = ', '.join(targets)

server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
server.login(username, password)
server.sendmail(sender, targets, msg.as_string())
server.quit()

print("[ " + dt.strftime(dt.now(), "%d-%m-%Y %H:%M:%S") + " ] IPs sent")
