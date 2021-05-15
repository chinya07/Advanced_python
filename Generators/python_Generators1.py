'''
Function loads entire result into memory
and shows us
On the other hand Generator only
loads desired or one result at a time
and when user asks for next result
that result is loaded into memory
and showed
'''


# def natural_Nums(n):
#     result = []
#     for n in range(1,n):
#         result.append(n)
#
#     return result
#
# output = natural_Nums(10)
# print(output)

# output: [1,2,3,4,5,6,7,8,9]


def natural_Nums(n):

    for n in range(1,n):
        yield(n)

output = natural_Nums(10)
print(output.__next__())  # -->output: 1
# print(output.__next__())  -->output: 2
# print(output.__next__())  -->output: 3
# print(output.__next__())  -->output: 4
# and so on..
