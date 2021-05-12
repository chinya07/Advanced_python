# Return numbers from the lists which are not equal, as a tuple

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

non_common_elements = [(x,y) for x in list1 for y in list2 if x!=y]
print(non_common_elements)