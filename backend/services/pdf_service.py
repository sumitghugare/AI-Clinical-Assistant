from fpdf import FPDF
import os


def generate_pdf_report(data):

    pdf = FPDF()

    pdf.add_page()

    # TITLE
    pdf.set_font("Arial", "B", 20)

    pdf.cell(
        200,
        10,
        "AI Clinical Assistant Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    # PATIENT DETAILS
    pdf.set_font("Arial", "B", 14)

    pdf.cell(200, 10, "Patient Information", ln=True)

    pdf.set_font("Arial", "", 12)

    pdf.cell(200, 10, f"Name: {data['name']}", ln=True)

    pdf.cell(200, 10, f"Age: {data['age']}", ln=True)

    pdf.cell(200, 10, f"Gender: {data['gender']}", ln=True)

    pdf.ln(5)

    # HEALTH DETAILS
    pdf.set_font("Arial", "B", 14)

    pdf.cell(200, 10, "Health Metrics", ln=True)

    pdf.set_font("Arial", "", 12)

    pdf.cell(
        200,
        10,
        f"Weight: {data['weight']} kg",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Height: {data['height']} cm",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Cholesterol: {data['cholesterol']}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Blood Pressure: {data['blood_pressure']}",
        ln=True
    )

    pdf.ln(5)

    # BMI
    pdf.set_font("Arial", "B", 14)

    pdf.cell(200, 10, "BMI Analysis", ln=True)

    pdf.set_font("Arial", "", 12)

    pdf.cell(
        200,
        10,
        f"BMI: {data['bmi']:.2f}",
        ln=True
    )

    pdf.cell(
        200,
        10,
        f"Status: {data['bmi_status']}",
        ln=True
    )

    pdf.ln(5)

    # HEART RISK
    pdf.set_font("Arial", "B", 14)

    pdf.cell(200, 10, "Heart Risk Prediction", ln=True)

    pdf.set_font("Arial", "", 12)

    pdf.cell(
        200,
        10,
        f"Heart Risk: {data['heart_risk']}",
        ln=True
    )

    pdf.ln(5)

    # SYMPTOMS
    pdf.set_font("Arial", "B", 14)

    pdf.cell(200, 10, "Symptoms", ln=True)

    pdf.set_font("Arial", "", 12)

    pdf.multi_cell(
        0,
        10,
        data["symptoms"]
    )

    pdf.ln(5)

    # AI SUMMARY
    pdf.set_font("Arial", "B", 14)

    pdf.cell(200, 10, "AI Medical Summary", ln=True)

    pdf.set_font("Arial", "", 12)

    pdf.multi_cell(
        0,
        10,
        data["summary"]
    )

    # SAVE PDF
    output_path = "report.pdf"

    pdf.output(output_path)

    return output_path