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
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap');

/* Hide automatic Streamlit pages menu */
[data-testid="stSidebarNav"] { display: none; }

/* ---- Animated Background ---- */
@keyframes gradientShift {
    0%   { background-position: 0% 50%; }
    50%  { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
@keyframes float { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.7} }
@keyframes glow { 0%,100%{box-shadow:0 0 15px rgba(139,92,246,.3)} 50%{box-shadow:0 0 30px rgba(139,92,246,.6)} }
@keyframes shimmer { 0%{background-position:-200% center} 100%{background-position:200% center} }

.stApp {
    background: linear-gradient(-45deg, #0f0c29, #1a1040, #302b63, #24243e, #0f0c29);
    background-size: 400% 400%;
    animation: gradientShift 15s ease infinite;
    color: #e2e8f0;
    font-family: 'Inter', sans-serif;
}

/* ---- Sidebar ---- */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0d0b1a 0%, #1a103a 50%, #0d0b1a 100%) !important;
    border-right: 1px solid rgba(139,92,246,0.2);
}
[data-testid="stSidebar"] .stRadio label {
    color: #c4b5fd !important;
    font-weight: 500;
    transition: all 0.3s ease;
}
[data-testid="stSidebar"] .stRadio label:hover { color: #a78bfa !important; }
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p { color: #a5b4fc; }

/* ---- Typography ---- */
h1 {
    background: linear-gradient(135deg, #a78bfa, #818cf8, #6366f1, #c084fc);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800 !important;
    letter-spacing: -0.5px;
}
h2 {
    background: linear-gradient(135deg, #c084fc, #f472b6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 700 !important;
}
h3 {
    color: #a5b4fc !important;
    font-weight: 600 !important;
}

/* ---- Glass Cards ---- */
.metric-card {
    background: linear-gradient(135deg, rgba(139,92,246,0.15), rgba(99,102,241,0.1));
    backdrop-filter: blur(12px);
    padding: 28px 20px;
    border-radius: 20px;
    text-align: center;
    border: 1px solid rgba(139,92,246,0.25);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
}
.metric-card:hover {
    transform: translateY(-6px);
    border-color: rgba(167,139,250,0.5);
    box-shadow: 0 16px 48px rgba(139,92,246,0.25);
}
.metric-card h3 {
    color: #c4b5fd !important;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 1.5px;
    margin-bottom: 8px;
}
.metric-card h2 {
    background: linear-gradient(135deg, #a78bfa, #818cf8);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-size: 28px !important;
    font-weight: 800 !important;
}

/* ---- Feature Card ---- */
.feature-card {
    background: linear-gradient(135deg, rgba(139,92,246,0.1), rgba(236,72,153,0.08));
    backdrop-filter: blur(10px);
    padding: 24px;
    border-radius: 18px;
    border: 1px solid rgba(139,92,246,0.2);
    margin-bottom: 12px;
    transition: all 0.3s ease;
}
.feature-card:hover {
    border-color: rgba(196,181,253,0.4);
    transform: translateY(-3px);
    box-shadow: 0 12px 36px rgba(139,92,246,0.15);
}
.feature-card .icon { font-size: 32px; margin-bottom: 10px; }
.feature-card .title { color: #c4b5fd; font-weight: 700; font-size: 18px; margin-bottom: 6px; }
.feature-card .desc { color: #94a3b8; font-size: 14px; line-height: 1.5; }

/* ---- Hero Banner ---- */
.hero-banner {
    background: linear-gradient(135deg, rgba(99,102,241,0.2), rgba(168,85,247,0.15), rgba(236,72,153,0.1));
    backdrop-filter: blur(16px);
    border: 1px solid rgba(139,92,246,0.3);
    border-radius: 24px;
    padding: 48px 40px;
    text-align: center;
    margin-bottom: 32px;
    position: relative;
    overflow: hidden;
}
.hero-banner::before {
    content: '';
    position: absolute;
    top: -50%; left: -50%;
    width: 200%; height: 200%;
    background: radial-gradient(circle, rgba(139,92,246,0.08) 0%, transparent 70%);
    animation: float 6s ease-in-out infinite;
}
.hero-banner h1 { font-size: 3em !important; margin-bottom: 8px; position: relative; }
.hero-banner p { color: #c4b5fd; font-size: 1.2em; position: relative; }

/* ---- Status Badge ---- */
.status-badge {
    display: inline-block;
    background: linear-gradient(135deg, #10b981, #059669);
    color: white;
    padding: 8px 24px;
    border-radius: 50px;
    font-weight: 600;
    font-size: 14px;
    box-shadow: 0 4px 15px rgba(16,185,129,0.3);
    animation: pulse 2s ease-in-out infinite;
}

/* ---- Buttons ---- */
.stButton>button {
    width: 100%;
    border-radius: 14px;
    height: 3.2em;
    background: linear-gradient(135deg, #8b5cf6, #6366f1, #a855f7) !important;
    color: white !important;
    font-size: 16px;
    font-weight: 700;
    border: none !important;
    letter-spacing: 0.5px;
    transition: all 0.4s cubic-bezier(0.4,0,0.2,1);
    box-shadow: 0 4px 20px rgba(139,92,246,0.3);
}
.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 30px rgba(139,92,246,0.5) !important;
    background: linear-gradient(135deg, #a78bfa, #818cf8, #c084fc) !important;
}

/* ---- File Uploader ---- */
[data-testid="stFileUploader"] {
    border: 2px dashed rgba(139,92,246,0.4);
    border-radius: 20px;
    padding: 24px;
    background: linear-gradient(135deg, rgba(139,92,246,0.05), rgba(99,102,241,0.03));
    transition: all 0.3s ease;
}
[data-testid="stFileUploader"]:hover {
    border-color: rgba(167,139,250,0.6);
    background: linear-gradient(135deg, rgba(139,92,246,0.1), rgba(99,102,241,0.06));
}

/* ---- Tech Badge ---- */
.tech-badge {
    display: inline-block;
    background: linear-gradient(135deg, rgba(139,92,246,0.2), rgba(99,102,241,0.15));
    color: #c4b5fd;
    padding: 6px 16px;
    border-radius: 50px;
    font-size: 13px;
    font-weight: 600;
    border: 1px solid rgba(139,92,246,0.25);
    margin: 4px;
    transition: all 0.3s ease;
}
.tech-badge:hover { background: linear-gradient(135deg, rgba(139,92,246,0.35), rgba(99,102,241,0.25)); transform: scale(1.05); }

/* ---- Result Cards ---- */
.result-card {
    background: linear-gradient(135deg, rgba(16,185,129,0.15), rgba(5,150,105,0.1));
    backdrop-filter: blur(12px);
    padding: 32px;
    border-radius: 20px;
    border: 1px solid rgba(16,185,129,0.3);
    text-align: center;
    animation: glow 3s ease-in-out infinite;
}
.result-card .digit { font-size: 72px; font-weight: 900; background: linear-gradient(135deg, #34d399, #10b981); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.result-card .label { color: #6ee7b7; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; }

.confidence-card {
    background: linear-gradient(135deg, rgba(99,102,241,0.15), rgba(139,92,246,0.1));
    backdrop-filter: blur(12px);
    padding: 32px;
    border-radius: 20px;
    border: 1px solid rgba(99,102,241,0.3);
    text-align: center;
}
.confidence-card .pct { font-size: 48px; font-weight: 900; background: linear-gradient(135deg, #a78bfa, #818cf8); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
.confidence-card .label { color: #a5b4fc; font-size: 14px; text-transform: uppercase; letter-spacing: 2px; }

/* ---- Divider ---- */
hr { border-color: rgba(139,92,246,0.15) !important; }

/* ---- Scrollbar ---- */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: #0f0c29; }
::-webkit-scrollbar-thumb { background: linear-gradient(#8b5cf6, #6366f1); border-radius: 3px; }

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

    # ---- Hero Banner ----
    st.markdown("""
    <div class="hero-banner">
        <h1>🧠 DeepVision AI</h1>
        <p>Advanced CNN Digit Classification System powered by Deep Learning</p>
        <br>
        <span class="status-badge">🟢 System Online</span>
    </div>
    """, unsafe_allow_html=True)

    # ---- Feature Cards ----
    st.markdown("## ✨ Key Features")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="icon">🎯</div>
            <div class="title">Real-time Prediction</div>
            <div class="desc">Instant digit recognition with high accuracy CNN model</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="icon">⚡</div>
            <div class="title">FastAPI Backend</div>
            <div class="desc">Lightning-fast REST API for seamless communication</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="feature-card">
            <div class="icon">🧠</div>
            <div class="title">Deep Learning</div>
            <div class="desc">TensorFlow CNN architecture for intelligent classification</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="feature-card">
            <div class="icon">📊</div>
            <div class="title">Confidence Scores</div>
            <div class="desc">Detailed probability scores for every prediction</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ---- Model Info Cards ----
    st.markdown("## 📊 Model Information")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown("""
        <div class="metric-card">
            <h3>Model Type</h3>
            <h2>CNN</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="metric-card">
            <h3>Framework</h3>
            <h2>TensorFlow</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="metric-card">
            <h3>Input Shape</h3>
            <h2>28×28×1</h2>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="metric-card">
            <h3>Classes</h3>
            <h2>0 — 9</h2>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # ---- Tech Stack Badges ----
    st.markdown("## 🛠️ Tech Stack")
    st.markdown("""
    <div style="text-align:center; padding: 20px 0;">
        <span class="tech-badge">🐍 Python</span>
        <span class="tech-badge">🎨 Streamlit</span>
        <span class="tech-badge">⚡ FastAPI</span>
        <span class="tech-badge">🧠 TensorFlow</span>
        <span class="tech-badge">🔢 NumPy</span>
        <span class="tech-badge">🖼️ Pillow</span>
        <span class="tech-badge">🌐 Uvicorn</span>
        <span class="tech-badge">📡 REST API</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")

    # ---- FastAPI Status ----
    st.markdown("## ⚡ FastAPI Backend")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        <div class="feature-card">
            <div class="icon">🟢</div>
            <div class="title">API Status: Online</div>
            <div class="desc">FastAPI backend connected and running successfully</div>
        </div>
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        <div class="feature-card">
            <div class="icon">📖</div>
            <div class="title">API Documentation</div>
            <div class="desc">Swagger UI available at http://127.0.0.1:8000/docs</div>
        </div>
        """, unsafe_allow_html=True)

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