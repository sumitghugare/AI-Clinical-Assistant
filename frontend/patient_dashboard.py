import streamlit as st
from components.styles import load_css
import requests

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="AI Clinical Assistant",
    page_icon="🏥",
    layout="wide"
)

# =====================================================
# LOAD CSS
# =====================================================

st.markdown(
    load_css(),
    unsafe_allow_html=True
)

API_URL = "http://127.0.0.1:8000"

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.title("🏥 AI Clinical Assistant")

    page = st.radio(
        "Navigation",
        [
            "Patient Analysis",
            "Prediction History",
            "AI Summary"
        ]
    )

# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
    <div class="main-title">
        AI Clinical Assistant
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="sub-title">
        AI Powered Healthcare Monitoring Platform
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# PATIENT ANALYSIS PAGE
# =====================================================

if page == "Patient Analysis":

    st.subheader("👤 Patient Healthcare Form")

    col1, col2 = st.columns(2)

    # =================================================
    # LEFT COLUMN
    # =================================================

    with col1:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        name = st.text_input(
            "Patient Name"
        )

        age = st.slider(
            "Age",
            1,
            100,
            30
        )

        gender = st.selectbox(
            "Gender",
            [
                "Male",
                "Female"
            ]
        )

        weight = st.number_input(
            "Weight (kg)",
            min_value=1.0,
            value=60.0
        )

        height = st.number_input(
            "Height (cm)",
            min_value=1.0,
            value=170.0
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    # =================================================
    # RIGHT COLUMN
    # =================================================

    with col2:

        st.markdown(
            '<div class="card">',
            unsafe_allow_html=True
        )

        smoking = st.radio(
            "Smoking Habit",
            [
                "Yes",
                "No"
            ]
        )

        diabetes = st.radio(
            "Diabetes",
            [
                "Yes",
                "No"
            ]
        )

        cholesterol = st.number_input(
            "Cholesterol Level",
            value=180.0
        )

        blood_pressure = st.number_input(
            "Blood Pressure",
            value=120.0
        )

        chest_pain = st.selectbox(
            "Chest Pain Type",
            [
                "Typical Angina",
                "Atypical Angina",
                "Non-anginal Pain",
                "Asymptomatic"
            ]
        )

        st.markdown(
            '</div>',
            unsafe_allow_html=True
        )

    st.divider()

    symptoms = st.text_area(
        "Describe Symptoms",
        height=150,
        placeholder="Example: chest pain, dizziness, fatigue..."
    )

    col3, col4 = st.columns(2)

    # =================================================
    # HEART RISK PREDICTION
    # =================================================

    with col3:

        if st.button("🔍 Predict Heart Risk"):

            patient_data = {

                "name": name,
                "age": age,
                "gender": gender,
                "weight": weight,
                "height": height,
                "smoking": smoking,
                "diabetes": diabetes,
                "cholesterol": cholesterol,
                "blood_pressure": blood_pressure,
                "chest_pain": chest_pain,
                "symptoms": symptoms
            }

            try:

                with st.spinner(
                    "Analyzing Patient Data..."
                ):

                    response = requests.post(
                        f"{API_URL}/prediction/",
                        json=patient_data
                    )

                    result = response.json()

                    heart_risk = result["heart_risk"]

                    summary_text = (
                        "AI analysis completed successfully."
                    )

                # =====================================
                # BMI CALCULATION
                # =====================================

                height_meter = height / 100

                bmi = weight / (
                    height_meter ** 2
                )

                bmi_status = "Normal"

                if bmi < 18.5:

                    bmi_status = "Underweight"

                elif bmi >= 25 and bmi < 30:

                    bmi_status = "Overweight"

                elif bmi >= 30:

                    bmi_status = "Obese"

                # =====================================
                # BMI CARD
                # =====================================

                st.markdown(
                    f"""
                    <div style="
                        background-color:#111827;
                        padding:25px;
                        border-radius:15px;
                        border:1px solid #374151;
                        margin-top:20px;
                    ">

                    <h2 style="color:#38bdf8;">
                        📊 BMI Analysis
                    </h2>

                    <h3 style="color:white;">
                        BMI: {bmi:.2f}
                    </h3>

                    <h4 style="color:#9ca3af;">
                        Status: {bmi_status}
                    </h4>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # =====================================
                # HIGH RISK CARD
                # =====================================

                if heart_risk == "High":

                    st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #ff4b4b, #b30000);
        padding: 30px;
        border-radius: 15px;
        color: white;
        margin-top: 20px;
        box-shadow: 0px 4px 20px rgba(255,0,0,0.3);
    ">

    <h1 style="color:white;">
        ⚠️ HIGH HEART RISK
    </h1>

    <h3 style="color:white;">
        Immediate medical attention recommended.
    </h3>

    <p style="font-size:18px;">
        The AI system detected elevated cardiovascular risk indicators.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)
                # =====================================
                # LOW RISK CARD
                # =====================================

                else:

                    st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, #00b894, #009970);
        padding: 30px;
        border-radius: 15px;
        color: white;
        margin-top: 20px;
        box-shadow: 0px 4px 20px rgba(0,255,150,0.2);
    ">

    <h1 style="color:white;">
        ✅ LOW HEART RISK
    </h1>

    <h3 style="color:white;">
        Patient currently appears stable.
    </h3>

    <p style="font-size:18px;">
        Current health indicators appear within safer ranges.
    </p>

    </div>
    """,
    unsafe_allow_html=True
)

                # =====================================
                # PDF REPORT
                # =====================================

                report_data = {

                    "name": name,
                    "age": age,
                    "gender": gender,
                    "weight": weight,
                    "height": height,
                    "cholesterol": cholesterol,
                    "blood_pressure": blood_pressure,
                    "bmi": bmi,
                    "bmi_status": bmi_status,
                    "heart_risk": heart_risk,
                    "symptoms": symptoms,
                    "summary": summary_text
                }

                report_response = requests.post(
                    f"{API_URL}/report/",
                    json=report_data
                )

                if report_response.status_code == 200:

                    st.download_button(
                        label="📄 Download Medical Report",
                        data=report_response.content,
                        file_name="medical_report.pdf",
                        mime="application/pdf"
                    )

            except Exception as e:

                st.error(
                    f"API Error: {e}"
                )

    # =================================================
    # AI SUMMARY
    # =================================================

    with col4:

        if st.button("🧠 Generate AI Summary"):

            try:

                with st.spinner(
                    "Generating AI Medical Summary..."
                ):

                    response = requests.post(
                        f"{API_URL}/summary/",
                        json={
                            "symptoms": symptoms
                        }
                    )

                    result = response.json()

                    summary = result["ai_summary"]

                st.markdown(
                    f"""
                    <div style="
                        background-color:#111827;
                        padding:30px;
                        border-radius:15px;
                        border:1px solid #374151;
                        margin-top:20px;
                    ">

                    <h2 style="color:#38bdf8;">
                        📋 AI Medical Summary
                    </h2>

                    <p style="
                        color:white;
                        font-size:18px;
                        line-height:1.8;
                    ">
                        {summary}
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

            except Exception as e:

                st.error(
                    f"Summary API Error: {e}"
                )