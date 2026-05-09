import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def score_candidate(extracted_data: dict, job_requirements: dict) -> dict:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    system_prompt = "You are a senior technical recruiter. Evaluate the candidate's extracted data against the job requirements. Return ONLY a raw JSON object with no markdown and no explanation. The object must have these exact keys: score (integer 0-100 based on skill overlap and experience), verdict (one of 'Strong Hire', 'Potential Fit', 'Reject'), matched_skills (list of skills they have that match), missing_skills (list of required skills they lack), reasoning (2-3 sentences explaining score and verdict)."

    user_message = f"Extracted Data: {extracted_data}\nJob Requirements: {job_requirements}"

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message}
            ]
        )

        raw_response = response.choices[0].message.content.strip()
        # Strip any markdown if present
        if raw_response.startswith('```json'):
            raw_response = raw_response[7:]
        if raw_response.endswith('```'):
            raw_response = raw_response[:-3]
        raw_response = raw_response.strip()

        scored_data = json.loads(raw_response)
        print(f"Scoring complete. Verdict: {scored_data['verdict']}")
        return scored_data

    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON response: {e}")
    except Exception as e:
        raise RuntimeError(f"Error during scoring: {e}")