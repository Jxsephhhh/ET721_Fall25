"""
Joseph Bernabe
Sep 15, 2025
Lab 5, Functions
"""

"""
- Pre-defined function: Python Library
- User-defined function: Create by the programmer

What is function?
- Block of code that begins with 'def' follows by the name of the function and parentheses ():
- The body of the function is indented after :
- The body of the function only runs when the function is called
- To call a function, we need to write the functions name and parentheses
"""
# import python file
from lab5_bernabe_functions import *

# Call function product()
print("\n---------- Example 1: Intro Function ----------")
n1 = 2
n2 = 5
p = product(n1,n2)
print(f"The product of {n1} and {n2} is {p}")
p = product()
print(f"The product is {p}")
p = product(5)
print(f"The product is {p}")

print("\n---------- Example 2: Function to calculate the hypotenuse ----------")
s1 = 5
s2 = 3
hyp = hypotenuse(s1,s2)
print(f"The hypotenuse is {hyp:.2f}")

print("\n---------- Example 3: Function to check if the number is positive, negative or zero ----------")
c = check_number(-3)
print(f"The number is {c}")
c = check_number(5)
print(f"The number is {c}")
c = check_number(0)
print(f"The number is {c}")

print("\n---------- Example 4: Function in a list ----------")
grades = [50, 60, 85, 93, 72, 98]
avg = check_grades(grades)
print(f"Did I pass the class? {check_pass(avg)}")
grades = [50, 60, 30, 50]
print(f"Did I pass the class? {check_pass(check_grades(grades))}")

print("\n---------- Lab Exercise: Random Number Generator and Compare ----------")
min_num = 1
max_num = 10
random_number = generate_random(min_num,max_num)
compare_guess(random_number)