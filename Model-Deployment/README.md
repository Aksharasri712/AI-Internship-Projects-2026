# Task 3: Model Deployment – API & Containerization

## Objective
To deploy a trained machine learning model as an API using Flask and prepare it for containerization using Docker.

## Model Used
Customer Churn Prediction Model

## Deliverables
- API code for model inference
- Dockerfile
- Sample request and response
- README with setup instructions

## Running the API Locally

```bash
pip install -r requirements.txt
python app.py
```

## Sample Request

```bash
curl -X POST http://127.0.0.1:5000/predict \
-H "Content-Type: application/json" \
-d '{"feature":"value"}'
```

## Sample Response

```json
{
    "prediction": "No Churn",
    "message": "This is a sample prediction response."
}
```
