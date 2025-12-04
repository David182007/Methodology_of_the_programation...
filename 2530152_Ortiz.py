# 2530152_OrtizReynaAxelDavid.py
# Student: Axel David Ortiz Reyna
# Tuition: 2530152
# Group: IM 1-3

# ------------------------------------------------------------------
# EXECUTIVE SUMMARY (English)
# This document contains six programming problems focused on string
# manipulation and loop constructs in Python. It explains the use of
# for and while loops: for when the number of iterations is known and
# while when repetition depends on a condition. Counters and accumulators
# are used to count items and accumulate sums respectively. Careful
# termination conditions prevent infinite loops. Each problem includes
# description, inputs, outputs, validations and three test cases.
# ------------------------------------------------------------------

# PRINCIPLES AND GOOD PRACTICES (comments)
# - Use for when you know how many iterations are needed (e.g., range).
# - Use while when iterations depend on a condition (e.g., sentinel input).
# - Initialize counters and accumulators before loops.
# - Update loop control variables inside while loops to avoid infinite loops.
# - Keep loop bodies simple; extract complex logic into functions.

# ------------------------------------------------------------------
# TEMPLATE FOR PROBLEMS (add before each problem in comments)
# Problem X: <short title>
# Description: ...
# Inputs: ...
# Outputs: ...
# Validations: ...
# Test cases:
#  1) Normal: ...
#  2) Border: ...
#  3) Error: ...
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# Problem 1: Sum of range with for
# Description: Calculate sum of integers from 1 to n (inclusive) and
# also the sum of even numbers in that range using a for loop.
# Inputs: n (int)
# Outputs: "Sum 1..n:" <total_sum>
#          "Even sum 1..n:" <even_sum>
# Validations: n must be int and n >= 1
# Test cases:
#  1) Normal: n=10 -> Sum 1..10:55, Even sum 1..10:30
#  2) Border: n=1 -> Sum 1..1:1, Even sum 1..1:0
#  3) Error: n=0 -> Error: invalid input
# ------------------------------------------------------------------

def problem_1_sum_range():
    raw = input("Enter n (int >= 1): ").strip()
    try:
        n = int(raw)
    except Exception:
        print("Error: invalid input")
        return
    if n < 1:
        print("Error: invalid input")
        return
    total_sum = 0
    even_sum = 0
    for i in range(1, n + 1):
        total_sum += i
        if i % 2 == 0:
            even_sum += i
    print("Sum 1..n:", total_sum)
    print("Even sum 1..n:", even_sum)

# ------------------------------------------------------------------
# Problem 2: Multiplication table with for
# Description: Generate multiplication table for base from 1 to m
# Inputs: base (int), m (int >=1)
# Outputs: lines like "5 x 1 = 5"
# Validations: convertible to int, m >= 1
# Test cases:
#  1) Normal: base=5, m=4 -> 5x1..5x4
#  2) Border: base=3, m=1 -> only 3 x 1 = 3
#  3) Error: m=0 -> Error: invalid input
# ------------------------------------------------------------------

def problem_2_multiplication_table():
    base_raw = input("Enter base (int): ").strip()
    m_raw = input("Enter m (int >= 1): ").strip()
    try:
        base = int(base_raw)
        m = int(m_raw)
    except Exception:
        print("Error: invalid input")
        return
    if m < 1:
        print("Error: invalid input")
        return
    for i in range(1, m + 1):
        product = base * i
        print(f"{base} x {i} = {product}")

# ------------------------------------------------------------------
# Problem 3: Average of numbers with while and sentinel
# Description: Read float numbers until sentinel -1 is entered. Compute
# count and average of valid inputs (excluding sentinel).
# Inputs: repeated floats; sentinel = -1
# Outputs: "Count:" <count> and "Average:" <average> or "Error: no data"
# Validations: each input convertible to float. Ignore sentinel for stats.
# Test cases:
#  1) Normal: 2,4,6,-1 -> Count:3 Average:4.0
#  2) Border: -1 -> Error: no data
#  3) Error: non-number input -> prompts message and continues
# ------------------------------------------------------------------

def problem_3_average_sentinel():
    SENTINEL = -1
    total = 0.0
    count = 0
    print("Enter numbers one by one. Enter -1 to finish.")
    while True:
        raw = input("Number: ").strip()
        try:
            value = float(raw)
        except Exception:
            print("Error: invalid number, try again")
            continue
        if value == SENTINEL:
            break
        total += value
        count += 1
    if count == 0:
        print("Error: no data")
    else:
        average = total / count
        print("Count:", count)
        print("Average:", average)

# ------------------------------------------------------------------
# Problem 4: Password attempts with while
# Description: Simple password check with MAX_ATTEMPTS attempts.
# Inputs: user_password each attempt
# Outputs: "Login success" or "Account locked"
# Validations: MAX_ATTEMPTS > 0
# Test cases:
#  1) Normal: correct on 2nd attempt -> Login success
#  2) Border: correct on 1st attempt -> Login success
#  3) Error: wrong all attempts -> Account locked
# ------------------------------------------------------------------

