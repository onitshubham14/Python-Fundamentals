# This file explains Python basic data types and reserved words
# Learned from: Python for Everybody (Coursera)

# some data types : 

# Integer (whole numbers)
age = 20
print("Age:", age)

# Float (decimal numbers)
height = 5.8
print("Height:", height)

# there is something more to know about float, if the two num divided by int data type the return value willbe automatically in float data type.
# a = 10
# b = 2
# print(a / b)       5.0
# print(type(a / b))  <class 'float'>


# string (text data)
name = "Shubham"
print("Name:", name)

# boolean (True or False)
is_student = True
print("is student:", is_student)

# Type checking :

print(type(age))       # <class 'int'>
print(type(height))    # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_student))# <class 'bool'>


# Reserved Words (Keywords)

# Reserved words are words that Python already understands.
# We cannot use them as variable names.

# Examples of reserved words:
# if, else, elif, for, while, break, continue
# True, False, None
# import, from, as, def, return, class

#example

# if = 5
# -------------------------
# Valid vs Invalid variable names :
# -------------------------

# Valid variable names
student_name = "Krish"
total_marks = 90

# Invalid variable names (examples)
# 1name = "Jaddu"      # Cannot start with a number
# class = "Python"  # 'class' is a reserved word

print("Student:", student_name)
print("Marks:", total_marks)
