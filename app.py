from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Helper function to check if a number is prime
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Helper function to check if a number is perfect
def is_perfect(num):
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

# Helper function to check if a number is Armstrong
def is_armstrong(num):
    digits = [int(d) for d in str(num)]
    power = len(digits)
    return sum(d**power for d in digits) == num

# Helper function to calculate digit sum
def digit_sum(num):
    return sum(int(d) for d in str(num))

# Helper function to get fun fact
def get_fun_fact(num):
    try:
        response = requests.get(f"http://numbersapi.com/{num}/math?json")
        if response.status_code == 200:
            data = response.json()
            return data.get("text", "No fun fact found.")
        return "Failed to fetch fun fact."
    except Exception as e:
        return f"Error fetching fun fact: {str(e)}"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    # Get the 'number' parameter from the query string
    number_str = request.args.get('number')

    # Validate input
    if not number_str or not number_str.isdigit():
        return jsonify({
            "number": number_str,
            "error": True
        }), 400

    # Convert to integer
    number = int(number_str)

    # Perform calculations
    is_prime_result = is_prime(number)
    is_perfect_result = is_perfect(number)
    properties = []

    if is_armstrong(number):
        properties.append("armstrong")
    if number % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    digit_sum_result = digit_sum(number)
    fun_fact = get_fun_fact(number)

    # Prepare response
    response = {
        "number": number,
        "is_prime": is_prime_result,
        "is_perfect": is_perfect_result,
        "properties": properties,
        "digit_sum": digit_sum_result,
        "fun_fact": fun_fact
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)