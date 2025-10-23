"""
Joseph Bernabe
Oct 15, 2025
Lab 9, File Operations Test
"""
import unittest
import os 
from file_operations import read_file, write_file, append_file

class TestFileOperations(unittest.TestCase):
    def setUp(self):
        # set up temporary test file name before each test
        self.filename = "test_file.txt"
        self.msg = "Joseph Bernabe"

    def tearDown(self):
        # remove the test file after each test 
        if os.path.exists(self.filename):
            os.remove(self.filename)

    def test_write_file(self):
        # use your function to write
        write_file(self.filename, self.msg)

        # verify file exists and content matches 
        self.assertTrue(os.path.exists(self.filename))
        result = read_file(self.filename)
        self.assertEqual(result, self.msg)

    def test_read_file(self):
        # prepare a file, then read it through your function
        expected_content = "READ ME!"
        write_file(self.filename, expected_content)

        data = read_file(self.filename)
        self.assertEqual(data, expected_content)

    def test_append_file(self):
        # test appending text to an existing file 
        initial_content = "line one"
        append_content = "\nline two"

        write_file(self.filename, initial_content)
        append_file(self.filename, append_content)

        final_data = read_file(self.filename)
        self.assertEqual(final_data, initial_content + append_content)

# run the unit tests automatically when the file is run 
if __name__ == "__main__":
    unittest.main()