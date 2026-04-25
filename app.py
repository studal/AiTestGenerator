import streamlit as st
from utils.file_handler import read_uploaded_file
from prompts.prompt_builder import build_system_prompt
from services.openai_service import generate_tests

st.set_page_config(page_title="AI Test Generator", layout="wide")

st.title("🧪 AI Test Generator")

# Layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("Input Panel")

    user_prompt = st.text_area(
        "Enter Payload / Endpoint / Schema / Requirement",
        height=300,
        placeholder="Paste API payload, endpoint, schema or describe what tests you need..."
    )

    uploaded_file = st.file_uploader(
        "Upload skills.md / architecture file",
        type=["md"]
    )

    generate_button = st.button("Generate Tests")

with col2:
    st.subheader("Output Panel")

    output_placeholder = st.empty()

if generate_button:
    if not uploaded_file:
        output_placeholder.error("Please upload a .md file.")
    elif not user_prompt.strip():
        output_placeholder.error("Please enter user input.")
    else:
        with st.spinner("Generating tests..."):
            md_content = read_uploaded_file(uploaded_file)
            system_prompt = build_system_prompt(md_content)
            generated_output = generate_tests(system_prompt, user_prompt)

            output_placeholder.code(generated_output)