"""
In OOP a child can access parent class's methods but a parent class cannot
access childe class method.
"""

# - In the following example if we try to access say_hello method from a Employee instance
# - It will execute the parent class's  say_hello method.
# - Because Employee class doesn't have a say_hello method.
# - However if we define say_hello method inside of the child -> Employee class.
# - Then again if we try to access say_hello method from a Employee instance
# - It will execute it from Employee class


class Person:
    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def say_hello(self):
        print(f"Hi my name is {self.first_name} {self.first_name} ")


class Employee(Person):
    def __init__(self, first_name, last_name, salary) -> None:
        # we can invoke parent class __init__ method by doing the following
        # we need send all the parameters that is required in the parent __init__ method
        # Except self
        # using super means manually calling the parent method(that is associated with super)
        super().__init__(first_name, last_name)
        self.salary = salary


# - The following inheritance means that any manager
# - is an Employee and also a Person
# - Which means any Manager instance is also an instance of
# - Employee and Person class technically
class Manager(Employee):
    def __init__(self, first_name, last_name, salary, department) -> None:
        super().__init__(first_name, last_name, salary)
        self.department = department


class Owner(Person):
    def __init__(self, first_name, last_name, net_worth) -> None:
        super().__init__(first_name, last_name)
        self.net_worth = net_worth
