# 🤖 AI Recruiting Inbox

> **Automate your entire hiring pipeline using a 4-agent AI system powered by OpenAI GPT-4o-mini and Streamlit.**

---

## 📋 Table of Contents

1. [Project Overview](#-project-overview)
2. [System Architecture](#-system-architecture)
3. [Project Structure](#-project-structure)
4. [Agent Descriptions](#-agent-descriptions)
5. [Quick Start](#-quick-start)
6. [Running the App](#-running-the-app)
7. [Demo Mode](#-demo-mode)
8. [Configuration](#-configuration)
9. [API Reference (Pipeline Functions)](#-api-reference-pipeline-functions)
10. [Known Limitations](#-known-limitations)
11. [Next Steps & Guidelines](#-next-steps--guidelines)

---

## 🎯 Project Overview

**AI Recruiting Inbox** is a multi-agent AI system that automates the repetitive and time-consuming parts of the recruiting workflow. A recruiter pastes a raw candidate email into the dashboard, and the 4-agent pipeline:

1. **Extracts** structured candidate data (name, skills, experience, intent)
2. **Scores** the candidate against the job requirements (0–100 score + verdict)
3. **Drafts** a professional email response and determines the next action
4. **Generates** a hiring manager brief with interview questions

All results are displayed in a clean, interactive **Streamlit dashboard**.

---

## 🏗 System Architecture

```
Raw Candidate Email (User Input)
         │
         ▼
┌─────────────────────┐
│  Agent 1: Extractor │  ← Parses email → structured JSON
└─────────────────────┘
         │
         ▼
┌─────────────────────┐
│  Agent 2: Assessor  │  ← Scores candidate vs. job requirements
└─────────────────────┘
         │
         ▼
┌──────────────────────────┐
│  Agent 3: Coordinator    │  ← Determines next action + drafts email
└──────────────────────────┘
         │
         ▼
┌──────────────────────────┐
│  Agent 4: Summarizer     │  ← Generates hiring manager brief
└──────────────────────────┘
         │
         ▼
  Streamlit Dashboard
  (Metrics · Profile · Brief · Email Draft)
         │
         ▼
  Human Review & Approval
```

All 4 agents call **OpenAI GPT-4o-mini** with carefully crafted system prompts and return clean JSON objects. They run **sequentially**, each feeding its output into the next.

---

## 📁 Project Structure

```
ai-recruiting-inbox/
│
├── src/
│   ├── agents/
│   │   ├── __init__.py          # Package init
│   │   ├── extractor.py         # Agent 1: Candidate data extraction
│   │   ├── assessor.py          # Agent 2: Scoring & evaluation
│   │   ├── coordinator.py       # Agent 3: Action drafting
│   │   └── summarizer.py        # Agent 4: Manager brief generation
│   │
│   ├── main.py                  # CLI pipeline runner (test harness)
│   └── app.py                   # Streamlit UI (main entry point)
│
├── .env                         # Your API keys (git-ignored)
├── .env.example                 # Template for environment variables
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🤖 Agent Descriptions

### Agent 1 — `extractor.py` · *Data Extraction Specialist*

**Input:** Raw email string  
**Output:** Structured JSON with candidate profile

| Field | Type | Description |
|---|---|---|
| `name` | string | Candidate's full name, or `"Unknown"` |
| `skills` | list[str] | Technical skills and tools mentioned |
| `experience_years` | int | Estimated years of experience |
| `current_role` | string | Most recent job title |
| `intent` | string | What the candidate is asking for |

---

### Agent 2 — `assessor.py` · *Technical Recruiter Assessor*

**Input:** Extracted candidate data + job requirements  
**Output:** Scoring JSON

| Field               | Type        | Description |
|---------------------|-------------|-------------|
| `score`             | int         | 0–100 fit score |
| `verdict`           | string      | `"Strong Hire"`, `"Potential Fit"`, or `"Reject"` |
| `matched_skills`    | list[str]   | Skills the candidate has that match the role |
| `missing_skills`    | list[str]   | Required skills the candidate lacks |
| `reasoning`         | string      | 2–3 sentence explanation of the score |

---

### Agent 3 — `coordinator.py` · *Recruiting Execution Agent*

**Input:** Scored candidate data + extracted profile  
**Output:** Action JSON

| Field               | Type        | Description |
|---------------------|-------------|-------------|
| `action_type`       | string      | `"Schedule Interview"`, `"Send Rejection"`, or `"Request More Info"` |
| `email_draft`       | string      | Fully written professional email to the candidate |
| `internal_notes`    | string      | 1-sentence note for the recruiting team |

---

### Agent 4 — `summarizer.py` · *Executive Assistant (Hiring Manager Brief)*

**Input:** Extracted profile + scored assessment  
**Output:** Manager brief JSON

| Field               | Type        | De   scription |
|---------------------|-------------|-------------|
| `tl_dr`             | string      | 1–2 sentence summary for the hiring manager |
| `interview_questions`| list[str]   | Exactly 3 tailored technical questions |
| `red_flags`         | list[str]   | Concerns or gaps (can be empty list) |

---

## 🚀 Quick Start

### 1. Prerequisites

- Python 3.9 or higher
- An OpenAI API key with credits ([Get one here](https://platform.openai.com/api-keys))

### 2. Clone / Navigate to the project

```bash
cd ai-recruiting-inbox
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set up your API key

Copy the example file and add your key:

```bash
cp .env.example .env
```

Edit `.env`:

```env
OPENAI_API_KEY=sk-proj-your-actual-key-here
```

### 5. Run the app

```bash
python -m streamlit run src/app.py
```

Open your browser at: **http://localhost:8501**

---

## 🖥 Running the App

### Streamlit UI (Recommended)

```bash
python -m streamlit run src/app.py
```

The dashboard provides:
- **Job Configuration** — Enter the target role and required skills
- **Candidate Email** — Paste the raw email from the candidate
- **Process Candidate** — Runs all 4 agents sequentially
- **Results Dashboard** — Displays score, verdict, profile, brief, and editable email draft

### CLI Pipeline Runner (Testing)

To run a quick test of the backend pipeline without the UI:

```bash
cd ai-recruiting-inbox
python src/main.py
```

This runs the 4-agent pipeline against a hardcoded test email (Alice, Senior React Developer) and prints the output to the terminal.

---

## 🎭 Demo Mode

The app includes a **Demo Mode** that runs the full pipeline using pre-built realistic mock data — no API key or internet connection required. This is ideal for:

- Hackathon demos
- Testing the UI without spending API credits
- Showing the app to stakeholders

**How to enable:**
1. Open the **sidebar** (click the `>` arrow on the left edge of the page)
2. Toggle **🎭 Demo Mode** to ON
3. Fill in the form (use **Load Sample Data** to auto-fill)
4. Click **Process Candidate**

You can also override your API key directly in the sidebar without editing `.env`.

---

## ⚙️ Configuration

### Environment Variables

| Variable         | Required    | Description              |
|------------------|-------------|--------------------------|
| `OPENAI_API_KEY` | Yes         | Your OpenAI API key      |

### Model

All agents use **`gpt-4o-mini`** by default. To change the model, edit the `model=` parameter in each agent file under `src/agents/`.

For higher accuracy (at higher cost), change to `gpt-4o`:

```python
# In each agent file
response = client.chat.completions.create(
    model="gpt-4o",   # ← change here
    ...
)
```

---

## 📦 API Reference (Pipeline Functions)

### `extract_candidate_info(email_content: str) -> dict`
*File: `src/agents/extractor.py`*

```python
from agents.extractor import extract_candidate_info

result = extract_candidate_info("Hi, I'm Alice. I have 5 years of React experience...")
# Returns: {"name": "Alice", "skills": ["React", ...], "experience_years": 5, ...}
```

---

### `score_candidate(extracted_data: dict, job_requirements: dict) -> dict`
*File: `src/agents/assessor.py`*

```python
from agents.assessor import score_candidate

result = score_candidate(extracted_data, {"target_role": "Senior React Dev", "required_skills": "React, TypeScript"})
# Returns: {"score": 82, "verdict": "Strong Hire", "matched_skills": [...], ...}
```

---

### `draft_action(scored_candidate: dict, extracted_data: dict) -> dict`
*File: `src/agents/coordinator.py`*

```python
from agents.coordinator import draft_action

result = draft_action(scored_candidate, extracted_data)
# Returns: {"action_type": "Schedule Interview", "email_draft": "...", "internal_notes": "..."}
```

---

### `generate_manager_brief(extracted_data: dict, scored_candidate: dict) -> dict`
*File: `src/agents/summarizer.py`*

```python
from agents.summarizer import generate_manager_brief

result = generate_manager_brief(extracted_data, scored_candidate)
# Returns: {"tl_dr": "...", "interview_questions": [...], "red_flags": [...]}
```

---

## ⚠️ Known Limitations

| Limitation | Details |
|---|---|
| **No real email inbox** | The app currently works with pasted emails only. There is no live IMAP/Gmail connection. |
| **No persistent storage** | Candidate results are held in session state only. Refreshing the page clears results. |
| **No authentication** | The app has no login. Anyone with the URL can use it. |
| **Single candidate per session** | You process one email at a time. There is no batch processing yet. |
| **API cost** | Each pipeline run makes 4 OpenAI API calls. At gpt-4o-mini rates, this is very cheap (~$0.001 per run), but costs accumulate at scale. |

---




# 🗺 Next Steps & Guidelines

Below are prioritized improvements, from lowest to highest effort, to take this from a hackathon MVP to a production-ready product.

---

### 🟢 Easy Wins (1–2 hours each)

#### 1. Persist results to a CSV or SQLite database
Store every processed candidate so you can review them later. Use Python's `sqlite3` module or `pandas` to write results to a local file.

```python
import sqlite3
# Save extracted_data + scored + action + brief to a candidates table
```

#### 2. Add a Candidates History tab
Use `st.tabs()` to add a second tab to the dashboard that shows a sortable table of all processed candidates using `st.dataframe()`.

#### 3. Add score threshold configuration
Let the recruiter set the minimum score for "Strong Hire" and "Potential Fit" in the sidebar, rather than using hard-coded thresholds.

#### 4. Export to PDF or CSV
Add a download button using `st.download_button()` to export the manager brief and email draft as a PDF or plain text file.

---

### 🟡 Medium Effort (half-day each)

#### 5. Gmail / Outlook inbox integration
Use Python's `imaplib` + `email` libraries to automatically pull unread emails from a real inbox and populate the candidate form.

```python
import imaplib, email
mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, PASSWORD)
mail.select("inbox")
# Fetch unread messages...
```

Requires an **App Password** from Gmail (not your main password). Add `GMAIL_USER` and `GMAIL_APP_PASSWORD` to `.env`.

#### 6. Actually send emails via SMTP
Use Python's `smtplib` to send the drafted email directly from the app.

```python
import smtplib
from email.mime.text import MIMEText
# Use the edited email_draft from st.text_area as the body
```

#### 7. Batch processing mode
Allow the recruiter to paste multiple emails (separated by a delimiter) and process them all in one run, displaying results in a table with approve/reject buttons.

#### 8. Slack / Discord notification
After processing, send a Slack message to a `#recruiting` channel using the Slack Incoming Webhooks API. This keeps the team informed without opening the app.

```python
import requests
requests.post(SLACK_WEBHOOK_URL, json={"text": f"New candidate: {name} — Score: {score} ({verdict})"})
```

---

### 🔴 Advanced Features (1–3 days each)

#### 9. FastAPI backend + Next.js frontend
The root `main.py` in this repo already has a FastAPI scaffold with a `/api/process-email` endpoint. You can:
- Deploy the FastAPI backend to **Railway** or **Render** (free tier)
- Build a more polished Next.js frontend and deploy to **Vercel**
- This makes the app accessible as a real web product

#### 10. Vector database for candidate memory
Use **ChromaDB** or **Pinecone** to store candidate embeddings. This enables:
- Searching past candidates by skill similarity
- Detecting duplicate applications
- Building a talent pool that grows over time

#### 11. Multi-job pipeline
Let the recruiter define multiple open roles. When an email comes in, automatically match it to the best-fitting role before scoring.

#### 12. Resume file upload (PDF parsing)
Add `st.file_uploader()` to accept PDF resumes alongside the email. Use `pdfplumber` or `PyPDF2` to extract resume text and pass it to the extractor agent.

```bash
pip install pdfplumber
```

#### 13. Human-in-the-loop approval workflow
Add **Approve / Reject** buttons that actually send the drafted email (via SMTP) and log the decision. This creates a proper review workflow before any email goes out.

#### 14. Docker + Cloud deployment
Package the Streamlit app in a Docker container and deploy to:
- **Railway** (simplest, 1-click deploy from GitHub)
- **Google Cloud Run** (scalable, pay-per-use)
- **AWS ECS** (enterprise-grade)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 8501
CMD ["python", "-m", "streamlit", "run", "src/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

---

## 🔑 Comprehensive Setup & Integrations Guide

To get the app fully functional with all its features (AI + Gmail), you need to configure your environment variables correctly. 

### 1. OpenAI API Key (Required)
The app requires an OpenAI API key to run the 4-agent pipeline.
1. Go to [OpenAI API Keys](https://platform.openai.com/api-keys).
2. Create a new secret key (e.g., `sk-proj-...`).
3. Open the `.env` file in the `ai-recruiting-inbox/` directory.
4. Add your key: `OPENAI_API_KEY=sk-proj-your-key-here`.
*(Alternatively, you can paste this directly into the Streamlit sidebar during runtime if you don't want to save it in `.env`)*

### 2. Gmail Integration (Optional but Recommended)
To pull unread candidate emails directly from your Gmail inbox into the dashboard, you must generate a **Google App Password**. You *cannot* use your regular Gmail password.

**How to generate an App Password:**
1. Go to your [Google Account Manage page](https://myaccount.google.com/).
2. Navigate to **Security** on the left menu.
3. Ensure **2-Step Verification** is turned ON.
4. Go to **2-Step Verification** > scroll to the bottom and click **App passwords**.
5. Give it a name (e.g., "AI Recruiting Inbox") and click **Create**.
6. Copy the 16-character password provided (e.g., `abcd efgh ijkl mnop`).

**Configure `.env` for Gmail:**
Add these variables to your `.env` file:
```env
GMAIL_USER=your.email@gmail.com
GMAIL_APP_PASSWORD=abcdefghijklmnop
```

### 3. Running the Complete System
Once your `.env` looks like this:
```env
OPENAI_API_KEY=sk-proj-...
GMAIL_USER=your.email@gmail.com
GMAIL_APP_PASSWORD=xxxx-xxxx-xxxx-xxxx
```

You can run the app:
```bash
pip install -r requirements.txt
python -m streamlit run src/app.py
```
1. In the sidebar, click **📥 Fetch Unread Emails**.
2. Select an email from the dropdown and click **⬇️ Load into Form**.
3. Fill in the "Target Role" and "Required Skills".
4. Click **🚀 Process Candidate**.

---

## 🛠 Tech Stack

| Component | Technology |
|---|---|
| **UI Framework** | Streamlit |
| **AI / LLM** | OpenAI GPT-4o-mini |
| **Language** | Python 3.9+ |
| **Config** | python-dotenv |
| **HTTP Client** | openai SDK |

---

## 📄 License

MIT — free to use, modify, and distribute.

---

*Built for the AtomCamp Hackathon 2026 🚀*
