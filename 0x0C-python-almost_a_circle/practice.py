#!/usr/bin/python3



class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def first(self):
        print("getter method called for first")
        return self.__first

    # a setter function
    @first.setter
    def first(self, a):
        print("setter method called for first")
        self.__first = a

    @property
    def last(self):
        print("getter method called for last")
        return self.__last

    # a setter function
    @last.setter
    def last(self, a):
        print("setter method called for last")
        self.__last = a

class Geeks(Person):
    def __init__(self, name, age=0):
        super().__init__(name, name)
        self._age = age

    # using property decorator
    # a getter function
    @property
    def age(self):
        print("getter method called")
        return self._age

    # a setter function
    @age.setter
    def age(self, a):
        if(a < 18):
            raise ValueError("Sorry you age is below eligibility criteria")
        print("setter method called")
        self._age = a

mark = Geeks('Mark Ruffalo', 20)

print(mark.age)
print(mark.name)

mark.age = 19
print(mark.age)
#mark.age = 10
#print(mark.age)
