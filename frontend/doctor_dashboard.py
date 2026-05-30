# # import streamlit as st
# # import requests
# # import pandas as pd

# # API_URL = "http://127.0.0.1:8000"

# # st.set_page_config(
# #     page_title="Doctor Dashboard",
# #     layout="wide"
# # )

# # st.title("🩺 Doctor Dashboard")

# # st.write("AI Clinical Monitoring System")

# # # REFRESH BUTTON
# # if st.button("Refresh Data"):
# #     st.rerun()
    

# # # GET PATIENT DATA
# # response = requests.get(
# #     f"{API_URL}/patients/"
# # )

# # data = response.json()

# # patients = data["patients"]

# # # TOTAL PATIENTS
# # total_patients = len(patients)

# # # HIGH RISK COUNT
# # high_risk = 0

# # for patient in patients:

# #     if patient["prediction"] == "High":
# #         high_risk += 1

# # # DASHBOARD CARDS
# # col1, col2 = st.columns(2)

# # with col1:
# #     st.metric(
# #         "Total Patients",
# #         total_patients
# #     )

# # with col2:
# #     st.metric(
# #         "High Risk Patients",
# #         high_risk
# #     )

# # st.divider()

# # # PATIENT TABLE
# # st.subheader("Patient Records")

# # if len(patients) > 0:

# #     df = pd.DataFrame(patients)

# #     st.dataframe(
# #         df,
# #         use_container_width=True
# #     )

# # else:
# #     st.warning("No Patients Found")
# import streamlit as st
# import requests
# import pandas as pd

# # =====================================================
# # CONFIG
# # =====================================================

# API_URL = "http://127.0.0.1:8000"

# st.set_page_config(
#     page_title="Doctor Dashboard",
#     page_icon="🩺",
#     layout="wide"
# )

# # =====================================================
# # CUSTOM CSS
# # =====================================================

# st.markdown(
#     """
#     <style>

#     .main {
#         background-color: #0f172a;
#     }

#     .stApp {
#         background-color: #0f172a;
#         color: white;
#     }

#     .metric-card {
#         background: linear-gradient(135deg, #111827, #1f2937);
#         padding: 20px;
#         border-radius: 15px;
#         border: 1px solid #374151;
#         text-align: center;
#     }

#     .title-text {
#         font-size: 42px;
#         font-weight: bold;
#         color: #38bdf8;
#     }

#     .subtitle-text {
#         font-size: 18px;
#         color: #9ca3af;
#         margin-bottom: 20px;
#     }

#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # =====================================================
# # HEADER
# # =====================================================

