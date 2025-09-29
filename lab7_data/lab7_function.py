"""
Joseph Bernabe
Lab 7, Accessing data in a file
Sep 29, 2025
"""
def testing():
    print("TESTING")

def read_data(filename):
    # pipe a text line in a file with a Python code
    fileuser = open(filename, 'r')

    # use a loop to go over each line in fileuser
    for each in fileuser:
        print(each)
