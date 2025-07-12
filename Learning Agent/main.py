import streamlit as st
import google.generativeai as genai

# ---------- Load Gemini API Key from Streamlit Secrets ----------
api_key = st.secrets["GEMINI_API_KEY"]

# ---------- Validate API Key ----------
if not api_key:
    st.error("❌ Gemini API key not found in Streamlit secrets.")
    st.stop()

# ---------- Configure Gemini ----------
genai.configure(api_key=api_key)

# ---------- UI Setup ----------
st.set_page_config(page_title="🧠 LingoMate", layout="centered")
st.title("🧠 LingoMate - Your AI Language Learning Buddy")
st.markdown("Translate or quiz yourself with AI-powered smart content.")

text_input = st.text_area("✏️ Enter your text here", height=150)

target_lang = st.selectbox("🌐 Select target language:", [
    "English", "Spanish", "French", "Urdu", "Roman Urdu", "Japanese", "Arabic"
])

task = st.radio("🤖 What should the agent do?", ["Translate", "Quiz Me"])

# ---------- Run the Agent ----------
if st.button("🚀 Run Agent"):
    if not text_input.strip():
        st.warning("⚠️ Please enter some text.")
    else:
        try:
            model = genai.GenerativeModel("gemini-1.5-flash")

            # Programming-related prompt adjustment
            programming_keywords = [
                "python", "typescript", "html", "css", "javascript", "java",
                "c++", "programming", "coding"
            ]

            if task == "Translate":
                prompt = f"Translate the following text into {target_lang}:\n\n{text_input}"

            elif task == "Quiz Me":
                if any(keyword in text_input.lower() for keyword in programming_keywords):
                    # Generate programming quiz
                    prompt = f"""
You are a programming instructor. Create an official beginner-level quiz on the topic: "{text_input}".

Requirements:
- 10 multiple choice questions (MCQs)
- Each question should have 4 options (A, B, C, D)
- Clearly mark the correct answer for each question

Format:
Q1. ...
A. ...
B. ...
C. ...
D. ...
Answer: ...
"""
                else:
                    # Language learning quiz
                    prompt = f"""
You are a language tutor. Create a language quiz based on this sentence: "{text_input}" in {target_lang}.

Instructions:
- Include 5 MCQs and 2 fill-in-the-blank questions.
- Format like:
Q1. ...
A. ...
B. ...
C. ...
Answer: ...
- Keep it beginner friendly.
"""

            response = model.generate_content(prompt)
            st.success(f"🧠 Agent Response ({task}):")
            st.markdown(f"```{response.text.strip()}```")

        except Exception as e:
            st.error(f"❌ Error: {str(e)}")

# ---------- Footer ----------
st.markdown("---")
st.markdown("Made with ❤️ by LavoraStudio")
