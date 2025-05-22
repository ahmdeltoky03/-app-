import streamlit as st
from utils.background_removal import remove_bg
from PIL import Image
import io
import os

def process_and_download_image(uploaded_file):
    
    # convert the uploaded file to a PIL Image
    image = Image.open(uploaded_file)
    # Display the original image
    st.image(image, caption="Original Image", use_container_width=True)

    with st.spinner("Removing background..."):
        result_image = remove_bg(uploaded_file)

        st.success("✅ Background removed successfully!")
        st.image(result_image, caption="Result Image", use_container_width=True)

        # Prepare download
        buf = io.BytesIO()
        result_image.save(buf, format="PNG")
        buf.seek(0)


        file_basename = uploaded_file.name.rsplit('.', 1)[0]
        download_filename = os.path.join(file_basename, "no_bg.png")

        st.download_button(
            label=" Download Image",
            data=buf,
            file_name=download_filename,
            mime="image/png"
        )

        # Center using st.markdown and HTML
        st.markdown(
            """
            <style>
            div.stDownloadButton > button {
                display: block;
                margin: 0 auto;
            }
            </style>
            """,
            unsafe_allow_html=True
        )