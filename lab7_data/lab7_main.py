"""
Joseph Bernabe
Lab 7, Accessing data in a file
Sep 29, 2025
"""
from lab7_function import *

testing()
print("\n----------- Example 1: Reading file -----------")
read_data("phrases.txt")

print("\n----------- Example 2: Reading specific portion of a file -----------")
read_up("phrases.txt")

print("\n----------- Example 3: Readlines -----------")
read_readline("phrases.txt")

print("\n----------- Example 4: Read all lines -----------")
read_all("phrases.txt")

print("\n----------- Example 5: Loop through a readlines file -----------")
read_each("phrases.txt")

print("\n----------- Example 6: Create a new file -----------")
new_file("lastname.txt")

print("\n----------- Example 7: Append data into an existing file -----------")
stamp_data("lastname.txt")

print("\n----------- EXERCISE -----------")
count_yahoo = email_read("user_email.txt", "@yahoo.com")
count_gmail = email_read("user_email.txt", "@gmail.com")
count_hotmail = email_read("user_email.txt", "@hotmail.com")