# Advanced app.py for DeepVision AI

import streamlit as st
import os

from pages.prediction import prediction_page

# ============================================
# PAGE CONFIG
# ============================================
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

    CNN Deep Learning Application

    Built with Streamlit & TensorFlow
    """
)

# ============================================
# HOME PAGE
# ============================================
if page == "🏠 Home":

    st.title("🧠 DeepVision AI")

    st.subheader(
        "Advanced CNN Image Classification System"
    )

    col1, col2 = st.columns([2,1])

    with col1:

        st.write("""
        Welcome to DeepVision AI.

        This application uses a Convolutional Neural
        Network (CNN) model for intelligent image
        classification and prediction.

        ### 🚀 Features

        - Real-time Prediction
        - CNN Deep Learning
        - Probability Scores
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
                <h2>28x28</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

# ============================================
# PREDICTION PAGE
# ============================================
elif page == "📷 Prediction":

    prediction_page()

# ============================================
# ABOUT PAGE
# ============================================
elif page == "ℹ️ About":

    st.title("ℹ️ About DeepVision AI")

    st.write("""
    DeepVision AI is a modern deep learning
    application built using:

    - Python
    - TensorFlow
    - Streamlit
    - CNN Architecture
    - NumPy & Pillow
    """)

    st.success("✅ App Running Successfully")   