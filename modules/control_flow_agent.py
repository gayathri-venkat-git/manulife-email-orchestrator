from langgraph_refactored import build_langgraph_orchestrator
from utils.helpers import detect_format
from modules.email_parser import parse_email

def orchestrate_email(raw_content):
    email_text = parse_email(raw_content, detect_format(raw_content))
    graph = build_langgraph_orchestrator()
    result = graph.invoke({"text": email_text})
    return result
