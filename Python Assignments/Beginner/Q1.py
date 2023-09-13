user_input = int(input("Please Enter the Number:"))
if user_input % 3 == 0 and user_input % 5 ==0:
    print("Consultadd - Python Training")
elif user_input % 3 == 0:
    print("Consultadd")
elif user_input % 5 == 0:
    print("Python Training")
else:
    print("None")