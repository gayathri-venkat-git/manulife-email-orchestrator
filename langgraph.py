from langgraph.graph import StateGraph
from modules.summarizer import summarize_with_llm, rule_based_summary
from modules.priority_detector import classify_priority

def summarizer_node(state):
    text = state['text']
    if len(text) < 200:
        summary = rule_based_summary(text)
    else:
        summary = summarize_with_llm(text)
    return {"summary": summary, "text": text}

def classifier_node(state):
    priority = classify_priority(state['text'])
    return {"priority": priority, "summary": state["summary"]}

def build_langgraph_orchestrator():
    builder = StateGraph()
    builder.add_node("summarizer", summarizer_node)
    builder.add_node("classifier", classifier_node)
    builder.set_entry_point("summarizer")
    builder.add_edge("summarizer", "classifier")
    builder.set_finish_point("classifier")
    return builder.compile()
