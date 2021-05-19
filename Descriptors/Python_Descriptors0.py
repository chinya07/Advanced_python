'''
- Python Descriptors are created for managing the attributes of different classes which use objects as reference
- Descriptors provide a powerful technique to write the reusable code which can be shared between the classes 
- They are not similar to INHERITANCE!
- They are the mechanism behind properties, static method, class method, super method
- They are classes which allow us to do manage property in other class
- They provide interface for __get__(), __set__(), __delete__()

-Syntax:
descr.__method__(self, obj, type=None)->value

Types of Descriptors:
1. Data Desc
2. Non-data Desc

- We can convert non data desc to data desc by adding empty __set__() method
- Remember Descriptors are assigned to the class and not to the instances
- Descriptors are invoked by __getattribute__() method
'''

class Person:
    def __init__(self, name, age, bmi):
        self.name=name
        self.age=age
        self.bmi=bmi
        if isinstance(self.name, str):
            print(self.name)
        else:
            raise ValueError("Name must be string ")
        if self.bmi<0:
            raise ValueError("BMI is never negative")

    def __str__(self):
        return "{0} is {1} years old and has bmi {2}".format(self.name, self.age, self.bmi)


person1 = Person("1", "16", 18)
print(person1)
person1.name = 10
print(person1)