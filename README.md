# 🤖 AI Recruiting Inbox — Hackathon Project

> An AI-powered recruiting assistant that automates the hiring pipeline using a **4-agent sequential pipeline** built on OpenAI GPT-4o-mini, with a Streamlit dashboard for human review.

---

## 📦 Repository Structure

```
Hackathon/
│
├── ai-recruiting-inbox/     ← ✅ Main project (Streamlit app + AI agents)
│   ├── src/
│   │   ├── agents/          ← 4 AI agents (extractor, assessor, coordinator, summarizer)
│   │   ├── app.py           ← Streamlit UI (run this)
│   │   └── main.py          ← CLI pipeline test runner
│   ├── .env                 ← API key (add yours here)
│   ├── requirements.txt
│   └── README.md            ← Full documentation ← READ THIS
│
├── ai-recruiter/            ← Scaffold / alternate backend (unused)
├── main.py                  ← FastAPI backend scaffold (optional REST API)
├── prompt.txt               ← Original build specification
├── workflow.txt             ← Development log
└── README.md                ← This file
```

---

## ⚡ How to Run

```bash
cd ai-recruiting-inbox
pip install -r requirements.txt
python -m streamlit run src/app.py
```

Open **http://localhost:8501** in your browser.

> 💡 **No API key?** Enable **Demo Mode** in the sidebar to run the full pipeline with mock data.

---

## 🗺 System Workflow

```
Candidate Email (pasted by recruiter)
        ↓
Agent 1 — Extractor     → name, skills, experience, intent
        ↓
Agent 2 — Assessor      → score (0-100), verdict, matched/missing skills
        ↓
Agent 3 — Coordinator   → action type, email draft, internal notes
        ↓
Agent 4 — Summarizer    → TL;DR, 3 interview questions, red flags
        ↓
Streamlit Dashboard     → Human reviews and approves
```

---

## 📖 Full Documentation

See **[`ai-recruiting-inbox/README.md`](./ai-recruiting-inbox/README.md)** for:
- Complete setup guide
- Agent descriptions and output schemas
- API reference (pipeline functions)
- Demo mode instructions
- Next steps & feature roadmap

---

## 🔧 Optional FastAPI Backend

A FastAPI REST backend scaffold is available at the root `main.py`. It exposes a `/api/process-email` endpoint that can be consumed by a Next.js frontend (see `README.md` lines 107–160 for a Next.js example component).

```bash
# Run the FastAPI backend (requires crewai + openai installed)
pip install fastapi uvicorn crewai openai
uvicorn main:app --reload --port 8000
```

---

*AtomCamp Hackathon 2026 · Built with Python, Streamlit, and OpenAI*