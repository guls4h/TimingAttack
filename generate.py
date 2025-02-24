import random
import string

def generate_strong_password(length=16):
    charset = string.ascii_letters + string.digits
    password = ''.join(random.choice(charset) for _ in range(length))
    return password

strong_password = generate_strong_password(18) 
print("Generated Strong Password:", strong_password)
