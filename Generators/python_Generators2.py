import time
import memory_profiler as mem_profile

print("Memory before: {}Mb".format(mem_profile.memory_usage()))

def naturalNoFunction(n):

    result = []
    for i in range(1,n):
        result.append(i)

    return result

def naturalNoGenerator(n):

    for i in range(1,n):
        yield i


t1=time.time()

# natural_nums = naturalNoFunction(1000000)

#output
# Memory before: [37.84375]Mb
# Memory after: [82.77734375]Mb
# Total time taken by a function is:  78.80330085754395

natural_nums = naturalNoGenerator(1000000)

# output
# Memory before: [37.77734375]Mb
# Memory after: [37.79296875]Mb
# Total time taken by a generator is:  0.0069141387939453125

t2=time.time()

print("Memory after: {}Mb".format(mem_profile.memory_usage()))
# print("Total time taken by a function is: ",(t2-t1)*1000)
print("Total time taken by a generator is: ",(t2-t1)*1000)