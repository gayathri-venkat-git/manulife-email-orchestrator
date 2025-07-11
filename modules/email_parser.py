#to load emails from .eml, HTML, .txt files
from bs4 import BeautifulSoup
import email
import re

def parse_email(raw_content, fmt):
    if fmt == "eml":
        msg = email.message_from_bytes(raw_content)
        if msg.is_multipart():
            parts = [part.get_payload(decode=True) for part in msg.walk() if part.get_content_type() == 'text/plain']
            return "\n".join([p.decode('utf-8', errors='ignore') for p in parts if p])
        return msg.get_payload(decode=True).decode('utf-8', errors='ignore')

    elif fmt == "html":
        soup = BeautifulSoup(raw_content, 'html.parser')
        return soup.get_text()

    return raw_content.decode('utf-8', errors='ignore')
