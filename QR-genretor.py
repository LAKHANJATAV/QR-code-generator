import streamlit as st
import qrcode
from imageio import imread
from io import BytesIO

st.title("QR Code Generator")

data = st.text_input("Enter the data you want to encode in the QR code")

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

        img = qr.make_image(fill_color="black", back_color="white")

        buf = BytesIO()
        img.save(buf, format="PNG")
        byte_im = buf.getvalue()

        st.image(imread(BytesIO(byte_im)))
    else:
        st.warning("Please enter data to generate a QR code")
