dict1 = {'a':1, 'b':2, 'c':3, 'd':4}

print(dict1.keys())

print(dict1.values())

print(dict1.items())

# dict2 = {k:v*2 for (k,v) in dict1.items()}
# print(dict2) 

dict2 = {k*2:v for (k,v) in dict1.items()}
print(dict2) 