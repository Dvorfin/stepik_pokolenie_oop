# Дартс
#
# n = int(input())
#
# matrix = [[1]*n for _ in range(n)]
# cnt = 2
# start = 1
# stop = n - 1
#
# for _ in range(n // 2):
#     for i in range(start, stop):
#         for j in range(start, stop):
#             matrix[i][j] = cnt
#     cnt += 1
#     start += 1
#     stop -= 1
#
# for i in range(n):
#     print(*matrix[i])
#
# for i in range(n):
#     print(*matrix[i])


# Скобочная последовательность

# srr = input()
# total = 0
#
# for c in srr:
#     if c == '(':
#         total += 1
#     if c == ')':
#         total -= 1
#     if total < 0:
#         break
# print(total == 0)


# Функция inversions()

# from itertools import combinations
#
# def inversions(sequence) -> int:
#     res = sum(map(lambda pair: pair[0] > pair[1], combinations(sequence, r=2)))
#     return res
#
# sequence = [1, 2, 3, 4, 5]
#
# print(inversions(sequence))


# Покемоны

# import sys
# data = set()
# res = 0
# for pok in sys.stdin:
#     if pok.strip() in data:
#         res += 1
#     else:
#         data |= {pok.strip()}
#
# print(res)


# Декоратор @jsonify

# import json
# from functools import wraps
#
# def jsonify(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         return json.dumps(func(*args, **kwargs))
#     return wrapper
#
# @jsonify
# def make_str(s1, s2):
#     return (s1 + s2) * 5
#
# print(make_str('bee', 'geek'))


# Координаты
#
# for srr in open(0):
#     print(srr.strip('()\n').split(', '))
#     x, y = map(float, srr.strip('()\n').split(', '))
#     print((-90 <= x <= 90) and (-180 <= y <= 180))


# Функция quantify()

# def quantify(iterable, predicate):
#     res = 0
#     if predicate is None:
#         predicate = lambda x: bool(x)
#
#     for el in iterable:
#         if predicate(el):
#             res += 1
#             print(el)
#     return res
#
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# print(quantify(numbers, lambda x: x > 1))


# Pycon

# from datetime import datetime
# import calendar
#
# year = int(input())
# month = int(input())
#
# cal = calendar.monthcalendar(year, month)
# if cal[0][3] == 0:
#     day = calendar.monthcalendar(year, month)[4][3]
# else:
#     day = calendar.monthcalendar(year, month)[3][3]
#
# date = datetime(year=year, month=month, day=day)
# print(date.strftime('%d.%m.%Y'))


# Функция is_integer()

# import re
#
# def is_integer(srr):
#     pattern = r'[-]?\d+[^-\.\w]?\d*'
#     if re.fullmatch(pattern, srr) is None:
#         return False
#     return True
#
# print(is_integer('1-1'))


# Функция is_decimal()

# def is_decimal(srr):
#     try:
#         res = float(srr)
#         return True
#     except ValueError:
#         return False
#
# print(is_decimal('100'))
# print(is_decimal('199.1'))
# print(is_decimal('-0.2'))
# print(is_decimal('.-95'))
# print(is_decimal('-.95'))
# print(is_decimal('.10'))


# Функция is_fraction()

import re

# import re
#
# def is_fraction(srr):
#     pattern = r'-?(\d+)+(\/){1}\d*[1-9]{1}\d*'
#     return bool(re.fullmatch(pattern, srr))
#
# print(is_fraction('1000/1'))
# print(is_fraction('-54/9'))
# print(is_fraction('54365486548645/472342935648904709456'))  # true
#
# print(is_fraction('1000/00001'))  # true
# print(is_fraction('-1000/00001'))  # true


# Функция intersperse()

# def intersperse(iterable, delimiter):
#     flag = False
#
#     for c in iterable:
#         if flag:
#             flag = not flag
#             yield delimiter
#         flag = not flag
#         yield c
#
# print(*intersperse([1, 2, 3], 0))
# print(*intersperse('beegeek', '!'))
# print(*intersperse('A', '...'))


# Аннуитет

# def annual_return(start, percent, years):
#     for _ in range(years):
#         start = start + start * (percent / 100)
#         yield start
#
#
# for value in annual_return(70000, 8, 10):
#     print(round(value))


# Функция pluck()

# def pluck(data, path, default=None):
#     key = path.split('.')
#     for k in key[0:-1]:
#         if type(data[k]) != dict:
#             return data.get(k, default)
#         else:
#             data = data[k]
#     return data.get(key[-1], default)
#
#
# d = {'a': {'b': {'c': {'d': {'e': 4}}}}}
#
# print(pluck(d, 'a.b.c'))


# Декоратор @recviz🌶️🌶️

# from functools import wraps
#
# def recviz(func):
#     func.__dict__['cnt'] = 0
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         params = ', '.join(map(repr, args))
#         for k, v in kwargs.items():
#             params += f', {k}=' + repr(v)
#
#         delimeter = func.__dict__['cnt']
#         print(' '*delimeter + f'-> {func.__name__}({params})')
#         func.__dict__['cnt'] += 4
#
#         res = func(*args, **kwargs)
#
#         print(' '*delimeter + f'<- {repr(res)}')
#         func.__dict__['cnt'] -= 4
#         return res
#
#     return wrapper
#
#
# @recviz
# def fact(n):
#     if n == 0:
#         return 1
#     else:
#         return n * fact(n - 1)
# fact(5)
