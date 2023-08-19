'''
When we are using private variables which should not be accessed outside of the
class directly,
In this situation we can utilize property method to access that variable indirectly outside of the class.
'''
class Person:
    def __init__(self, name: str) -> None:
        self.name: str = name
        self._age: int = None

    # - the following line is the old way of using getter and setter
    # - in the property function first parameter should be the get method and second parameter should be the set method
    # - Otherwise property method won't work
    # def set_age(self, age: int) -> None:
    #     self._age = age

    # def get_age(self) -> int:
    #     return self._age

    # - Here, age is the property name
    # age = property(get_age, set_age)

    # - Modern way of using getter and setter
    # - In the property method we have to define the getter method with the property name
    # - and then we define the setter below that with same property name
    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: int) -> int:
        self._age = age


p1 = Person('John')

print(p1.name)
p1.age = 80
print(p1.age)
