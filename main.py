from pprint import pprint
from random import randrange, shuffle
from collections import deque
from timeit import timeit
import matplotlib.pyplot as plt
from TimeDecorator import TimeDecorator


def check_new_func(n, func1, func2):
    lst = []
    for i in range(n):
        lst.append(func1(n) == func2(n))
    return all(lst)


