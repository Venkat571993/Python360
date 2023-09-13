number_list = list(input("Enter the list values:"))

frequency= {}
for num in number_list:
    if num in frequency:
        frequency[num] +=1
    else:
        frequency[num]=1

print(frequency)
    