# Filename: random_password.py

import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Usage Example
print("A randomly generated password  :"+generate_password())  # Output: A randomly generated password
