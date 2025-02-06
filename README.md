# Number Classification API

## Description
This API takes a number as input and returns interesting mathematical properties about it, along with a fun fact. It supports both positive and negative integers.

## Features
- Checks if the number is prime.
- Checks if the number is perfect.
- Determines if the number is an Armstrong number.
- Classifies the number as odd or even.
- Calculates the sum of its digits.
- Provides a fun mathematical fact about the number.

## Usage
Send a GET request to the following endpoint:
http://number-classification-api-dev.us-west-2.elasticbeanstalk.com/api/classify-number?number=<number>

### Example Requests
#### Valid Positive Input
http://number-classification-api-dev.us-west-2.elasticbeanstalk.com/api/classify-number?number=371

## Response:
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

## Valid Negative Input
```
http://number-classification-api-dev.us-west-2.elasticbeanstalk.com/api/classify-number?number=-5
```
## Response:
{
    "number": -5,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["odd"],
    "digit_sum": 5,
    "fun_fact": "5 is a Fibonacci number."
}

## Invalid Input
```
http://number-classification-api-dev.us-west-2.elasticbeanstalk.com/api/classify-number?number=alphabet
```
## Response:
{
    "number": "alphabet",
    "error": true
}

# Deployment
The API is deployed on AWS Elastic Beanstalk.

# Requirements
Python 3.x
Flask
Flask-CORS
Requests
Install dependencies using:
```
pip install flask flask-cors requests
```
# Running Locally
1. Clone the repository:
```
https://github.com/tolushub/API.git
```
2. Navigate to the project directory:
```
cd API
```
3. Install dependencies:
```
pip install -r requirements.txt
```
Run the application:
```
python app.py
```

Open your browser and go to http://127.0.0.1:5000/api/classify-number?number=371




