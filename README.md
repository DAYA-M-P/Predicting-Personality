## 🧠 Personality Prediction Web App

This project is a machine learning web application built using Flask that predicts a user's personality type (Introvert or Extrovert) based on numerical input features. The backend is powered by a trained Random Forest Classifier, and the model was developed in a Jupyter Notebook (Personality.ipynb).

# 🚀 Demo
The app takes input features from a web form and returns the predicted personality type.

Prediction Output Example:

Predicted Personality: Introvert

# 📁 Project Structure

├── app.py               # Flask application

├── rf_model.pkl         # Trained Random Forest model

├── Personality.ipynb    # Notebook used for data exploration, training & evaluation

├── templates/
│   └── index.html       # Web page for user input 

└── README.md            # Project overview

# 🧠 Model Overview

Algorithm Used: Random Forest Classifier
Target Variable: Personality Type (Introvert = 0, Extrovert = 1)
Model Input: Numerical values corresponding to user traits or survey responses


# 1 Install Dependencies

Make sure you have Python 3 installed. Then, install required packages:
pip install flask numpy scikit-learn

# 2 Run the Flask App

python app.py
The app will be available at http://127.0.0.1:5000/.

# ☁️ Deployment on AWS EC2 (Live Hosting)

The application is successfully deployed and shared with the public using AWS EC2:

# ✅ Deployment Steps:

Created an EC2 Instance.
Connected via SSH to the instance.
Installed Python and pip:

# 📄 How It Works

User enters numerical values in a web form.
app.py collects the form values and sends them to the trained Random Forest model (rf_model.pkl).
The model returns a prediction (0 or 1).
The result is mapped to a label (Introvert or Extrovert) and displayed on the webpage.

# 📊 Jupyter Notebook (Personality.ipynb)

This notebook contains:
Data preprocessing
Feature importance analysis
Model training (Random Forest)
SHAP analysis for explainability

# 🧪 Sample Input Format

The input form expects numeric values corresponding to specific personality-related features, such as:
Alone_to_Social_Ratio
Social_Comfort_Index
Other survey-based scores
Ensure that your input matches the order and type expected by the model.

# 💡 Future Enhancements

Add more personality classes (e.g., Ambivert)
Add charts/visualizations for personality breakdown
Use a front-end framework like React or Streamlit for UI improvement





