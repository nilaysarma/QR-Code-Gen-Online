import streamlit as st
from qr_generator import convert_to_qr
import io

def show_image(text):
    img = convert_to_qr(text)
    image_binary = io.BytesIO()
    img.save(image_binary, 'PNG')
    image_binary.seek(0)
    st.image(image_binary)
    return image_binary

def main():
    st.title("QR Code Generator Online")
    text = st.text_area("Convert text/URL to QR code", placeholder="Enter text/URL")
    
    if 'image_binary' not in st.session_state:
        st.session_state.image_binary = None
    
    if st.button("Generate", help="Click to generate QR code", type="primary"):
        if text == "":
            st.warning('Enter some text', icon="⚠️")
        else:
            st.session_state.image_binary = show_image(text)
    
    if st.session_state.image_binary:
        st.download_button(
            label="Download QR Code",
            data=st.session_state.image_binary,
            file_name="qr_code.png",
            mime="image/png"
        )

if __name__ == "__main__":
    main()
