# Creating Descriptors using class
# this can be used when same descriptors needed in multiple classes

class Descriptors:
    def __init__(self, x=""):
        self.x = x

    def __get__(self, obj, objtype):
        return "{} for {}".format(self.x, self.x)

    def __set__(self, obj, x):
        if isinstance(x, str):
            self.x = x
        else:
            raise TypeError("x should always be a string")


class Test:
    x = Descriptors()

y = Test()
y.x = "JOHN"
print(y.x)

z = Test()
z.x = 112233
print(z.x)  #will raise an exception
