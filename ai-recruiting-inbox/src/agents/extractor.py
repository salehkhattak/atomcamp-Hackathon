import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

def extract_candidate_info(email_content: str) -> dict:
    client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    system_prompt = "You are an expert AI recruiting assistant. Extract the candidate's details from the raw email text and return ONLY a raw JSON object with no markdown and no explanation with these exact keys: name (string, candidate's full name or 'Unknown'), skills (list of strings, technical skills and tools mentioned), experience_years (integer, extract or estimate total years, use 0 if unknown), current_role (string, their current or most recent job title), intent (string, what they are asking for, e.g., 'Applying for Backend role')."

    user_message = email_content

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

        extracted_data = json.loads(raw_response)
        print(f"Extraction complete for: {extracted_data['name']}")
        return extracted_data

    except json.JSONDecodeError as e:
        raise ValueError(f"Failed to parse JSON response: {e}")
    except Exception as e:
        raise RuntimeError(f"Error during extraction: {e}")