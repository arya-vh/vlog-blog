import streamlit as st
from langchain_ollama import OllamaLLM

# Initialize Ollama LLM
llm = OllamaLLM(model="gemma2:2b")  # or "llama2"

st.title("Vlog-Blog")
st.write("Enter a topic and get a generated blog or vlog script.")

# Input fields
topic = st.text_input("Topic")
audience = st.selectbox("Target Audience", ["General", "Data Scientist", "Software Engineer", "Teacher", "Body Builder"])
word_count = st.number_input("Word Count", min_value=50, max_value=1000, value=200)
content_type = st.radio("Content Type", ["Blog", "Vlog Script"])

# Generate button
if st.button("Generate"):
    prompt = f"Write a {word_count}-word {content_type.lower()} about {topic} for {audience}."
    with st.spinner("Generating..."):
        response = llm.invoke(prompt)
    st.subheader(f"Generated {content_type}")
    st.write(response)
