from app.models import Subscription
from app.forms import SubscriptionForm
import smtplib
from email.mime.text import MIMEText
import datetime
import os

def send_reminder_email(subr, sub):
    sender_email = "mindfullsubdemo@gmail.com"
    receiver_email = subr
    password = "odnj eqaj rfac rgnf"
    if not password:
        print("Error: Email password not set in environment variable 'EMAIL_PASSWORD'")
        return

    subject = "Time to pay yo bills"
    body = (
        f"Wazap,\n\n"
        f"This is a reminder that your subscription '{sub.name}' is due for renewal on {sub.renewal_date}. "
        "Or just cancel it idk."
    )

    message = MIMEText(body)
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    smtp_server = "smtp.gmail.com"
    port = 587

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(message)
        print(f"Email sent successfully to {receiver_email}!")
    except Exception as e:
        print(f"Error sending email to {receiver_email}: {e}")

def is_renewal_tomorrow(sub, subr):
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    if sub.renewal_date == tomorrow:
        send_reminder_email(subr, sub)

def send_daily_reminders(subr):
    if subr is None:
        subr = "artmsrv@gmail.com"
    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    subs_due = Subscription.query.filter_by(renewal_date=tomorrow).all()
    for sub in subs_due:
        if subr:  # Make sure subscriber exists
            is_renewal_tomorrow(sub, subr)
        else:
            print(f"Subscriber with ID {sub.subscriber_id} not found.")