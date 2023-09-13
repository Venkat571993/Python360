number = int(input("Enter Number:"))

sum_digits = 0
count = 1
condition = True

while condition:
    while number:
       sum_digits = sum_digits +(number%10)
       number = number//10

    print(f"Sum of digits at {count} : {sum_digits}")
    number = sum_digits
    sum_digits = 0
    count +=1
    condition = number>9
