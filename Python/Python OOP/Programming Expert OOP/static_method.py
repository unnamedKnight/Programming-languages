"""
Static method is a method that sits inside a class and doesn't have access
to any `cls` or `self` keyword.
Its just a function that belongs to the class.

The point of having static method is to better organize your code and keep related methods together.

Static methods are more like utility functions inside a class.

An instance method inside a class works with associated data of an instance.

Where the static method is just a function that is relevant to the class.
And it works like just a normal function.
Where we can pass any data that we want and that data don't need to be associated with any instance.

Static attribute == Class attributes.
"""

# - When you have a method inside your class that acts same for all the instances and it doesn't require any
# - instance or class attributes thats where we can use static method

# - We can call static method inside class method because class method has
# - access to all the class attributes, class methods and static methods inside the class


# - In theory inside static method we can still access class attributes and class methods Or other static methods
# - But this is not good practice
# - Because a staticmethod is supposed to act like a function
# - And it is not supposed to depend on class attribute or instance attribute
# - It should work independently without class attribute or instance attribute
# - That's why we call it a static method



class Student:
    grade_bump = 2.0

    def __init__(self, name, grade) -> None:
        self.name = name
        self.grade = grade

    @classmethod
    def average_from_grades_plus_bump(cls, grades):
        """Calling static method from a class method"""
        average = cls.average_from_grades(grades)
        return min(average + cls.grade_bump, 100)

    @staticmethod
    def average_from_grades(grade):

        # - In theory inside static method we can still access class attributes and class methods
        # - Or other static methods like the following
        # - But this is not good practice
        # Student.grade_bump = 4

        return sum(grade) / len(grade)


s1 = Student("Tim", [80, 75, 65, 100])
s2 = Student("Clement", [60, 50, 65, 60])


s1_average = s1.average_from_grades(s1.grade)
