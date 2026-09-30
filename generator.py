import secrets
import string

min = 8
max = 64

def generate_password(length=14):

    if not min <= length <= max:
        raise ValueError("Length must be between " + str(min) + " and " + str(max) + ".")

    all_chars = string.ascii_letters + string.digits + string.punctuation

    while True:
        password = "".join(secrets.choice(all_chars) for _ in range(length))
        for c in password:
            if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any(c in string.punctuation for c in password)):
                return password