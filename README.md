# Insurance Prediction API

This project provides a **containerized REST API** for predicting insurance charges based on user inputs using a trained machine learning model. The API is implemented using **FastAPI**, and the container is built and managed with **Docker**.

---

## Features

- RESTful API with **FastAPI**.
- Predicts insurance charges using a pre-trained **Random Forest Regressor** model.
- Easy deployment with **Docker**.
- Interactive API documentation available via **Swagger UI** and **ReDoc**.
- Hosted Docker image available on **Docker Hub**.

---

## Machine Learning Model: Random Forest Regressor

The API is powered by a **Random Forest Regressor**, a versatile and robust machine learning algorithm that excels at predicting continuous values. Below are the details of the model and its performance.

### **Model Details**

- **Algorithm Used:** Random Forest Regressor
- **Hyperparameters Tuned:**
  - `n_estimators`: 300
  - `min_samples_split`: 10
  - `min_samples_leaf`: 4
  - `max_features`: None
  - `max_depth`: None
- **Training Dataset:** The model was trained on the `insurance.csv` dataset, which includes the following features:
  - `age`: Age of the policyholder.
  - `sex`: Gender of the policyholder (1 = Female, 0 = Male).
  - `bmi`: Body Mass Index.
  - `children`: Number of children/dependents.
  - `smoker`: Whether the policyholder is a smoker (1 = Yes, 0 = No).
  - `region`: Categorical region indicators (northwest, southeast, southwest).

### **Model Performance**

The model was evaluated using the following metrics on a validation dataset:

- **Root Mean Squared Error (RMSE):** `4383.58`
  - Lower RMSE indicates better predictive accuracy.
- **R² Score:** `0.876`
  - The R² score of `0.876` means that 87.6% of the variance in insurance charges is explained by the model.

These results demonstrate that the Random Forest model provides accurate and reliable predictions for insurance charges.

### **Prediction Example**

The model takes input in the following format:
```json
{
    "age": 30,
    "sex": 1,
    "bmi": 28.5,
    "children": 2,
    "smoker": 1,
    "region_northwest": 0,
    "region_southeast": 1,
    "region_southwest": 0
}
```

The output prediction is:
```json
{
    "predicted_insurance_charge": 21421.72
}
```

---

## Requirements

To run this project, you need:
- **Docker** installed on your system.

---

## Getting Started

### **1. Pull the Docker Image**
Pull the pre-built image from Docker Hub:
```bash
docker pull byberkayyildirim/insurance-prediction-api:latest
```
### **2. Run the Docker Container**
Start the API server:
```bash
docker run -p 8000:8000 byberkayyildirim/insurance-prediction-api:latest
```
### **3. Access the API**
- Swagger UI: http://localhost:8000/docs \
Interactive documentation for testing endpoints.
- ReDoc: http://localhost:8000/redoc \
Alternate API documentation.
- Base URL: http://localhost:8000

---

## Usage

### POST /predict/
Send a JSON payload to the /predict/ endpoint to get insurance charge predictions.

#### Example Request
```json
{
    "age": 30,
    "sex": 1,
    "bmi": 28.5,
    "children": 2,
    "smoker": 1,
    "region_northwest": 0,
    "region_southeast": 1,
    "region_southwest": 0
}
```
#### Example Response
```json
{
    "predicted_insurance_charge": 21421.72211734341
}
```

---
## Development Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/containerized-ml-model.git
cd containerized-ml-model
```

### 2. Build and Run the Docker Container
```bash
docker build -t insurance-prediction-api .
docker run -p 8000:8000 insurance-prediction-api
```

### 3. Install Dependencies Locally (Optional)
If running without Docker, install dependencies with:
```bash
pip install -r requirements.txt
```

### 4. Run the API Locally (Optional)
```bash
uvicorn main:app --reload
```

---

## File Structure
containerized-ml-model/
├── datasets/                     # (Optional) Dataset files
├── __pycache__/                  # Python cache (ignored)
├── .ipynb_checkpoints/           # Jupyter Notebook checkpoints (ignored)
├── .gitignore                    # Git ignore file
├── Dockerfile                    # Docker instructions for containerizing the app
├── insurance_model.pkl           # Trained machine learning model
├── insurance.ipynb               # Jupyter Notebook for model training
├── main.py                       # FastAPI application
├── requirements.txt              # Python dependencies
└── README.md                     # Documentation

---

## Docker Hub
The Docker image is publicly available on Docker Hub:\
byberkayyildirim/insurance-prediction-api

---

## Contact

For any questions or collaboration requests, feel free to reach out:
- GitHub: byberkayyildirim
- Docker Hub: byberkayyildirim