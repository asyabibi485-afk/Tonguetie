
# TongueTie — Complete Multilingual Language Learning App

TongueTie is a Figma-inspired multilingual learning application with a Streamlit backend and an interactive browser prototype.

## Included
- 100+ language choices
- Gemini-powered AI tutor
- Translation
- Grammar and writing correction
- Vocabulary / difficult-word analysis
- Lesson generation
- Quiz/test generation
- Progress dashboard
- Voice recording UI
- Female/male voice preference in the browser prototype
- Pronunciation workflow extension point
- Lightweight RAG knowledge base
- Admin dashboard shell
- Responsive Figma-style design
- GitHub + Streamlit-ready structure

## Run the Streamlit app

```bash
cd streamlit_app
python -m pip install -r requirements.txt
streamlit run app.py
```

Configure secrets/environment:
- `GEMINI_API_KEY` — required for Gemini features
- `GEMINI_MODEL` — optional, set to a model available to your Gemini API account
- `TONGUETIE_ADMIN_PASSWORD` — optional admin password

For Streamlit Cloud, put the same values in the app's Secrets.

## Run the browser prototype

Open `prototype/index.html` in a modern browser. It includes:
- mobile Figma-style navigation
- voice recording
- browser speech synthesis with a female-voice preference
- translation demo
- AI tutor demo
- correction demo
- vocabulary, grammar, quiz and progress screens

The browser prototype uses local/demo responses. Connect it to your deployed backend for production AI.

## Real voice translation

The app deliberately separates speech from the UI because recording alone is not speech recognition.

Production pipeline:
1. Microphone audio
2. Multilingual Speech-to-Text
3. Language detection
4. Gemini translation/correction
5. Optional pronunciation assessment
6. Text-to-Speech using selected voice gender
7. Return translated audio + transcript + feedback

See `streamlit_app/speech_service.py`.

## Important

Do not commit API keys to GitHub. Use Streamlit Secrets or environment variables.

This package is a complete starter implementation, but external STT/TTS providers and authentication/database infrastructure must be connected before claiming production deployment.
