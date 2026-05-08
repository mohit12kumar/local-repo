# Advanced app.py for DeepVision AI

import streamlit as st
import os

from pages.prediction import prediction_page

# ============================================
# PAGE CONFIG
# =============================uvicorn main:app --reload===============
st.set_page_config(
    page_title="DeepVision AI",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================
# CUSTOM CSS
# ============================================
st.markdown("""
<style>

/* Hide automatic Streamlit pages menu */
[data-testid="stSidebarNav"] {
    display: none;
}

/* Main Background */
.stApp {
    background: linear-gradient(to right, #0f172a, #111827);
    color: white;
}

/* Sidebar */
[data-testid="stSidebar"] {
    background-color: #0b1120;
}

/* Titles */
h1, h2, h3 {
    color: #38bdf8;
}

/* Buttons */
.stButton>button {
    width: 100%;
    border-radius: 12px;
    height: 3em;
    background: linear-gradient(to right, #38bdf8, #0ea5e9);
    color: white;
    font-size: 16px;
    font-weight: bold;
    border: none;
}

/* File uploader */
[data-testid="stFileUploader"] {
    border: 2px dashed #38bdf8;
    border-radius: 15px;
    padding: 20px;
    background-color: rgba(255,255,255,0.03);
}

/* Cards */
.metric-card {
    background-color: rgba(255,255,255,0.05);
    padding: 20px;
    border-radius: 18px;
    text-align: center;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.3);
}

</style>
""", unsafe_allow_html=True)

# ============================================
# LOGO PATH
# ============================================
LOGO_PATH = r"C:\Users\riyam\OneDrive\Desktop\New folder (5)\local-repo\cnn.py\asset\logo.png"

# ============================================
# SIDEBAR
# ============================================

if os.path.exists(LOGO_PATH):
    st.sidebar.image(LOGO_PATH, width=220)
else:
    st.sidebar.error("❌ Logo image not found")

st.sidebar.markdown("---")

st.sidebar.title("📌 Navigation")

page = st.sidebar.radio(
    "Go To",
    [
        "🏠 Home",
        "📷 Prediction",
        "ℹ️ About"
    ]
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
    DeepVision AI

    CNN Digit Prediction System

    Built with Streamlit, FastAPI & TensorFlow
    """
)

# ============================================
# HOME PAGE
# ============================================
if page == "🏠 Home":

    st.title("🧠 DeepVision AI")

    st.subheader(
        "Advanced CNN Digit Classification System"
    )

    col1, col2 = st.columns([2,1])

    with col1:

        st.write("""
        Welcome to DeepVision AI.

        This application uses a Convolutional Neural
        Network (CNN) model for handwritten digit
        classification and prediction.

        ### 🚀 Features

        - Real-time Digit Prediction
        - CNN Deep Learning
        - FastAPI Backend
        - Probability Scores
        - Multiple Image Upload
        - Professional Dashboard
        - Streamlit Interactive UI
        - TensorFlow Model Integration
        """)

    with col2:

        if os.path.exists(LOGO_PATH):
            st.image(LOGO_PATH, width=280)

    st.markdown("---")

    st.header("📊 Model Information")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <div class="metric-card">
                <h3>Model</h3>
                <h2>CNN</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            """
            <div class="metric-card">
                <h3>Framework</h3>
                <h2>TensorFlow</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            """
            <div class="metric-card">
                <h3>Input Shape</h3>
                <h2>28x28x1</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ============================================
    # FASTAPI SECTION
    # ============================================
    st.markdown("---")

    st.header("⚡ FastAPI Backend")

    st.success(
        "FastAPI backend connected successfully"
    )

    st.code(
        "http://127.0.0.1:8000/docs"
    )

# ============================================
# PREDICTION PAGE
# ============================================
elif page == "📷 Prediction":

    prediction_page()

# ============================================
# ABOUT PAGE
# ============================================
# ============================================
# ABOUT PAGE
# ============================================
elif page == "ℹ️ About":

    st.title("ℹ️ About DeepVision AI")

    st.markdown("""
    # 🧠 DeepVision AI

    DeepVision AI is a modern Artificial Intelligence
    and Deep Learning based web application developed
    for handwritten digit recognition using a
    Convolutional Neural Network (CNN).

    This system is capable of identifying handwritten
    numerical digits from uploaded images with high
    accuracy using TensorFlow deep learning models.

    The application combines:

    - Streamlit Frontend
    - FastAPI Backend
    - TensorFlow CNN Model
    - REST API Communication

    into a complete full-stack AI application.

    ---

    # 🎯 Project Objective

    The main objective of this project is to develop
    an intelligent handwritten digit recognition system
    that can:

    ✔ Accept handwritten digit images

    ✔ Process and preprocess uploaded images

    ✔ Predict the handwritten digit accurately

    ✔ Display confidence scores

    ✔ Provide real-time prediction results

    ✔ Integrate Deep Learning with Web APIs

    ✔ Demonstrate AI-based image classification

    ---

    # 🏗️ System Architecture

    The project follows a full-stack AI architecture.

    ## Step 1 — User Upload

    The user uploads a handwritten digit image
    using the Streamlit web interface.

    ↓

    ## Step 2 — Frontend Processing

    Streamlit handles:
    - UI rendering
    - File upload
    - Image preview
    - API requests
    - Result display

    ↓

    ## Step 3 — FastAPI Backend

    The uploaded image is sent to the FastAPI backend
    using HTTP POST API requests.

    The backend handles:
    - API routes
    - Request validation
    - Image preprocessing
    - CNN prediction
    - JSON response generation

    ↓

    ## Step 4 — Image Preprocessing

    Before prediction, the image is processed:

    - Converted to grayscale
    - Resized to 28×28
    - Normalized between 0 and 1
    - Reshaped into CNN input format

    Model Input Shape:
    (1, 28, 28, 1)

    ↓

    ## Step 5 — CNN Prediction

    The TensorFlow CNN model predicts the digit.

    The model outputs:
    - Predicted digit
    - Confidence score

    ↓

    ## Step 6 — Result Display

    The prediction result is returned to Streamlit
    and displayed to the user in real-time.

    ---

    # 🤖 Convolutional Neural Network (CNN)

    The project uses a CNN deep learning model.

    CNN is a specialized neural network architecture
    mainly used for image classification and
    computer vision tasks.

    The CNN model automatically learns:

    - Image patterns
    - Edges
    - Shapes
    - Pixel relationships
    - Feature extraction

    from training data.

    ### CNN Layers Used

    ✔ Convolution Layer

    ✔ Activation Layer (ReLU)

    ✔ Pooling Layer

    ✔ Flatten Layer

    ✔ Dense Layer

    ✔ Output Layer (Softmax)

    ---

    # 📷 Input Specifications

    The application accepts:

    ✔ JPG Images

    ✔ JPEG Images

    ✔ PNG Images

    ### Image Requirements

    - Handwritten digit image
    - Clear background
    - Single digit preferred
    - 28×28 grayscale format

    ---

    # 📊 Prediction Classes

    The CNN model predicts the following digits:

    0, 1, 2, 3, 4, 5, 6, 7, 8, 9

    along with prediction confidence.

    Example:

    Predicted Digit → 7

    Confidence Score → 98.45%

    ---

    # ⚙️ Technologies Used

    ## Frontend Technologies

    ### Streamlit
    Used for creating:
    - Interactive UI
    - Dashboard
    - Upload system
    - Result display

    ### HTML/CSS
    Used for:
    - Styling
    - Layout design
    - Professional appearance

    ---

    ## Backend Technologies

    ### FastAPI
    Used for:
    - REST API development
    - Backend server
    - API routing
    - Prediction handling

    ### Uvicorn
    Used as FastAPI server.

    ---

    ## Deep Learning Technologies

    ### TensorFlow
    Used for:
    - CNN model development
    - Training
    - Prediction

    ### Keras
    Used for:
    - Model building
    - Neural network layers

    ---

    ## Python Libraries

    ### NumPy
    Numerical array operations.

    ### Pillow (PIL)
    Image processing library.

    ### Pandas
    Data handling and display.

    ### Requests
    API communication between frontend
    and backend.

    ---

    # 🔒 Validation & Error Handling

    The system contains multiple validation
    and error handling mechanisms.

    ## Validation Features

    ✔ File type validation

    ✔ Image upload validation

    ✔ API request validation

    ✔ Model loading validation

    ✔ Input preprocessing validation

    ✔ Prediction validation

    ---

    ## Error Handling Features

    ✔ Invalid image detection

    ✔ Backend connection handling

    ✔ Prediction exception handling

    ✔ File processing error handling

    ✔ API failure handling

    ✔ Model error handling

    ---

    # 🌐 API Integration

    The project uses REST API communication.

    Streamlit frontend communicates with
    FastAPI backend using HTTP POST requests.

    API Endpoint:

    http://127.0.0.1:8000/predict

    Swagger API Documentation:

    http://127.0.0.1:8000/docs

    ---

    # 📈 Advantages of the Project

    ✔ Real-time digit prediction

    ✔ Fast prediction speed

    ✔ Deep learning-based accuracy

    ✔ Interactive web interface

    ✔ Backend API integration

    ✔ Scalable architecture

    ✔ Professional deployment structure

    ✔ Reusable preprocessing pipeline

    ---

    # 🚀 Future Enhancements

    Future improvements may include:

    ✔ Multi-digit recognition

    ✔ Real-time webcam prediction

    ✔ Advanced CNN architectures

    ✔ Cloud deployment

    ✔ Database integration

    ✔ User authentication

    ✔ Model performance analytics

    ✔ AI explainability visualization

    ---

    # 👨‍💻 Developed By

    DeepVision AI Project

    Handwritten Digit Recognition System

    Built using:
    Streamlit + FastAPI + TensorFlow + CNN
    """)

    st.success("✅ DeepVision AI Application Running Successfully")