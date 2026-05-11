# pages/prediction.py

import streamlit as st
from PIL import Image
import requests
import io
import numpy as np
from streamlit_drawable_canvas import st_canvas

# ============================================
# FASTAPI CONFIG
# ============================================
API_URL = "http://127.0.0.1:8000/predict"
HEALTH_URL = "http://127.0.0.1:8000/health"

def check_backend():
    """Verify if the FastAPI server is reachable."""
    try:
        response = requests.get(HEALTH_URL, timeout=2)
        return response.status_code == 200
    except:
        return False

# ============================================
# PREDICTION PAGE
# ============================================
def prediction_page():

    # ---- Header ----
    st.markdown("""
    <div style="text-align:center; padding: 20px 0 10px 0;">
        <h1>📷 CNN Digit Prediction</h1>
        <p style="color:#c4b5fd; font-size:1.1em;">
            Draw or upload a handwritten digit and let AI analyze it
        </p>
    </div>
    """, unsafe_allow_html=True)

    # ---- Backend Status Check ----
    is_online = check_backend()
    if not is_online:
        st.warning("⚠️ Backend server (FastAPI) is offline. Please start it using: `uvicorn main:app --reload`")
    else:
        st.success("✅ Backend System Online")

    st.markdown("---")

    # ============================================
    # INPUT SECTION (Tabs for Draw/Upload)
    # ============================================
    input_tab1, input_tab2 = st.tabs(["✏️ Draw Digit", "📤 Upload Image"])
    
    source_image = None
    image_name = "input_image.png"
    is_drawing = False

    # ---- Tab 1: Drawing Pad ----
    with input_tab1:
        st.markdown("### ✍️ Drawing Pad")
        st.info("Draw a single digit (0-9) in the center of the black box below.")
        
        canvas_result = st_canvas(
            fill_color="rgba(255, 255, 255, 0.3)",
            stroke_width=20,
            stroke_color="#FFFFFF",
            background_color="#000000",
            height=280,
            width=280,
            drawing_mode="freedraw",
            key="canvas",
            display_toolbar=True,
        )
        
        if canvas_result.image_data is not None:
            # Check if user has actually drawn something (not just black)
            if np.any(canvas_result.image_data[:, :, :3] > 0):
                is_drawing = True
                # Convert canvas to PIL Image
                img_drawn = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')
                img_drawn = img_drawn.convert("RGB")
                
                # Convert to bytes
                buf = io.BytesIO()
                img_drawn.save(buf, format="PNG")
                buf.seek(0)
                source_image = buf
                image_name = "drawing.png"

    # ---- Tab 2: Upload ----
    with input_tab2:
        uploaded_file = st.file_uploader(
            "Choose a digit image...",
            type=["jpg", "jpeg", "png"],
            key="uploader"
        )
        if uploaded_file:
            source_image = uploaded_file
            image_name = uploaded_file.name
            is_drawing = False

    # ============================================
    # PREVIEW & PREDICT
    # ============================================
    if source_image is not None:
        
        # If it's a drawing, we skip the preview column to keep it clean
        if is_drawing:
            st.markdown("---")
            col_btn = st.columns([1, 2, 1])[1]
            with col_btn:
                predict_btn = st.button("🔍 Run Prediction", type="primary", use_container_width=True)
        else:
            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown("### 🖼️ Input Preview")
                img_preview = Image.open(source_image)
                st.image(img_preview, caption="Target Image", use_container_width=True)
            with col2:
                st.markdown("### ⚙️ Actions")
                predict_btn = st.button("🔍 Run Prediction", type="primary", use_container_width=True)

        # ---- Common Prediction Logic ----
        if 'predict_btn' in locals() and predict_btn:
            if not is_online:
                st.error("Cannot predict: Backend is offline.")
            else:
                with st.spinner("🧠 CNN is thinking..."):
                    try:
                        source_image.seek(0)
                        files = {"file": (image_name, source_image, "image/png")}
                        response = requests.post(API_URL, files=files)
                        
                        if response.status_code == 200:
                            result = response.json()
                            digit = result['prediction']
                            confidence = result['confidence']

                            st.markdown("---")
                            res_col1, res_col2 = st.columns(2)
                            with res_col1:
                                st.markdown(f"""
                                <div class="result-card">
                                    <div class="label">Predicted Digit</div>
                                    <div class="digit">{digit}</div>
                                </div>
                                """, unsafe_allow_html=True)
                            with res_col2:
                                st.markdown(f"""
                                <div class="confidence-card">
                                    <div class="label">Confidence</div>
                                    <div class="pct">{confidence}%</div>
                                </div>
                                """, unsafe_allow_html=True)
                            st.progress(confidence / 100)
                        else:
                            st.error(f"Prediction failed: {response.text}")
                    except Exception as e:
                        st.error(f"Connection Error: {e}")

    else:
        # ---- Empty State ----
        st.markdown("""
        <div style="text-align:center; padding:60px 20px;
                    background: linear-gradient(135deg, rgba(139,92,246,0.08), rgba(99,102,241,0.05));
                    border-radius: 20px;
                    border: 1px dashed rgba(139,92,246,0.3);
                    margin-top: 20px;">
            <div style="font-size:64px; margin-bottom:16px;">✏️</div>
            <div style="color:#a5b4fc; font-size:18px; font-weight:600;">
                Ready for Input
            </div>
            <div style="color:#6b7280; font-size:14px; margin-top:8px;">
                Draw or upload an image to start predicting digits.
            </div>
        </div>
        """, unsafe_allow_html=True)