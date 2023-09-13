student_name = list(map(str,input("Enter Student Name:").split()))
course_name = list(map(str,input("Enter the course:").split()))

student_dictonary ={i:j for (i, j) in zip(student_name,course_name)} 

print(student_dictonary)