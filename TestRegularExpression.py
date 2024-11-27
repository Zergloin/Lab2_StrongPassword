import requests
import unittest
from unittest.mock import patch, mock_open
from RegularExpression import is_valid_password, find_password_text
from SearchFromSite import find_password_site
from SearchFromFile import find_password_file


class TestRegularPassword(unittest.TestCase):
    def test_is_valid_password(self):
        self.assertTrue(is_valid_password('Strong1@'))
        self.assertTrue(is_valid_password('P@ssword1'))
        self.assertTrue(is_valid_password('GgdfjndGR12854$'))
        self.assertFalse(is_valid_password('weakpass'))
        self.assertFalse(is_valid_password('Password1'))
        self.assertFalse(is_valid_password('triqwew123'))

    def test_find_password_text(self):
        text = 'GgdfjndGR12854$\nweakpass\nStrong1@\n43827576834756'
        res = find_password_text(text)
        self.assertEqual(res, ['GgdfjndGR12854$', 'Strong1@'])


class TestSearchFromFile(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open,
           read_data='123456\n123456789\n111111\npassword\nL58jkdjP!\nmustang\n12345678\npassword1\n1234567\n123123\n!QAZ2wsx')
    def test_find_password_file(self, mock_file):
        result = find_password_file('passwords.txt')
        self.assertEqual(result, ['L58jkdjP!', '!QAZ2wsx'])

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_find_password_file_not_found(self, mock_file):
        with patch('builtins.print') as mock_print:
            find_password_file('password_nf.txt')
            mock_print.assert_called_with('Error: File not found. Check the path!')


class TestSearchFromSite(unittest.TestCase):
    @patch('requests.get')
    def test_find_password_site(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = 'polaca\n252024\n230160\nd@nI3011\njsb767\n110250\ncasulo\nLovedog@2\nmunike2009\nrocksoda1206\nAnaicul090481..'

        with patch('builtins.print') as mock_print:
            find_password_site(
                'https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/unkown-azul.txt')
            mock_print.assert_called_with("Found strong passwords on the site: ",
                                          ['d@nI3011', 'Lovedog@2', 'Anaicul090481..'])

    @patch('requests.get')
    def test_find_emails_on_webpage_error(self, mock_get):
        mock_get.side_effect = requests.RequestException('Network error')

        with patch('builtins.print') as mock_print:
            find_password_site(
                'https://raw.githubusercontent.com/danielmiessler/SecLists/refs/heads/master/Passwords/unkown-azul.txt')
            mock_print.assert_called_with('An unexpected error occurred: Network error!')


if __name__ == '__main__':
    unittest.main()
