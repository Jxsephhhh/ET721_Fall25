"""
Joseph Bernabe
Sep 17, 2025
Lab 6: Objects and Classes
"""
print("\n---------- Example 1: Create a class ----------")
class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


    # Method
    def add_radius(self, r):
        self.radius += r
        return self.radius

class Rectangle(object):
    def __init__(self, height, width, color):
        self.height = height
        self.width = width
        self.color = color
    
    # Method to calculate the area
    def area(self):
        return self.height * self.width
    
    # Method to calculate the perimeter
    def perimeter(self):
        return 2 * (self.height + self.width)

# Creating an instance of the class, which is an object
circle1 = Circle(4, "red")
circle2 = Circle(10, "green")

rectangle1 = Rectangle(2, 5, "magenta")
rectangle2 = Rectangle(7, 3, "blue")

# Accessing information in an object
print(f"The color of circle2 = {circle2.color}")
print(f"The width of rectangle1 = {rectangle1.width}")

# Updating data in an object
# Change circle1 color from 'red' to 'yellow'
print(f"The color of circle1 before the update = {circle1.color}")
circle1.color = "yellow"
print(f"The color of circle1 after the update = {circle1.color}")

# Accessing a method
print(f"Radius of circle2 = {circle2.radius}")
# Update the radius by adding 5
circle2.add_radius(5)
print(f"Radius of circle2 after method add_radius = {circle2.radius}")

# Accessing methods in Rectangle
print(f"The area of the rectangle1 with length {rectangle1.width} and height {rectangle1.height} is {rectangle1.area()}")
print(f"The perimeter of the rectangle2 = {rectangle2.perimeter()}")

print("\n---------- EXERCISE ----------")
# Create a BankAccount class
class BankAccount(object):
    def __init__(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 250.50   # initialize balance as 250.50
    
    # Method to deposit
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance = {self.balance}")
    
    # Method to withdraw
    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance = {self.balance}")
        else:
            print("Insufficient funds. Withdrawal cannot be made.")

# Creating an instance of the BankAccount class
useraccount = BankAccount(123456789, "Joseph Bernabe")

# Demonstrating deposits and withdrawals
useraccount.withdraw(700)    
useraccount.deposit(1000)    
useraccount.withdraw(500)    

# Result
print(f"Final balance = {useraccount.balance}")