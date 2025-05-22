import streamlit as st
from components.header import render_header
from services.image_service import process_and_download_image

st.set_page_config(page_title="Background Removal App", layout="centered")

render_header()

uploaded_file = st.file_uploader(" Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file:
    process_and_download_image(uploaded_file)
else:
    st.warning("Please upload an image to get started!")