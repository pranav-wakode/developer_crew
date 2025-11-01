# AI Developer Crew

This is a multi-agent system built with CrewAI that can research and write code.

## 🚀 Setup

1.  **Install Ollama:** [https://ollama.com/](https://ollama.com/)
2.  **Pull the model:**
    ```bash
    ollama pull yxchia/qwen2.5-3b-instruct:Q4_K_M
    ```
3.  **Create virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🏃‍♀️ Run

1.  **Start the Ollama server:**
    ```bash
    ollama serve
    ```
2.  **Run the crew (in a new terminal):**
    ```bash
    python3 main.py
    ```