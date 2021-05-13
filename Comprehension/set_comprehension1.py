input = [1,2,2,2,3,3,3,4,5,5,6,6,7,7,7,8]

# output = set()

# for num in input:
#     if num%2==0:
#         output.add(num)

# print(output)

output = {num for num in input if num%2==0}   

print(output)