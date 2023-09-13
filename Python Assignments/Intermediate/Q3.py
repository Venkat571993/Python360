user_input = list(map(int,input("Enter the numbers:").strip().split()))

sum_value = int(input("Enter the sum value of pair:"))
array_length  = len(user_input)
pair_count =0


for i in range(0,array_length):
   for j in range(i+1, array_length):
      if user_input[i] + user_input[j] == sum_value:
        pair_count +=1


print(f"pair count {pair_count}")
    

