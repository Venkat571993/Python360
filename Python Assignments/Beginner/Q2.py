user_input = input("Please enter the character:")
alphabets =0
number =0
for i in user_input:
    if i.isnumeric():
        number+=1
    else:
        alphabets+=1

print(f"Alphabets = {alphabets} and Numbers = {number}")