def problem_4_password_attempts():
    CORRECT_PASSWORD = "admin123"
    MAX_ATTEMPTS = 3
    if MAX_ATTEMPTS <= 0:
        print("Error: invalid configuration")
        return
    attempts = 0
    while attempts < MAX_ATTEMPTS:
        user_input = input("Enter password: ")
        attempts += 1
        if user_input == CORRECT_PASSWORD:
            print("Login success")
            return
        else:
            remaining = MAX_ATTEMPTS - attempts
            if remaining > 0:
                print(f"Wrong password. Attempts left: {remaining}")
    print("Account locked")

# ------------------------------------------------------------------
# Problem 5: Simple menu with while
# Description: Text menu repeats until the user selects 0 (Exit).
# Inputs: option (int: 0,1,2,3)
# Outputs: messages per option; invalid option message
# Validations: option convertible to int and in [0,1,2,3]
# Test cases:
#  1) Normal: 1->Hello!,2->Counter,3->Increment,0->Bye!
#  2) Border: 0 -> Bye! immediate
#  3) Error: invalid input -> Error: invalid option
# ------------------------------------------------------------------

def problem_5_simple_menu():
    counter = 0
    while True:
        print("\nMenu:")
        print("1) Show greeting")
        print("2) Show current counter value")
        print("3) Increment counter")
        print("0) Exit")
        choice_raw = input("Option: ").strip()
        try:
            option = int(choice_raw)
        except Exception:
            print("Error: invalid option")
            continue
        if option == 1:
            print("Hello!")
        elif option == 2:
            print("Counter:", counter)
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
            break
        else:
            print("Error: invalid option")

# ------------------------------------------------------------------
# Problem 6: Pattern printing with nested loops
# Description: Print a right triangle of '*' with n rows. Optionally
# print inverted pattern as well.
# Inputs: n (int >=1)
# Outputs: lines of '*' pattern
# Validations: n convertible to int and n >= 1
# Test cases:
#  1) Normal: n=4 -> *,**,***,****
#  2) Border: n=1 -> *
#  3) Error: n=0 -> Error: invalid input
# ------------------------------------------------------------------

def problem_6_pattern_printing():
    raw = input("Enter n (int >= 1): ").strip()
    try:
        n = int(raw)
    except Exception:
        print("Error: invalid input")
        return
    if n < 1:
        print("Error: invalid input")
        return
    # Regular triangle
    for i in range(1, n + 1):
        print("*" * i)
    # Inverted pattern (optional)
    print("\nInverted pattern:")
    for i in range(n, 0, -1):
        print("*" * i)

# ------------------------------------------------------------------
# Additional utilities: Full Name Formatter and other string problems
# (based on user's earlier work). These are optional extra problems
# that demonstrate string methods: strip, title, split, join, replace.
# ------------------------------------------------------------------

def extra_full_name_formatter():
    raw = input("Enter full name: ").strip()
    if not raw:
        print("Error: invalid input")
        return
    words = raw.split()
    if len(words) < 2:
        print("Error: invalid input")
        return
    formatted = " ".join(w.capitalize() for w in words)
    initials = ".".join(w[0].upper() for w in words) + "."
    print("Formatted name:", formatted)
    print("Initials:", initials)

# ------------------------------------------------------------------
# Main driver menu to run problems (this is optional but helps test)
# ------------------------------------------------------------------

def main():
    while True:
        print("\n=== Main Problems Menu ===")
        print("1) Problem 1 - Sum range (for)")
        print("2) Problem 2 - Multiplication table (for)")
        print("3) Problem 3 - Average with sentinel (while)")
        print("4) Problem 4 - Password attempts (while)")
        print("5) Problem 5 - Simple menu (while)")
        print("6) Problem 6 - Pattern printing (nested loops)")
        print("7) Extra - Full name formatter (strings)")
        print("0) Exit program")
        choice = input("Select option: ").strip()
        if choice == "1":
            problem_1_sum_range()
        elif choice == "2":
            problem_2_multiplication_table()
        elif choice == "3":
            problem_3_average_sentinel()
        elif choice == "4":
            problem_4_password_attempts()
        elif choice == "5":
            problem_5_simple_menu()
        elif choice == "6":
            problem_6_pattern_printing()
        elif choice == "7":
            extra_full_name_formatter()
        elif choice == "0":
            print("Program terminated. Goodbye!")
            break
        else:
            print("Error: invalid option")

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------
# CONCLUSIONS (comments)
# - For loops are ideal when the number of iterations is known; while
#   loops are best when repetition depends on runtime conditions.
# - Counters and accumulators help track iterations and sums inside loops.
# - While loops risk infinite loops if control variables are not updated.
# - Menus and password attempts are classic uses of while loops with
#   explicit termination conditions.
# - Nested loops allow pattern generation; their complexity grows
#   multiplicatively with nesting depth.

# REFERENCES (comments)
# 1) Python documentation - for statements and while statements
#    https://docs.python.org/3/tutorial/controlflow.html
# 2) W3Schools - Python For Loops
#    https://www.w3schools.com/python/python_for_loops.asp
# 3) Real Python - While Loops in Python
#    https://realpython.com/python-while-loop/
# 4) GeeksforGeeks - Python Patterns and Looping
#    https://www.geeksforgeeks.org/python-program-to-print-patterns/
# 5) Automate the Boring Stuff - Practical programming with loops
#    https://automatetheboringstuff.com/
# ------------------------------------------------------------------
