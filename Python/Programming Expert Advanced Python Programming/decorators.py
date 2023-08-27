"""
decorators are actually functions that is used to call another function.
"""

# - the wrapper function needs to have same parameters as the function that we are decorating.

# - When we use a decorator, the way it works as fas as i understand is
# - we call the decorator, and the decorator takes the function as an argument
# - then the decorator returns the wrapper
# - And then the wrapper is called with function's argument


# - when we call a decorator on a function
# - we get the what the wrapper returns, not what the functions returns
# - if wrapper returns None, then we will get None, even though the actual function is returning something.
# - Because when calling a decorator we get the result of the wrapper, not the actual function.


# - If we use *args and **kwargs as the parameter of the wrapper
# - We need use *args and **kwargs as the parameter of the function that we are calling inside wrapper function.


# ----------------------------- decorator example ---------------------------- #
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Wrapper function called func ")
#         result = func(*args, **kwargs)
#         return None

#     return wrapper


# @decorator
# def func(x):
#     return x


# print(func(1))

# ------------------------------------ end ----------------------------------- #

# - another way of calling the decorator is

# def func(x):
#     return x
# func = decorator(func)  --> decorator returns the wrapper
# func(1) --> what is getting executed here actually is wrapper(1)

# - the explanation of @decorator symbol is
# - func = decorator(func)
# - Now, decorator returns the wrapper
# - And then we execute the wrapper with func arguments


# ------------------------------ timer decorator ----------------------------- #

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print(result)
        end_time = time.time()
        return end_time - start_time

    return wrapper

@timer
def test():
    print('Hello world')


print(test())