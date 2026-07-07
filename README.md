# 💳 Credit Card Approval Prediction System

## 📌 Project Overview

The Credit Card Approval Prediction System is a Machine Learning web application that predicts whether a credit card application is likely to be approved or rejected based on the applicant's financial and demographic information.

The project automates the preliminary screening process by reducing manual effort and providing fast, data-driven predictions through a user-friendly web interface.

---

## 🚀 Features

- Credit Card Approval Prediction
- Machine Learning Classification
- Flask Web Application
- Interactive User Interface
- Confidence Score
- Applicant Summary
- Data Preprocessing and Feature Engineering
- Cloud Deployment Ready

---

## 🧠 Machine Learning Algorithms

The following classification algorithms were implemented and evaluated:

- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier ✅ (Best Model)
- XGBoost Classifier

---

## 📊 Model Performance

| Model | Accuracy |
|--------|----------|
| Logistic Regression | - |
| Decision Tree | - |
| Random Forest | **88.97%** |
| XGBoost | - |

The Random Forest Classifier achieved the best performance with an accuracy of **88.97%** and was selected as the final model for integration with the Flask web application.

---

## 📂 Dataset

The project uses the following datasets:

- Application Record Dataset
- Credit Record Dataset

**Dataset Source:** Kaggle Credit Card Approval Prediction Dataset

---

## 🔄 Project Workflow

The complete project workflow consists of:

1. Dataset Collection
2. Data Understanding
3. Exploratory Data Analysis
4. Data Preprocessing
5. Feature Engineering
6. Handling Class Imbalance using SMOTE
7. Machine Learning Model Training
8. Model Evaluation and Comparison
9. Best Model Selection
10. Flask Web Application Integration
11. Real-Time Prediction
12. Result Display

---

## 🛠 Technologies Used

### Backend

- Python
- Flask

### Machine Learning

- Scikit-learn
- XGBoost
- Pandas
- NumPy

### Frontend

- HTML5
- CSS3
- Bootstrap 5

### Development Tools

- Jupyter Notebook
- Visual Studio Code
- Git
- GitHub

---

## 📁 Project Structure
```text
Credit_Card_Approval_Prediction_System/
│
├── Dataset/
│
├── Documentation/
│
├── IBM_Deployment/
│
├── models/
│   ├── best_model.pkl
│   ├── feature_columns.pkl
│   └── label_encoders.pkl
│
├── notebook/
│   └── Credit_Card_Approval_Prediction.ipynb
│
├── static/
│   ├── css/
│   └── images/
│
├── templates/
│   ├── about.html
│   ├── index.html
│   ├── layout.html
│   ├── predict.html
│   └── result.html
│
├── .gitignore
├── app.py
├── LICENSE
├── manifest.yml
├── Procfile
├── README.md
├── requirements.txt
├── runtime.txt
└── utils.py
```
---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Durga1607/credit-card-approval-prediction.git
```

### 2. Navigate to the Project Directory

```bash
cd credit-card-approval-prediction
```

### 3. Install Required Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Flask Application

```bash
python app.py
```

### 5. Open the Application

Open the following address in your web browser:

```text
http://127.0.0.1:5000
```

---

## 📈 Workflow

User Input

↓

Data Preprocessing

↓

Feature Engineering

↓

Random Forest Model

↓

Prediction

↓

Confidence Score

↓

Result

---

## 📊 Prediction Output

The application predicts whether a credit card application is:

- ✅ Approved
- ❌ Rejected

The result page also displays:

- Prediction Confidence Score
- Applicant Summary

---

## 🌐 Web Application

The Flask web application contains the following pages:

### Home Page

Provides an introduction to the Credit Card Approval Prediction System and its main features.

### Prediction Page

Allows users to enter applicant demographic, employment, family, and financial information.

### Results Page

Displays the machine learning prediction, confidence score, and applicant summary.

### About Page

Provides information about the project, technologies used, and machine learning workflow.

---

## 🔮 Future Enhancements

- Cloud Deployment
- Database Integration
- User Authentication
- Batch Applicant Prediction
- Advanced Model Optimization
- Explainable AI using SHAP or LIME
- Improved Security and Access Control
- Larger and More Diverse Training Datasets

---

## 📄 License

This project is licensed under the MIT License.

---

## 🔗 GitHub Repository

https://github.com/Durga1607/credit-card-approval-prediction

---

## 👨‍💻 Developed By

**Puduvitil Durga Pavan Kumar**

B.Tech - Computer Science and Engineering

Sri Venkateswara College of Engineering & Technology
