
import streamlit as st
st.set_page_config(page_title="TongueTie",page_icon="🌐",layout="wide")
st.markdown("""
<style>
.stApp{background:radial-gradient(circle at 70% 0,#291453 0,#080b18 48%,#050713 100%);color:#f8f9ff}
.block-container{max-width:1180px;padding-top:2rem}
h1,h2,h3{letter-spacing:-.5px}
div[data-testid="stMetric"]{background:#10172d;border:1px solid #293761;padding:16px;border-radius:18px}
</style>
""",unsafe_allow_html=True)
st.markdown("# <span style='background:linear-gradient(90deg,#55c7ff,#9b5cff);-webkit-background-clip:text;color:transparent'>TongueTie</span>",unsafe_allow_html=True)
st.caption("Figma-style Streamlit implementation shell — connect your Gemini/RAG services here.")
page=st.sidebar.radio("Navigate",["Home","Voice Studio","Translate","AI Tutor","Vocabulary","Grammar","Quiz","Progress","Admin"])
if page=="Home":
    st.title("Build confidence, one conversation at a time.")
    a,b,c=st.columns(3);a.metric("Vocabulary","248","+18");b.metric("Speaking","74%");c.metric("Streak","7 days")
elif page=="Voice Studio":
    st.title("🎙️ Voice Studio")
    st.write("Dedicated recorder interface")
    audio=st.audio_input("Record your practice")
    if audio: st.audio(audio);st.success("Recording captured.")
elif page=="Translate":
    st.title("🌍 Translate")
    text=st.text_area("Text or difficult word")
    target=st.selectbox("Target language",["English","Urdu","Arabic","Persian (Farsi)","Spanish","French","German","Chinese"])
    if st.button("Translate") and text: st.info(f"Connect Gemini to translate into {target}.")
elif page=="AI Tutor":
    st.title("✦ AI Tutor");st.text_area("Ask a question");st.button("Ask TongueTie AI")
elif page=="Vocabulary":
    st.title("Aa Vocabulary");st.text_input("Difficult word");st.button("Explain word")
elif page=="Grammar":
    st.title("✓ Grammar");st.write("Present simple: I/you/we/they + base verb; he/she/it + s/es.")
elif page=="Quiz":
    st.title("◇ Quiz");st.radio("Choose the correct sentence",["He go to school.","He goes to school."]);st.button("Check answer")
elif page=="Progress":
    st.title("↗ Progress");st.progress(.68)
else:
    st.title("Admin Dashboard");st.info("Connect authentication and a database before production.")
