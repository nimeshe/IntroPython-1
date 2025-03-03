from validators import *

def main():
    print("Welcome to the patient information management system")
    print("====================================================\n")
    
    ## Collect Patient Name
    while True:
        patient_name = input('Enter patient\'s full name: ').strip()
        if is_valid_name(patient_name):
            break
        print("You have entered an invalid name! Please try again! \n")
    
    ## Collect Patient Age
    while True:
        patient_age = input('Enter patient\'s age: ').strip()
        if is_valid_age(patient_age):
            break
        print("You have entered an invalid age! Please try again! \n")

    ## Collect Patient Gender
    while True:
        patient_gender = input('Enter patient\'s Gender (M: Male, F: Female, NB: Non-Binary, O: Other / Do not wish to disclose): ').strip()
        if is_valid_gender(patient_gender):
            break
        print("You have entered an invalid gender! Please try again! \n")

     ## Collect Patient Phone
    while True:
        patient_phone_number = input('Enter patient\'s Phone Number (Enter country code with "+" with no spaces. Only digits allowed): ').strip()
        if is_valid_phone_number(patient_phone_number):
            break
        print("You have entered an invalid phone number! Please try again! \n")

     ## Collect Patient Address
    while True:
        patient_address = input('Enter patient\'s Address: ').strip()
        if is_valid_address(patient_address):
            break
        print("You have entered an invalid address! Please try again! \n")

    ## Collect Patient Reason for Visit
    while True:
        patient_reason_for_visit = input('Enter patient\'s Reason for Visit: ').strip()
        if is_valid_address(patient_reason_for_visit):
            break
        print("You have entered an invalid reason for visit! Please try again! \n")

    print("\nDetails you have entered:")
    print(f"Patient\'s name : {patient_name}")
    print(f"Patient\'s age : {patient_age}")
    print(f"Patient\'s gender : {patient_gender}")
    print(f"Patient\'s phone number : {patient_phone_number}")
    print(f"Patient\'s address : {patient_address}")
    print(f"Patient\'s reason for visit : {patient_reason_for_visit}")
    print("\nPatient\'s details have been saved! Good Bye!")
   
main()