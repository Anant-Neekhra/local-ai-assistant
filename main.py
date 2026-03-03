from assistant.config import MODELS
from assistant.model_runner import run_model

print("Local AI Assistant\n")

print("Select Model:")

for key in MODELS:
    print(f"{key} -> {MODELS[key]}")

choice = input("\nEnter choice: ")

model_name = MODELS.get(choice)

if model_name is None:
    print("Invalid choice")
    exit()

print("\nUsing model:", model_name)

while True:

    prompt = input("\nAsk (type exit to quit): ")

    if prompt == "exit":
        break

    try:
        result = run_model(model_name, prompt, temperature=0)

        print("\nAnswer:")
        print(result.answer)
        print("Confidence:", result.confidence)

    except Exception as e:
        print("\nError:", e)
        print("Retrying once...\n")

        try:
            result = run_model(model_name, prompt, temperature=0)
            print("\nAnswer:")
            print(result.answer)
            print("Confidence:", result.confidence)

        except:
            print("Model failed twice. Skipping.")