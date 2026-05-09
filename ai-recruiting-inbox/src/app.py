import sys
import os

# Ensure agents can be found regardless of where streamlit is run from
sys.path.insert(0, os.path.dirname(__file__))

import streamlit as st
from dotenv import load_dotenv
import time

# Load environment variables
load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env'))

# ─────────────────────────────────────────────
# Page Configuration
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="AI Recruiting Inbox",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ─────────────────────────────────────────────
# Custom CSS — Premium Dark Theme
# ─────────────────────────────────────────────
st.markdown("""
<style>
    /* ---------- Base ---------- */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%);
        min-height: 100vh;
    }

    /* ---------- Hide default streamlit elements ---------- */
    #MainMenu { visibility: hidden; }
    footer { visibility: hidden; }
    header { visibility: hidden; }

    /* ---------- Main container ---------- */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1300px;
    }

    /* ---------- Hero Header ---------- */
    .hero-header {
        text-align: center;
        padding: 2.5rem 1rem 2rem;
        background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, rgba(255,255,255,0.02) 100%);
        border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        margin-bottom: 2rem;
    }

    .hero-header h1 {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #a78bfa, #60a5fa, #34d399);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        margin: 0;
        line-height: 1.2;
    }

    .hero-header p {
        color: rgba(255,255,255,0.6);
        font-size: 1.1rem;
        margin-top: 0.75rem;
        font-weight: 400;
    }

    /* ---------- Agent badges ---------- */
    .agent-badges {
        display: flex;
        justify-content: center;
        gap: 0.75rem;
        margin-top: 1.25rem;
        flex-wrap: wrap;
    }

    .agent-badge {
        background: rgba(255,255,255,0.08);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 50px;
        padding: 0.35rem 1rem;
        font-size: 0.8rem;
        font-weight: 500;
        color: rgba(255,255,255,0.7);
    }

    /* ---------- Section Cards ---------- */
    .section-card {
        background: rgba(255,255,255,0.04);
        border: 1px solid rgba(255,255,255,0.08);
        border-radius: 16px;
        padding: 1.75rem;
        margin-bottom: 1.5rem;
        backdrop-filter: blur(8px);
    }

    .section-title {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.12em;
        color: rgba(255,255,255,0.4);
        margin-bottom: 1rem;
    }

    /* ---------- Metric Cards ---------- */
    .metric-card {
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.1);
        border-radius: 16px;
        padding: 1.5rem;
        text-align: center;
        height: 100%;
        transition: transform 0.2s ease, box-shadow 0.2s ease;
    }

    .metric-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    }

    .metric-label {
        font-size: 0.75rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.1em;
        color: rgba(255,255,255,0.45);
        margin-bottom: 0.6rem;
    }

    .metric-value {
        font-size: 2.4rem;
        font-weight: 800;
        line-height: 1;
        margin-bottom: 0.4rem;
    }

    .metric-sub {
        font-size: 0.8rem;
        color: rgba(255,255,255,0.45);
    }

    .score-green  { color: #34d399; }
    .score-orange { color: #fb923c; }
    .score-red    { color: #f87171; }
    .verdict-strong { color: #34d399; }
    .verdict-potential { color: #fbbf24; }
    .verdict-reject { color: #f87171; }
    .action-interview { color: #60a5fa; }
    .action-rejection { color: #f87171; }
    .action-info { color: #fbbf24; }

    /* ---------- Skill tags ---------- */
    .skill-tag {
        display: inline-block;
        background: rgba(96, 165, 250, 0.15);
        border: 1px solid rgba(96, 165, 250, 0.3);
        border-radius: 6px;
        padding: 0.25rem 0.65rem;
        margin: 0.2rem;
        font-size: 0.8rem;
        color: #93c5fd;
        font-weight: 500;
    }

    .skill-tag-missing {
        background: rgba(248, 113, 113, 0.12);
        border: 1px solid rgba(248, 113, 113, 0.25);
        color: #fca5a5;
    }

    /* ---------- Info rows ---------- */
    .info-row {
        display: flex;
        align-items: flex-start;
        padding: 0.6rem 0;
        border-bottom: 1px solid rgba(255,255,255,0.05);
    }

    .info-row:last-child { border-bottom: none; }

    .info-label {
        font-size: 0.78rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        color: rgba(255,255,255,0.4);
        min-width: 140px;
    }

    .info-value {
        font-size: 0.92rem;
        color: rgba(255,255,255,0.85);
        font-weight: 500;
        flex: 1;
    }

    /* ---------- Question items ---------- */
    .question-item {
        background: rgba(167, 139, 250, 0.08);
        border-left: 3px solid #a78bfa;
        border-radius: 0 8px 8px 0;
        padding: 0.75rem 1rem;
        margin-bottom: 0.6rem;
        color: rgba(255,255,255,0.8);
        font-size: 0.9rem;
        line-height: 1.5;
    }

    /* ---------- Pipeline progress indicator ---------- */
    .pipeline-step {
        display: flex;
        align-items: center;
        gap: 0.75rem;
        padding: 0.75rem 1rem;
        border-radius: 10px;
        margin-bottom: 0.5rem;
        font-size: 0.9rem;
        font-weight: 500;
    }

    .pipeline-step-active {
        background: rgba(167, 139, 250, 0.15);
        border: 1px solid rgba(167, 139, 250, 0.3);
        color: #c4b5fd;
    }

    .pipeline-step-done {
        background: rgba(52, 211, 153, 0.1);
        border: 1px solid rgba(52, 211, 153, 0.2);
        color: #6ee7b7;
    }

    /* ---------- Streamlit element overrides ---------- */
    .stTextInput > div > div > input,
    .stTextArea > div > div > textarea {
        background: rgba(255,255,255,0.06) !important;
        border: 1px solid rgba(255,255,255,0.12) !important;
        border-radius: 10px !important;
        color: rgba(255,255,255,0.9) !important;
        font-family: 'Inter', sans-serif !important;
    }

    .stTextInput > div > div > input:focus,
    .stTextArea > div > div > textarea:focus {
        border-color: rgba(167, 139, 250, 0.6) !important;
        box-shadow: 0 0 0 2px rgba(167, 139, 250, 0.15) !important;
    }

    .stTextInput label, .stTextArea label {
        color: rgba(255,255,255,0.65) !important;
        font-weight: 500 !important;
        font-size: 0.88rem !important;
    }

    div.stButton > button {
        background: linear-gradient(135deg, #7c3aed, #4f46e5) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2.5rem !important;
        font-size: 1rem !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        letter-spacing: 0.02em !important;
        transition: all 0.2s ease !important;
        box-shadow: 0 4px 20px rgba(124, 58, 237, 0.35) !important;
        cursor: pointer !important;
    }

    div.stButton > button:hover {
        background: linear-gradient(135deg, #6d28d9, #4338ca) !important;
        box-shadow: 0 6px 28px rgba(124, 58, 237, 0.5) !important;
        transform: translateY(-1px) !important;
    }

    div.stButton > button[disabled] {
        opacity: 0.5 !important;
        cursor: not-allowed !important;
    }

    .stAlert {
        border-radius: 10px !important;
    }

    .stSpinner > div {
        color: #a78bfa !important;
    }

    /* ---------- Divider ---------- */
    hr {
        border-color: rgba(255,255,255,0.08) !important;
        margin: 1.5rem 0 !important;
    }

    /* ---------- Subheader ---------- */
    h2, h3 {
        color: rgba(255,255,255,0.9) !important;
    }
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Hero Header
# ─────────────────────────────────────────────
st.markdown("""
<div class="hero-header">
    <h1>🤖 AI Recruiting Inbox</h1>
    <p>Automate your hiring pipeline with AI agents.</p>
    <div class="agent-badges">
        <span class="agent-badge">📧 Email Parser</span>
        <span class="agent-badge">⚡ Skills Assessor</span>
        <span class="agent-badge">📋 Action Coordinator</span>
        <span class="agent-badge">📊 Manager Briefer</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
# Sidebar — Gmail + Settings
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("### 📬 Gmail Integration")

    # ── Credential inputs (pre-filled from .env) ──
    gmail_user = st.text_input(
        "Gmail Address",
        value=os.getenv("GMAIL_USER", ""),
        placeholder="you@gmail.com",
        key="gmail_user_input"
    )
    gmail_pass = st.text_input(
        "App Password",
        value=os.getenv("GMAIL_APP_PASSWORD", ""),
        type="password",
        placeholder="xxxx-xxxx-xxxx-xxxx",
        help="Use a Gmail App Password, NOT your regular password.\nGenerate at: myaccount.google.com/apppasswords",
        key="gmail_pass_input"
    )

    # ── Fetch button ──
    if st.button("📥 Fetch Unread Emails", key="fetch_gmail_btn", use_container_width=True):
        if not gmail_user or not gmail_pass:
            st.error("Enter your Gmail address and App Password above.")
        else:
            with st.spinner("Connecting to Gmail..."):
                try:
                    from agents.gmail_listener import fetch_unread_emails
                    fetched = fetch_unread_emails(
                        user=gmail_user,
                        app_password=gmail_pass,
                        max_emails=15
                    )
                    st.session_state["gmail_emails"] = fetched
                    st.session_state["gmail_connected"] = True
                    if fetched:
                        st.success(f"✅ {len(fetched)} unread email(s) fetched!")
                    else:
                        st.info("📭 No unread emails found in your inbox.")
                except Exception as e:
                    st.session_state["gmail_connected"] = False
                    st.error(f"❌ {e}")

    # ── Email selector (shown after a successful fetch) ──
    if st.session_state.get("gmail_connected") and st.session_state.get("gmail_emails"):
        emails = st.session_state["gmail_emails"]

        st.markdown("---")
        st.markdown("**Select an email to process:**")

        # Build display labels: "From · Subject (snippet)"
        options = {
            f"{e['sender'][:28]} · {e['subject'][:30]}": i
            for i, e in enumerate(emails)
        }
        selected_label = st.selectbox(
            "Unread emails",
            list(options.keys()),
            key="gmail_selector",
            label_visibility="collapsed"
        )
        selected_idx = options[selected_label]
        selected_email = emails[selected_idx]

        # Show a brief preview
        st.caption(f"📅 {selected_email['date'][:22]}")
        st.caption(f"✉️ {selected_email['snippet']}")

        if st.button("⬇️ Load into Form", key="load_gmail_btn", use_container_width=True):
            # Clear existing widget keys, then set via session state
            for k in ["input_email"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.session_state["gmail_body_to_load"] = selected_email["body"]
            st.session_state["gmail_subject_loaded"] = selected_email["subject"]
            st.rerun()

    st.markdown("---")

    # ── OpenAI settings ──
    st.markdown("### ⚙️ Settings")
    demo_mode = st.toggle("🎭 Demo Mode", value=False, help="Use pre-built mock data — no API key needed!")

    if demo_mode:
        st.success("Demo Mode ON — No API key needed!")
    else:
        runtime_key = st.text_input(
            "🔑 Override API Key (optional)",
            type="password",
            placeholder="sk-proj-...",
            help="Overrides the key in your .env file for this session."
        )
        if runtime_key:
            os.environ["OPENAI_API_KEY"] = runtime_key
            st.success("API key set for this session!")

    st.markdown("---")
    st.markdown("""**📦 Tech Stack**
- 🐍 Python + Streamlit
- 🤖 OpenAI GPT-4o-mini
- 📬 Gmail IMAP
- 🔗 4-Agent Pipeline""")

    st.markdown("---")
    st.caption("AI Recruiting Inbox · Hackathon 2026")


# ─────────────────────────────────────────────
# Mock data for Demo Mode
# ─────────────────────────────────────────────
MOCK_RESULTS = {
    'extracted': {
        'name': 'Alice Johnson',
        'skills': ['React', 'TypeScript', 'Node.js', 'AWS', 'GraphQL', 'REST APIs'],
        'experience_years': 5,
        'current_role': 'Frontend Engineer',
        'intent': 'Applying for Senior React Developer role'
    },
    'scored': {
        'score': 82,
        'verdict': 'Strong Hire',
        'matched_skills': ['React', 'TypeScript', 'GraphQL'],
        'missing_skills': ['CI/CD'],
        'reasoning': 'Alice demonstrates strong proficiency in the core React and TypeScript stack with 5 years of hands-on experience. Her GraphQL knowledge is a significant plus, though CI/CD experience appears limited. Overall a strong candidate worth interviewing.'
    },
    'action': {
        'action_type': 'Schedule Interview',
        'email_draft': (
            "Subject: Interview Invitation — Senior React Developer\n\n"
            "Hi Alice,\n\n"
            "Thank you for reaching out! We were impressed by your background in React, TypeScript, and GraphQL.\n\n"
            "We'd love to schedule a technical interview to explore your fit for the Senior React Developer role. "
            "Please let us know your availability for a 45-minute call this week or next.\n\n"
            "Looking forward to speaking with you!\n\n"
            "Best regards,\nThe Recruiting Team"
        ),
        'internal_notes': 'Strong candidate — prioritize scheduling within 48 hours; verify CI/CD experience during interview.'
    },
    'brief': {
        'tl_dr': 'Alice is a 5-year Frontend Engineer with solid React/TypeScript/GraphQL skills who is actively seeking a Senior React role — worth interviewing based on strong skill overlap.',
        'interview_questions': [
            'Walk me through how you have architected a large-scale React application — what state management patterns did you use and why?',
            'Describe a complex GraphQL schema you designed — how did you handle relationships, pagination, and performance?',
            'What is your experience with CI/CD pipelines? Have you set up any automated deployment workflows for frontend apps?'
        ],
        'red_flags': ['Limited CI/CD experience mentioned — worth probing in interview.']
    }
}

# ─────────────────────────────────────────────
# Initialize session state
# ─────────────────────────────────────────────
if 'results' not in st.session_state:
    st.session_state.results = None
if 'pipeline_done' not in st.session_state:
    st.session_state.pipeline_done = False
if 'sample_loaded' not in st.session_state:
    st.session_state.sample_loaded = False

# Pre-fill sample data defaults before widgets are created
if st.session_state.sample_loaded:
    if 'input_role' not in st.session_state:
        st.session_state['input_role'] = "Senior React Developer"
    if 'input_skills' not in st.session_state:
        st.session_state['input_skills'] = "React, TypeScript, GraphQL, CI/CD"
    if 'input_email' not in st.session_state:
        st.session_state['input_email'] = (
            "Hi, I'm Alice. I saw your job post for a Senior React Dev. "
            "I have 5 years of experience building scalable web apps using React, TypeScript, and Node.js. "
            "I've also worked a bit with AWS and some GraphQL. I'd love to chat about the role. "
            "Attached is my resume."
        )
    st.session_state.sample_loaded = False

# ─────────────────────────────────────────────
# Main Flow: Input or Results
# ─────────────────────────────────────────────
if not st.session_state.pipeline_done:

    # ── Input Section ──────────────────────────
    st.markdown('<div class="section-card">', unsafe_allow_html=True)
    col_left, col_right = st.columns([1, 1.4], gap="large")

    with col_left:
        st.markdown('<div class="section-title">⚙️ Job Configuration</div>', unsafe_allow_html=True)
        target_role = st.text_input(
            "Target Role",
            placeholder="e.g., Senior React Developer",
            key="input_role"
        )
        required_skills = st.text_input(
            "Required Skills",
            placeholder="e.g., React, TypeScript, GraphQL, CI/CD",
            key="input_skills"
        )

        # Sample data helper
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("📋 Load Sample Data", key="sample_btn"):
            # Clear existing widget state, set flag, then rerun — widgets will pick up new defaults
            for k in ["input_role", "input_skills", "input_email"]:
                if k in st.session_state:
                    del st.session_state[k]
            st.session_state.sample_loaded = True
            st.rerun()

    with col_right:
        st.markdown('<div class="section-title">📬 Candidate Email</div>', unsafe_allow_html=True)
        email_content = st.text_area(
            "Paste Raw Candidate Email",
            placeholder="Hi, I'm applying for your open role. I have 5 years of experience with React...",
            height=200,
            key="input_email"
        )

    st.markdown('</div>', unsafe_allow_html=True)

    # ── Process Button ─────────────────────────
    col_btn = st.columns([1, 2, 1])[1]
    with col_btn:
        process_clicked = st.button("🚀  Process Candidate", key="process_btn", use_container_width=True)

    if process_clicked:
        # Validate inputs
        if not target_role.strip():
            st.error("⚠️ Please enter a Target Role.")
            st.stop()
        if not required_skills.strip():
            st.error("⚠️ Please enter Required Skills.")
            st.stop()
        if not email_content.strip():
            st.error("⚠️ Please paste the candidate email.")
            st.stop()

        job_requirements = {
            "target_role": target_role.strip(),
            "required_skills": required_skills.strip()
        }

        # ── Pipeline execution with progress ──
        st.markdown("<br>", unsafe_allow_html=True)
        progress_placeholder = st.empty()

        results = {}

        if demo_mode:
            # ── Demo Mode: simulate pipeline with mock data ──
            steps = [
                ("Agent 1 / 4", "Extracting candidate profile...", 'extracted'),
                ("Agent 2 / 4", "Scoring against job requirements...", 'scored'),
                ("Agent 3 / 4", "Drafting execution steps...", 'action'),
                ("Agent 4 / 4", "Generating hiring manager brief...", 'brief'),
            ]
            for label, msg, key in steps:
                progress_placeholder.markdown(f"""
                <div class="pipeline-step pipeline-step-active">
                    ⏳ &nbsp;<strong>{label}</strong> — {msg}
                </div>""", unsafe_allow_html=True)
                with st.spinner(msg):
                    time.sleep(0.8)
                results[key] = MOCK_RESULTS[key]

            progress_placeholder.markdown("""
            <div class="pipeline-step pipeline-step-done">
                ✅ &nbsp;<strong>All 4 agents completed successfully! (Demo Mode)</strong>
            </div>""", unsafe_allow_html=True)
            time.sleep(0.5)

            st.session_state.results = results
            st.session_state.pipeline_done = True
            st.rerun()

        else:
            # ── Live Mode: call real OpenAI agents ──
            try:
                from agents.extractor import extract_candidate_info
                from agents.assessor import score_candidate
                from agents.coordinator import draft_action
                from agents.summarizer import generate_manager_brief

                # Step 1 — Extract
                progress_placeholder.markdown("""
                <div class="pipeline-step pipeline-step-active">
                    ⏳ &nbsp;<strong>Agent 1 / 4</strong> — Extracting candidate profile...
                </div>""", unsafe_allow_html=True)
                with st.spinner("Extracting candidate profile..."):
                    results['extracted'] = extract_candidate_info(email_content)

                # Step 2 — Score
                progress_placeholder.markdown("""
                <div class="pipeline-step pipeline-step-active">
                    ⏳ &nbsp;<strong>Agent 2 / 4</strong> — Scoring against job requirements...
                </div>""", unsafe_allow_html=True)
                with st.spinner("Scoring against job requirements..."):
                    results['scored'] = score_candidate(results['extracted'], job_requirements)

                # Step 3 — Draft action
                progress_placeholder.markdown("""
                <div class="pipeline-step pipeline-step-active">
                    ⏳ &nbsp;<strong>Agent 3 / 4</strong> — Drafting execution steps...
                </div>""", unsafe_allow_html=True)
                with st.spinner("Drafting execution steps..."):
                    results['action'] = draft_action(results['scored'], results['extracted'])

                # Step 4 — Manager brief
                progress_placeholder.markdown("""
                <div class="pipeline-step pipeline-step-active">
                    ⏳ &nbsp;<strong>Agent 4 / 4</strong> — Generating hiring manager brief...
                </div>""", unsafe_allow_html=True)
                with st.spinner("Generating hiring manager brief..."):
                    results['brief'] = generate_manager_brief(results['extracted'], results['scored'])

                # Done!
                progress_placeholder.markdown("""
                <div class="pipeline-step pipeline-step-done">
                    ✅ &nbsp;<strong>All 4 agents completed successfully!</strong>
                </div>""", unsafe_allow_html=True)

                st.session_state.results = results
                st.session_state.pipeline_done = True
                st.rerun()

            except Exception as e:
                progress_placeholder.empty()
                st.error(f"❌ Pipeline failed: {str(e)}")
                st.warning("💡 Tip: Enable **Demo Mode** in the sidebar to run a full demo without an API key!")

# ─────────────────────────────────────────────
# Results Dashboard
# ─────────────────────────────────────────────
else:
    results = st.session_state.results
    extracted = results.get('extracted', {})
    scored    = results.get('scored', {})
    action    = results.get('action', {})
    brief     = results.get('brief', {})

    # ── Score color logic ──────────────────────
    score_val = scored.get('score', 0)
    if score_val >= 80:
        score_color_cls = "score-green"
        score_emoji = "🟢"
    elif score_val >= 50:
        score_color_cls = "score-orange"
        score_emoji = "🟡"
    else:
        score_color_cls = "score-red"
        score_emoji = "🔴"

    verdict = scored.get('verdict', 'N/A')
    verdict_cls = {
        "Strong Hire": "verdict-strong",
        "Potential Fit": "verdict-potential",
        "Reject": "verdict-reject"
    }.get(verdict, "")

    action_type = action.get('action_type', 'N/A')
    action_cls = {
        "Schedule Interview": "action-interview",
        "Send Rejection": "action-rejection",
        "Request More Info": "action-info"
    }.get(action_type, "")

    action_emoji = {
        "Schedule Interview": "📅",
        "Send Rejection": "❌",
        "Request More Info": "❓"
    }.get(action_type, "📋")

    # ─────────────────────────────────────────
    # TOP METRICS ROW
    # ─────────────────────────────────────────
    st.markdown("### 📊 Pipeline Results")
    m1, m2, m3 = st.columns(3, gap="medium")

    with m1:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">🎯 Candidate Score</div>
            <div class="metric-value {score_color_cls}">{score_val}</div>
            <div class="metric-sub">{score_emoji} out of 100</div>
        </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">⚖️ Recruiter Verdict</div>
            <div class="metric-value {verdict_cls}" style="font-size:1.6rem; padding-top:0.4rem;">{verdict}</div>
            <div class="metric-sub">AI assessment</div>
        </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">⚡ Action Needed</div>
            <div class="metric-value {action_cls}" style="font-size:1.25rem; padding-top:0.6rem;">{action_emoji} {action_type}</div>
            <div class="metric-sub">automated recommendation</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # ─────────────────────────────────────────
    # CANDIDATE PROFILE + MANAGER BRIEF
    # ─────────────────────────────────────────
    st.markdown("### 👤 Candidate Profile")
    prof_col, brief_col = st.columns([1, 1], gap="large")

    with prof_col:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">Extracted Details</div>', unsafe_allow_html=True)

        name = extracted.get('name', 'Unknown')
        current_role = extracted.get('current_role', 'N/A')
        exp_years = extracted.get('experience_years', 0)
        intent = extracted.get('intent', 'N/A')

        st.markdown(f"""
        <div class="info-row">
            <span class="info-label">Name</span>
            <span class="info-value">{name}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Current Role</span>
            <span class="info-value">{current_role}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Experience</span>
            <span class="info-value">{exp_years} year{'s' if exp_years != 1 else ''}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Intent</span>
            <span class="info-value">{intent}</span>
        </div>
        <div class="info-row">
            <span class="info-label">Reasoning</span>
            <span class="info-value" style="font-size:0.85rem; color:rgba(255,255,255,0.6);">{scored.get('reasoning', '')}</span>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("<br>", unsafe_allow_html=True)

        # Matched skills
        matched = scored.get('matched_skills', [])
        missing = scored.get('missing_skills', [])

        if matched:
            st.markdown('<div class="section-title">✅ Matched Skills</div>', unsafe_allow_html=True)
            skills_html = "".join([f'<span class="skill-tag">{s}</span>' for s in matched])
            st.markdown(f'<div style="margin-bottom:1rem;">{skills_html}</div>', unsafe_allow_html=True)

        if missing:
            st.markdown('<div class="section-title">❌ Missing Skills</div>', unsafe_allow_html=True)
            miss_html = "".join([f'<span class="skill-tag skill-tag-missing">{s}</span>' for s in missing])
            st.markdown(f'<div>{miss_html}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    with brief_col:
        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown('<div class="section-title">📋 Hiring Manager Brief</div>', unsafe_allow_html=True)

        tl_dr = brief.get('tl_dr', '')
        red_flags = brief.get('red_flags', [])
        interview_qs = brief.get('interview_questions', [])

        st.markdown(f"""
        <div class="info-row" style="border:none; padding-bottom:1rem;">
            <span class="info-value" style="font-size:0.95rem; line-height:1.6; color:rgba(255,255,255,0.8);">{tl_dr}</span>
        </div>
        """, unsafe_allow_html=True)

        if red_flags:
            flags_md = "\n".join([f"- {f}" for f in red_flags])
            st.warning(f"**⚠️ Red Flags:**\n{flags_md}")
        else:
            st.success("✅ No red flags identified.")

        if interview_qs:
            st.markdown('<div class="section-title" style="margin-top:1rem;">🎤 Interview Questions</div>', unsafe_allow_html=True)
            for i, q in enumerate(interview_qs, 1):
                st.markdown(f'<div class="question-item"><strong>Q{i}:</strong> {q}</div>', unsafe_allow_html=True)

        st.markdown('</div>', unsafe_allow_html=True)

    # ─────────────────────────────────────────
    # AUTOMATED EXECUTION
    # ─────────────────────────────────────────
    st.markdown("### ⚡ Automated Execution")
    st.markdown('<div class="section-card">', unsafe_allow_html=True)

    internal_notes = action.get('internal_notes', '')
    email_draft = action.get('email_draft', '')

    if internal_notes:
        st.info(f"📌 **Internal Notes:** {internal_notes}")

    st.markdown('<div class="section-title" style="margin-top:1rem;">📧 Drafted Email Response</div>', unsafe_allow_html=True)
    st.markdown('<p style="color:rgba(255,255,255,0.5); font-size:0.85rem; margin-bottom:0.75rem;">Review and edit the email below before sending.</p>', unsafe_allow_html=True)

    edited_email = st.text_area(
        label="Email Draft (editable)",
        value=email_draft,
        height=280,
        key="email_draft_editor",
        label_visibility="collapsed"
    )

    st.markdown('</div>', unsafe_allow_html=True)

    # ─────────────────────────────────────────
    # Process Another Email Button
    # ─────────────────────────────────────────
    st.markdown("<br>", unsafe_allow_html=True)
    col_reset = st.columns([1, 2, 1])[1]
    with col_reset:
        if st.button("🔄  Process Another Email", key="reset_btn", use_container_width=True):
            st.session_state.results = None
            st.session_state.pipeline_done = False
            # Clear input fields
            for key in ["input_role", "input_skills", "input_email"]:
                if key in st.session_state:
                    del st.session_state[key]
            st.rerun()

    # ── Footer ───────────────────────────────
    st.markdown("""
    <hr>
    <div style="text-align:center; color:rgba(255,255,255,0.25); font-size:0.8rem; padding: 1rem 0;">
        🤖 AI Recruiting Inbox &nbsp;·&nbsp; Powered by OpenAI GPT-4o-mini &nbsp;·&nbsp; 4-Agent Pipeline
    </div>
    """, unsafe_allow_html=True)
