from RegularExpression import is_valid_password


def check_user_input():
    try:
        password = input('Enter the password for verification: ')
        if not isinstance(password, str):
            raise TypeError('The specified password must be a string')
        if is_valid_password(password):
            print('Password is strong')
        else:
            print('Password is insecure')
    except TypeError as ex:
        print(f'Type error: {ex}!')
    except Exception as ex:
        print(f'An unexpected error has occurred: {ex}!')


if __name__ == '__main__':
    check_user_input()
