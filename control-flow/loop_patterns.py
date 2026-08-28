# LOOP PATTERNS

# These examples demonstrate common patterns used with loops:
# - Finding the largest number
# - Searching with a Boolean flag
# - Finding the smallest number
# - Understanding None



# ============================================================
# 1. FINDING THE LARGEST NUMBER

# Start with -1 as the initial largest number.
largest_num = -1

for num in [9, 4, 41, 67, 45, 79]:

    # If the current number is greater than
    # the largest number found so far, update it.
    if num > largest_num:
        largest_num = num

print("Largest number:", largest_num)


# ============================================================
# 2. SEARCHING WITH A BOOLEAN FLAG

# Boolean variables can be used as a flag to remember
# whether a particular value has been found.
found = False

for num in [9, 41, 12, 3, 74, 15]:

    # Check whether the current number is 3.
    if num == 3:
        found = True

print("Number 3 found:", found)


# ============================================================
# 3. NONE TYPE

# None represents the absence of a value.
# It means that a variable does not have a value yet.

value = None

print("Value:", value)
print("Type:", type(value))

# None is different from 0, False, or an empty string.

# 0     -> actual number
# False -> Boolean value
# ""    -> empty string
# None  -> no value


# ============================================================
# 4. FINDING THE SMALLEST NUMBER USING NONE


# We don't know the smallest number yet,
# so we start with None.

smallest_num = None
for num in [9, 4, 56, 1, 5, 99]:

    # On the first iteration, smallest_num is None.
    # So we use the first number as the starting value.
    if smallest_num is None:
        smallest_num = num

    # For the remaining numbers, check if the current
    # number is smaller than the smallest found so far.
    elif num < smallest_num:
        smallest_num = num

print("Smallest number:", smallest_num)


# IMPORTANT IDEA

# None is useful when we don't have a value yet.
# Example:
# smallest_num = None

# First number  -> becomes the starting smallest value
# Next numbers  -> are compared with it
# Smaller value -> updates smallest_num

# The standard way to check for None is:

# if smallest_num is None:
# rather than:
# if smallest_num == None: