import openai
import os

# Set your OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_bdd_scenario(app_description):
    """Generates a BDD feature file using OpenAI's GPT model."""
    prompt = f"Generate a BDD feature file for the following application:\n{app_description}\n\nFeature: "
    
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",  # Adjust model as needed (gpt-3.5-turbo or gpt-4)
        messages=[{"role": "user", "content": prompt}],
        max_tokens=300
    )

    return response.choices[0].message.content  # Correct response format

def save_feature_file(feature_text, filename="features/generated_feature.feature"):
    """Saves the AI-generated BDD feature text to a file."""
    os.makedirs("features", exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(feature_text)

if __name__ == "__main__":
    app_desc = "A banking web application where users can log in, view account details, and transfer funds."
    feature_text = generate_bdd_scenario(app_desc)
    save_feature_file(feature_text)
    print(f"✅ AI-generated feature saved to features/generated_feature.feature")
