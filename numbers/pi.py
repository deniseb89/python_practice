""" Module docstring"""
# Find PI to the Nth Digit - Enter a number and have the program generate
# PI up to that many decimal places. Keep a limit to how far the program will go.
import math

def pied_python(num):
    """Use input to return number of digits past decimal sign."""
    if num < 100:
        print(round(math.pi, num))
    else:
        print("That number is too large. Try a smaller number")
