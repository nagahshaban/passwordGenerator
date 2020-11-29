from random import choice


def validate_password(password: str):
    is_upper = False
    is_number = False
    is_special = False

    for char in password:
        is_number = char.isdigit()
        if is_number:
            break

    for char in password:
        is_upper = char.isupper()
        if is_upper:
            break

    for char in password:
        if char in '$#%^&*()@!':
            is_special = True
            break

    params = [is_number, is_upper, is_special]
    if all(params):
        return True
    return False


def get_password(chars, length, upper):
    password = ''
    for i in range(int(length)):
        char = choice(chars)
        password += char
    if upper is None:
        password = password.lower()
    return password
