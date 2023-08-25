"""
An interface is like an abstract class except it contains only abstract methods.
The point of interface is to outline and describe all of the methods
that any class that inherits from that interface must implement.
"""


# - Interface is only for rasing error while certain methods are not implemented.
# - if we use any logic or do anything except raising error inside the
# - Interface class then we cannot call it an interface class anymore.
# - All methods inside interface class should raise NotImplementedError only and do nothing else

# - A proper terminology is when a class inherits an Interface
# - That child class actually implements the interface

class RunCodeInterface:
    def compile_code(self):
        raise NotImplementedError('You must implement compile_code().')

    def execute_code(self):
        raise NotImplementedError('You must implement execute_code().')