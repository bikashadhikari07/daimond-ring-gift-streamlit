import streamlit as st
from PIL import Image
image = Image.open('daimond.png')

st.title("This is for you")
st.markdown("A precious gift from me")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

password = st.text_input("What was the password?")

if password == "1234":
    st.session_state.messages.append(
        {"role": "assistant", "content": f"Here's your precious gift:", "avatar": None})
    st.image(image, caption='you like it?')
