from modules.email_parser import parse_email

def test_parse_txt():
    assert "Hello" in parse_email(b"Hello there", "txt")
