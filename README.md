# AI Recruiting Inbox 🤖

An intelligent AI-powered recruiting system that automatically processes recruiter emails, extracts candidate information, analyzes opportunities, and manages the hiring pipeline with minimal human intervention.

---

## 📋 Project Overview

**AI Recruiting Inbox** is a hackathon project designed to automate the recruitment process by leveraging AI agents to:
- Monitor and listen to recruiter email inboxes
- Analyze incoming recruitment emails using LLM (Language Learning Models)
- Extract critical candidate and job information automatically
- Make intelligent decisions about candidate qualification
- Manage candidate pipelines and scheduling
- Notify the team via Slack/Discord
- Execute actions with human approval

This system transforms manual, time-consuming recruitment workflows into an automated, intelligent process.

---

## 🏗️ System Architecture

```
┌──────────────────────────────┐
│  Recruiter Email Inbox       │
│  (Gmail/Outlook/IMAP)        │
└──────────────────────────────┘
              ↓
┌──────────────────────────────┐
│  Email Listener Agent        │
│  (Polls/Listens to Emails)   │
└──────────────────────────────┘
              ↓
┌──────────────────────────────┐
│  LLM Analysis Agent          │
│  (OpenAI/Claude/Llama)       │
└──────────────────────────────┘
              ↓
┌──────────────────────────────┐
│  Information Extraction      │
│  • Candidate name            │
│  • Technical skills          │
│  • Job role                  │
│  • Urgency level             │
│  • Availability              │
│  • Contact information       │
└──────────────────────────────┘
              ↓
┌──────────────────────────────┐
│  Decision Agent              │
│  (Scoring & Filtering)       │
└──────────────────────────────┘
              ↓
┌──────────────────────────────┐
│  Automated Actions           │
│  • Create candidate profile  │
│  • Store in database         │
│  • Schedule interview        │
│  • Draft email response      │
│  • Send notifications        │
└──────────────────────────────┘
              ↓
┌──────────────────────────────┐
│  Human Approval UI           │
│  (Review & Approve/Reject)   │
└──────────────────────────────┘
              ↓
┌──────────────────────────────┐
│  Execution Agent             │
│  (Commit Actions)            │
└──────────────────────────────┘
              ↓
┌──────────────────────────────┐
│  Final Actions               │
│  • Send confirmation email   │
│  • Update candidate pipeline │
│  • Create calendar events    │
└──────────────────────────────┘
```

---

## ✨ Key Features

- **📧 Email Listening**: Automatically monitors recruiter inboxes for new applications
- **🧠 AI Analysis**: Intelligent parsing using LLMs to understand candidate fit
- **📊 Auto Extraction**: Extracts skills, experience, availability, and requirements
- **🤔 Smart Decision Making**: Scores candidates and prioritizes applications
- **⏱️ Pipeline Management**: Automatically creates candidate records and tracks progress
- **📅 Interview Scheduling**: Suggests and schedules interviews automatically
- **✉️ Intelligent Responses**: Drafts personalized email responses
- **🔔 Team Notifications**: Posts updates to Slack/Discord in real-time
- **👥 Human Approval**: Review step before executing actions
- **💾 Data Storage**: Stores all candidate info in a database for future reference

---

## 🛠️ Tech Stack

### Backend/Core
- **Python 3.9+** - Primary programming language
- **FastAPI** or **Flask** - REST API framework
- **SQLAlchemy** - ORM for database operations

### AI & LLM Integration
- **OpenAI API** (ChatGPT) / **Anthropic Claude** / **LLaMA** - LLM provider
- **LangChain** - Framework for building LLM applications
- **Agent Libraries** - AutoGen or CrewAI for multi-agent orchestration

### Email Integration
- **IMAP Protocol** - For email listening
- **smtplib / Python Email** - For sending emails
- **Gmail API** / **Microsoft Graph API** - Advanced email integrations

### Database
- **PostgreSQL** - Relational database (recommended)
- **SQLite** - For local testing
- **Redis** - For caching and task queuing

### Notifications & Communication
- **Slack API** - Team notifications
- **Discord API** - Team notifications
- **Webhooks** - Real-time updates

