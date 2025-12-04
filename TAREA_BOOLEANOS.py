
# Student Name: Axel David Ortiz Reyna
# Matriculation Number: 2530152
# Group: IM 1-3
# Assignment: Numeric Types and Boolean Exercises – 6 Problems

"""
This file contains six problems that exercise numeric types (int, float)
and boolean logic in Python. Each problem includes: Description,
Inputs, Outputs, Validations and three test cases (normal, border,
and error). All messages and variable names follow English naming
conventions and lower_snake_case for variables.
"""

# ------------------------------------------------------------------
# EXECUTIVE SUMMARY
# ------------------------------------------------------------------
# This document explains numeric types in Python: int for whole numbers
# and float for decimal numbers. Booleans (True/False) arise from
# comparisons and logical operators. Validating numeric ranges is
# critical to avoid runtime errors (e.g., division by zero) and to
# ensure meaningful results. The six problems cover conversions,
# arithmetic with conditionals, boolean flags for eligibility, and
# basic statistics using ints and floats.
# ------------------------------------------------------------------

# PRINCIPLES AND GOOD PRACTICES
# - Use int for counters and quantities that are whole numbers.
# - Use float for measurements, rates, and averages.
# - Validate inputs before conversion to int/float.
# - Avoid division by zero by checking denominators.
# - Use descriptive variable names and clear output messages.

# TEMPLATE FOR PROBLEMS
# Problem X: <short title>
# Description: ...
# Inputs: ...
# Outputs: ...
# Validations: ...
# Test cases: 1) Normal 2) Border 3) Error

# ------------------------------------------------------------------
# Problem 1: Temperature converter and range flag
# Description: Convert Celsius to Fahrenheit and Kelvin. Provide a
# boolean flag is_high_temperature when temp_c >= 30.0.
# Inputs: temp_c (float)
# Outputs: "Fahrenheit:", "Kelvin:", "High temperature:" true|false
# Validations: temp_c convertible to float; Kelvin must be >= 0.0
# Test cases: 1) Normal: 25.0 -> F=77.0 K=298.15 false
#             2) Border: 30.0 -> true
#             3) Error: non-numeric input
# ------------------------------------------------------------------

def problem_1_temperature_converter():
    raw = input("Enter temperature in Celsius: ").strip()
    try:
        temp_c = float(raw)
    except Exception:
        print("Error: invalid input")
        return
    temp_f = temp_c * 9 / 5 + 32
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid input")
        return
    is_high_temperature = temp_c >= 30.0
    print("Fahrenheit:", temp_f)
    print("Kelvin:", temp_k)
    print("High temperature:", str(is_high_temperature).lower())

# ------------------------------------------------------------------
# Problem 2: Work hours and overtime payment
# Description: Calculate regular pay for up to 40 hours and overtime at
# 150% for hours > 40. Provide has_overtime boolean.
# Inputs: hours_worked (float), hourly_rate (float)
# Outputs: "Regular pay:", "Overtime pay:", "Total pay:", "Has overtime:" true|false
# Validations: hours_worked >= 0, hourly_rate > 0
# Test cases: 1) Normal: 45, 10 -> regular=400, overtime=75, total=475, true
#             2) Border: 40, 12.5 -> overtime=0, false
#             3) Error: negative hours
# ------------------------------------------------------------------

def problem_2_overtime_payment():
    h_raw = input("Enter hours worked: ").strip()
    r_raw = input("Enter hourly rate: ").strip()
    try:
        hours_worked = float(h_raw)
        hourly_rate = float(r_raw)
    except Exception:
        print("Error: invalid input")
        return
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
        return
    regular_hours = min(hours_worked, 40.0)
    overtime_hours = max(0.0, hours_worked - 40.0)
    regular_pay = regular_hours * hourly_rate
    overtime_pay = overtime_hours * hourly_rate * 1.5
    total_pay = regular_pay + overtime_pay
    has_overtime = hours_worked > 40.0
    print("Regular pay:", regular_pay)
    print("Overtime pay:", overtime_pay)
    print("Total pay:", total_pay)
    print("Has overtime:", str(has_overtime).lower())

# ------------------------------------------------------------------
# Problem 3: Discount eligibility with booleans
# Description: Determine discount eligibility if student OR senior OR
# purchase_total >= 1000. Apply 10% discount when eligible.
# Inputs: purchase_total (float), is_student_text (YES/NO), is_senior_text (YES/NO)
# Outputs: "Discount eligible:", "Final total:" <float>
# Validations: purchase_total >= 0.0; texts must be YES or NO
# Test cases: 1) Normal: 1200, NO, NO -> eligible true final 1080
#             2) Border: 999.99, YES, NO -> eligible true
#             3) Error: invalid text
# ------------------------------------------------------------------

def problem_3_discount_eligibility():
    total_raw = input("Enter purchase total: ").strip()
    student_raw = input("Is student? (YES/NO): ").strip().upper()
    senior_raw = input("Is senior? (YES/NO): ").strip().upper()
    try:
        purchase_total = float(total_raw)
    except Exception:
        print("Error: invalid input")
        return
    if purchase_total < 0.0:
        print("Error: invalid input")
        return
    if student_raw not in ("YES", "NO") or senior_raw not in ("YES", "NO"):
        print("Error: invalid input")
        return
    is_student = student_raw == "YES"
    is_senior = senior_raw == "YES"
    discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
    if discount_eligible:
        final_total = purchase_total * 0.9
    else:
        final_total = purchase_total
    print("Discount eligible:", str(discount_eligible).lower())
    print("Final total:", final_total)

