# ❤️ Heart Disease Prediction Web App

## 📘 Overview
This project is a **Machine Learning–powered Flask web application** that predicts the likelihood of **heart disease (heart failure)** based on medical parameters entered by the user.  
It uses a trained ML model (`heart_model.pkl`) and a simple interactive web interface for predictions.

---

## 🎯 Objective
To build a **real-time prediction system** that helps identify potential heart problems early using data science and machine learning.

---

## ⚙️ Technologies Used

### 🧠 Machine Learning
- **Algorithm Used:** Logistic Regression / Random Forest (based on training)
- **Libraries:** `scikit-learn`, `numpy`, `pandas`
- **Model File:** `heart_model.pkl` (saved model)

### 🌐 Web Framework
- **Flask:** Backend web framework
- **HTML, CSS:** Frontend design
- **Jinja2:** Template rendering
- **Bootstrap:** For styling and layout (if used)

---Heart-Disease-Prediction/
│
├── static/
│ ├── background.jpg # Background image for the webpage
│ ├── failure.mp3 # Alert sound for failed prediction
│ └── style.css # CSS styling
│
├── templates/
│ ├── index.html # Home page with input form
│ └── result.html # Result page showing prediction output
│
├── app.py # Flask backend application
├── heart_model.pkl # Trained machine learning model
├── requirements.txt # Dependencies list
└── README.md # Project documentation

---

## 🧠 Model Description

The model (`heart_model.pkl`) was trained on the **UCI Heart Disease Dataset**, which contains patient health data such as:
- Age  
- Gender  
- Chest pain type  
- Blood pressure  
- Cholesterol level  
- Blood sugar  
- ECG results  
- Maximum heart rate  
- Exercise-induced angina  
- ST depression  
- Slope, Thal, etc.

The model uses these medical inputs to predict whether a person is likely to have **heart failure (1)** or **healthy heart (0)**.

---

## 🧮 How It Works
1. User enters medical details into the web form on `index.html`.
2. The input data is converted into a NumPy array.
3. The saved ML model (`heart_model.pkl`) processes the data.
4. The result (Healthy / Heart Failure) is displayed on the result page.
5. Optionally, an alert sound or message appears if a problem is detected.

---

## 🚀 Steps to Run Locally

### 1️⃣ Install Dependencies
Create a virtual environment and install all dependencies:
```bash
pip install -r requirements.txt


## 🧱 Project Structure
