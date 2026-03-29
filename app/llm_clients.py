import os
import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def extract_with_llm(text: str) -> dict:
    prompt = f"""
Extract these fields from the text below:
name, company, role, email

Return ONLY valid JSON with these keys:
name
company
role
email

If any field is missing, use null.

Text:
{text}
"""

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0
    )

    content = response.choices[0].message.content.strip()

    try:
        return json.loads(content)
    except json.JSONDecodeError:
        return {
            "name": None,
            "company": None,
            "role": None,
            "email": None
        }