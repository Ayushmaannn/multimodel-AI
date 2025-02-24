import streamlit as st
import os
import time
import requests
from google.generativeai import configure, GenerativeModel
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")  # Hugging Face API Key

configure(api_key=GEMINI_API_KEY)


# Streamlit Page Configuration
st.set_page_config(page_title="Home", layout="wide", page_icon="./images/logo.png")

st.title("CREATE YOUR OWN AI MODEL")
st.markdown("---")

# User selects the AI type
task_type = st.radio("Choose AI Model Type", ["Text Generation", "Image Generation"])

if task_type == "Text Generation":
    system_prompt = st.text_area("Enter System Prompt", "You are a helpful assistant.")
    user_prompt = st.text_area("Enter User Prompt", "Hello! How are you?")
    temperature = st.slider("Select Temperature", 0.0, 1.0, 0.7, 0.05)
    top_p_value = st.slider("Select Top P", 0.0, 1.0, 0.9)
    top_k_value = st.number_input("Select Top K", min_value=1, value=40, step=1)
    max_tokens = st.number_input("Max Tokens", min_value=1, value=1000, step=1)

elif task_type == "Image Generation":
    image_prompt = st.text_area("Enter Image Description", "A futuristic city with flying cars and neon lights.")

# Generate Button
if st.button("Generate Response"):
    if task_type == "Text Generation":
        try:
            model = GenerativeModel("gemini-1.5-pro")
            response = model.generate_content(
                contents=[system_prompt + user_prompt],
                generation_config={
                    "temperature": temperature,
                    "max_output_tokens": max_tokens,
                    "top_p": top_p_value,
                    "top_k": top_k_value
                }
            )
            st.subheader("Response:")
            st.write(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

    elif task_type == "Image Generation":
        try:
            # Hugging Face API Request
            headers = {"Authorization": f"Bearer {HUGGINGFACE_API_KEY}"}
            data = {"inputs": image_prompt}
            response = requests.post(
                "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-2",
                json=data,
                headers=headers
            )
            
            if response.status_code == 200:
                st.subheader("Generated Image:")
                st.image(response.content, caption="AI-Generated Image", use_column_width=True)
            else:
                st.error(f"Error: {response.json()}")
        except Exception as e:
            st.error(f"Error: {e}")


# Create and save the model file
if st.button("Submit Model"):

    sr_no = 100
    model_name = "Custom_Model"
    model_identidy = f"pages/{sr_no}_{model_name}.py"

    with open(model_identidy, "w", encoding="utf-8") as f:
        f.write(f'''import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as gen_ai

load_dotenv()

sr_no = 100
model_name="{model_name}"
system_prompt ="{system_prompt}"
top_p_value = {top_p_value}
top_k_value = {top_k_value}
temperature = {temperature}
max_tokens = {max_tokens}

st.set_page_config(page_title=model_name, page_icon=":brain:", layout="centered")

st.sidebar.markdown("### 📂 GitHub Repository")
st.sidebar.markdown("[🔗 View on GitHub](https://github.com/Amanlnctu/your-AI)")

st.sidebar.markdown("### 💼 LinkedIn")
st.sidebar.markdown("[🔗 Connect on LinkedIn](https://www.linkedin.com/in/amankahar/)")

st.sidebar.markdown("---")
st.sidebar.markdown("## 👨‍💻 Looking for an Internship!")
st.sidebar.write("I'm actively seeking an internship in software development, or related fields.")

st.sidebar.markdown("---")
st.sidebar.markdown("💡 *Let's collaborate and build something amazing!*")

GOOGLE_API_KEY = os.getenv("GEMINI_API_KEY")

if not GOOGLE_API_KEY:
    st.error("⚠️ Google API Key is missing. Please set GEMINI_API_KEY in .env")
    st.stop()

gen_ai.configure(api_key=GOOGLE_API_KEY)
model = gen_ai.GenerativeModel('gemini-pro')

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

st.title(model_name)

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_prompt = st.chat_input("Enter your query here")

if user_prompt:
    st.chat_message("user", avatar="./images/man.png").markdown(user_prompt)
    st.session_state.chat_history.append(dict(role="user", avatar="./images/man.png", content=user_prompt))

    full_prompt = system_prompt + user_prompt

    generation_config = dict(
        temperature=temperature,
        max_output_tokens=max_tokens,
        top_p=top_p_value,
        top_k=top_k_value,
    )

    gemini_response = model.generate_content(full_prompt, generation_config=generation_config)
    ai_response = gemini_response.text if hasattr(gemini_response, "text") else "⚠️ Error generating response."

    with st.chat_message("assistant", avatar="./images/AI.png"):
        st.markdown(ai_response)

    st.session_state.chat_history.append(dict(role="assistant", avatar="./images/man.png", content=ai_response))''')
    f.close()
    st.success(f"Model saved as {model_identidy}")
