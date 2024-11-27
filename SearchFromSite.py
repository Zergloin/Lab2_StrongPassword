import requests
from RegularExpression import find_password_text


def find_password_site(url):
    try:
        if not isinstance(url, str):
            raise TypeError('The URL must be a string')
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        passwords = find_password_text(response.text)
        if passwords:
            print('Found strong passwords on the site: ', passwords)
        else:
            print('No strong passwords were found on the site')
    except requests.exceptions.Timeout:
        print('Error: The request was interrupted by time. Check the connection or try a different URL!')
    except requests.exceptions.ConnectionError:
        print('Error: Unable to connect to the server. Check your internet connection!')
    except requests.exceptions.HTTPError as ex:
        print(f'HTTP error: {ex}!')
    except TypeError as ex:
        print(f'Type error: {ex}!')
    except Exception as ex:
        print(f'An unexpected error occurred: {ex}!')


if __name__ == '__main__':
    url = input('Enter the URL: ')
    find_password_site(url)
