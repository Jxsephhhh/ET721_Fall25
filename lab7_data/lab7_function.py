"""
Joseph Bernabe
Lab 7, Accessing data in a file
Sep 29, 2025
"""
def testing():
    print("Joseph Bernabe")

# EXAMPLE 1: read file
def read_data(filename):
    # pipe a text line  with a Python code
    with open(filename, 'r') as file1:
        filecontent = file1.read()
        print(filecontent)

    # check if the file is closed. If it is closed, it should return True
    print(f"Is the file closed? {file1.closed}")

# EXAMPLE 1: reading specific portion of a file 
def read_up(filename):
    with open(filename, "r") as file1:
        # Read the first 30 characters 
        print(file1.read(30))
        # read the next 5 chracters
        print(file1.read(5))

# EXAMPLE 3: readlines
def read_readline(filename):
    with open(filename, "r") as file1: 
        # read upt to 20 characters of the first line 
        print(file1.readline(30))
        # continues reading next line up to 5 characters
        print(file1.readline(5))

# EXAMPLE 4: readlines
def read_all(filename):
    with open(filename, "r") as file1:
        print(file1.readlines())

# EXAMPLE 5: Loop through a readlines file
def read_each(filename):
    with open(filename, "r") as file1:
        filelines = file1.readlines()

        # loop thourgh each item in 'filelines'
        for eachline in filelines:
            print(eachline.strip())
            # strip() removes the newline character \n

# EXAMPLE 6: create a new file 
def new_file(filename):
    with open(filename, "w") as file:
        file.write("Python Basics for data analysis\n")
        file.write("Joseph Bernabe\n")

# EXAMPLE 7: append data into an existing file 
from datetime import datetime

def stamp_data(filename):
    with open(filename, "a") as file:
        file.write(f"\n\n{datetime.now()}")

#EXCERCISE

def email_read(filename, email):
    count_email = 0 
    with open(filename, "r") as file1:
        filelines = file1.readlines()
        # loop through each item in 'filelines'
        for eachline in filelines:
            print(eachline.strip())
            if email in eachline:  # check if the email is in the line
                count_email += 1   # increase the count
        return count_email