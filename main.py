from fastapi import FastAPI, HTTPException
import joblib
import pandas as pd
from pydantic import BaseModel

# Load the model
best_rf = joblib.load("insurance_model.pkl")

# Initialize FastAPI app
app = FastAPI()

# Define the expected input data format using Pydantic
class PredictionInput(BaseModel):
    age: int
    sex: int
    bmi: float
    children: int
    smoker: int
    region_northwest: int
    region_southeast: int
    region_southwest: int

@app.get("/")
def read_root():
    return {"message": "Welcome to the Insurance Prediction API"}

@app.post("/predict/")
def predict(input_data: PredictionInput):
    try:
        # Convert input data to a DataFrame
        input_df = pd.DataFrame([input_data.dict()])

        # Debugging: Print the received data
        print("Received Data:", input_df)

        # Make prediction
        prediction = best_rf.predict(input_df)
        return {"predicted_insurance_charge": prediction[0]}
    except Exception as e:
        print("Error occurred:", e)
        raise HTTPException(status_code=500, detail=f"Prediction error: {str(e)}")