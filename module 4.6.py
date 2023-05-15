# 4.6 Декоратор @property

# Класс Person

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#         #self.fullname = f'{self.name} {self._surname}'
#
#     @property
#     def fullname(self):
#         return f'{self.name} {self.surname}'
#
#     @fullname.setter
#     def fullname(self, fullname):
#         self.name, self.surname = fullname.split()
#
# person = Person('Mike', 'Pondsmith')
#
# print(person.name)
# print(person.surname)
# print(person.fullname)


# Класс Account

# def hash_function(password):
#     hash_value = 0
#     for char, index in zip(password, range(len(password))):
#          hash_value += ord(char) * index
#     return hash_value % 10**9
#
#
# class Account:
#     def __init__(self, login, password):
#         self._login = login
#         self.password = password
#
#     @property
#     def login(self):
#         return self._login
#
#     @login.setter
#     def login(self, foo):
#         raise AttributeError('Изменение логина невозможно')
#
#     @property
#     def password(self):
#         return self._password
#
#     @password.setter
#     def password(self, password):
#         self._password = hash_function(password)
#
#
# account = Account('hannymad', 'cakeisalie')
#
# #account.login = '345345'
# print(account.password)


# Класс QuadraticPolynomial

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @property
#     def x1(self):
#         self._x1 = (-self.b - (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)
#         if self.b ** 2 - 4 * self.a * self.c < 0:
#             return None
#         return self._x1
#
#     @property
#     def x2(self):
#         self._x2 = (-self.b + (self.b ** 2 - 4 * self.a * self.c) ** 0.5) / (2 * self.a)
#         if self.b ** 2 - 4 * self.a * self.c < 0:
#             return None
#         return self._x2
#
#     @property
#     def view(self):
#         coefs = [self.a, self.b, self.c]
#         reprs = list(map(lambda x: x >= 0, coefs))
#         signs = [' + ' if t else ' - ' for t in reprs][1:]
#         return f"{self.a}x^2" + f'{signs[0]}' + f"{abs(self.b)}x" + f'{signs[1]}' + f"{abs(self.c)}"
#
#
#     @property
#     def coefficients(self):
#         return self.a, self.b, self.c
#
#     @coefficients.setter
#     def coefficients(self, tup):
#         self.a, self.b, self.c = tup
#
#
# polynom = QuadraticPolynomial(500, -601, 101)
#
# print(polynom.a, polynom.b, polynom.c)
# print(polynom.x1)
# print(polynom.x2)
# print(polynom.coefficients)
# print(polynom.view)
#
# print()
#
# polynom.coefficients = (-1000, 1202, -202)
# print(polynom.a, polynom.b, polynom.c)
# print(polynom.x1)
# print(polynom.x2)
# print(polynom.coefficients)
# print(polynom.view)


# Класс Color

# class Color:
#     def __init__(self, hexcode):
#         self.hexcode = hexcode
#
#     @property
#     def hexcode(self):
#         return self._hexcode
#
#     @hexcode.setter
#     def hexcode(self, hexcode):
#         self._hexcode = hexcode
#         r, g, b = hexcode[0:2], hexcode[2:4], hexcode[4:]
#         self.r, self.g, self.b = int(r, 16), int(g, 16), int(b, 16)
#
#
# color = Color('0000FF')
#
# color.hexcode = 'A782E3'
# print(color.hexcode)
# print(color.r)
# print(color.g)
# print(color.b)