### Frontend (Optional)
- **React** / **Vue.js** - Web UI for approval workflows
- **Streamlit** - Quick admin dashboard

---

## 📥 Prerequisites & What to Install

### Software Requirements
1. **Python 3.9 or higher** - [Download here](https://www.python.org/downloads/)
2. **Git** - [Download here](https://git-scm.com/)
3. **PostgreSQL** (optional, SQLite works for development) - [Download here](https://www.postgresql.org/download/)
4. **Docker** (optional) - [Download here](https://www.docker.com/products/docker-desktop)
5. **Node.js/npm** (if building frontend) - [Download here](https://nodejs.org/)

### Python Dependencies
```bash
pip install fastapi uvicorn python-dotenv pydantic
pip install sqlalchemy psycopg2-binary
pip install openai langchain
pip install python-imap
pip install slack-sdk discord.py
pip install email-validator
pip install requests
```

---

## 🔗 External Services & APIs to Connect

### 1. **LLM Provider** (Choose One)

#### Option A: OpenAI (ChatGPT)
- **Website**: https://platform.openai.com/
- **What to Do**:
  1. Sign up for OpenAI account
  2. Go to API keys section
  3. Create a new API key
  4. Copy and save the API key safely
- **Cost**: Pay-as-you-go model (~$0.002 per 1K tokens)
- **Environment Variable**: `OPENAI_API_KEY`

#### Option B: Anthropic (Claude)
- **Website**: https://console.anthropic.com/
- **What to Do**:
  1. Sign up for Anthropic account
  2. Navigate to API keys
  3. Create and copy API key
- **Cost**: Pay-as-you-go model
- **Environment Variable**: `ANTHROPIC_API_KEY`

#### Option C: Local LLaMA (Free)
- **Website**: https://ollama.ai/
- **What to Do**:
  1. Download Ollama
  2. Run: `ollama run llama2`
  3. Runs locally, no API key needed
- **Cost**: Free (requires GPU for better performance)

### 2. **Email Service**

#### Gmail
- **Website**: https://myaccount.google.com/
- **What to Do**:
  1. Enable 2-Factor Authentication
  2. Create App Password: https://myaccount.google.com/apppasswords
  3. Copy the generated 16-character password
- **Environment Variables**: 
  ```
  EMAIL_PROVIDER=gmail
  EMAIL_ADDRESS=your-email@gmail.com
  EMAIL_PASSWORD=your-app-password
  ```

#### Microsoft Outlook
- **Website**: https://login.microsoftonline.com/
- **What to Do**:
  1. Enable IMAP in Settings
  2. Create App Password (if 2FA enabled)
  3. Use your email and app password
- **Environment Variables**:
  ```
  EMAIL_PROVIDER=outlook
  EMAIL_ADDRESS=your-email@outlook.com
  EMAIL_PASSWORD=your-app-password
  ```

#### Custom IMAP Server
- Use any IMAP-compatible email server
- **Environment Variables**:
  ```
  EMAIL_PROVIDER=imap
  IMAP_SERVER=imap.example.com
  IMAP_PORT=993
  EMAIL_ADDRESS=your-email@example.com
  EMAIL_PASSWORD=your-password
  ```

### 3. **Database Setup**

#### PostgreSQL (Recommended)
- **Website**: https://www.postgresql.org/
- **Download & Install**: Follow PostgreSQL installation guide
- **Create Database**:
  ```bash
  psql -U postgres
  CREATE DATABASE recruiting_inbox;
  \q
  ```
- **Connection String**: `postgresql://user:password@localhost:5432/recruiting_inbox`

#### SQLite (Local Development)
- No installation needed
- Automatically created as a file
- **Connection String**: `sqlite:///recruiting_inbox.db`

### 4. **Slack Integration** (Optional)

- **Website**: https://api.slack.com/apps
- **What to Do**:
  1. Create a new app or select existing workspace
  2. Click "Create New App"
  3. Choose "From scratch"
  4. Give it a name and select workspace
  5. Go to "OAuth & Permissions"
  6. Add permissions: `chat:write`, `channels:read`
  7. Copy "Bot User OAuth Token"
  8. Install app to workspace
- **Environment Variable**: `SLACK_BOT_TOKEN`
- **Webhook Alternative**: Create Incoming Webhook in "Incoming Webhooks" section

### 5. **Discord Integration** (Optional)

- **Website**: https://discord.com/developers/applications
- **What to Do**:
  1. Create new application
  2. Go to "Bot" section and click "Add Bot"
  3. Copy the token
  4. Enable intents: Message Content Intent
  5. Go to OAuth2 → URL Generator
  6. Select scopes: `bot`
  7. Select permissions: `Send Messages`, `Read Messages`
  8. Copy generated URL and add bot to your server
- **Environment Variable**: `DISCORD_BOT_TOKEN`

### 6. **Calendar Integration** (Optional)

#### Google Calendar
- **Website**: https://console.cloud.google.com/
- **What to Do**:
  1. Create a new GCP project
  2. Enable Google Calendar API
  3. Create OAuth 2.0 credentials (Desktop app)
  4. Download credentials JSON
- **Environment Variable**: `GOOGLE_CALENDAR_CREDENTIALS_PATH`

#### Outlook Calendar
- Use Microsoft Graph API (same setup as Outlook email)

---

## 🚀 Installation & Setup Guide

### Step 1: Clone Repository
```bash
git clone https://github.com/yourusername/ai-recruiting-inbox.git
cd ai-recruiting-inbox
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Create `.env` File
Create a `.env` file in the project root:

```env
# LLM Configuration
LLM_PROVIDER=openai  # or 'anthropic' or 'ollama'
OPENAI_API_KEY=sk-your-api-key-here
# ANTHROPIC_API_KEY=your-anthropic-key
# OLLAMA_URL=http://localhost:11434

# Email Configuration
EMAIL_PROVIDER=gmail  # or 'outlook', 'imap'
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
IMAP_SERVER=imap.gmail.com
IMAP_PORT=993

# Database Configuration
DATABASE_URL=postgresql://user:password@localhost:5432/recruiting_inbox
# For SQLite: sqlite:///recruiting_inbox.db

# Slack Configuration (Optional)
SLACK_BOT_TOKEN=xoxb-your-bot-token

# Discord Configuration (Optional)
DISCORD_BOT_TOKEN=your-discord-token
DISCORD_CHANNEL_ID=your-channel-id

# Google Calendar (Optional)
GOOGLE_CALENDAR_CREDENTIALS_PATH=./config/google_credentials.json

# Application Configuration
DEBUG=True
PORT=8000
```

### Step 5: Initialize Database
```bash
python -m alembic upgrade head
# Or for SQLite with manual setup:
python scripts/init_db.py
```

### Step 6: Set Up Email Listener
Configure your email inbox settings in `config/email_config.py`:
```python
EMAIL_CONFIG = {
    'provider': 'gmail',
    'email': 'your-email@gmail.com',
    'app_password': 'your-app-specific-password',
    'poll_interval': 300,  # Check every 5 minutes
    'folder': 'INBOX'
}
```

### Step 7: Configure LLM Settings
Edit `config/llm_config.py`:
```python
LLM_CONFIG = {
    'provider': 'openai',  # or 'anthropic', 'ollama'
    'model': 'gpt-4',  # or 'claude-3-opus', 'llama2'
    'temperature': 0.7,
    'max_tokens': 1500
}
```

### Step 8: Set Up Database Tables
```bash
python scripts/create_tables.py
```

---

## 💻 Running the Application

### Start the API Server
```bash
uvicorn main:app --reload --port 8000
```

### Start the Email Listener Agent
```bash
python agents/email_listener.py
```

### Start the LLM Analysis Agent
```bash
python agents/analysis_agent.py
```

### Start the Decision Agent
```bash
python agents/decision_agent.py
```

### Start the Execution Agent
```bash
python agents/execution_agent.py
```

### Using Docker Compose (All-in-One)
```bash
docker-compose up
```

---

## 📁 Project Structure

```
ai-recruiting-inbox/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── .env.example                       # Example environment variables
├── docker-compose.yml                 # Docker orchestration
│
├── config/                            # Configuration files
│   ├── __init__.py
│   ├── email_config.py               # Email settings
│   ├── llm_config.py                 # LLM settings
│   └── database_config.py            # Database settings
│
├── agents/                            # AI Agents
│   ├── __init__.py
│   ├── email_listener.py             # Monitors email inbox
│   ├── analysis_agent.py             # LLM analysis
│   ├── decision_agent.py             # Scoring & filtering
│   ├── execution_agent.py            # Action execution
│   └── utils.py                      # Shared utilities
│
├── models/                            # Database models
│   ├── __init__.py
│   ├── candidate.py                  # Candidate model
│   ├── email.py                      # Email model
│   └── approval.py                   # Approval workflow
│
├── services/                          # Business logic services
│   ├── __init__.py
│   ├── email_service.py              # Email operations
│   ├── llm_service.py                # LLM interactions
│   ├── database_service.py           # Database operations
│   ├── slack_service.py              # Slack notifications
│   └── discord_service.py            # Discord notifications
│
├── api/                               # FastAPI routes
│   ├── __init__.py
│   ├── candidates.py                 # Candidate endpoints
│   ├── approvals.py                  # Approval endpoints
│   └── webhooks.py                   # Webhook endpoints
│
├── frontend/                          # Web UI (Optional)
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── package.json
│
├── scripts/                           # Utility scripts
│   ├── init_db.py                    # Database initialization
│   ├── create_tables.py              # Create DB tables
│   └── seed_data.py                  # Sample data
│
└── tests/                             # Unit & integration tests
    ├── test_agents.py
    ├── test_services.py
    └── test_api.py
```

---

## 🔌 API Endpoints

### Candidate Management
- `GET /api/candidates` - List all candidates
- `GET /api/candidates/{id}` - Get candidate details
- `POST /api/candidates` - Create new candidate
- `PUT /api/candidates/{id}` - Update candidate
- `DELETE /api/candidates/{id}` - Delete candidate

### Approvals
- `GET /api/approvals` - List pending approvals
- `POST /api/approvals/{id}/approve` - Approve action
- `POST /api/approvals/{id}/reject` - Reject action

### Webhooks
- `POST /api/webhooks/email` - Email listener webhook
- `POST /api/webhooks/slack-command` - Slack commands
- `POST /api/webhooks/calendar-event` - Calendar updates

---

## 🧪 Testing

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_agents.py

# Run with coverage
pytest --cov=.
```

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 Environment Variables Checklist

- [ ] `OPENAI_API_KEY` (or your chosen LLM provider key)
- [ ] `EMAIL_ADDRESS` and `EMAIL_PASSWORD`
- [ ] `DATABASE_URL`
- [ ] `SLACK_BOT_TOKEN` (if using Slack)
- [ ] `DISCORD_BOT_TOKEN` (if using Discord)
- [ ] `GOOGLE_CALENDAR_CREDENTIALS_PATH` (if using calendar)

---

## 🎯 Next Steps

1. **Set up the email listener** to start monitoring your inbox
2. **Configure your LLM provider** with API key
3. **Initialize the database** with candidate schema
4. **Set up notification channels** (Slack/Discord)
5. **Create approval workflow UI** for human review
6. **Test with sample emails** before going live
7. **Deploy to production** using Docker

---

## 📞 Support & Resources

- **OpenAI Documentation**: https://platform.openai.com/docs
- **Anthropic Claude**: https://docs.anthropic.com/
- **LangChain**: https://python.langchain.com/
- **FastAPI**: https://fastapi.tiangolo.com/
- **SQLAlchemy**: https://docs.sqlalchemy.org/

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 🚀 Ready to Get Started?

1. **Copy the `.env.example` to `.env`**
2. **Fill in your API keys** (Follow the "External Services" section above)
3. **Install dependencies**: `pip install -r requirements.txt`
4. **Run the application**: `python main.py`
5. **Access the UI**: http://localhost:8000

Good luck with your hackathon! 🎉

