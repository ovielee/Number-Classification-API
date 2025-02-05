import requests
from app.models.number_model import is_prime, is_perfect, is_armstrong

def classify_number(n):
    properties = []
    
    # Check if the number is an integer
    if isinstance(n, int):
        if is_prime(n):
            properties.append("prime")
        if is_perfect(n):
            properties.append("perfect")
        if is_armstrong(n):
            properties.append("armstrong")
        if n % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
    else:
        # For floating-point numbers, only check even/odd
        if n % 2 == 0:
            properties.append("even")
        else:
            properties.append("odd")
    
    return properties

def get_fun_fact(n):
    # Round floating-point numbers to the nearest integer
    if not isinstance(n, int):
        n = round(n)
    
    # Fetch fun fact from the Numbers API
    url = f"http://numbersapi.com/{n}/math"
    response = requests.get(url)
    
    # Return the fun fact if the request is successful
    return response.text if response.status_code == 200 else "No fun fact available."