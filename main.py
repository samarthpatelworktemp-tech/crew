import streamlit as st
from crew import CodeTranslatorCrew

st.set_page_config(page_title="Code Translator", layout="wide")
st.title("🧠 Code Translator")

# --- Sidebar input ---
st.sidebar.header("Translation Settings")
target_language = st.sidebar.selectbox(
    "Choose Target Language",
    ["Java", "C++", "C#", "Go", "Rust", "JavaScript", "TypeScript", "Python"],
    index=0
)

# --- Main UI ---
input_code = st.text_area(
    "✍️ Enter your source code here",
    height=300,
    placeholder="Paste source code...",
)

translate_btn = st.button("🔁 Translate Code")

if translate_btn and input_code.strip():
    with st.spinner("Translating..."):
        try:
            inputs = {
                "input_code": input_code.strip(),
                "target_language": target_language,
            }

            # Run Crew
            result = CodeTranslatorCrew().crew().kickoff(inputs=inputs)

            # Parse and display result
            st.subheader("📄 Translated Code")
            st.code(result, language=target_language.lower())

        except Exception as e:
            st.error(f"❌ An error occurred:\n{e}")
else:
    st.info("Enter code and click **Translate Code** to begin.")