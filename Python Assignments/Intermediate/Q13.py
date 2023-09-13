input_text = input("Enter the text:").lower()

input_char =  input("Enter the chracter:").lower()

string_start =lambda input_text, input_char :input_text[0]== input_char

print(string_start(input_text,input_char))