# 5.2 Строковое представление объектов

# Класс Book

# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
#
#     def __str__(self):
#         return f'{self.title} ({self.author}, {self.year})'
#
#     def __repr__(self):
#         return f"Book('{self.title}', '{self.author}', {self.year})"
#
# book = Book('Изучаем Python', 'Марк Лутц', 2021)
#
# print(book)
# print(repr(book))


# Класс Rectangle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def __repr__(self):
#         return f"Rectangle({self.length}, {self.width})"
#
#
# rectangle = Rectangle(1, 2)
#
# print(str(rectangle))
# print(repr(rectangle))


# Класс Vector

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"Вектор на плоскости с координатами ({self.x}, {self.y})"
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
# vector = Vector(1, 2)
#
# print(str(vector))
# print(repr(vector))


# Класс IPAddress

# from functools import singledispatchmethod
#
# class IPAddress:
#     @singledispatchmethod
#     def __init__(self, ipaddress):
#         self.ipaddress = ipaddress
#
#     @__init__.register(str)
#     def _from_str(self, arg):
#         self.ipaddress = arg
#
#     @__init__.register(tuple)
#     @__init__.register(list)
#     def _from_str(self, arg):
#         self.ipaddress = '.'.join(map(str, arg))
#
#     def __str__(self):
#         return f'{self.ipaddress}'
#
#     def __repr__(self):
#         return f'IPAddress({repr(self.ipaddress)})'
#
#
# ip = IPAddress([1, 1, 10, 10])
#
# print(str(ip))
# print(repr(ip))


# Класс PhoneNumber

# class PhoneNumber:
#     def __init__(self, phone):
#         self.phone = phone.replace(' ', '')
#
#     def __str__(self):
#         phone = '(' + self.phone[:3] + ') ' + self.phone[3:6] + '-' + self.phone[6:]
#         return phone
#
#     def __repr__(self):
#         return f"PhoneNumber('{self.phone}')"
#
# phone = PhoneNumber('9173963385')
#
# print(str(phone))
# print(repr(phone))


# Класс AnyClass

# class AnyClass:
#     def __init__(self, *args, **kwargs):
#         for k, v in kwargs.items():
#             setattr(self, k, v)
#
#     def __str__(self):
#         res = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
#         return "AnyClass: " + ', '.join(res)
#
#     def __repr__(self):
#         res = [f"{k}={repr(v)}" for k, v in self.__dict__.items()]
#         return "AnyClass(" + ', '.join(res) + ")"
#
#
# cowboy = AnyClass(name='John', surname='Marston')
#
# print(str(cowboy))
# print(repr(cowboy))