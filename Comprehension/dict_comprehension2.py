# Dictionary comprehension as lambda function

temp_f = {'temp1':10, 'temp2':20, 'temp3':30, 'temp4':40}

# temp_cel = list(map(lambda x: (float(5)/9)*(x-32), temp_f.values()))

# print("temperatures in celcius: ", temp_cel)

# cel_dict = dict(zip(temp_f.keys(), temp_cel))

# print("result dict: ",cel_dict)

cel_dict = {k:(float(5)/9)*(v-32) for (k,v) in temp_f.items()}
print(cel_dict)


