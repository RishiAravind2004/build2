import smtplib
from email.message import EmailMessage
import config
from utils.prints import success, error

def Send_Email(Recipient_Emails, Subject, Body):

    # Mail Message Setup
    msg = EmailMessage()
    msg['From'] = config.APP_EMAIL_ADDRESS

    if isinstance(Recipient_Emails, list):
        msg['To'] = ', '.join(Recipient_Emails)
    else:
        msg['To'] = Recipient_Emails

    msg['Subject'] = Subject
    msg.set_content(Body)

    server = None 

    try:
        # Connect and secure the connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login
        server.login(config.APP_EMAIL_ADDRESS, config.APP_PASSWORD)

        # Send the message
        server.send_message(msg)
        success(f" Email sent successfully to {Recipient_Emails}!")

    except smtplib.SMTPAuthenticationError:
        error(" Failed to authenticate. Check your email and password.")
    except smtplib.SMTPException as e:
        error(" SMTP error occurred:", e)
    except Exception as e:
        error(" Failed to send email:", e)
    finally:
        if server:
            server.quit()

def Setup_Email_Test():
    server = None  # Initialize so it exists in the finally block

    try:
        # Connect and secure the connection
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        # Login
        server.login(config.APP_EMAIL_ADDRESS, config.APP_PASSWORD)

        success(" Email setup test successful!")

    except smtplib.SMTPAuthenticationError:
        error(" Failed to authenticate. Check your email and password.")
    except smtplib.SMTPException as e:
        error(f" SMTP error occurred: {e}")
    except Exception as e:
        error(f" Failed to connect: {e}")
    finally:
        if server:
            server.quit()