import imaplib
import dotenv
import os
from datetime import datetime, timedelta

dotenv.load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), ".env"))


def get_email1():
    EMAIL_ACCOUNT = os.getenv("GMAIL_EMAIL")
    PASSWORD = os.getenv("GMAIL_PASSWORD")
    IMAP_SERVER = "imap.gmail.com"
    IMAP_PORT = 993

    date_since = (datetime.now() - timedelta(days=7)).strftime("%d-%b-%Y")

    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.select("inbox")

    # Search for unread emails in primary category only (excluding social and promotions)
    status, response = mail.search(None, f'(UNSEEN SINCE {date_since} X-GM-RAW "category:primary")')
    unread_msg_nums = response[0].split()

    mail.logout()

    return len(unread_msg_nums)

def get_email2():
    EMAIL_ACCOUNT = os.getenv("PROTON_EMAIL")
    PASSWORD = os.getenv("PROTON_PASSWORD")
    IMAP_SERVER = "127.0.0.1"
    IMAP_PORT = 1143

    date_since = (datetime.now() - timedelta(days=7)).strftime("%d-%b-%Y")

    mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
    mail.login(EMAIL_ACCOUNT, PASSWORD)
    mail.select("inbox")

    # Search for unread emails from the last 7 days
    status, response = mail.search(None, f'(UNSEEN SINCE {date_since})')
    unread_msg_nums = response[0].split()

    mail.logout()

    return len(unread_msg_nums)

print(get_email1())
print(get_email2())