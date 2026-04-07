import smtplib, ssl
from dotenv import load_dotenv
import os

load_dotenv()

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "pilouthomas03@gmail.com"
    password = os.getenv("GMAIL_APP_PASSWORD")

    receiver = "thomasheusdens@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)