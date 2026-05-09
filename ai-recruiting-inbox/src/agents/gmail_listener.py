"""
gmail_listener.py — Agent 0: Gmail Inbox Listener

Connects to Gmail via IMAP, fetches unread emails from the inbox,
and returns them as structured dicts ready for the recruiting pipeline.

Requirements:
    - GMAIL_USER=your.email@gmail.com in .env
    - GMAIL_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx in .env
      (Generate at: https://myaccount.google.com/apppasswords)
    - "Less secure app access" is NOT needed — App Passwords work with 2FA enabled.
"""

import imaplib
import email
import os
from email.header import decode_header
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '..', '.env'))

IMAP_SERVER = "imap.gmail.com"
IMAP_PORT   = 993


def _decode_str(value: str | bytes, charset: str = "utf-8") -> str:
    """Safely decode a possibly-encoded email header value."""
    if isinstance(value, bytes):
        try:
            return value.decode(charset or "utf-8", errors="replace")
        except Exception:
            return value.decode("latin-1", errors="replace")
    return value or ""


def _get_body(msg: email.message.Message) -> str:
    """Extract plain-text body from a (possibly multipart) email message."""
    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            disposition   = str(part.get("Content-Disposition", ""))
            if content_type == "text/plain" and "attachment" not in disposition:
                payload = part.get_payload(decode=True)
                charset = part.get_content_charset() or "utf-8"
                body += _decode_str(payload, charset)
    else:
        payload = msg.get_payload(decode=True)
        charset = msg.get_content_charset() or "utf-8"
        body    = _decode_str(payload, charset)
    return body.strip()


def connect_to_gmail(user: str = None, app_password: str = None) -> imaplib.IMAP4_SSL:
    """
    Connect and authenticate to Gmail IMAP.

    Args:
        user:         Gmail address (falls back to GMAIL_USER env var)
        app_password: Gmail App Password (falls back to GMAIL_APP_PASSWORD env var)

    Returns:
        Authenticated imaplib.IMAP4_SSL connection object.

    Raises:
        EnvironmentError: If credentials are missing.
        ConnectionError:  If login fails.
    """
    user         = user or os.getenv("GMAIL_USER", "")
    app_password = app_password or os.getenv("GMAIL_APP_PASSWORD", "")

    if not user or not app_password:
        raise EnvironmentError(
            "Gmail credentials missing. Set GMAIL_USER and GMAIL_APP_PASSWORD in your .env file.\n"
            "Get an App Password at: https://myaccount.google.com/apppasswords"
        )

    try:
        mail = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT)
        mail.login(user, app_password)
        print(f"✅ Connected to Gmail as {user}")
        return mail
    except imaplib.IMAP4.error as e:
        raise ConnectionError(
            f"Gmail login failed: {e}\n"
            "Make sure you are using an App Password, not your regular Gmail password."
        )


def fetch_unread_emails(
    user: str = None,
    app_password: str = None,
    mailbox: str = "INBOX",
    max_emails: int = 20
) -> list[dict]:
    """
    Fetch unread emails from Gmail.

    Args:
        user:         Gmail address.
        app_password: Gmail App Password.
        mailbox:      IMAP mailbox to read from (default: "INBOX").
        max_emails:   Maximum number of emails to return (most recent first).

    Returns:
        List of dicts, each with keys:
            uid      (str)  — IMAP UID
            subject  (str)  — Email subject line
            sender   (str)  — Sender name/address
            date     (str)  — Date string
            body     (str)  — Plain-text body (what the pipeline needs)
            snippet  (str)  — First 120 chars of body for display

    Raises:
        ConnectionError: If credentials are wrong.
        RuntimeError:    If fetching fails.
    """
    mail = connect_to_gmail(user, app_password)

    try:
        mail.select(mailbox)

        # Search for UNSEEN (unread) emails
        status, data = mail.search(None, "UNSEEN")
        if status != "OK":
            return []

        uid_list = data[0].split()
        if not uid_list:
            print("📭 No unread emails found.")
            return []

        # Take the most recent N emails (reversed so newest first)
        uid_list = uid_list[-max_emails:][::-1]

        emails = []
        for uid in uid_list:
            try:
                status, msg_data = mail.fetch(uid, "(RFC822)")
                if status != "OK" or not msg_data or not msg_data[0]:
                    continue

                raw_email = msg_data[0][1]
                msg       = email.message_from_bytes(raw_email)

                # Decode subject
                raw_subject = msg.get("Subject", "")
                decoded_parts = decode_header(raw_subject)
                subject = ""
                for part, charset in decoded_parts:
                    subject += _decode_str(part, charset)

                # Decode sender
                raw_from = msg.get("From", "")
                decoded_from = decode_header(raw_from)
                sender = ""
                for part, charset in decoded_from:
                    sender += _decode_str(part, charset)

                date   = msg.get("Date", "")
                body   = _get_body(msg)
                snippet = (body[:120] + "…") if len(body) > 120 else body

                emails.append({
                    "uid":     uid.decode(),
                    "subject": subject.strip() or "(No Subject)",
                    "sender":  sender.strip(),
                    "date":    date.strip(),
                    "body":    body,
                    "snippet": snippet
                })
            except Exception as e:
                print(f"⚠️  Could not parse email UID {uid}: {e}")
                continue

        print(f"📬 Fetched {len(emails)} unread email(s).")
        return emails

    except Exception as e:
        raise RuntimeError(f"Failed to fetch emails: {e}")
    finally:
        try:
            mail.logout()
        except Exception:
            pass


def mark_as_read(uid: str, user: str = None, app_password: str = None) -> None:
    """
    Mark a specific email as read (removes the \\Unseen flag).

    Args:
        uid:          IMAP UID of the email to mark as read.
        user:         Gmail address.
        app_password: Gmail App Password.
    """
    try:
        mail = connect_to_gmail(user, app_password)
        mail.select("INBOX")
        mail.store(uid, "+FLAGS", "\\Seen")
        mail.logout()
        print(f"✅ Email UID {uid} marked as read.")
    except Exception as e:
        print(f"⚠️  Could not mark email as read: {e}")
