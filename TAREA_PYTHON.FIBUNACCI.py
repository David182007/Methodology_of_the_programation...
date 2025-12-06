# ------------------------------------------------------------
# PORTADA
# ------------------------------------------------------------
# Name: Axel David Ortiz Reyna
# Student ID: 2530152
# Group: IM 1-3
#
# ------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------
# The Fibonacci series is a sequence of numbers where each term
# is the sum of the previous two, starting with 0 and 1.
# Calculating the series up to n means generating the first n
# terms using this pattern. This program reads n, validates the
# input, and prints the Fibonacci sequence up to n terms.
#
# ------------------------------------------------------------
# PROBLEM: Fibonacci series generator
# ------------------------------------------------------------
# Description:
# Program that reads an integer n and prints the first n terms of
# the Fibonacci series starting at 0 and 1.
#
# Inputs:
# - n (int; number of terms to generate)
#
# Outputs:
# - "Fibonacci series:" followed by the n terms separated by spaces
#
# Validations:
# - n must be an integer
# - n must be >= 1
# - Optional limit: n <= 50
#
# Test cases:
# 1) Normal: n = 5 → expected: 0 1 1 2 3
# 2) Border: n = 1 → expected: 0
# 3) Error: n = -4 → expected: "Error: invalid input"
#
# ------------------------------------------------------------
# OPTIONAL DIAGRAMS / TABLES
# ------------------------------------------------------------
# Flowchart (text description):
# 1. Read n
# 2. Validate if n is integer
# 3. Check n >= 1 and n <= 50
# 4. If valid, generate Fibonacci sequence
# 5. Print results
#
# Test case table (description):
# - Columns: Input n | Expected Output | Result type
#

# ------------------------------------------------------------
# ------------------------ CODE -------------------------------
# ------------------------------------------------------------

# Read input
n = input("Number of terms: ")

# Validation: must be integer
try:
    n = int(n)
except:
    print("Error: invalid input")
    exit()

# Validation: n >= 1
if n < 1:
    print("Error: invalid input")
    exit()

# Optional limit: n <= 50
if n > 50:
    print("Error: invalid input")
    exit()

# Generate Fibonacci series
print("Fibonacci series:", end=" ")

if n == 1:
    print(0)

elif n == 2:
    print("0 1")

else:
    a = 0
    b = 1
    print(a, b, end=" ")

    for _ in range(3, n + 1):
        c = a + b
        print(c, end=" ")
        a = b
        b = c

print()  # final newline

# ------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------
# Using a loop made it easier to generate the Fibonacci sequence
# because each new term depends on previous values. Handling the
# special cases n = 1 and n = 2 is important to avoid errors and
# ensure the program behaves correctly. The logic of iterative
# accumulation can be reused for other numerical sequences or
# algorithms that depend on previous computed values.
#
# ------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------
# 1) Python documentation – "for" and "while" loops
# 2) Official Python tutorial – Fibonacci examples
# 3) Class notes from programming fundamentals
# ------------------------------------------------------------


