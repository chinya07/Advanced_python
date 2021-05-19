# Descriptors using property

# Syntax:
# property(fget=None, fset=None, fdel=None, doc=None)

class Person:
    def __init__(self, name):
        self._name = name

    def getName(self):
        print("Getting the name")
        return self._name

    def setName(self, name):
        print("Setting the name to :" + name)

    def delName(self):
        print("Deleting the name")
        del self._name


    name = property(getName, setName, delName)

name = Person("John")
print(name.name)

name.name = "Alex"
del name.name