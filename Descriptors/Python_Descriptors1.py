class Descriptors:
    def __init__(self):
        self.__bmi=0

    def __get__(self, instance, owner):
        return self.__bmi

    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("BMI can only be an integer")

        if value<0:
            raise ValueError("BMI can never be less than 0")

        self.__bmi=value


    def __delete__(self, instance):
        del self.__bmi


class Person:
    bmi = Descriptors()   #output: Johnny age is 26 and has bmi of -17 --> if u comment this line
    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi

    def __str__(self):
        return "{0} age is {1} and has bmi of {2}".format(self.name, self.age, self.bmi)


person1 = Person("Johnny", "26", 17)
print(person1)
# person1.bmi = "seventeen"
# print(person1)
person2 = Person("Alex", "25", 22)
print(person2)
print(person1)  # Drawback of descriptors they overwrite value for previous object