"""
This folder is demonstrate Input, Processing, and Output (IPO)
Convert European elevator floor to US floor
"""
inp = input("European floor? ") # Input : get the european floor number from the user.

usf = int(inp) + 1 # Process :  convert input to integer and add 1

print("US floor:", usf) # Output : display the US floor number

# Fact: Europe starts floors at 0, US starts at 1.