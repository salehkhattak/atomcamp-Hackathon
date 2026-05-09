# AI Recruiting Inbox

An AI-powered recruiting assistant that automates the hiring process by analyzing recruiter emails, extracting candidate information, and managing the hiring pipeline efficiently.

---

## Project Overview

This project automates repetitive recruitment tasks, including:
- Monitoring recruiter inboxes for new emails
- Extracting candidate details (name, skills, role, availability, etc.)
- Scoring candidates and managing pipelines
- Scheduling interviews and drafting responses
- Sending notifications to Slack/Discord

---
## System Workflow

Recruiter / Candidate Email Input
        ↓
AI Analysis Engine (LLM)
        ↓
Extract:
- Name
- Skills
- Experience
- Job Role
- Intent
        ↓
Candidate Scoring System
        ↓
Hiring Pipeline Update
        ↓
Streamlit Dashboard Display
        ↓
Human Approval (Approve / Reject)
        ↓
Action Execution (Mock Email / Scheduling)

## Simplified Architecture

1. **Email Listener**: Monitors inbox for new emails.
2. **LLM Analysis**: Extracts and analyzes candidate information.
3. **Decision Agent**: Scores and prioritizes candidates.
4. **Action Agent**: Automates tasks like scheduling and notifications.
5. **Human Approval**: Allows manual review before execution.
6. **Execution Agent**: Finalizes actions (e.g., sending emails, updating pipelines).

---

## Key Features

- **Email Parsing**: Extracts structured data from emails.
- **AI Analysis**: Uses LLMs (e.g., OpenAI) for candidate evaluation.
- **Pipeline Management**: Tracks candidate progress.
- **Interview Scheduling**: Automates calendar invites.
- **Notifications**: Updates via Slack/Discord.

---

## Quick Setup

### Prerequisites
- **Python 3.9+**
- **Streamlit**: For the dashboard UI
- **OpenAI API Key**: For LLM integration

### Installation
```bash
pip install streamlit openai pandas
```

### Run the App
```bash
streamlit run app.py
```

---

## Next Steps

1. **Set up your `.env` file** with API keys and email credentials.
2. **Test with sample emails** to validate the pipeline.
3. **Deploy** using Docker or directly on a cloud platform.

---

## Simplified Workflow

1. **Email → Candidate Profile**: AI extracts structured data.
2. **Candidate Scoring**: AI evaluates and prioritizes.
3. **Pipeline Updates**: Automates tracking and scheduling.
4. **Notifications**: Keeps the team updated.

---

Good luck with your hackathon! 🚀