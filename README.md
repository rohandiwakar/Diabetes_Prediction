# 🩺 Diabetes Prediction System using Machine Learning

A web-based Machine Learning application built with **Streamlit** that predicts the risk of diabetes based on medical parameters such as glucose level, BMI, age, insulin, and more.

The system uses a trained **Support Vector Machine (SVM)** model with standardized input data to provide instant and reliable predictions.

---

## 🚀 Features

- 🔍 Predicts diabetes risk (High / Low)
- 📊 Uses real medical parameters for prediction
- 🤖 Machine Learning model (SVM)
- 📐 Data Standardization using Scaler
- 🌐 Interactive Web Interface using Streamlit
- ⚡ Instant prediction with user-friendly UI

---

## 🛠️ Tech Stack

- **Python**
- **Streamlit** – Web Interface
- **NumPy** – Numerical Computation
- **Scikit-learn** – Machine Learning
- **Pickle** – Model Serialization
- **Pandas** – Dataset Handling

---

## 📊 Input Parameters

The prediction is based on the following medical attributes:

- Pregnancies
- Glucose Level
- Blood Pressure
- Skin Thickness
- Insulin Level
- Body Mass Index (BMI)
- Diabetes Pedigree Function
- Age

---

## 🧠 Machine Learning Workflow
- 1.Load diabetes dataset (diabetes.csv)
- 2.Preprocess and standardize data
- 3.Train model using Support Vector Machine (SVM)
- 4.Save trained model and scaler using Pickle
- 5.Load model in Streamlit app
- 6.Take user input and predict diabetes risk

## 📈 Prediction Output
- *✅ Low Risk of Diabetes
- *⚠️ High Risk of Diabetes
- Along with health tips for better awareness.


## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/diabetes-prediction-system.git
cd diabetes-prediction-system
```

### 2️⃣ Install Required Libraries
```bash
pip install streamlit numpy scikit-learn pandas
```

### ▶️ Run the Application
```bash
streamlit run app.py
```

