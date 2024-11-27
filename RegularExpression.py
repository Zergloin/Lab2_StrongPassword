import re

password_regex = r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()_+{}.])[A-Za-z\d!@#$%^&*()_+{}.]{8,}'


def is_valid_password(password):
    try:
        if not isinstance(password, str):
            raise TypeError('The specified password must be a string')
        return re.match(password_regex, password) is not None
    except TypeError as ex:
        print(f'Error: {ex}!')
        return False


def find_password_text(text):
    try:
        if not isinstance(text, str):
            raise TypeError('The specified text must be a string')
        return re.findall(password_regex, text)
    except TypeError as ex:
        print(f'Type error: {ex}!')
        return []
