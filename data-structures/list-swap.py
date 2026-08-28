# Swapping values in Python

# We can swap two values without using a temporary variable.

a = 10
b = 20

a, b = b, a

print(a)  # 20
print(b)  # 10


# Swapping list elements

racers = ["Mario", "Bowser", "Luigi"]

racers[0], racers[-1] = racers[-1], racers[0]

print(racers)
# ['Luigi', 'Bowser', 'Mario']