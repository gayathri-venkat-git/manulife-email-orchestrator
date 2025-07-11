from transformers import pipeline
import os

summarizer = pipeline("summarization", model="t5-small")

def summarize_with_llm(text):
    return summarizer(text[:1000])[0]['summary_text']
def rule_based_summary(text):
    lines = text.strip().split("\n")
    return " ".join(lines[:3]) if lines else te
