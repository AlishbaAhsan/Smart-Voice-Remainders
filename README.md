# 🪄 AI Magical Reminder Generator
Turn your ordinary reminders into delightful, personality-rich audio messages!
This app uses the open-source openchat:latest model (powered by Ollama) to turn your event descriptions into cheerful, whimsical reminders. It then brings them to life with AI-generated speech, producing an audio file you can listen to or download.


# ✨ Features
- Open-Source AI Magic: Creative text generation powered by the open-source `openchat:latest` model.
- Magical Reminders: Converts plain event text into fun, expressive, and supportive reminders.
- Text-to-Speech: Instantly generates an MP3 audio file for your reminder using OpenAI’s TTS.
- Streamlit Web App: Simple, interactive interface—no coding required!
- Personalized: Weaves your name and event details into every reminder.
- Download & Listen: Play your reminder in the browser or download it for later.

# 🚀 Demo

![Screenshot from 2025-06-26 14-51-41](https://github.com/user-attachments/assets/2a6388b1-0518-4d5f-ab65-c92aefdf72b9)
Just type your name and event, click "Generate Reminder", and get your magical audio!

# 🛠️ Getting Started

1. Clone the Repository
```bash
git clone https://github.com/<your-username>/<repo-name>.git](https://github.com/AlishbaAhsan/Smart-Voice-Remainders.git
```

2. Set Up Your Environment
- Create the virtual enviornment and activate it.
```bash
 python3 -m venv venv
source venv/bin/activate
```
- Install dependencies.
```bash
pip install -r requirnments.txt
```

3. Configure your API Keys
- Create a new .env file in the project root.
```bash
  OPENAI_API_KEY=your_openai_api_key_here
  OLLAMA_API_KEY=your_ollama_api_key_here
  OLLAMA_BASE_URL=your_ollama_base_url_here
```

4. Run the app
```bash
streamlit run streamlit_app.py
```

# 📦 Project Strcuture
```text
ai_remainders.py     # Core logic for AI and TTS
streamlit_app.py     # Streamlit web interface
remainders/          # Generated MP3 files
requirements.txt     # Python dependencies
.env                 # (Not included) Your API keys
```

#   ⚡ Why You'll Love It
Makes reminders fun and memorable
Perfect for personal productivity, family, or team use
Easy to deploy and extend

# 🛡️ License
Feel free to use, modify, and share!

# 🙌 Contributing
Pull requests and stars are welcome!
For major changes, please open an issue first to discuss what you’d like to change.

# 📬 Contact
Questions or suggestions?
Open an issue or reach out at alishbaahsan127@gmail.com
