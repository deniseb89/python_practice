"""Find e to the Nth Digit"""
# Just like the previous problem, but with e instead of PI. Enter a
# number and have the program generate e up to that many decimal places. Keep a limit to how far
# the program will go.
import math

def find_e(num):
    """Use input to return number of digits past E."""
    if num < 100:
        print(round(math.e, num))
    else:
        print("That number is too large. Try a smaller number")

