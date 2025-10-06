from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_text(
    input: str,
    model: str = "gpt-4o-mini",
    instructions: str | None = None,
    temperature: float = 0.2,
    max_output_tokens: int = 300,
    previous_response_id: str | None = None,
) -> dict:
    response = client.responses.create(
        model=model,
        input=input,
        instructions=instructions,
        temperature=temperature,
        max_output_tokens=max_output_tokens,
        previous_response_id=previous_response_id,
    )
    return {"id": response.id, "text": response.output_text}
