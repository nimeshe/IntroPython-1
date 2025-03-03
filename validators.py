import re
from enum import Enum

# Define the maximum age
MAX_AGE = 125

# Define the Gender enum
class GENDER(Enum):
    MALE = "M" ## Male
    FEMALE = "F" ## Female
    NON_BINARY = "NB" ## Non-Binary
    OTHER = "O" ## Other or Do not want to disclose

def is_valid_name(name):
    ## Validates the name entered is valid against valid characters defined. 
    ## As per this definition, it can includes letters (including accented characters), spaces, hyphens, and apostrophes
    ## Check if name is None or empty
    if name is None or name == "":
        return False
    
    return bool(re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\s\-'’]+", name))

def is_valid_age(age):
    ## Validates the age entered is valid against valid characters
    ## Check if age is None or empty
    if age is None or age == "":
        return False
    elif isinstance(age, str) and age.isdigit() and 1 <= int(age) <= MAX_AGE:    ## Check if age is a valid integer, less than maximum age defined, and not negative
        return True
    else:
        return False
    
def is_valid_gender(gender):
    ## Validates the age entered is valid against valid characters
    ## Check if age is None or empty
    if gender is None or gender =="":
        return False
    
    if not isinstance(gender,str): 
        return False
    elif gender.upper() in [GENDER.MALE.value,GENDER.FEMALE.value,GENDER.NON_BINARY.value,GENDER.OTHER.value]:
        return True
    else:
        return False

def is_valid_phone_number(phone):
    """
    Validates the phone is valid against valid phone number format
    - A leading '+'
    - A country code (1-3 digits)
    - 7-12 digits for phone number
    - No spaces except for 
    """
    if phone is None or phone =="":
        return False
    
    return bool(re.fullmatch(r"^\+\d{1,3}\d{7,12}$", phone))

def is_valid_address(address):
    """
    Validates an address based on:
    - Allowed characters: letters, numbers, spaces, commas, hyphens, apostrophes, periods, accented characters
    - Minimum length: 5 characters
    - Maximum length: 100 characters
    """
    if address is None or address =="":
        return False
    
    return bool(re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ0-9\s,.'’-]{5,100}$", address))

def is_valid_reason_for_visit(reason_for_visit):
    """
    Validates an medical history / reason for visit based on:
    - Allowed: letters, numbers, spaces, commas, periods, apostrophes, hyphens, degree symbol (°)
    - Length: 100 to 500 characters
    """
    if reason_for_visit is None or reason_for_visit =="":
        return False
    
    return bool(re.fullmatch(r"^[A-Za-zÀ-ÖØ-öø-ÿ0-9\s,.'°:/–—”“-]{100,500}$", reason_for_visit))