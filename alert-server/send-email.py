import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, username, password):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Add body to email
    message.attach(MIMEText(body, 'plain'))

    # Create SMTP session for sending the mail
    try:
        session = smtplib.SMTP(smtp_server, smtp_port)
        session.starttls()
        session.login(username, password)
        text = message.as_string()
        session.sendmail(sender_email, receiver_email, text)
        session.quit()
        print('Email sent successfully!')
    except Exception as e:
        print('Error: ' + str(e))

