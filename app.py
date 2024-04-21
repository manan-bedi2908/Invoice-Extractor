from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import google.generativeai as genai

load_dotenv()

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content(input, image[0], prompt)
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getValue()
        image_parts = [
            {
                'mime_type': uploaded_file.type,
                'data': bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError('No file uploaded!!')
    

st.set_page_config(page_title='Invoice Extractor')

st.header('Invoice Extraction Tool')
input = st.text_input('Input Prompt: ', key='input')
uploaded_file = st.file_uploader('Choose an Image', 
                                 type=['jpg', 'jpeg', 'png'])
image = ''
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)

