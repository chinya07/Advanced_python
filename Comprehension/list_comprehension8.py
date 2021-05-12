# Accessing function using list comprehension

def demo(a):
    return a*2

# print(demo(5))

res = [demo(a) for a in range(10) if a%2==0]
print(res)