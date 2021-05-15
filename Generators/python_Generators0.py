'''
Generators and functions are similar
They return iterable set of items, one
at a time in a different way
It is very memory efficient as it
stores the result which is required
and not the entire result

Function-> return
Generator-> Yield

return statement terminates a function
yield statement pauses a function
'''

# def mul(n):
#     result = n*4
#     return result
#     print("This statement will exec or not ?")

# ans = mul(3)
# print(ans)

def mul(n):
    result = n*4
    result1 = n * 3
    result2 = n * 2

    yield result
    yield result1
    yield result2

ans = mul(3)
print(ans.__next__())
print(ans.__next__())
print(ans.__next__())
# OR
# print(next(ans))
# print(next(ans))
# print(next(ans))