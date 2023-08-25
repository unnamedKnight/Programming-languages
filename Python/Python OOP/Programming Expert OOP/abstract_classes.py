"""
An abstract class is just a class that never has any (direct) instance of it.
Its a class that never should be instantiated.
An abstract class in meant to act as base class/ parent class to
other classes in the program.
"""

# - An abstract method is a method that is not implemented by the abstract class
# - but is required to be implemented by any class that inherits from it

# - Here, we know that we cannot access child method from parent class
# - Because inheritance works from parent to child and not from child to parent.
# - But the following code works even when we call reset method from the parent class.
# - One possible explanation is
# - the object we are using is associated with RandomGuesser class
# - So, when we are invoking reset method from parent class
# - since the object is associated with RandomGuesser class, when the parent is invoking the reset method
# - parent class's reset method is not getting invoked
# - But the child class's reset method is getting invoked
# - Because the object we are working with is associated with RandomGuesser class
# - which is a child class of AbstractGame.
# - Which is why may be the child reset method is getting invoked


# ---------------------------------- SUMMARY --------------------------------- #
# - lets say we have two same methods in parent and child class just like the following
# - Now , we create an instance of the child class
# - Now, at some point we will invoke that same method from parent class
# - and the control of the program at that moment will be in parent class.
# - but when we call that method which in this case `reset` method
# - it will not invoke the parent class's reset method but it will invoke the child class's reset method
# - although the control of the program is within the parent class
# - The explanation of this behaviour is
# - since the object is associated with child class in this case RandomGuesser
# - so when reset method is invoked from the parent class in this case AbstractGame
# - the program will first look into objects own class
# - to check if there is any method named  `reset` available in its own class
# - In this case the objects own class is RandomGuesser
# - if there is, it will execute if from there
# - if that respective method is not available in its own class
# - then it will look into its parent class
# - which is why although we invoked `reset` method within the parent class
# - the child class's `reset` method got executed instead of parent class's `reset` method
# ------------------------------------ end ----------------------------------- #

import random


class AbstractGame:
    def start(self):
        while True:
            start = input("Would you like to play?")
            if start.lower() == "yes":
                break
        self.play()

    def end(self):
        print("The game has ended")
        self.reset()

    def play(self):
        raise NotImplementedError("You must provide an implementation for play")

    def reset(self):
        raise NotImplementedError("You must provide an implementation for reset")


class RandomGuesser(AbstractGame):
    def __init__(self, rounds) -> None:
        self.rounds = rounds
        self.round = 0

    def reset(self):
        self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to round {self.round}. Let's begin!")

            random_num = random.randint(0, 2)
            while True:
                guess = input("Enter a number between 1 to 10: ")
                if int(guess) == random_num:
                    print("You got it")
                    break
        self.end()


game = RandomGuesser(1)
game.start()
