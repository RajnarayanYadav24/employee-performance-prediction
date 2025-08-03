from flask import Flask, render_template, request
import joblib
import numpy as np

# Load the model and encoders
model = joblib.load('../models/performance_model.pkl')
label_encoders = joblib.load('../models/label_encoders.pkl')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form inputs
        age = int(request.form['age'])
        dept = request.form['department']
        education = int(request.form['education'])
        gender = request.form['gender']
        years = int(request.form['years'])
        training = int(request.form['training'])

        # Encode categorical inputs
        dept_encoded = label_encoders['Department'].transform([dept])[0]
        gender_encoded = label_encoders['Gender'].transform([gender])[0]

        # Create input array
        features = np.array([[age, dept_encoded, education, gender_encoded, years, training]])

        # Predict
        prediction = model.predict(features)[0]

        return render_template('index.html', prediction_text=f'Predicted Performance Rating: {prediction}')
    
    except Exception as e:
        return render_template('index.html', prediction_text=f'Error: {str(e)}')

if __name__ == '__main__':
    app.run(debug=True)
