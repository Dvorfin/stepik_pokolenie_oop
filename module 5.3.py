# 5.3 Сравнение объектов


# Класс Vector

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
#     def __eq__(self, other):
#         if isinstance(other, Vector):
#             return self.x == other.x and self.y == other.y
#         if isinstance(other, tuple) and len(other) == 2:
#             return self.x == other[0] and self.y == other[1]
#         return NotImplemented
#
# v1 = Vector(23, 45)
#
# print(v1)
#
# a = Vector(1, 2)
# b = Vector(3, 4)
# c = Vector(5, 6)
#
# vectors = [a, b, c]
# print(vectors)


# Класс Word

# from functools import total_ordering
#
#
# @total_ordering
# class Word:
#     def __init__(self, word):
#         self.word = word
#
#     def __repr__(self):
#         return f"Word('{self.word}')"
#
#     def __str__(self):
#         return f"{self.word.title()}"
#
#     def __eq__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) == len(other.word)
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Word):
#             return len(self.word) < len(other.word)
#         return NotImplemented
#
# word = Word('Beegeek')
#
# print(word.__eq__(1))
# print(word.__ne__(1.1))
# print(word.__gt__(range(5)))
# print(word.__lt__([1, 2, 3]))
# print(word.__ge__({4, 5, 6}))
# print(word.__le__({1: 'one'}))


# Класс Month

# from functools import total_ordering
#
#
# @total_ordering
# class Month:
#     def __init__(self, year, month):
#         self.year = year
#         self.month = month
#
#     def __repr__(self):
#         return f"Month({self.year}, {self.month})"
#
#     def __str__(self):
#         return f"{self.year}-{self.month}"
#
#     def __eq__(self, other):
#         if isinstance(other, Month):
#             return (self.year * 100 + self.month) == (other.year * 100 + other.month)
#         if isinstance(other, tuple) and len(other) == 2:
#             return (self.year * 100 + self.month) == (other[0] * 100 + other[1])
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Month):
#             return self.year * 100 + self.month < other.year * 100 + other.month
#
#         if isinstance(other, tuple) and len(other) == 2:
#             return self.year * 100 + self.month < other[0] * 100 + other[1]
#         return NotImplemented
#
#
# print(Month(1999, 12) == (1999, 12))
# print(Month(1999, 12) < (2000, 1))
# print(Month(1999, 12) > (2000, 1))
# print(Month(1999, 12) <= (1999, 12))
# print(Month(1999, 12) >= (2000, 1))


# Класс Version

# from functools import total_ordering
#
#
# @total_ordering
# class Version:
#     def __init__(self, version:str):
#         self.version = version.split('.')
#         self.version.extend(['0', '0'])
#         self.version = '.'.join(self.version[0:3])
#
#     def __repr__(self):
#         return f"Version('{self.version}')"
#
#     def __str__(self):
#         return f"{self.version}"
#
#     def __eq__(self, other):
#         if isinstance(other, Version):
#             v = self.version.split('.')
#             return v == other.version.split('.')
#         return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, Version):
#             v = self.version.split('.')
#             return list(map(int, v)) < list(map(int, other.version.split('.')))
#         return NotImplemented
#
# versions = [Version('2'), Version('2.1'), Version('1.9.1')]
#
# print(sorted(versions))
# print(min(versions))
# print(max(versions))
