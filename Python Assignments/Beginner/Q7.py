string_one = input("Enter first string:")
string_two = input("Enter second string:")


if sorted(string_one) == sorted(string_two):
    print("Anagram: True")
else:
    print("Anagram: False")