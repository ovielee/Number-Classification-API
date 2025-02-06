from flask import Blueprint, request, jsonify
from app.services.number_service import classify_number, get_fun_fact
from app.utils.helpers import validate_input

# Define the Blueprint
number_bp = Blueprint('number', __name__)

# Define the route
@number_bp.route('/api/classify-number', methods=['GET'])
def classify_number_api():
    number = request.args.get('number')
    if not validate_input(number):
        return jsonify({"number": number, "error": True}), 400

    # Convert the input to a float
    number = float(number)
    
    # If the number is an integer, convert it to int
    if number.is_integer():
        number = int(number)

    properties = classify_number(number)
    
    # Calculate digit_sum (sum of digits, ignoring non-digit characters like '-' and '.')
    digit_sum = sum(int(d) for d in str(abs(number)) if d.isdigit())
    
    fun_fact = get_fun_fact(number)

    return jsonify({
        "number": number,
        "is_prime": "prime" in properties if isinstance(number, int) else False,
        "is_perfect": "perfect" in properties if isinstance(number, int) else False,
        "properties": properties,
        "digit_sum": digit_sum,  # Correct field name as per the task
        "fun_fact": fun_fact
    })