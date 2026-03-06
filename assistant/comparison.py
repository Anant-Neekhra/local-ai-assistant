import csv
from assistant.config import MODELS
from assistant.benchmark import benchmark_model


def run_model_comparison(prompts_file="test_prompts.txt"):

    results = []

    with open(prompts_file, "r", encoding="utf-8") as f:
        prompts = [line.strip() for line in f if line.strip()]

    for model_key, model_name in MODELS.items():

        print(f"\nTesting model: {model_name}")

        for prompt in prompts:

            print(f"Prompt: {prompt}")

            stats = benchmark_model(model_name, prompt)

            results.append({
                "model": model_name,
                "prompt": prompt,
                "latency": round(stats["latency"], 2),
                "tokens_per_second": round(stats["tokens_per_second"], 2),
                "memory_gb": round(stats["memory_usage_gb"], 2)
            })

    save_results(results)


def save_results(results):

    with open("results/model_comparison.csv", "w", newline="", encoding="utf-8") as csvfile:

        fieldnames = ["model", "prompt", "latency", "tokens_per_second", "memory_gb"]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        for row in results:
            writer.writerow(row)

    print("\nComparison results saved to results/model_comparison.csv")