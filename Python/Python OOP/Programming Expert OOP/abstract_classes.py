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
# - One possible explanation is that,



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

    # def reset(self):
    #     print('reset done')
    #     self.round = 0

    def play(self):
        while self.round < self.rounds:
            self.round += 1

            print(f"Welcome to round {self.round}. Let's begin!")

            random_num = random.randint(0, 10)
            while True:
                guess = input(
                    'Enter a number between 1 to 10: '
                )
                if int(guess) == random_num:
                    print('You got it')
                    break
        self.end()

game = RandomGuesser(1)
game.start()