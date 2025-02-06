from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Helper function to check if a number is prime
def is_prime(num):
    """
    Determines if a given number is a prime number.
    
    A prime number is greater than 1 and divisible only by 1 and itself.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Helper function to check if a number is perfect
def is_perfect(num):
    """
    Determines if a given number is a perfect number.
    
    A perfect number is equal to the sum of its proper divisors (excluding itself).
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is perfect, False otherwise.
    """
    divisors = [i for i in range(1, num) if num % i == 0]
    return sum(divisors) == num

# Helper function to check if a number is Armstrong
def is_armstrong(num):
    """
    Determines if a given number is an Armstrong number.
    
    An Armstrong number is equal to the sum of its digits raised to the power of the number of digits.
    
    Args:
        num (int): The number to check.
    
    Returns:
        bool: True if the number is an Armstrong number, False otherwise.
    """
    digits = [int(d) for d in str(abs(num))]  # Use absolute value for negative numbers
    power = len(digits)
    return sum(d**power for d in digits) == abs(num)

# Helper function to calculate digit sum
def digit_sum(num):
    """
    Calculates the sum of the digits of a given number.
    
    Args:
        num (int): The number whose digits will be summed.
    
    Returns:
        int: The sum of the digits of the number.
    """
    return sum(int(d) for d in str(abs(num)))  # Use absolute value for negative numbers

# Helper function to get fun fact
def get_fun_fact(num):
    """
    Fetches a fun mathematical fact about a given number from the Numbers API.
    
    Args:
        num (int): The number to fetch the fact for.
    
    Returns:
        str: The fun fact as a string, or an error message if the request fails.
    """
    try:
        response = requests.get(f"http://numbersapi.com/{abs(num)}/math?json")  # Use absolute value
        if response.status_code == 200:
            data = response.json()
            return data.get("text", "No fun fact found.")
        return "Failed to fetch fun fact."
    except Exception as e:
        return f"Error fetching fun fact: {str(e)}"

@app.route('/api/classify-number', methods=['GET'])
def classify_number():
    """
    API endpoint to classify a number based on its mathematical properties.
    
    Accepts a 'number' parameter via GET request and returns a JSON response containing:
    - Whether the number is prime.
    - Whether the number is perfect.
    - Mathematical properties such as Armstrong, odd, or even.
    - The sum of its digits.
    - A fun fact about the number.
    
    Returns:
        JSON: A JSON object containing the classification results.
    """
    # Get the 'number' parameter from the query string
    number_str = request.args.get('number')
    
    # Validate input
    if not number_str or not number_str.lstrip('-').isdigit():  # Allow negative numbers
        return jsonify({
            "number": number_str,
            "error": True
        }), 400
    
    # Convert to integer
    number = int(number_str)
    
    # Perform calculations
    is_prime_result = is_prime(number) if number > 0 else False  # Primes are only for positive numbers
    is_perfect_result = is_perfect(number) if number > 0 else False  # Perfect numbers are only for positive numbers
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