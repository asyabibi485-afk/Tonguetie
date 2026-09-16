import os
import streamlit as st
from pathlib import Path
from rag import retrieve_context
from gemini_service import ask_gemini
from language_data import LANGUAGES

st.set_page_config(page_title="TongueTie", page_icon="🌐", layout="wide")

st.markdown("""
<style>
.stApp {background: linear-gradient(135deg,#070B1A 0%,#101633 55%,#17103A 100%); color:#F7F8FF;}
.block-container {max-width:1200px; padding-top:2rem;}
.hero {padding:28px; border-radius:24px; background:linear-gradient(135deg,#151D46,#24164F);
border:1px solid #39447D; box-shadow:0 12px 40px rgba(0,0,0,.25);}
.brand {font-size:42px;font-weight:800;letter-spacing:-1px;}
.grad {background:linear-gradient(90deg,#55B7FF,#A46BFF);-webkit-background-clip:text;color:transparent;}
.card {padding:20px;border-radius:20px;background:#111936;border:1px solid #2D3968;margin:8px 0;}
.small {color:#AAB5D8;}
</style>
""", unsafe_allow_html=True)

if "history" not in st.session_state:
    st.session_state.history = []

with st.sidebar:
    st.markdown("## 🌐 TongueTie")
    st.caption("Learn Languages. Speak Confidently. Understand the World.")
    page = st.radio("Navigate", ["Learn", "Translate", "Speaking Agent", "Quiz", "Dictionary", "Progress", "Admin"])
    source_lang = st.selectbox("Learning language", LANGUAGES, index=0)
    native_lang = st.selectbox("Your language", LANGUAGES, index=1 if len(LANGUAGES)>1 else 0)
    st.divider()
    st.caption("Powered by Gemini API • RAG • Streamlit")

if page == "Learn":
    st.markdown('<div class="hero"><div class="brand"><span class="grad">TongueTie</span></div><p>One app. Infinite languages. A smarter daily learning partner.</p></div>', unsafe_allow_html=True)
    a,b,c,d = st.columns(4)
    for col,title,value in [(a,"Vocabulary","248"),(b,"Grammar","12"),(c,"Streak","7 days"),(d,"Progress","68%")]:
        with col:
            st.markdown(f'<div class="card"><div class="small">{title}</div><h2>{value}</h2></div>', unsafe_allow_html=True)
    st.subheader("Today's lesson")
    topic = st.selectbox("Choose a daily-life topic", ["Greetings & introductions","At the restaurant","Travel & transportation","Shopping","Work & business","Academic English"])
    if st.button("✨ Generate lesson", type="primary"):
        context = retrieve_context(topic)
        prompt = f"Create a beginner-friendly {source_lang} lesson for a learner whose native language is {native_lang}. Topic: {topic}. Include 8 vocabulary words, 3 grammar points, examples, and a short exercise. Context: {context}"
        answer = ask_gemini(prompt)
        st.markdown(answer)
    st.info("RAG flow: Learn → Retrieve relevant knowledge → Generate with Gemini → Practice → Review.")

elif page == "Translate":
    st.title("🔄 Translate")
    text = st.text_area("Text or difficult word", placeholder="Type a word, sentence, or question...")
    target = st.selectbox("Translate to", LANGUAGES, index=1 if len(LANGUAGES)>1 else 0)
    if st.button("Translate", type="primary") and text.strip():
        context = retrieve_context(text)
        st.markdown(ask_gemini(f"Translate the following into {target}. Explain difficult vocabulary briefly and give a natural everyday version. Text: {text}\nContext: {context}"))

elif page == "Speaking Agent":
    st.title("🎙️ AI Speaking Agent")
    st.write("Practice a real-life conversation and receive language feedback.")
    scenario = st.selectbox("Scenario", ["Introducing yourself","Job interview","Restaurant","Travel","Doctor visit","Casual conversation"])
    user_text = st.text_area("Type what you would say (voice input can be added through your deployment's browser/audio layer)", height=130)
    if st.button("Analyze my speaking practice", type="primary") and user_text.strip():
        st.markdown(ask_gemini(f"Act as a supportive {source_lang} speaking coach. Scenario: {scenario}. Analyze this learner response: {user_text}. Return: corrected version, grammar notes, vocabulary improvements, pronunciation tips, and a score out of 100. Do not shame the learner."))

elif page == "Quiz":
    st.title("🧠 Quiz & Test")
    topic = st.selectbox("Quiz topic", ["Vocabulary","Grammar","Daily conversation","Translation"])
    if st.button("Generate quiz", type="primary"):
        st.markdown(ask_gemini(f"Create a 5-question {source_lang} {topic} quiz for a learner whose native language is {native_lang}. Give four options per question, then put an answer key at the end."))
    st.divider()
    st.caption("Use generated questions for self-testing; review mistakes after the test.")

elif page == "Dictionary":
    st.title("📖 Dictionary & Difficult Word Helper")
    word = st.text_input("Enter a difficult word")
    if st.button("Explain word", type="primary") and word.strip():
        context = retrieve_context(word)
        st.markdown(ask_gemini(f"Explain the word '{word}' to a language learner. Include meaning in {native_lang}, part of speech, simple definition, synonyms, antonyms, two examples, and a pronunciation guide. Context: {context}"))

elif page == "Progress":
    st.title("📈 My Progress")
    st.progress(0.68)
    x,y,z = st.columns(3)
    x.metric("Words learned","248","+18")
    y.metric("Lessons","48","+4")
    z.metric("Current streak","7 days","+2")
    st.markdown('<div class="card"><h3>Learning review</h3><p>Focus next on speaking confidence, grammar practice, and recently missed quiz questions.</p></div>', unsafe_allow_html=True)

elif page == "Admin":
    st.title("🛠️ Admin Dashboard")
    st.caption("Demo analytics interface — connect your database/auth layer before production.")
    a,b,c,d = st.columns(4)
    a.metric("Users","12,458")
    b.metric("Active today","3,247")
    c.metric("Lessons","1,248")
    d.metric("Languages","100+")
    st.subheader("RAG / Gemini configuration")
    st.write("Gemini API key detected:", bool(os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")))
    st.write("Knowledge base:", "data/knowledge_base.txt")
    st.write("UI:", "TongueTie dark-mode responsive Streamlit interface")
