import random
import string

def generate_password(length):
    # Define possible characters for the password: lowercase, uppercase, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Use random.choice to generate the password of the desired length
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

# Example usage: generate a password of length 12
password_length = 12
password = generate_password(password_length)
print(f"Generated password: {password}")
