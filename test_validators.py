import pytest
from validators import *


# Define list of names to run the tests
test_names = [
    ("Jean-Luc",True),
    ("Anne-Marie",True),
    ("O'Connor",True),
    ("D'Angelo",True),
    ("María José",True),
    ("Renée",True),
    ("José",True),
    ("João",True),
    ("François",True),
    ("Márquez",True),
    ("López",True),
    ("García",True),
    ("Nuñez",True),
    ("Chloé",True),
    ("Saoirse O’Brien",True),
    ("Åsa",True),
    ("Björn",True),
    ("Éléonore",True),
    ("Siobhán",True),
    ("Mikhail Gorbachev",True),
    ("Hans Grüber", True),
    ("", False),
    (None, False),
    ("John123", False),
    ("@John$", False),
]

# Define list of ages to run tests
test_ages = [
    ("9",True),     #Valid age - single digit
    ("49",True),    #Valid age - two digits
    ("101",True),   #Valid age - three digits
    (str(MAX_AGE+1),False),  #Invalid age - more than MAX_AGE
    ("",False),     #Invalid age - Empty
    (None,False),   #Invalid age - None
    ("-12",False),   #Invalid age - Negative Number
    ("12.59",False),   #Invalid age - Decimal Values
    ("1001",False),   #Invalid age - more than 3 digits
    ("Ten",False),   #Invalid age - Not digits
]

# Define list of ages to run tests
test_genders = [
    (GENDER.MALE.value,True),     #Valid Gender - M - Male
    (GENDER.FEMALE.value,True),     #Valid Gender - F - Female
    (GENDER.NON_BINARY.value,True),    #Valid Gender - NB - Non-Binary
    (GENDER.OTHER.value,True),     #Valid Gender - O - Other / Do not wish to disclose
    ("0",False),     #Invalid Gender - 0 - Zero not a valid gender
    ("",False),     #Invalid Gender - Gender cannot be empty
    (None,False),     #Invalid Gender - Gender cannot be None
    ("0",False)     #Invalid Gender - 0 - Zero not a valid gender
]

# Define list of valid phone numbers to run the tests
test_phone_numbers =[
    ("+61412345678",True),  # Mobile number (standard format)
    ("+61498765432",True),  # Mobile number
    ("+61234567890",True),  # Landline (Sydney)
    ("+61398765432",True),  # Landline (Melbourne)
    ("+61731234567",True),  # Landline (Brisbane)
    ("+61881234567",True),  # Landline (Adelaide/Perth)
    ("0412345678",False),     # Missing '+61'
    ("+61 412 345 678",False),# Contains spaces
    ("+61-412-345-678",False),# Contains hyphens
    ("+610412345678",True),  # Extra '0' after country code
    ("+614",False),           # Too short
    ("+61abcdefghi",False),   # Contains letters
    ("1234567890",False),     # No country code
    ("",False),               # Empty string
    (None,False)              # NoneType
]

# Define list of valid addresses to run tests
test_addresses = [
    ("123 Main St.", True),               # Standard address
    ("456 Elm Street, Apt 5B", True),      # Includes apartment number
    ("789-B Maple Ave", True),             # Includes hyphen
    ("10 King's Road", True),              # Includes apostrophe
    ("Calle de la Rosa, 24", True),        # Non-English characters
    ("300 La Trobe St, Melbourne VIC 3000, Australia", True), # Australian address
    ("Straße des 17. Juni, Berlin", True), # German address with 'ß'
    ("100 Rue de Rivoli, Paris", True),    # French address
    ("", False),                          # Empty string
    (None, False),                        # NoneType
    ("@", False),                         # Only special character
    ("#123 Main St.", False),             # Starts with invalid character
    ("12345 Elm Street!@", False),        # Contains invalid characters
    ("4 St", False),                      # Too short
    ("A" * 101, False) 
]

# Define List of "Reasons for Visit" to run tests
test_reasons_for_visit = [
    ("John, aged 45, has a history of high blood pressure. In 2019, he had a heart attack and was treated successfully. His current temperature is 98.6°F. No known allergies.", True),  
    ("Patient had a knee injury in 2020. Recovered fully. Blood pressure is stable. No prior surgeries, except appendectomy in childhood.", True),  
    ("Previous asthma, but no attacks since 2018. Has mild seasonal allergies. Occasionally experiences migraines, takes ibuprofen when needed.", True),  
    ("Diabetes Type-2 diagnosed in 2015. Maintains a balanced diet and exercises regularly. Blood sugar levels controlled with medication.", True),  
    ("Hypertension, cholesterol issues. Blood pressure: 120/80. No family history of cardiac diseases. Last check-up: 6 months ago.", True),  
    ("", False),   # Empty text
    (None, False), # NoneType
    ("Short des.", False), # Less than 25 characters
    ("A" * 501, False), # More than 500 characters
    ("Patient has heart issues! @#!", False), # Contains invalid characters (`! @ #`)
    ("John, 32, BP=120/80, had COVID-19, recovered well. Weight 70kg, height 5'9\". No allergies, no meds currently. Last flu shot 2023.", False) # Contains quotes (`"`)
]

@pytest.mark.parametrize("name, expected", test_names)
def test_is_valid_name(name, expected):
    assert is_valid_name(name) == expected, f"Failed for name: {name}"

@pytest.mark.parametrize("age, expected", test_ages)
def test_is_valid_age(age,expected):
    assert is_valid_age(age) == expected, f"Failed for: {age}"

@pytest.mark.parametrize("gender, expected", test_genders)
def test_is_valid_gender(gender,expected):
    assert is_valid_gender(gender) == expected, f"Failed for: {gender}"   

@pytest.mark.parametrize("phone, expected", test_phone_numbers)
def test_is_valid_phone_number(phone,expected):
    assert is_valid_phone_number(phone) == expected, f"Failed for: {phone}"

@pytest.mark.parametrize("address, expected", test_addresses)
def test_is_valid_address(address,expected):
    assert is_valid_address(address) == expected, f"Failed for: {address}"

@pytest.mark.parametrize("reason_for_visit, expected", test_reasons_for_visit)
def test_is_valid_reason_for_visit(reason_for_visit,expected):
    assert is_valid_reason_for_visit(reason_for_visit) == expected, f"Failed for: {reason_for_visit}"
