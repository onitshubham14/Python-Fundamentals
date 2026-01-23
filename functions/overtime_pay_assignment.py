"""
Module 6 Assignment: Overtime Pay Calculation.
Course: Python for Everybody.
"""

# Write a program to calculate gross pay using a function called computepay().
# - Normal pay applies up to 40 hours
# - Overtime (above 40 hours) is paid at 1.5 times the rate
# - Use input() to read hours and rate
# - Convert inputs using float()
# - The function must return the computed pay
# - Test case: 45 hours, rate 10.50 → Pay should be 498.75

def computepay(hours, rate):
    # Calculate overtime pay if hours exceed 40
    if hours > 40:
        return hours * rate + ((hours - 40) * 0.50 * rate)
    else:
        # Normal pay for 40 hours or less
        return hours * rate


# User input
hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

# Function call
p = computepay(hours, rate)

# Output result
print("Pay", p)
