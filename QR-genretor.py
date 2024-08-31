import streamlit as st
import qrcode
from PIL import Image
from io import BytesIO

st.title("QR Code Generator")

# Input for the data to be encoded in the QR code
data = st.text_input("Enter the data you want to encode in the QR code")

# Button to generate QR code
if st.button("Generate QR Code"):
    if data:
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        # Generate the QR code image
        img = qr.make_image(fill_color="black", back_color="white")

        # Convert PilImage to bytes
        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        # Display the QR code
        st.image(byte_im)
    else:
        st.warning("Please enter data to generate a QR code")
