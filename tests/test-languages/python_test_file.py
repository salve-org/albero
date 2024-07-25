from typing import Any

from xyz import abc as efg  # noqa: F401

# Example comment

# Variables and literals
u = {"x": "y\f"}  # String with escape sequence
v = 5.5  # float
w = []  # list
x = 5  # integer
y = int("5")  # integer from string
z = lambda: print  # lambda function # noqa: E731

# Control structures
if x == 5:  # if statement
    x += 5 + x  # Addition and compound assignment
    x -= 5 - x  # Subtraction and compound assignment
    x *= 2 * x  # Multiplication and compound assignment
    x /= 2 / x  # Division and compound assignment
    x **= 2**x  # Exponentiation and compound assignment
    if x is not None:  # is not
        pass  # pass statement
    elif x is None:  # elif and is
        pass
    else:  # else
        pass

# match-case statement
match x:
    case 5:  # case
        print("Nice")
    case _:  # case _
        print("Woah")

# while loop and break statement
while 2 in w:  # in operator
    break
if 2 not in w:  # not in operator
    pass


# Function with decorator
def decorator(arg) -> Any:  # Function definition and type hint
    def wrapper():  # Nested function
        return arg()  # return statement

    return wrapper


@decorator
def example():
    if x > y:  # Greater than
        pass
    if x >= y:  # Greater than or equal
        pass
    if x < y:  # Less than
        pass
    if x <= y:  # Less than or equal
        pass
    ...
    if x or y:  # Logical OR
        pass
    with open("xyz.foo") as l:  # with statement and as  # noqa: F841, E741
        assert False == False  # assert statement and equality  # noqa: E712
        assert True == True  # noqa: E712
        pass


# Class with method
class Foo:
    def break_func(self):
        raise Exception("NO")  # raise statement


# for loop and continue statement
for i in range(x):
    continue

# Dictionary merging (Python 3.9+)
q = {} | {}  # Dictionary merge operator

# try-except-finally block
try:
    pass
except:  # bare except  # noqa: E722
    pass
finally:  # finally
    pass
