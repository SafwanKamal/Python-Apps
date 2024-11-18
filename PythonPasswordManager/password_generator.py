import string
import random

def password_generator(length = 20, restrict_symbols = ""):
    all_char_list = list(string.ascii_letters + string.digits + string.punctuation)
    restrict_symbols = list(restrict_symbols)
    all_char_list = [x for x in all_char_list if x not in restrict_symbols]
    password = ""
    for i in range(0, length):
        password += random.choice(all_char_list)

    return password

