from collections import OrderedDict

def encode_message(input):
    enoded_msg =""

    dictionary_words = OrderedDict.fromkeys(input, 0)

    for char in input:
        dictionary_words[char] += 1

    for key,value in dictionary_words.items():
        enoded_msg = enoded_msg + key + str(value)
    return enoded_msg
 
input_message = input("Enter the message:")
print (encode_message(input_message))


