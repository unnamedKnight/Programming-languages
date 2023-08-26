"""
Operator overloading gives us the ability to implement custom operations on our own classes.
"""

# - We cannot just add p1 and p2 like this p1+p2
# - If we do p1+p2 we will get an error
# - Because python doesn't know how to add two page objects
# - Since the addition behaviour for objects of this class is not defined
# - So, in order to perform addition between two objects of this class we need to implement that


# ----------------------- overriding addition operation ---------------------- #
class Page:
    def __init__(self, words, page_number) -> None:
        self.words = words
        self.page_number = page_number

    # - Here when we are trying to do p1+p2
    # - p1 is going to be associated with self
    # - p2 is going to be associated with other

    def __add__(self, other):
        new_words = self.words + " " + other.words
        new_page_number = max(self.page_number, other.page_number) + 1
        return Page(new_words, new_page_number)


# p1 = Page('Tim is a great instructor', 1)
# p2 = Page('This is another page', 2)

# p3 = p1 + p2
# print(p3.words, p3.page_number)

# ------------------------------------ end ----------------------------------- #


# ------------------------- overloading sub operation ------------------------ #


class Store:
    TAX = 0.13

    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price
        self.after_tax_price = None
        self.set_after_tax_price()

    def set_after_tax_price(self):
        self.after_tax_price = self.price * (1 + Store.TAX)

    def __sub__(self, discount):
        return Store(self.name, self.price - discount)


bread = Store("Bread", 7)

discounted_bread = bread - 2
print(discounted_bread.after_tax_price)


# ------------------------------------ end ----------------------------------- #


