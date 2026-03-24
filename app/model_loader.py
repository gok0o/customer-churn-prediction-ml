import joblib

def load_model():
    model = joblib.load("models/churn_model.pkl")
    return model