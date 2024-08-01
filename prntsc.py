import webbrowser
import random


# Feel free to edit the char_list if you want to exclude certain characters

char_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


# Change this value to either 5 or 6 to generate different length URLs
url_len = 5



def get_random_url():
    url = "prnt.sc/"
    chars = random.sample(char_list, url_len)

    for char in chars:
        url += char

    print("visiting url "+ url)
    webbrowser.open(url)


get_random_url()