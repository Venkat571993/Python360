user_input = list(map(int,input("Enter the array:").strip().split()))

swift_position = int(input("Enter number of swift:"))

array_len = len(user_input)
x=1

while (x<= swift_position):
    
    last_element = user_input[0]
    for i in range(0, array_len-1):
        user_input[i]= user_input[i+1]
    user_input[array_len-1] = last_element
    x +=1

for i in range(array_len):
 print(user_input[i],end=" ")



