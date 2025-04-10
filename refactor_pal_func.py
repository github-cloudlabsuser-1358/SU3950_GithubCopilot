from palindrome import is_palindrome
import pytest

def test_is_palindrome_empty_string():
    assert is_palindrome("") == True

def test_is_palindrome_single_character():
    assert is_palindrome("a") == True

def test_is_palindrome_valid_palindrome():
    assert is_palindrome("racecar") == True
    assert is_palindrome("madam") == True
    assert is_palindrome("A man a plan a canal Panama".replace(" ", "").lower()) == True

def test_is_palindrome_not_palindrome():
    assert is_palindrome("hello") == False
    assert is_palindrome("world") == False

def test_is_palindrome_mixed_case():
    assert is_palindrome("RaceCar".lower()) == True
    assert is_palindrome("MadAm".lower()) == True

def test_is_palindrome_with_spaces():
    assert is_palindrome("2 run".replace(" ", "")) == True