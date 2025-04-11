# Website Status Checker
### Description
This Python script monitors the status of a specified website by periodically sending an HTTP GET request. If the website does not respond with a 200 status code (indicating it’s online) or if an error occurs (such as a timeout or connection issue), the script sends an email notification to alert the user.

### Features
* Periodically checks the availability of a website every 60 seconds.
* ends email notifications when the website is offline or encounters an error.
* Uses environment variables to securely manage sensitive information like email credentials.

### Requirements
* Python 3.x
* Python packages:
    - `requests`
    - `python-dotenv`

### Setup
Follow these steps to set up the script:

1. Install the required dependencies: 
``` bash
pip install requests python-dotenv
```

2. Create a .env file: In the same directory as the script, create a file named .env with the following content:
```text
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_email_password
EMAIL_RECEIVER=receiver_email@gmail.com
WEBSITE_URL=https://example.com
```

### Gmail Configuration:
* If you have two-factor authentication (2FA) enabled on your Gmail account, you must generate an app password and use it as the `EMAIL_PASSWORD` in the `.env` file.
* If 2FA is not enabled, ensure that "Less secure app access" is turned on in your Google 
### Account settings.
Usage
To run the script, follow these steps:

1. Save the script as website_checker.py (or any name you prefer).
2. Open a terminal in the directory containing the script and the .env file.
3. Run the script with:

```bash
python website_checker.py
```

The script will check the website specified in `WEBSITE_URL` every 60 seconds.
If the website is offline (status code ≠ 200) or an error occurs, an email will be sent to the `EMAIL_RECEIVER` address with details about the issue.
To stop the script, press Ctrl+C in the terminal.

### Example Output
* If the website is online:

```text
10/15/2023: 14:30:45 Status code: 200 https://example.com is online!
```

* If the website is offline:
```text
10/15/2023: 14:31:45 Status code: 503 https://example.com is offline!
Email sent!
```

* If an error occurs (e.g., timeout):
```text
10/15/2023: 14:32:45 Error checking https://example.com: HTTPSConnectionPool(Max retries exceeded)
Email sent!
```

### Customization
You can modify the script to suit your needs:

* Check Interval: Change the frequency of website checks by editing the `time.sleep(60)` line in the main function. The value is in seconds (e.g., `time.sleep(300)` for 5-minute intervals).

* Email Content: Customize the email subject or body by modifying the subject and body variables in the send_email function.