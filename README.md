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
  <img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/458b744d-f455-4f4f-8119-9903f8041bc8" />
  <img width="1872" height="904" alt="image" src="https://github.com/user-attachments/assets/a9aa596d-c37e-4ae3-86bb-04af43535112" />
  <img width="1785" height="510" alt="image" src="https://github.com/user-attachments/assets/aa0cd9a6-e0cb-473b-ad6e-51a4fe8cf4dd" />
  <img width="1852" height="853" alt="image" src="https://github.com/user-attachments/assets/b7864397-ae09-428f-8047-a4c72aed179a" />
  <img width="1855" height="667" alt="image" src="https://github.com/user-attachments/assets/697c02b2-2025-4bd7-8606-2e49ac69019e" />
  <img width="1803" height="818" alt="image" src="https://github.com/user-attachments/assets/c1fc827c-0736-42e4-8e13-13990f433b93" />
  <img width="1587" height="586" alt="image" src="https://github.com/user-attachments/assets/096de411-565f-419c-9876-6eae11679a8b" />









# 🙌 Author
Rajnarayan Yadav









