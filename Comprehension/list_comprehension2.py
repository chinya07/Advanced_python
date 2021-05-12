# find common numbers from two lists

'''
list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

intersection = []

for x in list1:
    for y in list2:
        if(x==y):
            intersection.append(x)

print(intersection)
'''

list1 = [1,2,3,4,5]
list2 = [3,4,5,6,7]

intersection = [x for x in list1 for y in list2 if x==y]
print(intersection)