# This file Explains if,if-else & elif statement

# Topic: Conditional execution (if / elif / else)
# Course: Python for Everybody (Coursera)
# Purpose: Demonstrate how Python makes decisions
#----------------------------------------------------------------------------------------
# 1: Simple if statement
x = 5

if x < 10:
    print("smaller") #If the condition is True, the indented block will execute

if x > 20:
    print("bigger")

print("finis") #This line always runs (sequential execution)

#----------------------------------------------------------------------------------
# 2: if-else statement

y = 15
# Python checks the condition
if y > 10:
    print("y is greater than 10")
else:
    print("y is 10 or less") # Runs only when the if condition is False

#-----------------------------------------------------------------------------------
# 3: if-elif-else statement 

x = 10
# Only ONE block will run

if x < 10:
    print("x is less than 10")
elif x == 10:
    print("x is exactly 10")
else:
    print("x is greater than 10")
print('All done')

#-----------------------------------------------------------------------------------------------------
# 5: Conditional with user input

try:
    num = int(input("Enter a number: ")) # input() returns a string, so we convert it to int.

    if num > 0:
        print("Positive number")
    elif num == 0:
        print("Zero")
    else:
        print("Negative number")

except:
    print("Invalid input")    # Handles invalid input (non-numeric)


# things to remember :
# if checks a condition
# elif checks another condition if previous was False
# else runs when all conditions are False
# Indentation defines which code belongs to the condition
