def average_temp(temp,num_temp):
    average = sum(temp)/num_temp
    temp_max = max(temp)
    tem_min = min(temp)
    print(f"The average temperature: {average} \n Maximum Temperature: {temp_max} \n Minimum Temp: {tem_min}")


input_temperature = list(map(int,input("Enter the values seperated by space:").split()))
total_temp = len(input_temperature)
average_temp(input_temperature,total_temp)