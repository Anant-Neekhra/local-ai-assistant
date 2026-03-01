import ollama

model = "llama3.2"

while True:

    prompt = input("\nAsk: ")

    if prompt == "exit":
        break

    response = ollama.chat(
        model=model,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    print("\nAnswer:")
    print(response['message']['content'])