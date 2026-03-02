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

    answer = run_model(model_name, prompt)

    print("\nAnswer:")
    print(answer)