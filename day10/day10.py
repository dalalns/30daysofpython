#day 10 and 11 included in this only
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Can also use sendgrid to send million of emails
#Turn on the less secure apps 2. You'll get the security mail in your gmail inbox, Click Yes,it's me in that. 3. Now run your code again.
host = "smtp.gmail.com"
port = 587
username = "monikanavinshaurya@gmail.com"
password = "$Shaurya1"
from_email = username
to_email =  username

email_conn = smtplib.SMTP(host, port)
print(email_conn.ehlo())
print(email_conn.starttls())
print(email_conn.login(username, password))

the_msg = MIMEMultipart("alternative")
the_msg["Subject"] = "hello there!"
the_msg["From"] = from_email
#the_msg["To"] = to_email[0]

plain_text = "texting the message"

html_text = """
<html>
<head></head>
<body><p>testing this email <a href="https://www.facebook.com/">fb</a></p></body>
</html>
"""

part_1 = MIMEText(plain_text, 'plain')
part_2 = MIMEText(html_text, 'html')

the_msg.attach(part_1)
the_msg.attach(part_2)

print(the_msg.as_string())
email_conn.sendmail(from_email, to_email, the_msg.as_string())
email_conn.quit()
