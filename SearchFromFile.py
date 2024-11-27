from RegularExpression import find_password_text


def find_password_file(path):
    try:
        if not isinstance(path, str):
            raise TypeError('The path must be a string')
        with open(path, 'r', encoding='utf-8') as file:
            text = file.read()
            passwords = find_password_text(text)
            if passwords:
                print('Found strong passwords on file: ', passwords)
                return passwords
            else:
                print('No strong passwords found in the file')
    except FileNotFoundError:
        print('Error: File not found. Check the path!')
    except PermissionError:
        print('Error: Insufficient permissions to access the file!')
    except TypeError as ex:
        print(f'Type error: {ex}!')
    except Exception as ex:
        print(f'An unexpected error has occurred: {ex}!')


if __name__ == '__main__':
    path = input('Enter the path to the file: ')
    find_password_file(path)
