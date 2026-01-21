"""
This file demonstrates basic usage of try and except in Python.
We attempt to convert strings to integers. If the conversion fails,
we catch the error and assign a default value (-1).

"""
# Example 1:
astr = 'hello bob'  # a string that cannot be converted to an integer

try:
    # Attempt to convert astr to an integer
    istr = int(astr)
except:
    # If conversion fails, handle the error and assign -1
    istr = -1

print('first:', istr)  # Output: first: -1


# Example 2:
astr = '123'  # a string that can be converted to an integer

try:
    # Attempt to convert astr to an integer
    istr = int(astr)
except ValueError:
    # If conversion fails, handle the error and assign -1
    istr = -1

print('second:', istr)  # Output: second: 123


# Example 3: with user input with try/except.
rawstr = input('Enter a number: ') # Ask the user to enter a number

try:
    # Try to convert the user input to an integer
    ival = int(rawstr)
except ValueError:
    # If conversion fails, assign -1
    ival = -1

# Check the result and print appropriate message
if ival > 0:
    print('Nice work!')  # valid positive number
else:
    print('Not a number or not positive')  # invalid or negative input