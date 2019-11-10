import smtplib
from email.message import EmailMessage 
import os

def send_email(subject, content):
  login_pass = os.environ.get("GMAILPASS")
  login_email = os.environ.get("GMAIL")
  msg = EmailMessage()
  msg['From'] = login_email
  msg['To'] = "fkmkfkmasum41@gmail.com"
  msg['Subject'] = subject
  msg.set_content(content)


  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

    smtp.login(login_email, login_pass)
    smtp.send_message(msg)
    print(f"""
      message sent to {msg['To']}
      """)


