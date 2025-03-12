import os
import time
import requests
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import datetime


def check_website(url, email_sender, email_password, email_receiver):
    try:
        response = requests.get(url, timeout=10)
        now = datetime.now()
        formatted_time = now.strftime("%m/%d/%Y: %H:%M:%S")

        if response.status_code == 200:
            print(f"{formatted_time} Status code: 200 {url} is online!")
            return True
        else:
            print(f"{formatted_time} Status code: {response.status_code} {url} is offline!")
            send_email(url, response.status_code, email_sender, email_password, email_receiver, formatted_time)
            return False

    except requests.exceptions.RequestException as e:
        now = datetime.now()
        formatted_time = now.strftime("%m/%d/%Y: %H:%M:%S")
        print(f"{formatted_time} Error checking {url}: {e}")
        send_email(url, str(e), email_sender, email_password, email_receiver, formatted_time)
        return False


def send_email(url, error, email_sender, email_password, email_receiver, formatted_time):
    if isinstance(error, int): # handles status codes.
        status_code_str = str(error)
    else:
        status_code_str = "N/A" # handles exceptions.
    subject = f"WARNING: Website {url} is offline!"
    body = f"{formatted_time} Status Code: {status_code_str}\n\nThe website {url} is not responding correctly. Error: {error}"

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = email_sender
    msg["To"] = email_receiver

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(email_sender, email_password)
            server.send_message(msg)
        print("Email sent!")
    except Exception as e:
        print(f"Failed to send email: {e}")


def main():
    load_dotenv()

    url = os.getenv("WEBSITE_URL")
    email_sender = os.getenv("EMAIL_SENDER")
    email_password = os.getenv("EMAIL_PASSWORD")
    email_receiver = os.getenv("EMAIL_RECEIVER")

    if not all([url, email_sender, email_password, email_receiver]):
        print("Error: Missing environment variables in .env file. Please set WEBSITE_URL, EMAIL_SENDER, EMAIL_PASSWORD, and EMAIL_RECEIVER.")
        return

    while True:
        check_website(url, email_sender, email_password, email_receiver)
        time.sleep(60)


if __name__ == "__main__":
    main()
