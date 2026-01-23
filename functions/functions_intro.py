"""
# Module 6: Functions (Introduction)
# Course: Python for Everybody
"""
# What I learned:
# 1.Built-in functions like max() work on sequences such as strings
# 2.A function must be CALLED to be useful
# 3.User-defined functions can take arguments, process data, and return results

# -----------------------------------
# Example 1: Built-in function with string

big = max("hello!")
print(big)  # Output: 'w'

# Among all characters in "hello!",
# 'w' has the highest ASCII value, so it is returned

# -----------------------------------
# Example 2: User-defined function

def addtwo(a, b):
    
    #Takes two numbers and returns their sum
    added = a + b
    return added

# Function calls
x = addtwo(3, 5)
print(x)  # Output: 8

# Important concept:
# Defining a function alone does nothing.
# The function must be CALLED to execute.
