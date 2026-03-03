from assistant.config import MODELS
from assistant.model_runner import run_model
from assistant.benchmark import benchmark_model

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

mode = input("\nChoose mode: (1) Chat  (2) Benchmark : ")

if mode == "1":

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

elif mode == "2":

    prompt = input("\nEnter prompt for benchmarking: ")

    stats = benchmark_model(model_name, prompt)

    print("\nBenchmark Results:")
    print("Model:", stats["model"])
    print("Latency:", round(stats["latency"], 2), "seconds")
    print("Tokens:", stats["tokens"])
    print("Tokens/sec:", round(stats["tokens_per_second"], 2))
    print("Memory Usage:", round(stats["memory_usage_gb"], 2), "GB")

else:
    print("Invalid mode selected.")