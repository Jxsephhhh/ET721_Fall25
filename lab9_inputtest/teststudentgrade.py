"""
Joseph Bernabe
Oct 8, 2025
Lab 9, Test input and output data
Unit Test
"""
import unittest
from unittest.mock import patch
import io
import studentgrade

class TestStudentGrade(unittest.TestCase):
    # Test with valid input with 3 students and 3 grades
    @patch('builtins.input', side_effect=['3', '85', '90','75'])
    # Capture the printed output
    @patch('sys.stdout', new_callable=io.StringIO)

    # Define a function to test the input and output
    def test_valid_input(self, mock_stdout, mock_input):
        # Call the main function from file 'studentgrade.py'
        studentgrade.main()

        # Retrieve the captured output
        output = mock_stdout.getvalue()

        # Check if the printed output contains the expected average
        self.assertIn("The average grade is: 83.33", output)

    # TEST WITH INVALID INPUTS, THEN VALID INPUTS
    @patch('builtins.input', side_effect=['-1', '0', '2', '95', '110', '80'])
    @patch('sys.stdout', new_callable=io.StringIO)

    def test_invalid_and_valid_input(self, mock_stdout, mock_input):
        studentgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("Number of students must be greater than 0. Please try again", output)
        self.assertIn("Invalid input. Enter a grade between 0 and 100", output)
        self.assertIn("The average grade is: 87.50", output)

    # EXERCISE: Create a unittest for invalid data type, for example when the user input 

    # Invalid data type for number of students (user inputs string)
    @patch('builtins.input', side_effect=['Peter', '2', '80', '90'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_number_of_students_string(self, mock_stdout, mock_input):
        studentgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid input. Please enter a positive number", output)

    # Invalid data type for grade (user inputs string instead of number)
    @patch('builtins.input', side_effect=['2', 'Peter', '85', '90'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_grade_string(self, mock_stdout, mock_input):
        studentgrade.main()
        output = mock_stdout.getvalue()
        self.assertIn("Invalid! Enter a numerical value", output)


# Run the unit test automatically
if __name__ == '__main__':
    unittest.main()