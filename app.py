import streamlit as st
import qrcode
from PIL import Image
import io

def generate_qr_code(data: str) -> Image.Image:
    """Generate a QR code as a PIL image."""
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
    return img

# Streamlit App
st.title("QR Code Generator for Business Cards")

# User inputs
name = st.text_input("Full Name")
job_title = st.text_input("Job Title")
company = st.text_input("Company Name")
phone = st.text_input("Phone Number")
email = st.text_input("Email Address")
website = st.text_input("Website (optional)")

if st.button("Generate QR Code"):
    if not name or not phone or not email:
        st.error("Name, phone, and email are required!")
    else:
        # Format vCard data
        qr_data = f"""
        BEGIN:VCARD
        VERSION:3.0
        FN:{name}
        TITLE:{job_title}
        ORG:{company}
        TEL:{phone}
        EMAIL:{email}
        URL:{website if website else ''}
        END:VCARD
        """
        # Generate QR code
        img = generate_qr_code(qr_data)

        # Display the QR code
        st.image(img, caption="Your QR Code", use_column_width=True)

        # Download button
        buf = io.BytesIO()
        img.save(buf, format="JPEG")
        byte_im = buf.getvalue()
        st.download_button("Download QR Code", data=byte_im, file_name="business_card_qr.jpg", mime="image/jpeg")
