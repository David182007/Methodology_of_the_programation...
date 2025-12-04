# Student Name: Axel David Ortiz Reyna
# Matriculation Number: 2530152
# Group: IM 1-3

# Assignment: Lists, Tuples, and Dictionaries – 6 Problems
# --------------------------------------------------

# --------------------------------------------------
# EXECUTIVE SUMMARY
# --------------------------------------------------
# This document demonstrates the use of Python core data structures:
# lists, tuples, and dictionaries. Lists are mutable sequences that
# allow insertion, deletion, and reordering. Tuples are immutable and
# are ideal for storing fixed, constant data such as coordinates.
# Dictionaries store key-value pairs, enabling fast lookup by key.
# The document covers six problems illustrating practical uses of these
# structures, input validation, error handling, test cases, and proper
# English-based naming conventions.

# --------------------------------------------------
# BEST PRACTICES
# --------------------------------------------------
# - Use lists when data must change frequently.
# - Use tuples when data must remain constant.
# - Use dictionaries to associate names/keys with values (fast lookup).
# - Avoid modifying a list while iterating through it.
# - Use descriptive key names in dictionaries.
# - Keep code readable with clear variable names and output messages.

# ==================================================
# PROBLEM 1: SHOPPING LIST BASICS (LIST OPERATIONS)
# ==================================================
# Description:
# Manage a shopping list by creating an initial list of items, adding a
# new item, showing the total number of items, and checking if a search
# item exists.
#
# Inputs:
# - initial_items_text (str)
# - new_item (str)
# - search_item (str)
#
# Outputs:
# - Items list
# - Total items count
# - Boolean indicating if search item was found
#
# Validations:
# - Input strings must not be empty.
# - initial_items_text split by commas.
#
# Test Cases:
# 1) Normal: "apple, banana, orange", "grapes", "banana"
# 2) Border: "apple", "pear", "pear"
# 3) Error: "   ", "mango", "mango"

initial_items_text = input("Enter initial items separated by commas: ").strip()
new_item = input("Enter item to add: ").strip()
search_item = input("Enter item to search: ").strip()

if initial_items_text == "" or new_item == "" or search_item == "":
    print("Error: invalid input")
else:
    items_list = [item.strip() for item in initial_items_text.split(',') if item.strip()]
    items_list.append(new_item)
    print("Items list:", items_list)
    print("Total items:", len(items_list))
    print("Found item:", search_item in items_list)

# ==================================================
# PROBLEM 2: POINTS AND DISTANCES WITH TUPLES
# ==================================================
# Description:
# Create two points using tuples, compute Euclidean distance and midpoint.
#
# Inputs:
# - x1, y1, x2, y2 (float)
#
# Outputs:
# - Point A
# - Point B
# - Distance
# - Midpoint
#
# Validations:
# - Inputs must be valid floats.
#
# Test Cases:
# 1) Normal: (0,0),(3,4)
# 2) Border: (1.5,2.5),(1.5,2.5)
# 3) Error: invalid float

try:
    x1 = float(input("x1: "))
    y1 = float(input("y1: "))
    x2 = float(input("x2: "))
    y2 = float(input("y2: "))

    point_a = (x1, y1)
    point_b = (x2, y2)

    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)

    print("Point A:", point_a)
    print("Point B:", point_b)
    print("Distance:", distance)
    print("Midpoint:", midpoint)
except:
    print("Error: invalid input")

# ==================================================
# PROBLEM 3: PRODUCT CATALOG WITH DICTIONARY
# ==================================================
# Description:
# Use a dictionary to store product prices and compute purchase total.
#
# Inputs:
# - product_name (str)
# - quantity (int)
#
# Outputs:
# - Unit price, quantity, total OR error
#
# Validations:
# - product must exist
# - quantity must be > 0
#
# Test Cases:
# 1) Normal: apple,2
# 2) Border: banana,1
# 3) Error: unknown product

product_prices = {
    "apple": 10.0,
    "banana": 8.0,
    "orange": 12.5
}

product_name = input("Enter product name: ").strip()
quantity_text = input("Enter quantity: ").strip()

if product_name == "":
    print("Error: invalid input")
