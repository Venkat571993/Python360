number = int(input("Enter Number:"))
perfect_number =0
for num in range(1,number):
    if number % num == 0:
        perfect_number += num

if perfect_number == number:
    print("It is a perfect number")
else:
    print("it is not a perfect number")
