# While Loop

# A while loop repeats a block of code
# as long as its condition remains True.

n = 5

while n > 0:
    print(n)
    n = n - 1
print("Blastoff!")

# The iteration variable is n.
# It changes after every iteration.
# When n becomes 0, n > 0 becomes False,
# so the loop stops.

# ------------------------------------------

# Infinite Loop

#n = 5
#while n > 0:
     #print(n)

# n never changes, so n > 0 always remains True.
# The loop would continue forever.

# ------------------------------------------

# Zero-trip Loop

# If the while condition is False from the beginning,
# the loop body will never execute.

n = 0

while n > 0:
    print(n)
    n = n - 1

print("Loop was skipped.")

# ------------------------------------------

# break

# break immediately stops the loop
# and moves to the first line after the loop.

while True:
    line = input("Enter something: ")

    if line == "done":
        break

    print(line)

print("Loop finished.")

# ------------------------------------------
# continue

# continue skips the rest of the current iteration
# and goes back to the top of the loop.

while True:
    line = input("Enter something: ")

    if line == "done":
        break

    if line.startswith("#"):
        continue

    print(line)

print("Loop finished.")

# ------------------------------------------
# LOOP PATTERN: SEARCHING WITH A BOOLEAN FLAG

# A Boolean variable can be used to remember
# whether a particular value has been found.

found = False

for num in [9, 41, 12, 3, 74, 15]:

    # Check if the current number is 3.
    if num == 3:
        found = True

    # Show the current status of found.
    print(found, num)

print("Found:", found)

"""
Concepts learned:
- while loops
- Iteration
- Iteration variables
- Loop conditions
- Infinite loops
- Zero-trip loops
- break
- continue

Important idea:
A while loop keeps executing as long as its condition is True.
The iteration variable should normally change so that the
condition eventually becomes False and the loop terminates.
"""