# ------------------------------------------------------------------
# Problem 4: Basic statistics of three integers
# Description: Read three integers and compute sum, average, max, min
# and boolean all_even if all are even.
# Inputs: n1, n2, n3 (int)
# Outputs: "Sum:", "Average:", "Max:", "Min:", "All even:" true|false
# Validations: inputs convertible to int
# Test cases: 1) Normal: 2,4,6 -> sum 12 avg 4 max6 min2 all_even true
#             2) Border: 1,2,3 -> all_even false
#             3) Error: invalid int
# ------------------------------------------------------------------

def problem_4_basic_statistics():
    try:
        n1 = int(input("Enter first integer: ").strip())
        n2 = int(input("Enter second integer: ").strip())
        n3 = int(input("Enter third integer: ").strip())
    except Exception:
        print("Error: invalid input")
        return
    sum_value = n1 + n2 + n3
    average_value = sum_value / 3.0
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", str(all_even).lower())

# ------------------------------------------------------------------
# Problem 5: Loan eligibility (income and debt ratio)
# Description: Determine loan eligibility based on monthly income,
# monthly debt and credit score. eligible if income >= 8000 and
# debt_ratio <= 0.4 and credit_score >= 650
# Inputs: monthly_income (float), monthly_debt (float), credit_score (int)
# Outputs: "Debt ratio:", "Eligible:" true|false
# Validations: monthly_income > 0, monthly_debt >= 0, credit_score >= 0
# Test cases: 1) Normal: 10000,3000,700 -> debt_ratio 0.3 eligible true
#             2) Border: income 8000 debt 3200 score 650 -> eligible true
#             3) Error: income 0 -> invalid input
# ------------------------------------------------------------------

def problem_5_loan_eligibility():
    try:
        monthly_income = float(input("Enter monthly income: ").strip())
        monthly_debt = float(input("Enter monthly debt: ").strip())
        credit_score = int(input("Enter credit score: ").strip())
    except Exception:
        print("Error: invalid input")
        return
    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
        return
    debt_ratio = monthly_debt / monthly_income
    eligible = (monthly_income >= 8000.0) and (debt_ratio <= 0.4) and (credit_score >= 650)
    print("Debt ratio:", debt_ratio)
    print("Eligible:", str(eligible).lower())

# ------------------------------------------------------------------
# Problem 6: Body Mass Index (BMI) and category flag
# Description: Compute BMI and boolean flags for underweight, normal,
# and overweight categories.
# Inputs: weight_kg (float), height_m (float)
# Outputs: "BMI:", "Underweight:", "Normal:", "Overweight:"
# Validations: weight_kg > 0, height_m > 0
# Test cases: 1) Normal: 70,1.75 -> bmi ~22.86 normal true
#             2) Border: bmi = 18.5 or 25
#             3) Error: zero or negative inputs
# ------------------------------------------------------------------

def problem_6_bmi_category():
    try:
        weight_kg = float(input("Enter weight in kg: ").strip())
        height_m = float(input("Enter height in meters: ").strip())
    except Exception:
        print("Error: invalid input")
        return
    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
        return
    bmi = weight_kg / (height_m * height_m)
    bmi_rounded = round(bmi, 2)
    is_underweight = bmi < 18.5
    is_normal = (bmi >= 18.5) and (bmi < 25.0)
    is_overweight = bmi >= 25.0
    print("BMI:", bmi_rounded)
    print("Underweight:", str(is_underweight).lower())
    print("Normal:", str(is_normal).lower())
    print("Overweight:", str(is_overweight).lower())

# ------------------------------------------------------------------
# Main driver menu
# ------------------------------------------------------------------

def main():
    while True:
        print("\n=== Numeric Exercises Menu ===")
        print("1) Temperature converter")
        print("2) Overtime payment")
        print("3) Discount eligibility")
        print("4) Basic statistics of three ints")
        print("5) Loan eligibility")
        print("6) BMI and category")
        print("0) Exit")
        choice = input("Select option: ").strip()
        if choice == "1":
            problem_1_temperature_converter()
        elif choice == "2":
            problem_2_overtime_payment()
        elif choice == "3":
            problem_3_discount_eligibility()
        elif choice == "4":
            problem_4_basic_statistics()
        elif choice == "5":
            problem_5_loan_eligibility()
        elif choice == "6":
            problem_6_bmi_category()
        elif choice == "0":
            print("Program terminated. Goodbye!")
            break
        else:
            print("Error: invalid option")

if __name__ == "__main__":
    main()

# ------------------------------------------------------------------
# CONCLUSIONS
# ------------------------------------------------------------------
# Integers and floats serve different purposes: ints for discrete
# counts, floats for continuous measurements. Booleans arise from
# comparisons and guide program flow. Validating ranges and avoiding
# division by zero are essential practices. These exercises illustrate
# common patterns in payroll, eligibility checks, and health metrics.

# ------------------------------------------------------------------
# REFERENCES
# ------------------------------------------------------------------
# 1) Python documentation - Numeric and Boolean types
# 2) Real Python - Python Booleans
# 3) W3Schools - Python Numbers
# 4) GeeksforGeeks - BMI calculator in Python
# 5) Course notes - Programming Methodology
# ------------------------------------------------------------------
