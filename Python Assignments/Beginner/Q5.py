number = int(input("Enter Number:"))
factorial = 1
for num in range(1,number+1):
    factorial *= num

print(f"{number} Factorial : {factorial}")