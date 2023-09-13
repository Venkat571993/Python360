MAX_CHAR = 26
 
def ComputerAllocation(n, seq):

    seen = [0] * MAX_CHAR
    nocomputers = 0
    occupied = 0    
 
    for i in range(len(seq)):
        index = ord(seq[i]) - ord('A')
        if seen[index] == 0:
            seen[index] = 1
            if occupied < n:
                occupied+=1
                seen[index] = 2
            else:
                nocomputers+=1
        else:
            if seen[index] == 2:
                occupied-=1
            seen[index] = 0
 
    return nocomputers
 

code_sequence = input("Enter the Sequence:")
computers = int(input("Enter the number of computers available:"))
print (ComputerAllocation(computers,code_sequence))