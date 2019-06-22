# Function to validate a phone number
import re
def PhoneNumberValidator(number):
        pattern='^[6-9]{1}[0-9]{9}$|^[0][6-9][0-9]{9}$|^[+][9][1][6-9][0-9]{9}$'
        if re.match(pattern,str(number)):
            return True
        return False
# PhoneNumberValidator(9876543216)

def emailvalidator(email):
    pattern="^[0-9a-z][0-9a-z_.]{4,13}[0-9a-z][@][0-9a-z]{3,18}[.][a-z]{2,4}$"
    if re.match(pattern,email):
        return True
    return False
