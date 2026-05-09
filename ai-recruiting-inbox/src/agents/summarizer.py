import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def generate_manager_brief(extracted_data: dict, scored_candidate: dict) -> dict:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    system_prompt = "You are an executive assistant to the hiring manager. Review the candidate's profile and assessment, and create a brief for the hiring manager. Return ONLY a raw JSON object with no markdown and no explanation with these exact keys: tl_dr (1-2 sentence summary of who they are and if worth interviewing), interview_questions (list of exactly 3 specific highly technical questions), red_flags (list of concerns or gaps, can be empty)."

    user_message = f"Extracted Data: {extracted_data}\nScored Assessment: {scored_candidate}"

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

        brief_data = json.loads(raw_response)
        print("Manager brief generated.")
        return brief_data

    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON response: {e}")
    except Exception as e:
        raise RuntimeError(f"Error during brief generation: {e}")