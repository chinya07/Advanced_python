# Lazy properties
import random
import time

# class Waiting:
#     def wait(self):
#         time.sleep(3)
#         return 42
#
#
# x = Waiting()
# print(x.wait())
# print(x.wait())
# print(x.wait())

class Lazy:
    def __init__(self, function):
        self.function = function
        self.name = function.__name__

    def __get__(self, obj, type=None) -> object:
        obj.__dict__[self.name] = self.function(obj)
        return obj.__dict__[self.name]

    def __set__(self, obj, value):
        pass

class Waiting:
    @Lazy
    def wait(self):
        time.sleep(3)
        return 42

x = Waiting()
print(x.wait)
print(x.wait)
print(x.wait)

'''
-@Lazy is instanciating a descriptor and passing it
to x.wait
-Here the decriptor is non-data descriptor so
when you first access the value of the wait attribute, 
the get method is going to automatically get called and
execute wait method on x object
-The the resulting value is going to get stored in the 
dictionary attribute of the object itself
-when you accept the wait attribute again, by then it
will use the lookup chain to find a value for that
attribute inside the dictionary attribute, which now 
already has the value And that value will be returned 
immediately because that value has been cached in the 
dictionary
- This trick wont work if u add set method because it 
would create data descriptor as following the lookup
chain it would have had precedence over the value stored 
in the dictionary 
'''