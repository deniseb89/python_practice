"""Next Prime Number"""
# Have the program find prime numbers until the user chooses to stop
# asking for the next one.
def is_prime(num1):
    """test whether number is prime"""
    num2 = 2
    while num2 < num1:
        if num1 % num2 == 0:
            return False
        num2 += 1
    return True

def next_prime():
    """find prime numbers one by one"""
    for num in range(100):
        if is_prime(num):
            yield num
