"""
This file contains function-related concepts learned from Kaggle Python course.
Topics include:
- Built-in functions
- User-defined functions
- Default arguments
- Absolute value (abs)

"""

# --------------------------------------------------
# 1. Built-in function: round()

# round() is a built-in Python function, It rounds a decimal number using standard math rules

def round_to_nearest(num):
    return round(num)

print(round_to_nearest(9.9999))
# Output : 10

# --------------------------------------------------
# 2. Built-in function: abs()

# abs() returns the absolute value of a number
# It removes the negative sign and returns a positive value

def absolute_difference(a, b):
    # Find distance between two numbers
    return abs(a - b)

print(absolute_difference(5, 12))
# Output : 7 

# --------------------------------------------------
# 3. Default arguments in functions

# This function calculates how many candies are left
# after splitting them evenly among friends

def candies_to_smash(total_candies, friends=3):
    """
    total_candies: total number of candies
    friends: number of friends sharing the candies (default is 3)
    returns: number of leftover candies
    """

    # % gives the remainder after division
    return float(total_candies % friends)

print(candies_to_smash(91))
# Output : 1 
