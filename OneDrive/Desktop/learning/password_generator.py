import string
import random
sys = "!@#$%^&*"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + sys
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if __name__ =="__main__":
    print("Generated Password:", generate_password(12))