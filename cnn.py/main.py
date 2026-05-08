import sys
import io as _io

# ============================================
# FIX: Force UTF-8 encoding on Windows
# Prevents UnicodeEncodeError with emoji/unicode
# characters in print() on cp1252 terminals
# ============================================
sys.stdout = _io.TextIOWrapper(
    sys.stdout.buffer, encoding="utf-8", errors="replace"
)
sys.stderr = _io.TextIOWrapper(
    sys.stderr.buffer, encoding="utf-8", errors="replace"
)

from fastapi import FastAPI, UploadFile, File, HTTPException
import tensorflow as tf
import numpy as np
from PIL import Image
import io

# ============================================
# FASTAPI APP
# ============================================
app = FastAPI()

# ============================================
# LOAD MODEL
# ============================================
try:

    model = tf.keras.models.load_model(
        "cnn_model.keras"
    )

    print("✅ CNN Model Loaded Successfully")

except Exception as e:

    print(f"❌ Model Loading Error: {e}")

    model = None

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
def preprocess_image(image):

    try:

        # Convert to grayscale
        image = image.convert("L")

        # Resize image
        image = image.resize((28, 28))

        # Convert image to array
        img_array = np.array(image)

        # Normalize
        img_array = img_array / 255.0

        # Reshape for CNN
        img_array = img_array.reshape(
            1,
            28,
            28,
            1
        )

        return img_array

    except Exception as e:

        raise HTTPException(
            status_code=400,
            detail=f"Image preprocessing failed: {e}"
        )

# ============================================
# HOME ROUTE
# ============================================
@app.get("/")
def home():

    return {
        "message": "DeepVision AI FastAPI Backend Running"
    }

# ============================================
# PREDICTION API
# ============================================
@app.post("/predict")
async def predict(
    file: UploadFile = File(...)
):

    # ============================================
    # CHECK MODEL
    # ============================================
    if model is None:

        raise HTTPException(
            status_code=500,
            detail="CNN model not loaded"
        )

    # ============================================
    # VALIDATE FILE TYPE
    # ============================================
    allowed_types = [
        "image/jpeg",
        "image/png",
        "image/jpg"
    ]

    if file.content_type not in allowed_types:

        raise HTTPException(
            status_code=400,
            detail="Invalid image format"
        )

    try:

        # ============================================
        # READ IMAGE
        # ============================================
        contents = await file.read()

        # ============================================
        # OPEN IMAGE
        # ============================================
        image = Image.open(
            io.BytesIO(contents)
        )

        # ============================================
        # PREPROCESS IMAGE
        # ============================================
        processed = preprocess_image(image)

        # ============================================
        # PREDICT
        # ============================================
        prediction = model.predict(processed)

        # ============================================
        # GET PREDICTED INDEX
        # ============================================
        predicted_index = int(
            np.argmax(prediction)
        )

        # ============================================
        # CONFIDENCE SCORE
        # ============================================
        confidence = float(
            np.max(prediction) * 100
        )

        # ============================================
        # PREDICTED CLASS
        # ============================================
        predicted_class = class_names[
            predicted_index
        ]

        # ============================================
        # RETURN JSON RESPONSE
        # ============================================
        return {
            "success": True,
            "prediction": predicted_class,
            "confidence": round(confidence, 2)
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {e}"
        )

# ============================================
# HEALTH CHECK ROUTE
# ============================================
@app.get("/health")
def health_check():

    return {
        "status": "API Running Successfully"
    }