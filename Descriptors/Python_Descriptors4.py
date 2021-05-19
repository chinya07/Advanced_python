'''
Descriptors using @property (decorators)
syntax:

@property --> Get method
@x.setter --> Set method
@x.deleter --> Delete method
'''

class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        print("Getting the name")
        return self._name

    @name.setter
    def name(self, name):
        print("Setting the name: " + name)
        self._name = name

    @name.deleter
    def name(self):
        print("Deleting the name")
        del self._name


x = Person("JOHN")
print(x.name)
x.name = "ALEX"
del x.name
