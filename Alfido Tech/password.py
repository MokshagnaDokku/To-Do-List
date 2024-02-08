import random
import string

def generate_password(length=12, use_special_chars=True, use_numbers=True):
    characters = string.ascii_letters
    if use_special_chars:
        characters += string.punctuation
    if use_numbers:
        characters += string.digits
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
password = generate_password(length=16, use_special_chars=True, use_numbers=True)
print("Generated Password:", password)