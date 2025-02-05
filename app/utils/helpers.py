def validate_input(number):
    if not number or not number.lstrip('-').isdigit():
        return False
    return True