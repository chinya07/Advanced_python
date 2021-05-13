'''
- Generator Comprehension, List Comprehension and 
Set Comprehension are almost similar
- Generator Comprehension uses circular brackets 
while List Comprehension uses square brackets
- Generators dont allocate memory for whole list
they generate each value one by one hence
memory efficient
'''

input = [1,2,3,4,4,5,6,7,7,7]

output = (ele for ele in input  if ele % 2 == 0)

print("Output values using generator comprehension: ", end='')

for ele in output:
    print(ele, end='')