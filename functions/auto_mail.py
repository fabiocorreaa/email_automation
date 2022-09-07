import os
from ssl import create_default_context
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from dotenv import load_dotenv


load_dotenv()
message = """
Hello!
I used your email as a test for my new application. You should feel honored!
Well, if you are seeing this message, then I am succesful. I don't have anything
useful to say though, so you should probably ignore this mail.
"""

def auto_mail(receiver, body, subject):

    em = EmailMessage()
    em['From'] = 'fabiomailtest432681@gmail.com'
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)
    em.add_alternative(f"""\
        {body}
    """, subtype='html')
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('fabiomailtest432681@gmail.com', os.environ.get('EMAIL_PASSWORD'))
        smtp.sendmail('fabiomailtest432681@gmail.com', receiver, em.as_string())

'''    host = 'smtp.gmail.com'
    port = 587
    login = 'fabiomailtest432681@gmail.com'
    email_password = os.environ.get('EMAIL_PASSWORD')

    server = smtplib.SMTP(host, port)

    server.ehlo()
    server.starttls()
    server.login(login, email_password)

    subject = "Automated Emails"

    em = MIMEMultipart()
    em['From'] = login
    em['To'] = receiver
    em['Subject'] = subject
    em.attach(MIMEText(body, 'Plain'))

    server.sendmail(em, receiver, em.as_string())

    server.quit()'''
if __name__ == '__main__':
    auto_mail('fabiosupremo123@gmail.com', message, "Check this! So cool!")