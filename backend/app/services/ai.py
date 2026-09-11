import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise RuntimeError("OPENAI_API_KEY is not configured")

client = OpenAI(api_key=api_key)


def ask_tutor(question: str) -> str:
    response = client.responses.create(
        model="gpt-5.6-luna",
        instructions=(
            "You are Toppers Path AI, an educational assistant for "
            "Toppers Path Academy. Help students prepare for ECET and "
            "technical subjects. Explain concepts clearly, step by step. "
            "Use formulas and simple examples when appropriate. "
            "Do not invent information from Toppers Path study material "
            "when that material has not been provided."
        ),
        input=question,
    )

    return response.output_text
