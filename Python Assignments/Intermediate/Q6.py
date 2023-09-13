def power_two(n):

    if (n==0):
        return False
    
    while(n!=1):
        if n%2 != 0:
            return False
        n = n//2
    return True



number =  int(input("Enter the number:"))

if power_two(number):
    print("The number is power of 2")
else:
    print("The number is not power of 2")

