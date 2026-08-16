"""
Assignment: Gross Pay Calculator
Calculate gross pay using user input()
Inputs: hours worked, rate per hour
Output: total pay after calculation

"""

hrs = input("Enter Hours:")
hr_rate = input("enter rate per hour:")

hrs = float(hrs)
hr_rate = float(hr_rate)

grosspay = hrs*hr_rate 
print("Pay:", grosspay)

# Example test case:
# Hours: 35
# Rate: 2.75
# Expected Output: Gross Pay = 96.25