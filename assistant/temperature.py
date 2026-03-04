from assistant.model_runner import run_model


def run_temperature_experiment(model_name, prompt):

    temperatures = [0, 0.3, 0.7]

    results = {}

    for temp in temperatures:
        try:
            response = run_model(model_name, prompt, temperature=temp)
            results[temp] = response.answer
        except Exception as e:
            results[temp] = f"Error: {e}"
    with open("results/temperature_results.txt", "a", encoding="utf-8") as f:

        f.write(f"\nModel: {model_name}\n")
        f.write(f"Prompt: {prompt}\n")

        for temp, output in results.items():
            f.write(f"\nTemperature {temp}:\n")
            f.write(output + "\n")

        f.write("\n" + "=" * 60 + "\n")
        
    return results