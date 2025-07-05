from flask import Flask, request, render_template
import numpy as np
import pickle

# Initialize Flask app
app = Flask(__name__)

# Load the trained model
with open('rf_model.pkl', 'rb') as file:
    model = pickle.load(file)

# (Optional) If you used a vectorizer or pipeline, load it here
# with open('tfidf.pkl', 'rb') as file:
#     vectorizer = pickle.load(file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        print("Form received!")  # ✅ Debug: confirm form submission

        # Collect form data and convert to float list
        input_features = [float(x) for x in request.form.values()]
        input_array = np.array([input_features])  # Reshape to 2D for model

        # Make prediction
        prediction = model.predict(input_array)[0]

        # Optional: Map class to label
        label_map = {0: 'Introvert', 1: 'Extrovert'}
        result = label_map.get(prediction, str(prediction))

        return render_template('index.html', prediction_text=f'Predicted Personality: {result}')

    except Exception as e:
        print("Error during prediction:", e)  # ✅ Print error in terminal
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
