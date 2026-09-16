
import os
from google import genai

def _client():
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise RuntimeError("GEMINI_API_KEY is not configured.")
    return genai.Client(api_key=key)

def _model():
    # Configure a current model in Streamlit secrets/environment.
    # The app intentionally avoids assuming a model name that may change.
    return os.getenv("GEMINI_MODEL", "gemini-2.5-flash")

def ask(prompt):
    try:
        response = _client().models.generate_content(model=_model(), contents=prompt)
        return getattr(response, "text", None) or str(response)
    except Exception as e:
        return f"AI service error: {e}"

def ai_tutor(question, source, target, context=""):
    return ask(f"""You are TongueTie, a multilingual language tutor.
Learner's first language: {source}
Target language: {target}
Question: {question}
Relevant learning context:
{context}
Answer clearly. If useful, give examples, common mistakes, a mini exercise, and an English/learner-language explanation. Do not pretend to have heard audio unless a transcript is supplied.""")

def translate_text(text, source, target):
    return ask(f"""Translate the following text from {source} to {target}.
Preserve meaning and natural register.
Return:
1. Natural translation
2. Literal/learning note when useful
3. Romanization only when the target script normally needs it for learners
Text: {text}""")

def correct_text(text, language):
    return ask(f"""Correct this {language} text for a learner.
Return:
- Corrected version
- What was wrong
- Why
- A more natural alternative when appropriate
Text: {text}""")

def explain_word(word, source, target):
    return ask(f"""Teach the word/phrase "{word}" for someone who speaks {source} and is learning {target}.
Include meaning, part of speech, pronunciation guidance, examples, common mistakes, synonyms/related words, and a short practice question.""")

def generate_quiz(source, target, topic):
    return ask(f"""Create a 10-question language-learning quiz for {target}, explained for a {source}-speaking learner.
Topic: {topic}
Include multiple choice questions and an answer key at the end.""")

def lesson_plan(source, target, level, topic):
    return ask(f"""Create a practical 10-minute {target} lesson for a {source}-speaking learner.
Level: {level}
Topic: {topic}
Include dialogue, vocabulary, grammar point, pronunciation focus, comprehension check, speaking task and review.""")
