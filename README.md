# Number Classification API

## Description
This API takes a number as input and returns interesting mathematical properties about it.

## Usage
Send a GET request to: 
http://your-aws-url.amazonaws.com/api/classify-number?number= <number>


### Example
http://number-classification-api-dev.us-west-2.elasticbeanstalk.com/api/classify-number?number=371

### Response
```json
{
    "number": 371,
    "is_prime": false,
    "is_perfect": false,
    "properties": ["armstrong", "odd"],
    "digit_sum": 11,
    "fun_fact": "371 is an Armstrong number because 3^3 + 7^3 + 1^3 = 371"
}

Error Handling
If the input is invalid, the API returns:

{
    "number": "alphabet",
    "error": true
}

Deployment
The API is deployed on AWS Elastic Beanstalk.
