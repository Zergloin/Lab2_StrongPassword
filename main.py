from InputFromUser import check_user_input
from SearchFromFile import find_password_file
from SearchFromSite import find_password_site

if __name__ == '__main__':
    check_user_input()
    find_password_file(input('Enter the path to the file: '))
    find_password_site(input('Enter the URL: '))
