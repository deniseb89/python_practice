"""Prime Factorization"""
# Have the user enter a number and find all Prime Factors (if there are any)
# and display them.

def is_prime(num1):
    """test whether number is prime"""
    num2 = 2
    while num2 < num1:
        if num1 % num2 == 0:
            return False
        num2 += 1
    return True

def prime_factors(num):
    """find the prime numbers that divide num exactly"""
    result = []
    for i in range(2, num):
        if (is_prime(i)) and (num % i == 0):
            result.append(i)
    if not result:
        print("No prime factors")
    else:
        return result
