from assistant.config import MODELS
from assistant.model_runner import run_model
from assistant.benchmark import benchmark_model
from assistant.temperature import run_temperature_experiment
from assistant.comparison import run_model_comparison

print("Local AI Assistant\n")

mode = input("\nChoose mode: (1) Chat (2) Benchmark (3) Temperature Test (4) Model Comparison : ")

if mode in ["1", "2", "3"]:

    print("\nSelect Model:")

    for key in MODELS:
        print(f"{key} -> {MODELS[key]}")

    choice = input("\nEnter choice: ")

    model_name = MODELS.get(choice)

    if model_name is None:
        print("Invalid model choice")
        exit()

    print("\nUsing model:", model_name)

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

elif mode == "3":

    prompt = input("\nEnter prompt for temperature testing: ")

    results = run_temperature_experiment(model_name, prompt)

    print("\nTemperature Experiment Results:\n")

    for temp, output in results.items():
        print(f"\n--- Temperature {temp} ---")
        print(output)

elif mode == "4":

    print("\nRunning model comparison across all prompts and models...\n")

    run_model_comparison()

else:
    print("Invalid mode selected.")