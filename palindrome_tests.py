import unittest
from palindrome import is_palindrome

class TestIsPalindrome(unittest.TestCase):
    def test_palindrome_with_spaces_and_case(self):
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_simple_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))

    def test_non_palindrome(self):
        self.assertFalse(is_palindrome("hello"))

    def test_empty_string(self):
        self.assertTrue(is_palindrome(""))

    def test_single_character(self):
        self.assertTrue(is_palindrome("a"))

    def test_palindrome_with_numbers(self):
        self.assertTrue(is_palindrome("12321"))

    def test_non_palindrome_with_numbers(self):
        self.assertFalse(is_palindrome("12345"))

if __name__ == "__main__":
    unittest.main()