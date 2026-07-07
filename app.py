# ============================================================
# Credit Card Approval Prediction System
# app.py
# ============================================================

from flask import Flask, render_template, request
import pickle
import os

from utils import preprocess_input

# ------------------------------------------------------------
# Flask App
# ------------------------------------------------------------

app = Flask(__name__)

# ------------------------------------------------------------
# Load Model Files
# ------------------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_FOLDER = os.path.join(BASE_DIR, "models")

with open(os.path.join(MODEL_FOLDER, "best_model.pkl"), "rb") as file:
    model = pickle.load(file)

with open(os.path.join(MODEL_FOLDER, "label_encoders.pkl"), "rb") as file:
    label_encoders = pickle.load(file)

# ------------------------------------------------------------
# Home Page
# ------------------------------------------------------------

@app.route("/")
def home():
    return render_template("index.html")

# ------------------------------------------------------------
# About Page
# ------------------------------------------------------------

@app.route("/about")
def about():
    return render_template("about.html")

# ------------------------------------------------------------
# Prediction Page
# ------------------------------------------------------------

@app.route("/predict", methods=["GET", "POST"])
def predict():

    if request.method == "POST":

        # Get Form Data
        form_data = request.form.to_dict()

        # Preprocess Input
        input_data = preprocess_input(form_data)

        # Prediction
        prediction = model.predict(input_data)[0]

        # Probability
        probability = model.predict_proba(input_data)[0]

        confidence = round(max(probability) * 100, 2)

        if prediction == 1:
            result = "Approved"
            message = "The applicant is likely to be approved for a credit card."
        else:
            result = "Rejected"
            message = "The applicant is likely to be rejected for a credit card."

        return render_template(
            "result.html",
            prediction=result,
            confidence=confidence,
            message=message,
            form=form_data
        )

    # -------- GET Request --------

    return render_template(
        "predict.html",

        genders=label_encoders["CODE_GENDER"].classes_,

        income_types=label_encoders["NAME_INCOME_TYPE"].classes_,

        education_types=label_encoders["NAME_EDUCATION_TYPE"].classes_,

        family_statuses=label_encoders["NAME_FAMILY_STATUS"].classes_,

        housing_types=label_encoders["NAME_HOUSING_TYPE"].classes_,

        occupations=label_encoders["OCCUPATION_TYPE"].classes_
    )

# ------------------------------------------------------------
# Run Application
# ------------------------------------------------------------

if __name__ == "__main__":
    app.run()