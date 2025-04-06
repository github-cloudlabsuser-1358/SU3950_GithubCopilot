def fibonacci(n):
    """
    Returns the nth Fibonacci number.
    
    :param n: The position of the Fibonacci number to return (0-indexed).
    :return: The nth Fibonacci number.
    """
    if not isinstance(n, int):
        raise ValueError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

print(fibonacci(5)) # Output: 5
print(fibonacci(10)) # Output: 55   
import unittest

class TestFibonacciFunction(unittest.TestCase):
    def test_fibonacci_positive(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(7), 13)
        self.assertEqual(fibonacci(8), 21)
        self.assertEqual(fibonacci(9), 34)
        self.assertEqual(fibonacci(10), 55)

    def test_fibonacci_negative(self):
        with self.assertRaises(ValueError):
            fibonacci(-5)

    def test_fibonacci_float(self):
        with self.assertRaises(ValueError):
            fibonacci(5.5)

    def test_fibonacci_string(self):
        with self.assertRaises(ValueError):
            fibonacci("5")

    def test_fibonacci_list(self):
        with self.assertRaises(ValueError):
            fibonacci([5])

    def test_fibonacci_dict(self):
        with self.assertRaises(ValueError):
            fibonacci({"n": 5})

    def test_fibonacci_none(self):
        with self.assertRaises(ValueError):
            fibonacci(None)

    def test_fibonacci_empty(self):
        with self.assertRaises(ValueError):
            fibonacci() # No argument provided

# Run the tests
    if __name__ == "__main__":
        unittest.main()
    # Run the tests