# st.markdown(
#     """
#     <div class="title-text">
#         🩺 Doctor Dashboard
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(
#     """
#     <div class="subtitle-text">
#         AI Clinical Monitoring System
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # =====================================================
# # REFRESH BUTTON
# # =====================================================

# col_btn1, col_btn2 = st.columns([1, 5])

# with col_btn1:

#     if st.button("🔄 Refresh Data"):
#         st.rerun()

# st.divider()

# # =====================================================
# # GET PATIENT DATA
# # =====================================================

# try:

#     response = requests.get(
#         f"{API_URL}/patients/"
#     )

#     data = response.json()

#     patients = data["patients"]

# except Exception as e:

#     st.error(f"API Connection Error: {e}")

#     patients = []

# # =====================================================
# # ANALYTICS
# # =====================================================

# total_patients = len(patients)

# high_risk = 0

# low_risk = 0

# for patient in patients:

#     if patient["prediction"] == "High":
#         high_risk += 1
#     else:
#         low_risk += 1

# # =====================================================
# # METRIC CARDS
# # =====================================================

# col1, col2, col3 = st.columns(3)

# with col1:

#     st.metric(
#         "👥 Total Patients",
#         total_patients
#     )

# with col2:

#     st.metric(
#         "⚠️ High Risk Patients",
#         high_risk
#     )

# with col3:

#     st.metric(
#         "✅ Stable Patients",
#         low_risk
#     )

# st.divider()

# # =====================================================
# # PATIENT RECORDS
# # =====================================================

# st.subheader("📋 Patient Records")

# if len(patients) > 0:

#     df = pd.DataFrame(patients)

#     # Optional column ordering
#     preferred_columns = [
#         "name",
#         "age",
#         "gender",
#         "prediction",
#         "cholesterol",
#         "blood_pressure",
#         "symptoms"
#     ]

#     available_columns = [
#         col for col in preferred_columns
#         if col in df.columns
#     ]

#     df = df[available_columns]

#     # Highlight high-risk patients
#     def highlight_risk(row):

#         if row["prediction"] == "High":
#             return [
#                 "background-color: #7f1d1d; color: white"
#             ] * len(row)

#         return [
#             "background-color: #052e16; color: white"
#         ] * len(row)

#     styled_df = df.style.apply(
#         highlight_risk,
#         axis=1
#     )

#     st.dataframe(
#         styled_df,
#         use_container_width=True,
#         height=500
#     )

# else:

#     st.warning("No patient records found.")

# # =====================================================
# # FOOTER
# # =====================================================

# st.divider()

# st.caption(
#     "AI Clinical Assistant • Doctor Monitoring Panel"
# )
import streamlit as st
import requests
import pandas as pd

# =====================================================
# CONFIG
# =====================================================

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="Doctor Dashboard",
    page_icon="🩺",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown(
    """
    <style>

    .stApp {
        background-color: #0f172a;
        color: white;
    }

    .title-text {
        font-size: 42px;
        font-weight: bold;
        color: #38bdf8;
    }

    .subtitle-text {
        font-size: 18px;
        color: #9ca3af;
        margin-bottom: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# =====================================================
# HEADER
# =====================================================

st.markdown(
    """
    <div class="title-text">
        🩺 Doctor Dashboard
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle-text">
        AI Clinical Monitoring System
    </div>
    """,
    unsafe_allow_html=True
)

# =====================================================
# REFRESH BUTTON
# =====================================================

if st.button("🔄 Refresh Data"):
    st.rerun()

st.divider()

# =====================================================
# GET PATIENT DATA
# =====================================================

try:

    response = requests.get(
        f"{API_URL}/patients/"
    )

    data = response.json()

    patients = data["patients"]

except Exception as e:

    st.error(f"API Connection Error: {e}")

    patients = []

# =====================================================
# ANALYTICS
# =====================================================

total_patients = len(patients)

high_risk = sum(
    1 for p in patients
    if p["prediction"] == "High"
)

low_risk = total_patients - high_risk

# =====================================================
# METRIC CARDS
# =====================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "👥 Total Patients",
        total_patients
    )

with col2:
    st.metric(
        "⚠️ High Risk",
        high_risk
    )

with col3:
    st.metric(
        "✅ Stable",
        low_risk
    )

st.divider()

# =====================================================
# SEARCH PATIENT
# =====================================================

st.subheader("🔍 Search Patient")

patient_search = st.text_input(
    "Enter Patient Name"
)

filtered_patients = patients

if patient_search:

    filtered_patients = [

        patient for patient in patients

        if patient_search.lower()
        in patient["name"].lower()

    ]

# =====================================================
# SELECT PATIENT
# =====================================================

selected_patient = None

if len(filtered_patients) > 0:

    patient_names = [

        f"{patient['id']} - {patient['name']}"

        for patient in filtered_patients
    ]

    selected_name = st.selectbox(
        "Select Patient",
        patient_names,
        key="patient_selector"
    )

    selected_patient_id = int(
        selected_name.split(" - ")[0]
    )

    for patient in filtered_patients:

        if patient["id"] == selected_patient_id:

            selected_patient = patient

            break

st.divider()

# =====================================================
# PATIENT DETAILS
# =====================================================

if selected_patient:

    st.subheader("🩺 Patient Details")

    st.markdown(
        f"""
        <div style="
            background-color:#111827;
            padding:25px;
            border-radius:15px;
            border:1px solid #374151;
        ">

        <h3 style="color:#38bdf8;">
            {selected_patient['name']}
        </h3>

        <p style="color:white;">
            <b>Age:</b> {selected_patient['age']}
        </p>

        <p style="color:white;">
            <b>Prediction:</b> {selected_patient['prediction']}
        </p>

        <p style="color:white;">
            <b>Symptoms:</b>
            {selected_patient['symptoms']}
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )

    st.divider()

    # =================================================
    # VOICE CONSULTATION
    # =================================================

    st.subheader("🎤 Doctor Voice Consultation")

    audio_file = st.file_uploader(
        "Upload Consultation Recording",
        type=["mp3", "wav"]
    )

    transcription = ""

    if audio_file is not None:

        try:

            with st.spinner(
                "Analyzing consultation audio..."
            ):

                files = {
                    "file": (
                        audio_file.name,
                        audio_file,
                        audio_file.type
                    )
                }

                response = requests.post(
                    f"{API_URL}/transcribe",
                    files=files
                )

                result = response.json()

                if result["success"]:

                    transcription = result[
                        "transcription"
                    ]

                    st.success(
                        "Voice transcription completed!"
                    )

                else:

                    st.error(result["error"])

        except Exception as e:

            st.error(
                f"Voice Upload Error: {e}"
            )

    st.divider()

    # =================================================
    # DOCTOR NOTES
    # =================================================

    st.subheader("📝 Consultation Notes")

    doctor_note = st.text_area(
        "Doctor Notes",
        value=transcription,
        height=180
    )

    if st.button(
        "💾 Save Consultation Note"
    ):

        try:

            requests.post(

                f"{API_URL}/consultation/add",

                json={

                    "patient_id":
                    selected_patient["id"],

                    "note":
                    doctor_note
                }
            )

            st.success(
                "Consultation note saved successfully!"
            )

        except Exception as e:

            st.error(
                f"Save Error: {e}"
            )

    st.divider()

    # =================================================
    # CONSULTATION HISTORY
    # =================================================

    st.subheader("📜 Consultation History")

    try:

        response = requests.get(
            f"{API_URL}/consultation/{selected_patient['id']}"
        )

        notes_data = response.json()

        notes = notes_data["notes"]

        if len(notes) > 0:

            for note in notes:

                st.markdown(
                    f"""
                    <div style="
                        background-color:#111827;
                        padding:20px;
                        border-radius:12px;
                        border:1px solid #374151;
                        margin-bottom:15px;
                    ">

                    <p style="
                        color:#9ca3af;
                        font-size:14px;
                    ">
                        {note['created_at']}
                    </p>

                    <p style="
                        color:white;
                        font-size:18px;
                        line-height:1.7;
                    ">
                        {note['note']}
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:

            st.info(
                "No consultation history found."
            )

    except Exception as e:

        st.error(
            f"History Error: {e}"
        )

st.divider()

# =====================================================
# PATIENT RECORDS
# =====================================================

st.subheader("📋 Patient Records")

if len(filtered_patients) > 0:

    df = pd.DataFrame(filtered_patients)

    display_columns = [
        "name",
        "age",
        "prediction",
        "symptoms"
    ]

    available_columns = [

        col for col in display_columns

        if col in df.columns
    ]

    df = df[available_columns]

    st.dataframe(
        df,
        use_container_width=True,
        height=400
    )

else:

    st.warning(
        "No matching patient records found."
    )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "AI Clinical Assistant • Doctor Monitoring Panel"
)