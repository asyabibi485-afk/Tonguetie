import os

def ask_gemini(prompt: str) -> str:
    api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not api_key:
        return ("### Gemini API key not configured\n\n"
                "Add `GEMINI_API_KEY` to Streamlit Secrets or your environment. "
                "The app remains usable as a UI demo, but AI generation requires the key.")
    try:
        from google import genai
        client = genai.Client(api_key=api_key)
        model = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
        response = client.models.generate_content(model=model, contents=prompt)
        return getattr(response, "text", str(response))
    except Exception as exc:
        return f"### Gemini service error\n\n`{type(exc).__name__}: {exc}`\n\nCheck your API key, model name, quota, and network configuration."
