file_doc = open("Advanced\Q1\demofile.txt")
contents = file_doc.read()
contents_list = contents.split()

for word in contents_list:
    if len(word) % 2 == 0:
     print(word)   



file_doc.close() 