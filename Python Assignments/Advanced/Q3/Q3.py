def JtoI():
  with open("Advanced\Q3\words.txt") as file1:
    content = file1.read().lower()
    new_content = content.replace("j","i")
    print(new_content)

JtoI()
