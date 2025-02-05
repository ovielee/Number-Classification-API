def validate_input(number):
    try:
        # Try to convert the input to a float (supports integers and decimals)
        float(number)
        return True
    except (ValueError, TypeError):
        # If conversion fails, the input is invalid
        return False