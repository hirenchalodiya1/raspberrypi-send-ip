import smtplib
from email.mime.text import MIMEText
from ip import get_ip
from datetime import datetime as dt
from decouple import config, Config, RepositoryEnv


env_config = Config(RepositoryEnv(config("ENVFILE_PATH", cast=str)))
print("[ " + dt.strftime(dt.now(), "%d-%m-%Y %H:%M:%S") + " ] IP in process..")

ethernet_interface = env_config.get("ETHNET_INTERFACE", cast=str)
wifi_interface = env_config.get("WIFI_INTERFACE", cast=str)

smtp_ssl_host = env_config.get("HOST", cast=str)  # smtp.mail.yahoo.com
smtp_ssl_port = env_config.get("PORT", cast=int)
username = env_config.get("SMTP_USERNAME", cast=str)
password = env_config.get("PASSWORD", cast=str)
sender = env_config.get("SENDER", cast=str)
targets = [env_config.get("RECEIVER", cast=str)]

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
