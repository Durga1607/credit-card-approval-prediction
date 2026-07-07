import pickle
import pandas as pd
import numpy as np
import os

# ---------------------------------------------------
# Load Encoders
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_FOLDER = os.path.join(BASE_DIR, "models")

with open(os.path.join(MODEL_FOLDER, "label_encoders.pkl"), "rb") as f:
    label_encoders = pickle.load(f)

with open(os.path.join(MODEL_FOLDER, "feature_columns.pkl"), "rb") as f:
    feature_columns = pickle.load(f)

# ---------------------------------------------------
# Helper Function
# ---------------------------------------------------

def encode_value(column, value):

    if column in label_encoders:
        encoder = label_encoders[column]

        if value not in encoder.classes_:
            value = encoder.classes_[0]

        return encoder.transform([value])[0]

    return value

# ---------------------------------------------------
# Main Preprocessing Function
# ---------------------------------------------------

def preprocess_input(form):

    data = {}

    # Gender
    data["CODE_GENDER"] = encode_value(
        "CODE_GENDER",
        form["CODE_GENDER"]
    )

    # Own Car
    data["FLAG_OWN_CAR"] = encode_value(
        "FLAG_OWN_CAR",
        form["FLAG_OWN_CAR"]
    )

    # Own House
    data["FLAG_OWN_REALTY"] = encode_value(
        "FLAG_OWN_REALTY",
        form["FLAG_OWN_REALTY"]
    )

    # Children
    data["CNT_CHILDREN"] = int(form["CNT_CHILDREN"])

    # Income
    data["AMT_INCOME_TOTAL"] = float(form["AMT_INCOME_TOTAL"])

    # Income Type
    data["NAME_INCOME_TYPE"] = encode_value(
        "NAME_INCOME_TYPE",
        form["NAME_INCOME_TYPE"]
    )

    # Education
    data["NAME_EDUCATION_TYPE"] = encode_value(
        "NAME_EDUCATION_TYPE",
        form["NAME_EDUCATION_TYPE"]
    )

    # Family Status
    data["NAME_FAMILY_STATUS"] = encode_value(
        "NAME_FAMILY_STATUS",
        form["NAME_FAMILY_STATUS"]
    )

    # Housing
    data["NAME_HOUSING_TYPE"] = encode_value(
        "NAME_HOUSING_TYPE",
        form["NAME_HOUSING_TYPE"]
    )

    # Occupation
    data["OCCUPATION_TYPE"] = encode_value(
        "OCCUPATION_TYPE",
        form["OCCUPATION_TYPE"]
    )

    # Family Members
    data["CNT_FAM_MEMBERS"] = float(
        form["CNT_FAM_MEMBERS"]
    )

    # Age
    age = int(form["AGE"])

    data["AGE"] = age

    # Employment Years
    emp = float(form["EMPLOYMENT_YEARS"])

    data["EMPLOYMENT_YEARS"] = emp

    # Income Category
    income = data["AMT_INCOME_TOTAL"]

    if income < 100000:
        category = "Low"

    elif income < 200000:
        category = "Lower Middle"

    elif income < 500000:
        category = "Middle"

    elif income < 1000000:
        category = "Upper Middle"

    else:
        category = "High"

    data["INCOME_CATEGORY"] = encode_value(
        "INCOME_CATEGORY",
        category
    )

    # Family Size

    members = data["CNT_FAM_MEMBERS"]

    if members <= 2:
        family = "Small"

    elif members <= 4:
        family = "Medium"

    else:
        family = "Large"

    data["FAMILY_SIZE"] = encode_value(
        "FAMILY_SIZE",
        family
    )

    # Phone

    if "FLAG_PHONE" in feature_columns:
        data["FLAG_PHONE"] = int(form["FLAG_PHONE"])

    # Work Phone

    if "FLAG_WORK_PHONE" in feature_columns:
        data["FLAG_WORK_PHONE"] = int(form["FLAG_WORK_PHONE"])

    # Email

    if "FLAG_EMAIL" in feature_columns:
        data["FLAG_EMAIL"] = int(form["FLAG_EMAIL"])

    # Arrange Columns

    final = pd.DataFrame([data])

    final = final.reindex(
        columns=feature_columns,
        fill_value=0
    )

    return final