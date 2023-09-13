first_number = int(input("Enter first Number:"))
second_number = int(input("Enter second Number:"))

factor = 0

if first_number > second_number:
    factor = first_number
else:
    factor =second_number

while True:

    if factor% first_number == 0 and factor % second_number == 0 :
        LCM = factor
        break
    factor +=1


print (f"LCM of {first_number} and {second_number} = {LCM}")