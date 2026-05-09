from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from crewai import Agent, Task, Crew, Process
import os

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = "your_openai_api_key"

app = FastAPI()

# CRITICAL FOR HACKATHONS: Enable CORS so Next.js can talk to FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, restrict this to your Next.js localhost port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define the data Next.js will send
class EmailPayload(BaseModel):
    email_content: str
    target_role: str

# --- 1. DEFINE YOUR AGENTS ---
extractor_agent = Agent(
    role='Data Extraction Specialist',
    goal='Extract candidate details (Name, Skills, Experience) from raw emails.',
    backstory='You are an expert at parsing unstructured text into clean data.',
    verbose=True,
    allow_delegation=False
)

assessor_agent = Agent(
    role='Technical Recruiter Assessor',
    goal='Evaluate extracted candidate data against the target role and score them out of 100.',
    backstory='You are a senior technical recruiter with a keen eye for top talent.',
    verbose=True,
    allow_delegation=False
)

# --- 2. FASTAPI ENDPOINT ---
@app.post("/api/process-email")
async def process_email(payload: EmailPayload):
    
    # Define Tasks based on the incoming data
    extract_task = Task(
        description=f"Extract details from this email: {payload.email_content}",
        expected_output="A JSON format containing name, skills, and years of experience.",
        agent=extractor_agent
    )
    
    score_task = Task(
        description=f"Based on the extracted data, score the candidate's fit for the role: {payload.target_role}. Provide the final output as a simple JSON with 'score', 'status' (Approved/Rejected based on >80 score), and 'reasoning'.",
        expected_output="JSON containing score, status, and reasoning.",
        agent=assessor_agent
    )

    # Assemble the Crew
    recruiting_crew = Crew(
        agents=[extractor_agent, assessor_agent],
        tasks=[extract_task, score_task],
        process=Process.sequential # Agents run one after another
    )

    # Start the agent workflow!
    result = recruiting_crew.kickoff()
    
    # Return the agent's final decision back to Next.js
    return {"status": "success", "agent_analysis": result.raw}