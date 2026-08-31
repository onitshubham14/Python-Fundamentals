# Creating a list using a for loop

squares = []

for n in range(10):
    squares.append(n**2)

print(squares)

# List comprehension

squares = [n**2 for n in range(10)]

print(squares)

# The learning point is:

[n**2 for n in range(10)]

# A shorter way of doing is:

squares = []

for n in range(10):
    squares.append(n**2)