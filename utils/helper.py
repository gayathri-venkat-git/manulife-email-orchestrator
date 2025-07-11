import re

def detect_format(raw):
    if b"Content-Type:" in raw:
        return "eml"
    elif b"<html" in raw:
        return "html"
    return "txt"
