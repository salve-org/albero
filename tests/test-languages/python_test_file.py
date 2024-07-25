from typing import Any

from xyz import abc as efg  # noqa: F401

# Example comment

u = {"x": "y\f"}
v = 5.5
w = []
x = 5
y = int("5")
z = lambda: print  # noqa: E731

if x == 5:
    x += 5 + x
    x -= 5 - x
    x *= 2 * x
    x /= 2 / x
    x **= 2**x
    if x is not None:
        pass
    elif x is None:
        pass
    else:
        pass

match x:
    case 5:
        print("Nice")
    case _:
        print("Woah")

while 2 in w:
    break
if 2 not in w:
    pass


def decorator(arg) -> Any:
    def wrapper():
        return arg()

    return arg


@decorator
def example():
    if x > y:
        pass
    if x >= y:
        pass
    if x < y:
        pass
    if x <= y:
        pass
    ...
    if x or y:
        pass
    with open("xyz.foo") as l:  # noqa: E741, F841, F401
        assert False == False  # noqa: E712
        assert True == True  # noqa: E712
        pass


class foo:
    def break_func(self):
        raise Exception("NO")


for i in range(x):
    continue

q = {} | {}
try:
    pass
except:
    pass
finally:
    pass
