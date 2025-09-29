"""
Joseph Bernabe
Lab 8, Unittest
Sep 29, 2025
"""
import unittest
import calculations
# function to add and return the sum of two numbers
def addtronumbers(a,b):
    return a+b

print("----------- Example 1: Test for equality -----------")
# create a code to test function 'addtwonumbers'
class TestAddTwoNumbers(unittest.TestCase):
    def test_add(self):
        self.assertEqual(addtronumbers(2,3),5)

print("\n----------- Example 2: Unittest for calculations -----------")
class TestCalculations(unittest.TestCase):
    def test_multiplication(self):
        self.assertEqual(calculations.multiplythreenumbers(5),5)
        self.assertEqual(calculations.multiplythreenumbers(2,3),6)
        self.assertEqual(calculations.multiplythreenumbers(2,3,4),24)
        self.assertEqual(calculations.multiplythreenumbers(0),0)

    def test_division(self):
        self.assertEqual(calculations.dividetwonumbers(8,4),2)
        self.assertAlmostEqual(calculations.dividetwonumbers(9,2),4.5)
        self.assertEqual(calculations.dividetwonumbers(9,0),-1)
        self.assertIsNone(calculations.dividetwonumbers("a",2))
if __name__ == '__main__':
    unittest.main()
