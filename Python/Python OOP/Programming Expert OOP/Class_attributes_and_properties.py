"""
Class attributes and class methods differ from instance attributes and instance methods.
Because class attributes only works with the class itself, it doesn't work with instance.
A class attribute has no information about instances. It is solely related to class, Not related to different instances.
I can access class attributes from instance but its not the preferred way.
if i have a class attribute and also have an instance attribute with the same variable name.
Then whenever i try to access that variable from instance i will get the value of the attribute that is associated
with instances. I will not get the value of the attribute that is associated with the class.

"""

# - the point of class attribute is to have some information that is associated with every instances of the class.

# - A class method is a method that acts on a class, but id doesn't act on an instance

# - when working with class method instead of self we should pass cls param.
# - Inside a class method we can only access the attributes that is associated with class.
# - We can call class methods from instances, but we can't access any attribute form instances.

# - When we try to access class attribute inside of instance method
# - we need to use Class_name.attribute_name inside that method.

# - The class methods do not access anything related to instances
# - these methods only access attributes and methods that is just related to class.

class Circle:
    pi = 3.14

    @classmethod
    def area(cls, radius):
        return cls.pi * (radius**2)

    @classmethod
    def perimeter(cls, radius):
        return 2 * cls.pi * radius

    @classmethod
    def get_area_and_perimeter(cls, radius):
        """Using two class methods inside a single class method"""
        return cls.area(radius), cls.perimeter(radius)
