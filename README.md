# Email Orchestrator  
**AI-powered Email Summarization and Prioritization Microservice**  
Built with FastAPI • LangGraph • Docker • Kubernetes • GitHub Actions

## Overview

The **Email Orchestrator** is a production-ready AI microservice that intelligently summarizes incoming emails and classifies them by priority using a hybrid decision engine combining Large Language Models (LLMs) and rule-based heuristics.

It is built to demonstrate:

- Agentic AI control using **LangGraph**
- Rule-based and LLM-based fallback summarization
- Email priority detection using custom ML classifier
- Dockerized and Kubernetes-deployable architecture
- CI/CD with GitHub Actions & Docker Hub integration

## Features

- Upload an email `.txt` file and receive:
  - A concise **summary**
  - A **priority classification** (e.g., High / Medium / Low)
- Modular design for easy extension
- Auto-decision logic for summarization strategy (Rule vs LLM)
- Deployable on Kubernetes with load balancing

---

## Tech Stack

| Layer              | Tools / Frameworks             |
|--------------------|--------------------------------|
| API                | FastAPI                        |
| Control Flow       | LangGraph (Agentic AI)         |
| Summarization      | Transformers (LLM) + Rule-based|
| Priority Detection | Scikit-learn (ML Classifier)   |
| Deployment         | Docker, Kubernetes             |
| CI/CD              | GitHub Actions                 |

---

## Installation (Local)

```bash
# Clone the repo
git clone https://github.com/gayathri-venkat-git/manulife-email-orchestrator.git
cd manulife-email-orchestrator

# Create a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the service
python main.py
