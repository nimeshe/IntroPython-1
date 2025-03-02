import pytest
from main import *

def test_is_valid_name():
    assert is_valid_name("John")   #  Valid name - name contains only allowed characters 
    assert is_valid_name("Mary-Anne")   #  Valid name - name contains only allowed characters 
    assert is_valid_name("O’Connor")  #  Valid name - name contains only allowed characters
    assert not is_valid_name("John123")  # Invalid name - name entered has numbers
    assert not is_valid_name("@John")  # Invalid name - name entered has an invalid character
    
def test_is_valid_age():
    assert is_valid_age(9) # Valid age - age not null or empty, not negative or decimal, contains digits (between 1 and 3)
    assert is_valid_age(45) # Valid age - age not null or empty, not negative or decimal, contains digits (between 1 and 3)
    assert is_valid_age(100) # Valid age - age not null or empty, not negative or decimal, contains digits (between 1 and 3)
    
    assert not is_valid_age("") # Invalid age - age cannot be empty
    assert not is_valid_age(None) #Invalid age - age cannot be NULL / None
    assert not is_valid_age(0) # Invalid age - age cannot be zero
    assert not is_valid_age(-2) # Invalid age - age cannot be negative
    assert not is_valid_age(1001) # Invalid age - age contains 4 digits
    assert not is_valid_age(12.51) # Invalid age - age contains decimal places
    assert not is_valid_age("John") # Invalid age - age is not a number


pytest.main()