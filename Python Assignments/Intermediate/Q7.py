def median(number_list):
    sorted_list = number_list.sort()
    middle = len(number_list)//2
    median = (number_list[middle]+number_list[~middle])/2

    print(f"The median of the list is: {median}")



input_list = list(map(int,input("Enter the list:").split()))

median(input_list)