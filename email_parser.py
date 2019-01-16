import email
from bs4 import BeautifulSoup


EMAIL_HTML_FILE = 'test_email_msg.html'
# EMAIL_HTML_FILE = 'original_msg.txt'


def email_parser(filename):
    """Email parser function that takes in a email file object and returns list of text"""
    soup_email_html = BeautifulSoup(open(filename), "html.parser")
    email_html_text = soup_email_html.get_text()
    email_str = email_html_text.split(' ')
    email_str_list = list(email_str)
    return email_str_list


def convert_email_list_to_dict(list):
    """Returns a dictionary of integer keys for an email list"""
    i = 0
    email_dict = {}
    for text in list:
        i += 1
        email_dict[i] = text
    return email_dict


def find_dict_number_of_search_text(word_to_search, dictionary):
    """Returns a list of found words in email text"""
    key_list = []
    for key, value in dictionary.items():
        if word_to_search in value:
            key_list.append(key)
    return key_list


e = email_parser(EMAIL_HTML_FILE)
# print(e)

d = convert_email_list_to_dict(e)
# print(d)

w = find_dict_number_of_search_text(word_to_search='called', dictionary=d)

print(w)



