import os
import tempfile
import unittest


def email_read(filename, email):
    """
    Reads a file and counts how many times the given email appears.
    Returns the total count.
    """
    count = 0
    with open(filename, "r") as file:
        for line in file:
            if email in line.strip():
                count += 1
    return count


class TestEmailReadLab10(unittest.TestCase):
    def setUp(self):
        # Create a temporary file with known contents
        self.tmp = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        self.tmp.write(
            "vsingh@gmail.com\n"
            "pfranco@gmail.com\n"
            "kbrook@gmail.com\n"
            "someoneelse@example.com\n"
        )
        self.tmp.flush()
        self.tmp.close()
        self.path = self.tmp.name

    def tearDown(self):
        # Remove the temp file after each test
        try:
            os.remove(self.path)
        except FileNotFoundError:
            pass

    def test_read_mode(self):
        """
        email_read() should correctly read and count occurrences
        without modifying the file (read-only behavior).
        """
        size_before = os.stat(self.path).st_size
        mtime_before = os.stat(self.path).st_mtime

        count = email_read(self.path, "vsingh@gmail.com")
        self.assertEqual(count, 1)

        size_after = os.stat(self.path).st_size
        mtime_after = os.stat(self.path).st_mtime

        self.assertEqual(size_after, size_before, "File size changed—should only read.")
        self.assertEqual(mtime_after, mtime_before, "File mtime changed—should only read.")

    def test_email_not_found(self):

        self.assertEqual(email_read(self.path, "not_in_file@example.com"), 0)


if __name__ == "__main__":
    unittest.main()