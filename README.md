# 🧠 Employee Performance Prediction Using Machine Learning

A Machine Learning-based system to predict employee performance using historical data such as experience, education, and feedback. Built with Flask, Python, and Scikit-learn.

---

## 🚀 Features

- Predicts employee performance ratings (1–5)
- Easy-to-use web interface built with Flask
- Uses a trained Machine Learning model
- Supports training, prediction, and model updates
- Encodes categorical data using LabelEncoder

---

## 🛠️ Tech Stack

- Python
- Scikit-learn
- Pandas
- Flask
- HTML/CSS (Jinja2 templates)

---

## 📊 Dataset Columns Used

| Feature             | Description                           |
|---------------------|---------------------------------------|
| `experience`        | Total years of experience             |
| `education`         | Education level (e.g., Graduate)      |
| `last_rating`       | Previous performance rating           |
| `feedback_score`    | Feedback score from peers/supervisor  |
| `training_score`    | Recent training performance score     |

---

## 🧠 ML Model

- **Algorithm**: RandomForestClassifier
- **Preprocessing**: Label Encoding for categorical features
- **Saved Files**:
  - `models/performance_model.pkl`: Trained model
  - `models/label_encoders.pkl`: Encoders for categorical columns

---

## 📂 Folder Structure
employee-performance-prediction/
│
├── app.py # Flask backend
├── templates/
│ └── index.html # UI form for prediction
├── models/
│ ├── performance_model.pkl # Trained ML model
│ └── label_encoders.pkl # Encoders for features
├── data/
│ └── employee_data.csv # Dataset (if public)
├── static/ # CSS or images (optional)
└── README.md



---

## ▶️ Run the App Locally

### 1. Clone the repository

# 2. Install dependencies
  pip install -r requirements.txt
  pip install flask pandas scikit-learn


# 3. Run the Flask App
 python app.py

# 📷 Screenshots
Input Form	Prediction Result

# 🙌 Author
Rajnarayan Yadav









