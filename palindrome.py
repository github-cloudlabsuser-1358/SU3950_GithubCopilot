#create a function for checking the string is palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# create a test cases for is_palindrome function
import unittest

class TestPalindrome(unittest.TestCase):
    def test_is_palindrome(self):
        self.assertFalse(is_palindrome('my name is sujit'))
        self.assertTrue(is_palindrome('madam'))
        self.assertFalse(is_palindrome('hello'))

if __name__ == "__main__":
    unittest.main()
