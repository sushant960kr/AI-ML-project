import streamlit as st
import qrcode
from PIL import Image, ImageDraw, ImageFont
from gtts import gTTS
from io import BytesIO
import base64

# Title of the app
st.title("Multi-functional Text Converter")

# Text Input
text_input = st.text_area("Enter Text:")

# Language Selection (Optional - Default is English)
language = st.selectbox("Select Language:", ["en", "fr", "de", "es", "it"])

# QR Code Generation
if st.button("Generate QR Code"):
    if text_input:
        # Generate QR code
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(text_input)
        qr.make(fit=True)

        # Create an image from the QR Code instance
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert PIL image to bytes
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        img_bytes = buffered.getvalue()

        # Display the QR code
        st.image(img_bytes, caption="Generated QR Code", use_column_width=True)
        
        # Option to download the QR code
        st.download_button(
            label="Download QR Code",
            data=img_bytes,
            file_name="qr_code.png",
            mime="image/png",
        )
    else:
        st.error("Please enter some text to generate a QR Code.")

# Function to Convert Text to Audio
def text_to_speech(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    fp = BytesIO()
    tts.write_to_fp(fp)
    return fp



# Convert Button for Audio
if st.button("Convert to Audio"):
    if text_input:
        audio_file = text_to_speech(text_input, language)
        st.audio(audio_file)

# # Convert Button for Image
# if st.button("Convert to Image"):
#     if text_input:
#         image = create_image_with_text(text_input)
#         st.image(image)

# # Download Button for Image
# if st.button("Download Image"):
#     if text_input:
#         image = create_image_with_text(text_input)
#         st.markdown(download_image(image), unsafe_allow_html=True)
