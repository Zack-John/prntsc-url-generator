import webbrowser
import random

my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9']



def get_random_url(li):
    url = "prnt.sc/"
    chars = random.sample(my_list, 6)

    for char in chars:
        url += char

    print("visiting url "+ url)
    webbrowser.open(url)


get_random_url(my_list)