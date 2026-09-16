
"""Speech integration extension point.

The included app records audio with Streamlit. Production transcription and
pronunciation scoring require a speech service. Keep credentials server-side.

Suggested providers:
- Google Cloud Speech-to-Text + Text-to-Speech
- Azure AI Speech
- ElevenLabs (TTS)
- Another provider with multilingual STT/TTS

Expected pipeline:
audio -> speech-to-text -> language detection -> translation -> correction /
pronunciation analysis -> TTS -> response audio
"""
def transcribe_audio(audio_bytes, language_code):
    raise NotImplementedError("Connect your chosen STT provider here.")

def synthesize_speech(text, language_code, voice_gender="female"):
    raise NotImplementedError("Connect your chosen TTS provider here.")

def score_pronunciation(audio_bytes, reference_text, language_code):
    raise NotImplementedError("Connect pronunciation assessment here.")
