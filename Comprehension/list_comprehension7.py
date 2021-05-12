# Parsing file using list comprehension

file1 = open("test.txt", "r")

output = [i for i in file1 if "All" in i]
print(output)