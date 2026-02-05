# 🩺 Diabetes Prediction System using Machine Learning

Diabetes is one of the most common chronic diseases worldwide, and early detection plays a crucial role in effective management and prevention of complications.
This Diabetes Prediction System uses Machine Learning to predict whether a person is likely to have diabetes based on important medical parameters.

## 🚀 Project Overview

This project predicts the risk of diabetes by analyzing the following health-related features:
-Number of pregnancies
-Glucose level
-Blood pressure
-Skin thickness
-Insulin level
-Body Mass Index (BMI)
-Diabetes Pedigree Function
-Age
The system helps in early health risk assessment by providing fast and data-driven predictions through an interactive web interface.

## 🧠 Technologies Used

### Programming Language: Python

### Libraries & Tools:
-NumPy
-Pandas
-Scikit-learn
-Streamlit

### Machine Learning Algorithm:
-Support Vector Machine (SVM)

### Tools Used:
-PyCharm (IDE)
-Jupyter Notebook

## 📊 Dataset Information
The dataset used is the PIMA Indians Diabetes Dataset, which contains medical records with the following features:

## Feature	Description
-Pregnancies	Number of pregnancies
-Glucose	Plasma glucose concentration
-BloodPressure	Diastolic blood pressure
-SkinThickness	Triceps skin fold thickness
-Insulin	2-Hour serum insulin
-BMI	Body Mass Index
-DiabetesPedigreeFunction	Diabetes pedigree function
-Age	Age of the patient
-Outcome	1 = Diabetic, 0 = Non-Diabetic

### ⚙️ How It Works
-User enters medical details through the web interface
-Input data is standardized using StandardScaler
-Trained SVM model processes the input data
-System predicts whether the person is Diabetic or Not Diabetic
