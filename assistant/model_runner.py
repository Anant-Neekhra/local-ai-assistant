import ollama
import json
from assistant.schema import AssistantResponse


def run_model(model_name, prompt, temperature=0):

    structured_prompt = f"""
You are a structured AI assistant.

Respond ONLY in valid JSON format:

{{
  "answer": "string",
  "confidence": float between 0 and 1
}}

Question:
{prompt}
"""

    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": structured_prompt}],
        options={"temperature": temperature}
    )

    raw_output = response['message']['content']

    try:
        parsed_json = json.loads(raw_output)
        validated = AssistantResponse(**parsed_json)
        return validated

    except Exception as e:
        raise ValueError(f"Invalid model output: {e}")