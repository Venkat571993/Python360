start_number = int(input("Enter Starting Number:"))
end_number = int(input("Enter Ending Number:"))
sum_odd =0
for num in range(start_number,end_number+1):
    if num % 2 !=0:
        sum_odd += num

print(sum_odd)
