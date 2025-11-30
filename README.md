## Ollama-Powered Local Chatbot (Streamlit + LangChain + LLMs)

- A fully local, privacy-friendly AI chatbot built using Streamlit, LangChain, and Ollama.
- This project allows users to run a high-performance LLM (like Llama 3, Mistral, Gemma, Phi-3) directly on their machine without relying on cloud APIs.

### Perfect for:

- Offline Chatbots

- Privacy-focused assistants

- Fast local LLM experimentation

- Students, researchers, hobbyists

#### ⚠️ IMPORTANT — REQUIREMENTS

This chatbot uses Ollama for LLM inference.
To run this project, you must install Ollama on your local machine.

#### 👉 Install Ollama:
https://ollama.com/download

Without Ollama, the chatbot will not run.

#### 🧠 Features

✔ Runs fully locally — no API keys required
✔ Uses LangChain for LLM invocation
✔ Built with Streamlit for an interactive UI
✔ Supports any Ollama model (Llama, Mistral, Gemma, Phi, Qwen, etc.)
✔ Clean modular code
✔ Easy to extend for RAG, Memory, Tools, API Agents

#### 📦 Tech Stack
Python 3.10+	Main programming language
Streamlit	UI layer
LangChain	LLM interface + chaining
Ollama	Local LLM server
httpx	Model communication
GitHub Actions	CI/CD (optional)