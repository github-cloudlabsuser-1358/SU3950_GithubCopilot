def celsius_to_fahrenheit(celsius):
    """
    Convert temperature from Celsius to Fahrenheit.

    Parameters:
    celsius (float): Temperature in Celsius.

    Returns:
    float: Temperature in Fahrenheit.
    """
    factor = 1.8
    return (celsius * factor) + 32


def fahrenheit_to_celsius(fahrenheit):
    """
    Convert temperature from Fahrenheit to Celsius.

    Parameters:
    fahrenheit (float): Temperature in Fahrenheit.
    Returns:
    float: Temperature in Celsius.
    """
    factor = 1.8
    return (fahrenheit - 32) / factor
# Test cases for the temperature conversion functions


import unittest
class TestTemperatureConversion(unittest.TestCase):
    def test_positive_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(25), 77.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)

    def test_negative_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0)
        self.assertAlmostEqual(celsius_to_fahrenheit(-10), 14.0)

    def test_zero_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)

    def test_float_celsius(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(37.5), 99.5)

    def test_numeric_string(self):
        with self.assertRaises(ValueError):
            celsius_to_fahrenheit("25")

    def test_positive_fahrenheit(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(77), 25.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)
    def test_negative_fahrenheit(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(14), -10.0)
    def test_zero_fahrenheit(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)
    def test_float_fahrenheit(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(99.5), 37.5)
    def test_numeric_string_fahrenheit(self):
        with self.assertRaises(ValueError):
            fahrenheit_to_celsius("77")
    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            celsius_to_fahrenheit(None)
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius(None)
    def test_large_numbers(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(1e6), 1.8e6 + 32)
        self.assertAlmostEqual(fahrenheit_to_celsius(1e6), (1e6 - 32) / 1.8)
    def test_small_numbers(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(1e-6), 1.8e-6 + 32)
        self.assertAlmostEqual(fahrenheit_to_celsius(1e-6), (1e-6 - 32) / 1.8)
        
if __name__ == "__main__":
    unittest.main()
# In this test suite, we have defined multiple test cases to cover different scenarios: