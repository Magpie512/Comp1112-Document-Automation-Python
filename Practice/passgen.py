import secrets
import string

def generate_password(length=12):
    """Generate a secure random password."""
    password = input("Enter desired password: ")

    #Length check
    if len(password) < 8:
        print("Password length should be at least 8 characters.")
    else:
        print("Long enough")
    
    #Checks if password has doesnt both alphabetic and numeric characters
    if not any(c.isalpha() for c in password) and not any(c.isdigit() for c in password):
        print("Password should contain both alphabetic and numeric characters.")
    else:
        print("Character soup")

    """
    string.ascii_letters: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    string.digits: '0123456789'
    string.punctuation: '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

    """

generate_password()
