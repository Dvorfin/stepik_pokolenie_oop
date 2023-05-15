# 4.7 Декораторы @classmethod и @staticmethod


# Класс Circle

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#
#     @classmethod
#     def from_diameter(cls, diameter):
#         return cls(diameter / 2)
#
# circle = Circle.from_diameter(10)
#
# print(circle.radius)


# Класс Rectangle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     @classmethod
#     def square(cls, side):
#         return cls(side, side)
#
# rectangle = Rectangle.square(5)
#
# print(rectangle.length)
# print(rectangle.width)


# Класс QuadraticPolynomial

# class QuadraticPolynomial:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     @classmethod
#     def from_iterable(cls, it):
#         return cls(*it)
#
#     @classmethod
#     def from_str(cls, srr):
#         srr = map(float, srr.split())
#         return cls(*srr)
#
#
# polynom = QuadraticPolynomial.from_str('-1.5 4 14.8')
#
# print(polynom.a)
# print(polynom.b)
# print(polynom.c)
# print(polynom.a + polynom.b + polynom.c)


# Класс Pet

# class Pet:
#     pets = None
#
#     def __init__(self, name):
#         self.name = name
#         if Pet.pets:
#             Pet.pets.append(self)
#         else:
#             Pet.pets = [self]
#
#     @classmethod
#     def first_pet(cls):
#         if cls.pets:
#             return cls.pets[0]
#         return cls.pets
#
#     @classmethod
#     def last_pet(cls):
#         if cls.pets:
#             return cls.pets[-1]
#         return cls.pets
#
#     @classmethod
#     def num_of_pets(cls):
#         if cls.pets:
#             return len(cls.pets)
#         return 0
#
#
# pet1 = Pet('Ratchet')
# pet2 = Pet('Clank')
# pet3 = Pet('Rivet')
#
# print(Pet.first_pet().name)
# print(Pet.last_pet().name)
# print(Pet.num_of_pets())


# Класс StrExtension

# class StrExtension:
#     def __init__(self):
#         pass
#
#     @staticmethod
#     def remove_vowels(srr):
#         return ''.join(filter(lambda x: x.lower() not in 'aeiouy', srr))
#
#     @staticmethod
#     def leave_alpha(srr):
#         return ''.join(filter(lambda x: x.isalpha(), srr))
#
#     @staticmethod
#     def replace_all(srr, chars, char):
#         for c in chars:
#             srr = srr.replace(c, char)
#         return srr
#
#
# print(StrExtension.remove_vowels('Python'))
# print(StrExtension.leave_alpha('Python111'))
# print(StrExtension.replace_all('Python', 'Ptn', '-'))


# Класс CaseHelper 🌶️

# import re
#
# class CaseHelper:
#
#     @staticmethod
#     def is_snake(srr):
#         pattern = r'([a-z]+_?[a-z]+)'
#         return True if re.fullmatch(pattern, srr) else False
#
#     @staticmethod
#     def is_upper_camel(srr):
#         pattern = r'([A-Z]+[a-z]+)+'
#         return True if re.fullmatch(pattern, srr) else False
#
#     @staticmethod
#     def to_snake(srr):
#         pattern = r'\B(?P<w1>[A-Z]+[a-z]+)'
#
#         def func(match_obj):
#             s = match_obj.group(0)  # строка совпадения
#             return '_' + s.lower()
#
#         return re.sub(pattern, func, srr).lower()
#
#     @staticmethod
#     def to_upper_camel(srr):
#         result = re.split(r'_', srr)
#         return ''.join(map(str.title, result))
#

# print(CaseHelper.is_upper_camel('beegeek'))
# print(CaseHelper.is_upper_camel('bee_geek'))
# print(CaseHelper.is_upper_camel('Beegeek'))
# print(CaseHelper.is_upper_camel('BeeGeek'))
# print(CaseHelper.to_snake('Beegeek'))
# print(CaseHelper.to_snake('BeeGeek'))
# print(CaseHelper.to_upper_camel('beegeek'))
# print(CaseHelper.to_upper_camel('bee_geek'))
