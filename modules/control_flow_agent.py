from utils.helpers import detect_format
from modules.email_parser import parse_email
from modules.summarizer import summarize_with_llm, rule_based_summary
from modules.priority_detector import classify_priority

def orchestrate_email(raw_content):
    email_text = parse_email(raw_content, detect_format(raw_content))
    
    if len(email_text) < 200:
        summary = rule_based_summary(email_text)
    else:
        summary = summarize_with_llm(email_text)

    priority = classify_priority(email_text)

    return {
        "summary": summary,
        "priority": priority
    }
