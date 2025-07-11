from modules.summarizer import summarize_with_llm, rule_based_summary

def test_rule_summary():
    assert rule_based_summary("line1\nline2") == "line1 line2"
