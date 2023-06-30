# 6.8 Протокол дескрипторов
import random


# Класс NonKeyword
# from keyword import kwlist
#
#
# class NonKeyword:
#     def __init__(self, name):
#         self._attr = name
#
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         if self._attr in obj.__dict__:
#             return obj.__dict__[self._attr]
#         else:
#             raise AttributeError('Атрибут не найден')
#
#     def __set__(self, obj, value):
#         if value not in kwlist:
#             obj.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
#     def __delete__(self, obj):
#         del obj.__dict__[self._attr]
#
# class NonKeywordData:
#     obj = NonKeyword('obj')


# data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, 'Mantrida']
# nonkeyworddata = NonKeywordData()
#
# for item in data:
#     nonkeyworddata.obj = item
#     print(nonkeyworddata.obj)


# Класс NonNegativeInteger

# class NonNegativeInteger:
#     def __init__(self, name, default=None):
#         self._attr = name
#         self._default = default
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr not in obj.__dict__:
#             if self._default is None:
#                 raise AttributeError('Атрибут не найден')
#             else:
#                 return self._default
#         return obj.__dict__[self._attr]
#
#     def __set__(self, obj, value):
#         if isinstance(value, int) and int(value) >= 0:
#             obj.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
# class Student:
#     score = NonNegativeInteger('score', 0)
#
# student = Student()
#
# print(student.score)
# student.score = 0
# print(student.score)


# Класс LimitedTakes

# class MaxCallsException(Exception):
#     pass
#
#
# class LimitedTakes:
#     def __init__(self, times):
#         self._times = times
#
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr not in obj.__dict__:
#             raise AttributeError('Атрибут не найден')
#         if self._times == 0:
#             raise MaxCallsException('Превышено количество доступных обращений')
#         else:
#             self._times -= 1
#             return obj.__dict__[self._attr]
#
#     def __set__(self, obj, value):
#         obj.__dict__[self._attr] = value
#
#
#
# class Student:
#     name = LimitedTakes(3)
#
# student = Student()
# student.name = 'Gwen'
#
# print(student.name)
# print(student.name)
# print(student.name)
#
# try:
#     print(student.name)
# except MaxCallsException as e:
#     print(e)


# Класс TypeChecked

# class TypeChecked:
#     def __init__(self, *args):
#         self._attrs = args
#
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._attr not in obj.__dict__:
#             raise AttributeError('Атрибут не найден')
#         return obj.__dict__[self._attr]
#
#     def __set__(self, obj, value):
#         if type(value) not in self._attrs:
#             raise TypeError('Некорректное значение')
#         obj.__dict__[self._attr] = value
#
#
# class Student:
#     name = TypeChecked(str)
#
# student = Student()
#
# try:
#     print(student.name)
# except AttributeError as e:
#     print(e)


# Класс RandomNumber

# class RandomNumber:
#     def __init__(self, start, end, cache=False):
#         self._start = start
#         self._end = end
#         self._cache = cache
#         self._val = None
#
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         if obj is None:
#             return self
#         if self._cache:
#             if self._val is None:
#                 self._val = random.randint(self._start, self._end)
#             return self._val
#         return random.randint(self._start, self._end)
#
#     def __set__(self, obj, value):
#         if obj not in self.__dict__:
#             raise AttributeError('Изменение невозможно')
#
#
# class MagicPoint:
#     x = RandomNumber(0, 5)
#     y = RandomNumber(0, 5)
#     z = RandomNumber(0, 5)
#
# magicpoint = MagicPoint()
#
# try:
#     magicpoint.x = 10
# except AttributeError as e:
#     print(e)


# Класс Versioned🌶️

class Versioned:
    def __set_name__(self, cls, attr):
        self._attr = attr
        self._ver = dict((attr, []))

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._attr not in obj.__dict__:
            raise AttributeError('Атрибут не найден')
        return obj.__dict__[self._attr]

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value
        if obj in self._ver:
            self._ver[obj].append(value)
        else:
            self._ver[obj] = [value]

    def get_version(self, obj, n):
        return self._ver[obj][n]

    def set_version(self, obj, n):
        obj.attr = self._ver[obj][n]


class Student:
    age = Versioned()


student = Student()

student.age = 18
student.age = 19

print(student.age)