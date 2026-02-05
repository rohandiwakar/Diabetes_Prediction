import streamlit as st
import numpy as np
import pickle
import time

# ===================== PAGE CONFIG =====================
st.set_page_config(
    page_title="Diabetes Risk Predictor",
    page_icon="🩺",
    layout="wide"
)

# ===================== REMOVE EXTRA TOP SPACE =====================
st.markdown("""
<style>
.block-container {
    padding-top: 0.8rem;
}
</style>
""", unsafe_allow_html=True)

# ===================== LOAD MODEL =====================
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ===================== TITLE =====================
st.markdown(
    "<h1 style='text-align:center; margin-top:0;'>🩺 Diabetes Risk Prediction System</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>AI-powered health risk assessment using Machine Learning</p>",
    unsafe_allow_html=True
)

st.divider()

# ===================== SIDEBAR INPUTS =====================
st.sidebar.header("🧾 Patient Information")

pregnancies = st.sidebar.slider("Pregnancies", 0, 20, 1)
glucose = st.sidebar.slider("Glucose Level", 50, 300, 120)
blood_pressure = st.sidebar.slider("Blood Pressure", 40, 200, 80)
skin_thickness = st.sidebar.slider("Skin Thickness", 0, 100, 20)
insulin = st.sidebar.slider("Insulin Level", 0, 900, 80)
bmi = st.sidebar.slider("BMI", 10.0, 60.0, 25.0)
dpf = st.sidebar.slider("Diabetes Pedigree Function", 0.0, 3.0, 0.5)
age = st.sidebar.slider("Age", 1, 100, 30)

# ===================== MAIN CONTENT =====================
col1, col2 = st.columns(2)

with col1:
    st.subheader("📌 About This App")
    st.write("""
    - Uses **Support Vector Machine (SVM)**
    - Medical data is **standardized**
    - Gives instant diabetes risk prediction
    """)

with col2:
    st.subheader("📊 Input Summary")
    st.json({
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "Blood Pressure": blood_pressure,
        "Skin Thickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "Diabetes Pedigree Function": dpf,
        "Age": age
    })

st.divider()

# ===================== PREDICT BUTTON =====================
if st.button("🔍 Predict Diabetes Risk", use_container_width=True):

    with st.spinner("Analyzing patient data..."):
        time.sleep(1.5)

        input_data = np.array([
            pregnancies,
            glucose,
            blood_pressure,
            skin_thickness,
            insulin,
            bmi,
            dpf,
            age
        ]).reshape(1, -1)

        scaled_data = scaler.transform(input_data)
        prediction = model.predict(scaled_data)

    if prediction[0] == 1:
        st.error("⚠️ High Risk of Diabetes Detected")
        st.warning("💡 Tip: Maintain healthy diet, exercise regularly, and consult a doctor.")
    else:
        st.success("✅ Low Risk of Diabetes")
        st.info("💡 Tip: Continue healthy lifestyle and regular checkups.")

# ===================== FOOTER =====================
st.divider()
st.markdown(
    "<p style='text-align:center; color:gray;'>Made with ❤️ using Streamlit & Machine Learning</p>",
    unsafe_allow_html=True
)
