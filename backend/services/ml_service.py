import pickle
import numpy as np

# LOAD TRAINED MODEL
model = pickle.load(
    open("models/heart_risk_model.pkl", "rb")
)


def predict_heart_risk(data):

    # GENDER
    sex = 1 if data["gender"] == "Male" else 0

    # CHEST PAIN TYPE
    chest_pain_mapping = {
        "Typical Angina": 0,
        "Atypical Angina": 1,
        "Non-anginal Pain": 2,
        "Asymptomatic": 3
    }

    cp = chest_pain_mapping[data["chest_pain"]]

    # DIABETES
    fbs = 1 if data["diabetes"] == "Yes" else 0

    # SMOKING
    exang = 1 if data["smoking"] == "Yes" else 0

    # DEFAULT VALUES
    restecg = 1
    thalach = 150
    oldpeak = 1.0
    slope = 1
    ca = 0
    thal = 2

    # CREATE INPUT ARRAY
    input_data = np.array([[
        data["age"],
        sex,
        cp,
        data["blood_pressure"],
        data["cholesterol"],
        fbs,
        restecg,
        thalach,
        exang,
        oldpeak,
        slope,
        ca,
        thal
    ]])

    # PREDICT
    prediction = model.predict(input_data)

    # RETURN RESULT
    if prediction[0] == 1:
        return "High"

    return "Low"