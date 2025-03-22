import unittest

# Create a Factorial Function to return the factorial of a number

def factorial(n):
    """
    This function returns the factorial of a given number using recursion.
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":

    class TestFactorialFunction(unittest.TestCase):
        def test_factorial_positive(self):
            self.assertEqual(factorial(5), 120)
            self.assertEqual(factorial(7), 5040)

        def test_factorial_zero(self):
            self.assertEqual(factorial(0), 1)

        def test_factorial_one(self):
            self.assertEqual(factorial(1), 1)

        def test_factorial_negative(self):
            with self.assertRaises(ValueError):
                factorial(-5)

    # Run the tests
    unittest.main()


# Run the tests