# 5.6 Вызываемые объекты

# Класс Calculator

# class Calculator:
#     def __init__(self):
#         pass
#
#     def __call__(self, a, b, operation):
#         opers = {'+': lambda x, y: x + y, '-': lambda x, y: x - y,
#                  '*': lambda x, y: x * y, '/': lambda x, y: x / y}
#         if operation == '/' and b == 0:
#             raise ValueError('Деление на ноль невозможно')
#         res = opers[operation](a, b)
#         return res
#
#
# calculator = Calculator()
#
# try:
#     print(calculator(10, 0, '/'))
# except ValueError as e:
#     print(e)


# Класс RaiseTo

# class RaiseTo:
#     def __init__(self, degree):
#         self.degree = degree
#
#     def __call__(self, x):
#         return x ** self.degree
#
#
# raise_to_two = RaiseTo(2)
#
# print(raise_to_two(2))
# print(raise_to_two(3))
# print(raise_to_two(4))


# Класс Dice

# import random
#
#
# class Dice:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def __call__(self):
#         return random.randint(1, self.sides)
#
#
# kingdice = Dice(6)
#
# print(kingdice() in [1, 2, 3, 4, 5, 6])
# print(kingdice() in [1, 2, 3, 4, 5, 6])
# print(kingdice() in [7, 8, 9, 10])


#  Класс QuadraticPolynomial

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def __call__(self, x):
#         return self.a * x * x + self.b * x + self.c
#
# func = QuadraticPolynomial(1, 2, 1)
#
# print(func(1))
# print(func(2))


# Класс Strip

# class Strip:
#     def __init__(self, chars):
#         self.chars = chars
#
#     def __call__(self, string):
#         return string.strip(self.chars)
#
# strip = Strip('!? ')
#
# print(strip('     ?beegeek!'))
# print(strip('!bee?geek!'))


# Класс Filter

# class Filter:
#     def __init__(self, predicate):
#         if predicate:
#             self.predicate = predicate
#         else:
#             self.predicate = bool
#
#     def __call__(self, iterable):
#         return list(filter(self.predicate, iterable))
#
#
# leave_even = Filter(lambda x: x % 2 == 0)
# numbers = [1, 2, 3, 4, 5, 6]
#
# print(leave_even(numbers))


# Класс DateFormatter

# from datetime import date
#
#
# class DateFormatter:
#     _data = {
#         "ru": r"%d.%m.%Y",
#         "us": r"%m-%d-%Y",
#         "ca": r"%Y-%m-%d",
#         "br": r"%d/%m/%Y",
#         "fr": r"%d.%m.%Y",
#         "pt": r"%d-%m-%Y"
#     }
#
#     def __init__(self, country_code):
#         self.country_code = country_code
#
#     def __call__(self, d):
#         return d.strftime(self._data[self.country_code])
#
#
# ru_format = DateFormatter('ru')
#
# print(ru_format(date(2022, 11, 7)))


# Декоратор @CountCalls

# class CountCalls:
#     def __init__(self, func):
#         self.func = func
#         self.calls = 0
#
#     def __call__(self, *args, **kwargs):
#         self.calls += 1
#         return self.func(*args, **kwargs)
#
#
# @CountCalls
# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
# print(add(2, 3))
# print(add.calls)


# Декоратор @CachedFunction

# class CachedFunction:
#     def __init__(self, func):
#         self.func = func
#         self.cache = dict()
#
#     def __call__(self, *args, **kwargs):
#         if args not in self.cache:
#             self.cache[args] = self.func(*args)
#         return self.cache[args]
#
#
# @CachedFunction
# def slow_fibonacci(n):
#     if n == 1:
#         return 0
#     elif n in (2, 3):
#         return 1
#     return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
#
#
# print(slow_fibonacci(100))


