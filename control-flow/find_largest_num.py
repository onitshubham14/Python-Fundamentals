# ============================================================
# LOOP PATTERN: FINDING THE LARGEST NUMBER
# ============================================================

# Start with a value that is smaller than the numbers
# we expect to check.
largest_num = -1

for num in [9, 4, 41, 67, 45, 79]:

    # Compare the current number with the largest
    # number found so far.
    if num > largest_num:
        largest_num = num

print("Largest number:", largest_num)