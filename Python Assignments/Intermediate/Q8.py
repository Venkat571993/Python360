def vowels_count(text, vowels):
    vowels_number = 0
    for word in text:
        if word in vowels:
            vowels_number +=1

    print(vowels_number)





text_input = str(input("Enter the text:"))

vowels = ["a","e","i","o","u"]

vowels_count(text_input,vowels) 