import os

from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu

from gemini_utility import (load_gemini_pro_model,
                            gemini_pro_response,
                            gemini_pro_vision_response,
                            embeddings_model_response)


working_dir = os.path.dirname(os.path.abspath(__file__))

st.set_page_config(
    page_title="J.A.R.V.I.S",
    page_icon="🧠",
    layout="centered",
)

with st.sidebar:
    selected = option_menu('J.A.R.V.I.S',
                           ['ChatBot',
                            'Image Captioning',
                            'Embed text',
                            'Ask me anything'],
                           menu_icon='robot', icons=['chat-dots-fill', 'image-fill', 'textarea-t', 'patch-question-fill'],
                           default_index=0
                           )


# Function to translate roles between Gemini-Pro and Streamlit terminology
def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role


# chatbot page
# Chatbot page
if selected == 'ChatBot':
    gemini_pro_model = load_gemini_pro_model()  # Load the model at the start

    # Initialize chat session in Streamlit if not already present
    if "chat_session" not in st.session_state:
        st.session_state.chat_session = gemini_pro_model.start_chat(history=[])

    st.title("J.A.R.V.I.S")

    # Display the chat history
    for message in st.session_state.chat_session.history:
        with st.chat_message(translate_role_for_streamlit(message.role)):
            st.markdown(message.parts[0].text)

    # Input field for user's message
    user_prompt = st.chat_input("Ask J.A.R.V.I.S.")
    if user_prompt:
        st.chat_message("user").markdown(user_prompt)  # Display user message

        # Check for "What's your name?" question
        if "what's your name" in user_prompt.lower():
            st.write("DEBUG: Triggered 'what's your name' condition")  # Debugging statement
            jarvis_response = "JARVIS: I am a large language model, trained by Google. I do not have a name."
        elif "who are you" in user_prompt.lower():
            jarvis_response = None  # Skip the response
        else:
            gemini_response = st.session_state.chat_session.send_message(user_prompt)
            # Display the response
            with st.chat_message("assistant"):
                st.markdown(gemini_response.text)

# Image captioning page
if selected == "Image Captioning":

    st.title("📷 Snap Narrate")

    uploaded_image = st.file_uploader("Upload an image...", type=["jpg", "jpeg", "png"])

    if st.button("Generate Caption"):
        image = Image.open(uploaded_image)

        col1, col2 = st.columns(2)

        with col1:
            resized_img = image.resize((800, 500))
            st.image(resized_img)

        default_prompt = "write a short caption for this image"  # change this prompt as per your requirement

        # get the caption of the image from the gemini-pro-vision LLM
        caption = gemini_pro_vision_response(default_prompt, image)

        with col2:
            st.info(caption)


# text embedding model
if selected == "Embed text":

    st.title("🔡 Embed Text")

    # text box to enter prompt
    user_prompt = st.text_area(label='', placeholder="Enter the text to get embeddings")

    if st.button("Get Response"):
        response = embeddings_model_response(user_prompt)
        st.markdown(response)


# text embedding model
if selected == "Ask me anything":

    st.title("❓ Ask me a question")

    # text box to enter prompt
    user_prompt = st.text_area(label='', placeholder="Ask me anything...")

    if st.button("Get Response"):
        response = gemini_pro_response(user_prompt)
        st.markdown(response)

