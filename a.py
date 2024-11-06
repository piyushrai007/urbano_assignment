import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, body, smtp_server, port, login, password):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject
    
    # Attach the body to the message
    message.attach(MIMEText(body, 'plain'))
    
    try:
        # Set up the server and login
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()  # Secure the connection
        server.login(login, password)
        
        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    
    except Exception as e:
        print(f"Error: {e}")
    
    finally:
        server.quit()

# Email details
sender_email = "piyush25ai037@satiengg.in"
receiver_email = "piyushraivds45@gmail.com"
subject = "Test Email"
body = "This is a test email sent from Python."
smtp_server = "smtp.gmail.com"
port = 587
login = "piyush25ai037@satiengg.in"
password = "piyush#965"  # Use app-specific password if using two-factor authentication

# Send the email
send_email(sender_email, receiver_email, subject, body, smtp_server, port, login, password)
