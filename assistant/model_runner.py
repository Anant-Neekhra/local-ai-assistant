import ollama

def run_model(model_name, prompt):

    response = ollama.chat(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']