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
    return bool(re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\s\-'’]+", name))

def is_valid_age(age):
    ## Validates the age entered is valid against valid characters
    ## Check if age is None or empty
    if age is None or age == "":
        return False
    
    ## Check if age is a valid integer, less than maximum age defined, and not negative
    if isinstance(age, int) and 1 <= age <= MAX_AGE:
        return True
    
    ## If age is not an integer, or it contains decimals or is out of valid range
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


def main():
    print("Welcome to the patient information management system")
    print("====================================================")
    print("TO DO")

main()