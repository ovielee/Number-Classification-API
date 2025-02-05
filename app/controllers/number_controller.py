from flask import Blueprint, request, jsonify
from app.services.number_service import classify_number, get_fun_fact
from app.utils.helpers import validate_input

number_bp = Blueprint('number', __name__)

@number_bp.route('/api/classify-number', methods=['GET'])
def classify_number_api():
    number = request.args.get('number')
    if not validate_input(number):
        return jsonify({"number": number, "error": True}), 400

    number = int(number)
    properties = classify_number(number)
    class_sum = sum(int(d) for d in str(number))
    fun_fact = get_fun_fact(number)

    return jsonify({
        "number": number,
        "is_prime": "prime" in properties,
        "is_perfect": "perfect" in properties,
        "properties": properties,
        "class_sum": class_sum,
        "fun_fact": fun_fact
    })