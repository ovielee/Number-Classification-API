def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n):
    if n < 2:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

def is_armstrong(n):
    # Convert the number to a string and ignore the negative sign
    digits = [int(d) for d in str(abs(n))]
    length = len(digits)
    return sum(d**length for d in digits) == abs(n)