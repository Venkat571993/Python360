import re


def split_code(encoded_text):
    info = re.split("0+",encoded_text)
    dictionary_name ={"first_name":info[0],"last_name":info[1],"id":info[2]}
    print(dictionary_name)




encoded_text1 = input("Enter the Encoded text:")
split_code(encoded_text1)

