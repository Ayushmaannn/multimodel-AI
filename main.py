import streamlit as st
import os
import time
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
configure(api_key=API_KEY)

# Adding default prompts 

system_prompt = "You are a helpful assistant."
user_prompt = "Hello! How are you?"

# Streamlit UI
st.title("CREATE YOUR OWN AI MODEL")

# User Inputs
system_prompt = st.text_area("Enter System Prompt", "You are a helpful assistant.")
user_prompt = st.text_area("Enter User Prompt", "Hello! How are you?")
temperature = st.slider("Select Temperature", 0.0, 1.0, 0.7, 0.05)
#min_tokens = st.number_input("Min Tokens", min_value=1, value=50, step=1)
max_tokens = st.number_input("Max Tokens", min_value=1, value=200, step=1)

# Generate Response Button
if st.button("Generate Response"):
    model = GenerativeModel("gemini-pro")
    
    print("Generating response with the following parameters:")
    print(f"System Prompt: {system_prompt}")
    print(f"User Prompt: {user_prompt}")
    print(f"Temperature: {temperature}")
    print(f"Min Tokens: min_tokens, Max Tokens: {max_tokens}")
    finalprompt =system_prompt+user_prompt
    try:
        time.sleep(2)  # Adding delay to avoid rate limit errors
        response = model.generate_content(
             contents= [finalprompt],
            generation_config={
                "temperature": temperature,
                "max_output_tokens": max_tokens
            }
        )
        print("Response received successfully")
        st.subheader("Response:")
        st.write(response.text)
    except Exception as e:
        print(f"Error occurred: {e}")
        st.error("Error: API Quota exceeded or service unavailable. Try again later.")
