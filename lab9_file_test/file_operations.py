"""
Joseph Bernabe
Oct 15, 2025
Lab 9, File Operations Test
"""
def write_file(filename, msg):
    with open(filename, "w") as file:
        file.write(msg)

def read_file(filename):
    with open(filename, "r") as file:
        return file.read()   

def append_file(filename, msg):
    with open(filename, "a") as file:
        file.write(msg)   