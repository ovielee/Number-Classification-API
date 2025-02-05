from app.models.number_model import is_prime, is_perfect, is_armstrong

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(4) == False

def test_is_perfect():
    assert is_perfect(6) == True
    assert is_perfect(10) == False

def test_is_armstrong():
    assert is_armstrong(371) == True
    assert is_armstrong(123) == False