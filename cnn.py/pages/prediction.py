# pages/prediction.py

import streamlit as st
from PIL import Image
import requests

# ============================================
# FASTAPI URL
# ============================================
API_URL = "http://127.0.0.1:8000/predict"

# ============================================
# PREDICTION PAGE
# ============================================
def prediction_page():

    st.title("📷 CNN Digit Prediction")

    st.write(
        "Upload a handwritten digit image for prediction"
    )

    st.markdown("---")

    # ============================================
    # FILE UPLOADER
    # ============================================
    uploaded_file = st.file_uploader(
        "Upload Digit Image",
        type=["jpg", "jpeg", "png"]
    )

    # ============================================
    # VALIDATION
    # ============================================
    if uploaded_file is not None:

        try:

            # ============================================
            # DISPLAY IMAGE
            # ============================================
            image = Image.open(uploaded_file)

            st.image(
                image,
                caption="Uploaded Image",
                width=250
            )

            st.markdown("---")

            # ============================================
            # PREDICT BUTTON
            # ============================================
            if st.button("🔍 Predict Digit"):

                # ============================================
                # LOADING
                # ============================================
                with st.spinner(
                    "Predicting digit..."
                ):

                    # ============================================
                    # SEND IMAGE TO FASTAPI
                    # ============================================
                    uploaded_file.seek(0)

                    files = {
                        "file": (
                            uploaded_file.name,
                            uploaded_file,
                            uploaded_file.type
                        )
                    }

                    response = requests.post(
                        API_URL,
                        files=files
                    )

                    # ============================================
                    # CHECK RESPONSE
                    # ============================================
                    if response.status_code == 200:

                        result = response.json()

                        st.success(
                            f"✅ Predicted Digit: {result['prediction']}"
                        )

                        st.info(
                            f"🎯 Confidence: {result['confidence']}%"
                        )

                    else:

                        st.error(
                            f"❌ API Error: {response.text}"
                        )

        except Exception as e:

            st.error(
                f"❌ Error Processing Image: {e}"
            )

    else:

        st.warning(
            "⚠ Please upload an image"
        )