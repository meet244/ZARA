# ZARA - Zingi Autonomous Response Assistant 🤖

![Banner](https://github.com/meet244/ZARA/assets/83262693/330b129f-54c7-4ef3-9ffc-4cbba1be036c)

ZARA (Zingi Autonomous Response Assistant) is a virtual assistant powered by a customtkinter GUI and backed by Hugging Face models. It can answer questions and perform tasks using natural language processing. 🌐

## Features ✨

ZARA can handle various queries and tasks, including:
- Opening applications (e.g., "open chrome") 🖥️
- Coding tasks (e.g., "make a simple hi program in java") 💻
- Riddles and puzzles 🧩
- Temperature inquiries (e.g., "current temperature at New York") ☀️❄️
- Navigation and travel queries (e.g., "take me from Mumbai to Goa") 🗺️✈️
- Playing music (e.g., "play 'Aaisa Dekha Nahi Khubsoorat Koi'") 🎵🎶
- Setting alarms and timers ⏰⏳
- Answering general knowledge questions (e.g., "tallest building in the world") 🏢⁉️
- Engaging in casual conversation (e.g., "what is your name?") 💬


## Demo Video 📽️

[![Demo Video](https://github.com/meet244/ZARA/assets/83262693/120112b5-1df7-4feb-b7a1-2092f5324fb2)](https://github.com/meet244/ZARA/assets/83262693/120112b5-1df7-4feb-b7a1-2092f5324fb2)

## How to Interact 🗣️💬

Users can interact with ZARA by saying "Hey Zara" or by typing in the GUI. ZARA's responses are accompanied by Text-to-Speech (TTS) output for a more interactive experience. 🗨️🔊

## Getting Started 🚀

To use ZARA, you'll need to set up API keys by creating a `.env` file in the project directory with the following keys:
- `HUGGINGFACEHUB_API_TOKEN`: Hugging Face API key from [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)
- `NEWSAPI_KEY`: NewsAPI.org API key from [https://newsapi.org/](https://newsapi.org/)
- `WOLFARM_API`: Wolfram Alpha API key from [https://developer.wolframalpha.com/](https://developer.wolframalpha.com/)
- `PORCUPINE_API`: Picovoice Porcupine API key from [https://console.picovoice.ai/](https://console.picovoice.ai/)

## Installation ⚙️

1. Clone the repository:
   ```sh
   git clone https://github.com/meet244/ZARA.git
   cd ZARA
   ```

2. Install required Python packages:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the application:
   ```sh
   python main.py
   ```

## Used Python Modules 📦

This project relies on various Python modules to achieve its functionality. Here is a list of the modules that are being used:

- `json`: For working with JSON data.
- `time`: For time-related operations.
- `pygame`: For creating games and multimedia applications.
- `os`: For interacting with the operating system.
- `pyaudio`: For working with audio.
- `requests`: For making HTTP requests.
- `wolframalpha`: For querying Wolfram Alpha computational knowledge engine.
- `re`: For regular expressions.
- `subprocess`: For running subprocesses.
- `wikipedia`: For interacting with Wikipedia articles.
- `datetime`: For working with dates and times.
- `BeautifulSoup`: For parsing HTML and XML documents.
- `dotenv`: For loading environment variables from a file.
- `streamlit`: For creating interactive web applications.
- `langchain`: A library related to language generation.
- `final`: It's not clear which module/package this refers to.
- `pvporcupine`: For keyword detection.
- `pyttsx3`: For text-to-speech conversion.
- `speech_recognition`: For speech recognition.
- `customtkinter`: It's not clear which module/package this refers to.
- `PIL`: For working with images.
- `markdown2`: For converting Markdown to HTML.
- `threading`: For working with threads.
- `timeIsImportant`: It's not clear which module/package this refers to.
- `programs`: It's not clear which module/package this refers to.
- `openAssist`: It's not clear which module/package this refers to.
- `flans`: It's not clear which module/package this refers to.
- `pywhatkit`: For performing various tasks using the web.
- `pyautogui`: For programmatically controlling the mouse and keyboard.

## Acknowledgments 🙌

ZARA uses the following libraries and APIs:
- CustomTkinter: [https://customtkinter.tomschimansky.com/](https://customtkinter.tomschimansky.com/)
- Hugging Face: [https://huggingface.co/](https://huggingface.co/)
- OpenAssistant API: [https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5](https://huggingface.co/OpenAssistant/oasst-sft-4-pythia-12b-epoch-3.5)

## Contribution 🤝

Feel free to contribute, report issues, and give suggestions!

Note: This project is not affiliated with the services and APIs mentioned above. 🚫📡
