import time
import psutil
import ollama


def get_ollama_memory():
    total_memory = 0

    for proc in psutil.process_iter(['name', 'memory_info']):
        try:
            if proc.info['name'] and "ollama" in proc.info['name'].lower():
                total_memory += proc.info['memory_info'].rss
        except:
            pass

    return total_memory / (1024 ** 3)


def benchmark_model(model_name, prompt, temperature=0):

    start_time = time.time()

    response = ollama.chat(
        model=model_name,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": temperature}
    )

    end_time = time.time()

    total_latency = end_time - start_time

    output_text = response['message']['content']

    char_count = len(output_text)

    estimated_tokens = char_count / 4

    tokens_per_second = estimated_tokens / total_latency if total_latency > 0 else 0

    memory_usage_gb = get_ollama_memory()

    return {
        "model": model_name,
        "latency": total_latency,
        "tokens": estimated_tokens,
        "tokens_per_second": tokens_per_second,
        "memory_usage_gb": memory_usage_gb
    }