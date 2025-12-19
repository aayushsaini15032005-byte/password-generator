import random
import string

def generate_password(length, strength):
    if strength == "weak":
        chars = string.ascii_lowercase
    elif strength == "medium":
        chars = string.ascii_letters + string.digits
    else:
        chars = string.ascii_letters + string.digits + string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password
