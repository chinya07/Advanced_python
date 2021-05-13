# Dict comprehension with if else statements

dict1 = {'a':1, 'b':2, 'c':3, 'd':4}

res_dict = {k:('Even No' if v%2==0 else 'Odd No') for (k,v) in dict1.items()}

print(res_dict)

res_dict1 = {k:v for (k,v) in dict1.items() if v>3 if v%2==0}

print(res_dict1)