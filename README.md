🚀 Customer Churn Prediction API (Production ML System)

📌 Overview

This project implements an end-to-end machine learning system to predict customer churn using a trained SVM model.
The system is deployed as a FastAPI service and fully containerized using Docker for production readiness.

---

🧠 Features

- End-to-end ML pipeline (preprocessing + model)
- Real-time prediction API using FastAPI
- Dockerized deployment (portable across environments)
- Structured production-ready project design
- Handles class imbalance using SMOTE
- Model optimized for recall (churn detection priority)

---

⚙️ Tech Stack

- Python
- Scikit-learn
- FastAPI
- Docker
- Pandas / NumPy

---

🧱 Project Structure

customer-churn-prediction-ml/
│
├── app/                # FastAPI application
├── models/             # Saved ML model
├── train/              # Training scripts
├── notebooks/          # Experimentation (Jupyter)
├── Dockerfile          # Container setup
├── requirements.txt
└── README.md

---

🚀 Run with Docker

docker build -t churn-api .
docker run -p 8000:8000 churn-api

Then open:

👉 http://127.0.0.1:8000/docs

---

🔌 API Endpoint

POST "/predict"

Example Input:

{
  "age": 35,
  "income_bracket": "Medium",
  "membership_years": 2,
  "marital_status": "Single",
  "occupation": "Engineer",
  "product_category": "Electronics",
  "avg_purchase_value": 200,
  "purchase_frequency": "Monthly",
  "avg_discount_used": 10,
  "online_purchases": 5,
  "in_store_purchases": 3,
  "total_transactions": 20,
  "total_items_purchased": 50,
  "promotion_effectiveness": "High"
}

Example Output:

{
  "churn_prediction": 0,
  "churn_probability": 0.23
}

---

📊 Model Details

- Algorithm: Support Vector Machine (SVM)
- Preprocessing: Scaling + Encoding Pipeline
- Class imbalance handled using SMOTE
- Optimized for recall to minimize false negatives

---

📈 Results

- Achieved ~90% recall on churn class
- Identified key churn drivers:
  - Purchase frequency
  - Discount usage
  - Customer spending patterns

---

🧠 Key Insight

Customer churn is primarily driven by behavioral changes rather than demographic attributes.
Early decline in engagement is a strong churn indicator.

---

🔥 Why This Project Stands Out

Unlike basic ML projects, this system:

- Serves predictions via API
- Is fully containerized using Docker
- Follows production-level architecture
