import streamlit as st
import pandas as pd
# Page Configuration
st.set_page_config(page_title="About Us", layout="wide", page_icon="./images/logo/jpg")

# Main Title with Styling
st.markdown("""
    <h1 style='text-align: center; color: #4A90E2;'>About Us</h1>
    """, unsafe_allow_html=True)

# Story Section with Better Formatting
st.markdown(
    """
    ## My Journey
    
    🚀 **Inspiration**  
    It all started with an inspiring seminar at our college, where a team from [Rent Prompts](https://rentprompts.com)
    introduced us to the world of no-code AI model creation. The CEO and the team demonstrated how anyone can create
    and share AI models effortlessly. This hands-on workshop on text-to-text models was a game-changer.
    
    🔍 **What We Learned**  
    Their platform allows users to define key parameters like **system prompts, user prompts, temperature, top-P, top-K,**
    and **token limits** to fine-tune AI models. Seeing this, I was so fascinated that I decided to replicate
    their approach and create my own version of a similar platform using **Streamlit**.
    
    💡 **Creation**  
    With my prior knowledge and the support of tools like **ChatGPT**, I built this project as a learning experience
    and a tribute to their vision. This is an ongoing experiment, and while it may not be perfect, I hope it serves
    as an inspiration for others to dive into AI and explore its possibilities.
    """
)

# Layout with Two Columns
col1, col2 = st.columns([1, 2])  # Adjust column width for balance

# Profile Image (Left Column)
with col1:
    st.image("images/ayushman.jpg", caption=None, width=252)

# Profile Info (Right Column)
with col2:
    st.markdown("### **Ayushman Nema**")  # Name & Role
    st.markdown("[LinkedIn](http://www.linkedin.com/in/ayushman-nema-203383286)")  # Social link
    st.write('''Hi, I'm Ayushman Nema, a passionate tech enthusiast and an aspiring software developer. Currently pursuing my BCA in AI and Data Analytics,
    I have a keen interest in exploring AI, coding, and building innovative projects. My journey into AI began with curiosity,
    and this project is a result of my continuous learning and experimentation.''')

st.markdown("---")  # Adds a horizontal line for separation


# Contact & Socials Section with Icons
st.markdown("## 📬 Contact Me")
st.markdown("""
    - 📧 Email: **ayushmaannema1234@gmail.com**
    - 🔗 [**LinkedIn**](http://www.linkedin.com/in/ayushman-nema-203383286)
""")

# Footer Note with Styling
st.markdown("""
    <hr>
    <p style='text-align: center; font-style: italic;'>
        *This project is a work in progress and is not intended for commercial use. Inspired by Rent Prompts.*
    </p>
    """, unsafe_allow_html=True)
import streamlit as st
import pandas as pd

# Create a DataFrame with the new location data
data = pd.DataFrame({
    'latitude': [23.249848],
    'longitude': [77.528255]
})

# Display the map
st.map(data, zoom=13.5, use_container_width=True)
