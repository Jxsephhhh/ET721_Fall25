"""
Joseph Bernabe
Function File
Sep 15, 2025
Lab 5, Function
"""
import random
# Example 1: Define a function that passes two numbers and return the product of it
def product(a = 0,b = 0):
    c = a * b
    return c

# Example 2: Function to calculate the hypotenuse
def hypotenuse(side1,side2):
    return(side1**2 + side2**2)**0.5

# Example 3: Function to check if the number is positive, negative or zero
# The function returns a string
def check_number(num):
    if(num > 0):
        return "POSITIVE"
    elif(num < 0):
        return "NEGATIVE"
    else:
        return "ZERO"
    
# Example 4: Function to calculate the average of a list of grades, and return 'true' if the average is greather than 60, otherwise, it returns 'false'

def check_grades(grades):
    # initialize the average value
    avg = 0
    # sum the individual 'grade' from list 'grades' into 'avg'
    for g in grades:
        avg += g
    # find the average grade
    avg /= len(grades)
    return avg

def check_pass(avg_grade):
    # check if the average is greater than 60
    if avg_grade >= 60:
        return True
    else:
        return False
    
# LAB EXERCISE
def generate_random(min_val,max_val):
    return random.randint(min_val,max_val)

def compare_guess(rand_num):
    GUESS_NUMBER = 5
    if rand_num < GUESS_NUMBER:
        print("The number is smaller than the guess number")
    elif rand_num > GUESS_NUMBER:
        print("The number is bigger than the guess number")
    else:
        print("You got it!")
