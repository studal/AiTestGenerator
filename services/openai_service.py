import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4")  # Default to gpt-4 if not set

client = OpenAI(api_key=OPENAI_API_KEY)


def generate_tests(system_prompt: str, user_prompt: str) -> str:
    """
    Sends prompt to OpenAI and returns generated response.
    """
    final_prompt = f"""
SYSTEM PROMPT:
{system_prompt}

USER INPUT:
{user_prompt}
"""

    response = client.chat.completions.create(
        model=OPENAI_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )

    return response.choices[0].message.content