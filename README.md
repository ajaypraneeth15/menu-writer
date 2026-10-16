 # Menu Description Writer

A small offline tool that writes appetizing English menu descriptions for local restaurants and tea shops in Tamil Nadu.

## Why open-source AI?

- **Private:** The restaurant's menu and prices never leave the computer.
- **Free to run:** No API fees, so even a small shop can afford it.
- **Works offline:** No internet needed once the model is downloaded.
- **Swappable:** Change one line of code to try a different model (Llama, Qwen, etc.).

## Built with

- Gemma 3 (4B) running locally through Ollama
- Python and Streamlit

## How to run

1. Install Ollama and run: `ollama pull gemma3:4b`
2. Install the libraries: `pip install ollama streamlit`
3. Start the app: `python -m streamlit run app.py`

## Honest limitations

The 4B model writes good English, but its Tamil was unreliable (some outputs were meaningless). So the shop owner types the Tamil dish name, and the model writes only the English description.
