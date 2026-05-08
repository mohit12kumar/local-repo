# pages/prediction.py

import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import pandas as pd

# ============================================
# LOAD MODEL
# ============================================
model = tf.keras.models.load_model(
    r"C:\Users\riyam\OneDrive\Desktop\New folder (5)\local-repo\cnn_model.keras"
)

# ============================================
# CLASS NAMES
# ============================================
class_names = [
    "0",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9"
]

# ============================================
# IMAGE PREPROCESS FUNCTION
# ============================================
def preprocess_image(uploaded_file):

    # Open image
    image = Image.open(uploaded_file)

    # Convert to grayscale
    image = image.convert("L")

    # Resize image
    image = image.resize((28, 28))

    # Convert image to numpy array
    img_array = np.array(image)

    # Normalize image
    img_array = img_array / 255.0

    # Reshape for CNN
    img_array = img_array.reshape(
        1,
        28,
        28,
        1
    )

    return img_array

# ============================================
# SINGLE IMAGE PREDICTION
# ============================================
def predict_image(uploaded_file):

    # Preprocess image
    processed = preprocess_image(uploaded_file)

    # Predict
    prediction = model.predict(processed)

    # Get class index
    predicted_index = np.argmax(prediction)

    # Confidence score
    confidence = np.max(prediction) * 100

    # Predicted class
    predicted_class = class_names[predicted_index]

    return predicted_class, confidence

# ============================================
# PREDICTION PAGE
# ============================================
def prediction_page():

    st.title("📷 CNN Digit Prediction Dashboard")

    st.write(
        "Upload single or multiple digit images for prediction"
    )

    # ============================================
    # FILE UPLOADER
    # ============================================
    uploaded_files = st.file_uploader(
        "Upload Images",
        type=["jpg", "jpeg", "png"],
        accept_multiple_files=True
    )

    # ============================================
    # IF FILES UPLOADED
    # ============================================
    if uploaded_files:

        results = []

        for uploaded_file in uploaded_files:

            # Open image for display
            image = Image.open(uploaded_file)

            # Prediction
            predicted_class, confidence = predict_image(
                uploaded_file
            )

            st.markdown("---")

            col1, col2 = st.columns([1, 2])

            with col1:

                st.image(
                    image,
                    caption=uploaded_file.name,
                    width=200
                )

            with col2:

                st.success(
                    f"Predicted Digit: {predicted_class}"
                )

                st.info(
                    f"Confidence: {confidence:.2f}%"
                )

            # Store results
            results.append({
                "Image Name": uploaded_file.name,
                "Prediction": predicted_class,
                "Confidence": f"{confidence:.2f}%"
            })

        # ============================================
        # RESULTS TABLE
        # ============================================
        st.markdown("---")

        st.subheader(
            "📊 Batch Prediction Results"
        )

        df = pd.DataFrame(results)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.warning(
            "⚠ Upload one or more images"
        )