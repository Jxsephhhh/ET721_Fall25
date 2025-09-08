"""
Joseph Bernabe
Lab 3, Python Conditional Statements and Loops
Sep 8, 2025
"""
# Conditional Statement
print("\n------------ Example 1: If, Elif, ..., Else ------------")
"""
modify example 1: 
- use while loop to validate if the user_number is between 1 and 9
- user can only guess three times. This can be done using for loop or while loop
"""
# Guess a number between 1 and 9
GUESS_NUM = 8
# Loop for only 3 chances
for attempt in range(1, 4):
# Collect the number
    user_number = int(input(f"Guess {attempt}: Enter a number between 1 and 9: "))
# Validate the number
    while user_number <= 0 or user_number >= 10:
        user_number = int(input("ERROR! Guess a number between 1 and 9: "))
# Compare
    if user_number == GUESS_NUM:
        print(f"Great job! {user_number} is the guess number.")
        break
    elif user_number > GUESS_NUM:
        print(f"{user_number} should be lower")
    elif user_number < GUESS_NUM:
        print(f"{user_number} should be higher")
    else:
        print("ERROR!")
print("End of guessing!")

print("\n------------ Example 2: Control Flow with Logical Operators ------------")
# 'and', 'or' 'not' operators
# 'and' operator returns TRUE ONLY if all statements are true
# 'or' operator returns TRUE if at least ONE of the statements is true
# 'not' operator retursn the invert of the logic. True --> not operator --> False
"""
Example 2: 
- Children under the age of 9 are only given milk for lunch
- Children from 10 to 14 are given sandwiches
- Children from 15 to 17 are given a burger
"""
age_student = int(input("Enter an age: "))
lunch = "None"
if age_student < 9 and age_student >= 5:
    lunch = "milk"
elif age_student >= 10 and age_student <= 14:
    lunch = "sandwich"
elif age_student >= 15 and age_student <= 17:
    lunch = "burger"
else:
    lunch = "None"

print(f"At age {age_student} the food is {lunch}")

print("\n------------ Example 3: For Loops ------------")
# 'for' loop enables the program to execute a code block multiple times
for n in range(2,10):
    print(n)

print("\n------------ Example 4: For loop in a list ------------")
years = [2011, 2005, 1998, 1980, 1973]
for y in years:
    print(y)

for index in range(len(years)):
    print(f"Year {index + 1} = {years[index]}")

print("\n------------ Example 5: While Loops as a counter ------------")
count = 1
while count <= 5:
    print(count)
    count += 1

print("\n------------ Example 6: While Loops to validate a number ------------")
# Validate if a number is between -5 and 5 (inclusive)
num = int(input("Enter a number between -5 and 5: "))
# use a while to recollect if the number is not between -5 and 5
while num < -5 or num > 5:
    num  = int(input("ERROR! Enter a number between -5 and 5: "))

print(f"Entered number = {num}")
