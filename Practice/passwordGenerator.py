import secrets
import string

print("Please input a password with the following criteria:")
UserInput = input()
print("- At least 8 characters long")
print("- Contains at least one uppercase letter")
print("- Contains at least one lowercase letter")
print("- Contains at least one digit")
print("- Contains at least one special character")

def generate_password():
    length = int(input("Enter desired password length (minimum 8): "))
    
    if length < 8:
        print("Password must be at least 8 characters long")
        return
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    print(f"Generated password: {password}")
    return password

def validate_password(password):
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)
    has_length = len(password) >= 8
    
    return all([has_upper, has_lower, has_digit, has_special, has_length])

if __name__ == "__main__":
    generate_password()