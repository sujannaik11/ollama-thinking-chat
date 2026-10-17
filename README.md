# Ollama Thinking Chat

A simple AI chat application built with Python, Ollama, and the Qwen 3.5 0.8B model. It runs locally on your computer and accepts user questions through the terminal.

## Features

- Uses the Qwen 3.5 0.8B language model.
- Supports thinking mode with `think=True`.
- Generates AI responses from user prompts.
- Runs locally using Ollama.
- Allows configurable response generation settings.

## Technologies Used

- Python
- Ollama
- Qwen 3.5 0.8B

## Requirements

- Python 3.10 or later
- Ollama installed on your computer
- Qwen 3.5 0.8B model downloaded locally

## Installation

**1. Install Ollama**

Download Ollama from https://ollama.com/

**2. Download the model**

Open your terminal and run:

```bash
ollama pull qwen3.5:0.8b
```

**3. Clone this repository**

```bash
git clone YOUR_REPOSITORY_URL
cd ollama-thinking-chat
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

**4. Install the Python dependency**

```bash
pip install ollama
```

**5. Run the application**

```bash
python prompt.py
```

Make sure the Ollama service is running before starting the application.

## How It Works

The application receives a question from the user, sends it to the locally running Qwen model through the Ollama Python client, and displays the generated response in the terminal. Thinking mode can be enabled to request reasoning output from the model.

## Project Structure

```text
ollama-thinking-chat/
├── prompt.py
├── README.md
└── requirements.txt
```

## Configuration

The application connects to Ollama at `http://localhost:11434`. The model name, thinking mode, and generation settings can be configured in `prompt.py`.

## Note

The AI model runs locally and is not included in this repository. Response speed depends on your computer's hardware and the model's generation settings.

## License

This project is available for educational and personal use.
