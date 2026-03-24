from fastapi import FastAPI
import pandas as pd
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from app.schemas import CustomerData
from app.model_loader import load_model

app = FastAPI()

# Load model once at startup
model = load_model()

from fastapi import HTTPException

@app.post("/predict")
def predict(customer: CustomerData):

    try:
        input_df = pd.DataFrame([customer.dict()])

        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        return {
            "churn_prediction": int(prediction),
            "churn_probability": float(probability)
        }

    except Exception as e:
        logger.error(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=400, detail="Invalid input data")