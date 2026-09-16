# TongueTie 🌐

**Learn Languages. Speak Confidently. Understand the World.**

TongueTie is a Streamlit-ready multilingual AI language-learning starter application with a Figma-inspired dark UI, Gemini integration, lightweight RAG workflow, quizzes, translation, dictionary help, speaking-coach analysis, and progress/admin screens.

## Features
- English learning with Urdu, Arabic, Persian/Farsi and many additional languages
- Daily-life lessons
- Vocabulary and difficult-word explanations
- Grammar concepts and practice
- Translation
- AI speaking coach
- Quiz/test generation
- RAG retrieval from a local knowledge base
- Progress and demo admin dashboard
- Gemini API through environment variables / Streamlit Secrets
- GitHub + Streamlit Cloud friendly structure

## Run locally

```bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Set `GEMINI_API_KEY` in your environment or Streamlit Secrets.

## Streamlit Cloud
1. Push this folder to a GitHub repository.
2. Create a Streamlit Cloud app from the repository.
3. Set the main file to `app.py`.
4. In Streamlit Secrets, add:
   `GEMINI_API_KEY = "your-key"`
5. Deploy.

## Production roadmap
- Add authentication and role-based access.
- Store users/progress in PostgreSQL/Supabase/Firebase.
- Add embeddings + vector database for stronger RAG.
- Add browser/mobile audio recording and speech-to-text.
- Add text-to-speech and pronunciation scoring.
- Add rate limits, logging, monitoring, and secret rotation.
- Replace demo admin metrics with real database queries.

## Security
Never commit a Gemini API key to GitHub. Use Streamlit Secrets or environment variables.
