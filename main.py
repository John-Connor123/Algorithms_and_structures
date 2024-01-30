'''
Подвиг 7. Вводится строка (слаг). Замените в этой строке все двойные дефисы (--) и тройные (---) на одинарные (-).
Подумайте, в какой последовательности следует выполнять эти замены. Результат преобразования выведите на экран.

dobavlyaem---slagi--slug-k--url---adresam

dobavlyaem-slagi-slug-k-url-adresam

s = 'dobavlyaem---slagi--slug-k--url---adresam'
j, is_end = 0, False
print(s)
for i, char in enumerate(s):
    if i > 8:
        print(s)
        print(i, char, j, is_end)
    if char == '-' and not is_end:
        j = 0
        while s[i+j] == '-':
            j += 1
        s = s[:i+1] + s[i+j:]
        is_end = True
    if j > 0:
        j -= 1
        if not j:
            is_end = False
    if i > 8:
        print(i, char, j, is_end, end='\n\n')
print(s)'''
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


