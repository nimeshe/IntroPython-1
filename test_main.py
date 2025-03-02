import pytest
from main import *


# Define list of names to run the tests
test_names = ["Jean-Luc", "Anne-Marie", "O'Connor", "D'Angelo", "María José", "Renée", "José", "João", "François", "Márquez", 
              "López", "García", "Nuñez", "Chloé", "Saoirse O’Brien", "Åsa", "Björn", "Éléonore", "Siobhán", "Mikhail Gorbachev", 
              "Hans Grüber", "Jürgen Klopp"]

@pytest.mark.parametrize("name", test_names)
def test_is_valid_name(name):
    assert is_valid_name(name), f"Failed for name: {name}"
    assert not is_valid_name(None)  # Invalid name - name cannot be None
    assert not is_valid_name("")  # Invalid name - name cannot be None
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

def test_is_valid_gender():
    assert is_valid_gender("M") #Valid Gender
    assert is_valid_gender("m") #Valid Gender
    assert is_valid_gender("F") #Valid Gender
    assert is_valid_gender("f") #Valid Gender
    assert is_valid_gender("NB") #Valid Gender
    assert is_valid_gender("Nb") #Valid Gender
    assert is_valid_gender("nB") #Valid Gender
    assert is_valid_gender("nb") #Valid Gender
    assert is_valid_gender("O") #Valid Gender
    assert is_valid_gender("o") #Valid Gender
    
    assert not is_valid_gender("0") #Invalid Gender
    assert not is_valid_gender("") #Invalid Gender
    assert not is_valid_gender(None) #Invalid Gender
    assert not is_valid_gender(0) #Invalid Gender

pytest.main()