number = int(input("Enter Number:"))

reversed_num = 0

while number!=0:
    calculation = number %10
    number = number//10

    reversed_num = reversed_num*10 +calculation

print(reversed_num)

