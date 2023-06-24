# 5.7 Преобразования типов

# Класс Vector

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def __bool__(self):
#         return self.x > 0 or self.y > 0
#
#     def __int__(self):
#         return int(((self.x ** 2) + (self.y ** 2)) ** 0.5)
#
#     def __float__(self):
#         return ((self.x ** 2) + (self.y ** 2)) ** 0.5
#
#     def __complex__(self):
#         return complex(self.x, self.y)
#
#
# vector = Vector(3, 4)
#
# print(vector)
# print(int(vector))
# print(float(vector))
# print(complex(vector))


# Класс Temperature

# class Temperature:
#     def __init__(self, temperature):
#         self.t = temperature
#
#     def to_fahrenheit(self):
#         return 32 + (9 / 5) * self.t
#
#     @classmethod
#     def from_fahrenheit(cls, tf):
#         return cls((5 / 9) * (tf - 32))
#
#     def __str__(self):
#         return f"{round(self.t, 2)}°C"
#
#     def __bool__(self):
#         return self.t > 0
#
#     def __int__(self):
#         return int(self.t)
#
#     def __float__(self):
#         return float(self.t)
#
#
# t = Temperature.from_fahrenheit(41)
#
# print(t)
# print(int(t))
# print(float(t))
# print(t.to_fahrenheit())


# Класс RomanNumeral🌶️🌶️

# from functools import total_ordering
# from collections import OrderedDict as od
#
# @total_ordering
# class RomanNumeral:
#     # to_roman = {0: '', 1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V', 6: 'VI', 7: 'VII', 8: 'VIII', 9: 'IX', 10: 'X',
#     #             20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC', 100: 'C', 200: 'CC',
#     #             300: 'CCC', 400: 'CD', 500: 'D', 600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM', 1_000: 'M'}
#     #
#     # from_roman = dict(zip(to_roman.values(), to_roman.keys()))
#
#     @staticmethod
#     def to_roman(num):
#         num = str(num)
#         romans = (
#             ('C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM', ''),
#             ('X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC', ''),
#             ('I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', '')
#         )
#         result = ''
#         for i in range(len(num)):
#             if i == 0 and len(num) == 4:
#                 result += 'M' * int(num[i])
#             else:
#                 result += romans[(i - len(num)) % 3][int(num[i]) - 1]
#
#         return result
#
#     @staticmethod
#     def from_roman(num):
#         decimal = 0
#
#         d = (
#             (900, 'CM'),
#             (1000, 'M'),
#             (400, 'CD'),
#             (500, 'D'),
#             (90, 'XC'),
#             (100, 'C'),
#             (40, 'XL'),
#             (50, 'L'),
#             (9, 'IX'),
#             (10, 'X'),
#             (4, 'IV'),
#             (5, 'V'),
#             (1, 'I')
#         )
#
#         d = od(d)
#
#         for k in d:
#             if num.find(d[k]) >= 0:
#                 decimal += k * num.count(d[k])
#                 num = num.replace(d[k], '')
#
#         return decimal
#
#     def __init__(self, number):
#         self.num = number
#
#     def __str__(self):
#         return self.num
#
#     def __int__(self):
#         return self.from_roman(self.num)
#
#     def __eq__(self, other):
#         if isinstance(other, RomanNumeral):
#             return self.num == other.num
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, RomanNumeral):
#             return self.from_roman(self.num) < self.from_roman(other.num)
#         return NotImplemented
#
#     def __add__(self, other):
#         digit = self.from_roman(self.num) + self.from_roman(other.num)
#         return RomanNumeral(self.to_roman(digit))
#
#     def __sub__(self, other):
#         digit = self.from_roman(self.num) - self.from_roman(other.num)
#         return RomanNumeral(self.to_roman(digit))
#
#
# a = RomanNumeral('X')
# b = RomanNumeral('XII')
#
# print(a == b)
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)

# number = RomanNumeral('IV')
# print(number)
# print(int(number))
# print(RomanNumeral('IV') == RomanNumeral('IV'))
