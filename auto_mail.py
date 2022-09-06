import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

email_sender = 'fabiomailtest432681@gmail.com'
email_password = os.environ.get('EMAIL_PASSWORD')
print(email_password)
email_receiver = 'fabiosupremo123@gmail.com'

subject = "Automated Emails"
body = """
Hello!
I used your email as a test for my new application. You should feel honored!
Well, if you are seeing this message, then I am succesful. I don't have anything
useful to say though, so you should probably ignore this mail.
"""