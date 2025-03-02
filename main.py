import re

MAX_AGE = 125

def is_valid_name(name):
    ## Validates the name entered is valid against valid characters defined. 
    ## As per this definition, it can includes letters (including accented characters), spaces, hyphens, and apostrophes
    return bool(re.fullmatch(r"[A-Za-zÀ-ÖØ-öø-ÿ\s\-'’]+", name))

def is_valid_age(age):
    ## Validates the age entered is valid against valid characters
    # Check if age is None or empty
    if age is None or age == "":
        return False
    
    # Check if age is a valid integer, less than maximum age defined, and not negative
    if isinstance(age, int) and 1 <= age <= MAX_AGE:
        return True
    
    # If age is not an integer, or it contains decimals or is out of valid range
    return False


def main():
    print("Welcome to the patient information management system")
    print("====================================================")
    print("TO DO")

main()