else:
    if product_name not in product_prices:
        print("Error: product not found")
    else:
        try:
            quantity = int(quantity_text)
            if quantity <= 0:
                print("Error: invalid quantity")
            else:
                unit_price = product_prices[product_name]
                total_price = unit_price * quantity
                print("Unit price:", unit_price)
                print("Quantity:", quantity)
                print("Total:", total_price)
        except:
            print("Error: invalid input")

# ==================================================
# PROBLEM 4: STUDENT GRADES WITH DICT + LIST
# ==================================================
# Description:
# Use a dictionary mapping student names to a list of grades.
#
# Inputs:
# - student_name
#
# Outputs:
# - Grades list, average, pass/fail
#
# Validations:
# - student must exist
# - grade list must not be empty
#
# Test Cases:
# 1) Normal: Alice
# 2) Border: Bob (single grade)
# 3) Error: unknown student

grades = {
    "Alice": [90, 85, 88],
    "Bob": [70],
    "Carol": [95, 91, 89]
}

student_name = input("Enter student name: ").strip()

if student_name not in grades:
    print("Error: student not found")
else:
    student_grades = grades[student_name]
    if len(student_grades) == 0:
        print("Error: empty grade list")
    else:
        average = sum(student_grades) / len(student_grades)
        is_passed = average >= 70
        print("Grades:", student_grades)
        print("Average:", average)
        print("Passed:", is_passed)

# ==================================================
# PROBLEM 5: WORD FREQUENCY COUNTER
# ==================================================
# Description:
# Count frequency of words in a sentence.
#
# Inputs:
# - sentence (str)
#
# Outputs:
# - words list, frequency dict, most common word
#
# Validations:
# - sentence must not be empty
#
# Test Cases:
# 1) Normal: "hello world hello"
# 2) Border: "test"
# 3) Error: empty input

sentence = input("Enter a sentence: ").strip().lower()

if sentence == "":
    print("Error: invalid input")
else:
    words_list = sentence.split()
    freq_dict = {}

    for word in words_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    most_common = None
    max_count = 0

    for word, count in freq_dict.items():
        if count > max_count:
            max_count = count
            most_common = word

    print("Words list:", words_list)
    print("Frequencies:", freq_dict)
    print("Most common word:", most_common)

# ==================================================
# PROBLEM 6: SIMPLE CONTACT BOOK (DICT CRUD)
# ==================================================
# Description:
# A simple contact book that supports ADD, SEARCH, and DELETE.
#
# Inputs:
# - action_text
# - name
# - phone (only for ADD)
#
# Outputs:
# - Confirmation messages
#
# Validations:
# - action must be ADD/SEARCH/DELETE
# - name must not be empty
# - phone required for ADD
#
# Test Cases:
# 1) Normal ADD: John, 12345
# 2) Normal SEARCH: Alice
# 3) Error: delete unknown contact

contacts = {
    "Alice": "1111111111",
    "Bob": "2222222222"
}

action_text = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()

if action_text not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid action")
else:
    name = input("Enter name: ").strip()
    if name == "":
        print("Error: invalid name")
    else:
        if action_text == "ADD":
            phone = input("Enter phone: ").strip()
            if phone == "":
                print("Error: invalid phone")
            else:
                contacts[name] = phone
                print("Contact saved:", name, phone)

        elif action_text == "SEARCH":
            if name in contacts:
                print("Phone:", contacts[name])
            else:
                print("Error: contact not found")

        elif action_text == "DELETE":
            if name in contacts:
                contacts.pop(name)
                print("Contact deleted:", name)
            else:
                print("Error: contact not found")

# --------------------------------------------------
# CONCLUSIONS
# --------------------------------------------------
# Lists provide flexible structures for dynamic data.
# Tuples ensure that fixed data remains unchanged, enhancing safety.
# Dictionaries allow fast lookups using descriptive keys.
# Combining these structures enables powerful data modeling patterns,
# such as dictionaries of lists or key-value mappings.
# These exercises demonstrate real-world uses for each structure and
# highlight the importance of input validation.

# --------------------------------------------------
# REFERENCES
# --------------------------------------------------
# 1) Python Official Documentation – Built-in Types
# 2) W3Schools Python Lists, Tuples, Dictionaries
# 3) Real Python – Data Structures in Python
# 4) Programiz – Python Collections
# 5) Course Notes – Programming Methodology
