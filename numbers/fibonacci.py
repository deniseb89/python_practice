"""Find the fibonacci sequence to the given digit"""
# Enter a number and have the program generate the Fibonacci
# sequence to that number or to the Nth number.

def fibo_n(num):
    """uses given number as stopping point"""
    result = []
    num1, num2 = 0, 1
    while num1 < num:
        result.append(num1)
        num1, num2 = num2, num1+num2
    return result
    