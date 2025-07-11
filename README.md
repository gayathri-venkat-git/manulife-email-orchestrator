# manulife-email-orchestrator
Email Summarizer &amp; Prioritizer Agent for Manulife
An LLM-powered agent to parse, summarize and prioritize emails for the Manulife use case. Includes fallback logic and runs as a REST API service.

## Features
- LLM + rule based summarizer
- Lightweight priority classifier
- Email parser (.txt, .eml, .html)
- FastAPI interface + Docker support

## Run Locally
```
pip install -r requirements.txt
python main.py
```
