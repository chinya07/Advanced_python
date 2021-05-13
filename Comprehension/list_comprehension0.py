'''
list comprehension

syntax:

[ expression
    for item in list
    if conditional ]

this is similar to normal loop -

for item in list:
    if condition:
        expression
'''

# Example-Finding Square of a number 

'''
nums = [1,3,5,7,9]
squares = []

for i in nums:
    # if (i%2==0):
    squares.append(i**2)

print(squares)
'''
nums = [1,3,5,7,9]
squares = [i**2 for i in nums]
print(squares)