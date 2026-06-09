from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Customer Churn Prediction API is running!"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()

    response = {
        "prediction": "No Churn",
        "message": "This is a sample prediction response."
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
