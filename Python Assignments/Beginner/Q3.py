physics =int(input("Please enter the physics mark:"))
chemistry =int(input("Please enter the chemistry mark:"))
biology =int(input("Please enter the biology mark:"))
maths =int(input("Please enter the maths mark:"))
computer =int(input("Please enter the computer mark:"))

percentage = (physics+chemistry+biology+maths+computer)/5
grade =""
if percentage >= 90:
    grade ="A"
elif percentage >= 80:
    grade ="B"
elif percentage >= 70:
    grade ="C"
elif percentage >= 60:
    grade ="D"
elif percentage >= 40:
    grade ="E"
elif percentage < 40:
    grade ="F"

print(f"The Percentage of marks: {percentage} and the Grade: {grade}")