import openai
import json
from utils.context_extractor import extract_context

openai.api_key = "your-openai-api-key"

def generate_bdd_scenarios(context):
    prompt = f"Generate BDD scenarios for the following web page elements: {json.dumps(context)}"

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": prompt}]
    )

    return response["choices"][0]["message"]["content"]

if __name__ == "__main__":
    context = extract_context("https://example.com")
    print(generate_bdd_scenarios(context))
