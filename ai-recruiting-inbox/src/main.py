import os
from dotenv import load_dotenv
from agents.extractor import extract_candidate_info
from agents.assessor import score_candidate
from agents.coordinator import draft_action
from agents.summarizer import generate_manager_brief

# Load environment variables from .env file
load_dotenv()

# Check for OPENAI_API_KEY
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise EnvironmentError("ERROR: OPENAI_API_KEY missing.")

# Hardcoded test email
test_email = "Hi, I'm Alice. I saw your job post for a Senior React Dev. I have 5 years of experience building scalable web apps using React, TypeScript, and Node.js. I've also worked a bit with AWS. I'd love to chat about the role. Attached is my resume."

# Hardcoded job requirements
job_requirements = {
    "target_role": "Senior React Developer",
    "required_skills": "React, TypeScript, GraphQL, CI/CD"
}

try:
    # Run the full pipeline
    extracted_data = extract_candidate_info(test_email)
    print(f"Extracted Name: {extracted_data['name']}")
    print(f"Extracted Skills: {extracted_data['skills']}")

    scored_candidate = score_candidate(extracted_data, job_requirements)
    print(f"Score: {scored_candidate['score']}")
    print(f"Verdict: {scored_candidate['verdict']}")

    action_data = draft_action(scored_candidate, extracted_data)
    print(f"Action Type: {action_data['action_type']}")

    manager_brief = generate_manager_brief(extracted_data, scored_candidate)
    print(f"TL;DR: {manager_brief['tl_dr']}")

    print("Pipeline complete.")

except Exception as e:
    print(f"Pipeline failed: {e}")