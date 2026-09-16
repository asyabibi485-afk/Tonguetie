# TongueTie — Figma-Style Full App Package

This ZIP is the revised package requested for the TongueTie app.

## Main prototype
Open `prototype/index.html`.

The interface is deliberately designed as a polished Figma-style product prototype:
- mobile-responsive visual system
- dark premium UI
- rounded cards and panels
- gradients and design tokens
- persistent navigation
- clickable screen-to-screen prototype flow

## Clickable flow
Home → Daily Lesson → Voice Studio → Translate → AI Tutor → Vocabulary → Grammar → Quiz → Progress → Profile.

## Voice Studio
Includes a dedicated waveform screen with browser microphone recording, stop and playback controls.

## Streamlit
`streamlit_app/app.py` is a development shell for moving the visual system into Streamlit.

## Production integration
Connect:
- Gemini API
- RAG/vector database
- speech-to-text
- text-to-speech
- pronunciation scoring
- authentication
- user progress database

Never commit API keys to GitHub; use Streamlit Secrets/environment variables.
