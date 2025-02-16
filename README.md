# Insurance Prediction API

This project provides a **containerized REST API** for predicting insurance charges based on user inputs using a trained Machine Learning model. The API is built with **FastAPI**, containerized with **Docker**, and deployed on **Kubernetes** for scalability.


## ✨ Features
- **ML-powered RESTful API** → Predicts insurance charges using a Random Forest Regressor with **FastAPI**.
- **Dockerized** → Easily deployable with Docker & Kubernetes.
- **Interactive API Docs** → Swagger UI (/docs) and ReDoc (/redoc).
- **Scalable Deployment** → Runs on Kubernetes (Minikube/AWS EKS).

## 🤖 Machine Learning Model: Random Forest Regressor
The API is powered by a **Random Forest Regressor**, a robust algorithm for predicting insurance charges.

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

- **Model Performance**
  - **Root Mean Squared Error (RMSE):** `4383.58`
    - Lower RMSE indicates better predictive accuracy.
  - **R² Score:** `0.876`
    - The R² score of `0.876` means that 87.6% of the variance in insurance charges is explained by the model.

These results demonstrate that the Random Forest model provides accurate and reliable predictions for insurance charges.

## 📌 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/berkayyildirim/containerized-ml-model.git
cd containerized-ml-model
```

### 2. Run with Docker 🐳
Option 1: Pull Pre-built Image from Docker Hub
```bash
docker pull byberkayyildirim/insurance-prediction-api:latest
docker run -p 8000:8000 byberkayyildirim/insurance-prediction-api:latest
```

Option 2: Build & Run Locally
```bash
docker build -t insurance-prediction-api .
docker run -p 8000:8000 insurance-prediction-api
```

### 3. Access the API 🌐
- Swagger UI → http://localhost:8000/docs
- ReDoc → http://localhost:8000/redoc

### 4. Make a Prediction (POST Request)
Example Request:
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

Response:
```json
{
    "predicted_insurance_charge": 21421.72
}
```

## ☸️ Deploying on Kubernetes
### 1. Start Minikube
```bash
minikube start
```

### 2. Deploy to Kubernetes
```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
```

### 3. Verify Deployment
```bash
kubectl get pods
kubectl get svc
```

### 4. Access the API in Kubernetes
```bash
kubectl port-forward svc/insurance-api-service 8000:80
```

Now, access the API at:
```bash
http://127.0.0.1:8000/predict/
```

## File Structure
```plaintext
containerized-ml-model/
├── datasets/                     # (Optional) Dataset files
├── __pycache__/                  # Python cache (ignored)
├── .ipynb_checkpoints/           # Jupyter Notebook checkpoints (ignored)
├── .gitignore                    # Git ignore file
├── Dockerfile                    # Docker instructions for containerizing the app
├── deployment.yaml               # Kubernetes Deployment
├── service.yaml                  # Kubernetes Service
├── insurance_model.pkl           # Trained ML model
├── insurance.ipynb               # Jupyter Notebook for model training
├── main.py                       # FastAPI application
├── requirements.txt              # Python dependencies
└── README.md                     # Documentation
```

## 🐳 Docker Hub
The Docker image is publicly available on Docker Hub:\
byberkayyildirim/insurance-prediction-api

## 📩 Contact

For any questions or collaboration requests:
- GitHub: byberkayyildirim
- Docker Hub: byberkayyildirim