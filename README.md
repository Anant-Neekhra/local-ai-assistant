# Local AI Assistant with SLM Benchmarking

## Project Overview

This project implements a **local AI assistant using Small Language Models (SLMs)** running entirely offline through **Ollama**.

The system allows users to interact with local models and perform structured experiments to evaluate their performance. The project benchmarks different models on the same hardware and analyzes the tradeoffs between **latency, speed, memory usage, and output quality**.

The goal is to demonstrate practical understanding of **local LLM deployment under real-world constraints**, including privacy, hardware limitations, inference speed, and model efficiency.

---

## Features

* Run **small language models locally** using Ollama
* Structured AI responses using **Pydantic validation**
* Benchmark model inference performance
* Perform **temperature experiments** to study output variance
* Compare multiple models using identical prompts
* Evaluate **quality vs speed tradeoffs**
* Run **quantized model experiments** for performance optimization
* Log experiment results for reproducibility

---

## Project Architecture

The system follows a modular architecture separating model execution, benchmarking, and experimentation.

User
  ↓
main.py (CLI Interface)
  ↓
Assistant Modules
   ├── model_runner.py
   ├── benchmark.py
   ├── temperature.py
   └── comparison.py
  ↓
Ollama
  ↓
Local Small Language Models

### Core Modules

| File            | Responsibility                           |
| --------------- | ---------------------------------------- |
| config.py       | Stores model configurations              |
| model_runner.py | Handles LLM interaction                  |
| schema.py       | Validates structured responses           |
| benchmark.py    | Measures latency, tokens/sec, and memory |
| temperature.py  | Runs temperature experiments             |
| comparison.py   | Runs automated model comparison          |

---

## Installation

### 1. Install Ollama

Install Ollama from the official website:

https://ollama.com

---

### 2. Clone the Repository

git clone https://github.com/Anant-Neekhra/local-ai-assistant
cd local-ai-assistant

---

### 3. Install Dependencies

pip install -r requirements.txt

---

### 4. Pull Models

ollama pull llama3.2
ollama pull mistral
ollama pull phi

---

## Usage

Run the assistant:

python main.py

You will see the following modes:

1 -> Chat with local model
2 -> Benchmark model performance
3 -> Temperature experiment
4 -> Model comparison study

---

## Benchmark Results

Each model was benchmarked on the same hardware using identical prompts.

| Model    | Avg Latency   | Tokens/sec     | Memory   |
| -------- | ------------- | -------------- | -------- |
| Phi      | ~2.7 seconds  | ~40 tokens/sec | ~0.51 GB |
| Llama3.2 | ~12.8 seconds | ~28 tokens/sec | ~0.84 GB |
| Mistral  | ~29 seconds   | ~7 tokens/sec  | ~2.28 GB |

### Observations

* **Phi** provides extremely fast inference with minimal memory usage.
* **Llama3.2** provides a balanced tradeoff between performance and quality.
* **Mistral** requires more compute but may provide stronger reasoning capabilities.

---

## Temperature Experiments

Temperature experiments were performed to study output determinism and randomness.

| Temperature | Behavior                            |
| ----------- | ----------------------------------- |
| 0           | Deterministic output                |
| 0.3         | Slight variation in phrasing        |
| 0.7         | More creative and diverse responses |

Higher temperatures increase randomness but may reduce response stability.

---

## Model Comparison Study

Each model was evaluated on a set of prompts including:

Explain recursion
Explain what Earth is
Write a Python quicksort implementation
Solve 2x + 3 = 11
Explain neural networks

Metrics measured:

* Inference latency
* Token generation speed
* Memory usage

Results were stored in:

results/model_comparison.csv

---

## Quantization Study

Quantization experiments were performed to analyze the effect of model compression on performance.

| Model      | Latency | Memory Usage |
| ---------- | ------- | ------------ |
| Mistral    | slow    | high         |
| Mistral Q5 | medium  | medium       |
| Mistral Q4 | fast    | low          |

### Observations

Quantization significantly reduces memory usage and improves inference speed. However, aggressive quantization may slightly reduce output quality.

---

## Key Insights

This project demonstrates several important aspects of local AI deployment:

* Running models locally ensures **privacy and full data control**
* Smaller models provide **fast inference with minimal hardware requirements**
* Larger models provide **better reasoning but require more resources**
* **Quantization** is an effective technique for optimizing local AI systems
* Benchmarking and evaluation are essential for understanding model tradeoffs

---

## Repository Structure

local-ai-assistant/

assistant/
   benchmark.py
   comparison.py
   config.py
   model_runner.py
   schema.py
   temperature.py

results/
   model_comparison.csv
   temperature_results.txt

main.py
requirements.txt
test_prompts.txt
README.md

---

## Future Improvements

Potential improvements for this project include:

* Adding GPU benchmarking support
* Adding visualization for benchmark results
* Expanding prompt datasets
* Building a web interface using FastAPI or Streamlit
* Adding automated experiment reports

---

## Conclusion

This project demonstrates how small language models can be deployed locally and evaluated systematically. By combining structured outputs, benchmarking, and experimentation, it provides insight into the practical tradeoffs involved in local AI systems.

The framework can be extended to evaluate new models and experiment with different deployment strategies.

---
