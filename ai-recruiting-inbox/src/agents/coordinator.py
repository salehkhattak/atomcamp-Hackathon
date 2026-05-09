import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def draft_action(scored_candidate: dict, extracted_data: dict) -> dict:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    system_prompt = "You are a recruiting execution agent. Based on the candidate's score and verdict, determine the next step and draft an email response. Return ONLY a raw JSON object with no markdown and no explanation with these exact keys: action_type (one of 'Schedule Interview', 'Send Rejection', 'Request More Info'), email_draft (fully written professional email to candidate), internal_notes (1-sentence note for recruiting team)."

    user_message = f"Candidate Name: {extracted_data['name']}\nIntent: {extracted_data['intent']}\nScored Data: {scored_candidate}"

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

        action_data = json.loads(raw_response)
        print(f"Action drafted: {action_data['action_type']}")
        return action_data

    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON response: {e}")
    except Exception as e:
        raise RuntimeError(f"Error during action drafting: {e}")