list_one = list(input("Enter List 1:"))
list_two = list(input("Enter List 2:"))
common_item=[]

for item in list_one:
    if item in list_two:
        common_item.append(item)

print(common_item)