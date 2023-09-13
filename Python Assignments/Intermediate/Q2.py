 
def unique_list (num_list):
    unique_num = []
    for item in num_list:
        if item not in  unique_num:
            unique_num.append(item)
    return unique_num


print(unique_list([45,56,78,78,56,4,5,3,5,6,45]))


 