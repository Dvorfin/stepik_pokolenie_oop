# 7.4 Наследование. Часть 4

# Класс DefaultList

# from collections import UserList
# import copy
#
# class DefaultList(UserList):
#     def __init__(self, iterable=list, default=None):
#         super().__init__(iterable)
#         self.default = default
#
#     def __getitem__(self, item):
#         try:
#             return self.data[item]
#         except:
#             return self.default
#
#
# defaultlist = DefaultList([1, 2, 3])
#
# print(defaultlist[0])
# print(defaultlist[-1])
# print(defaultlist[100])
# print(defaultlist[-100])


# Класс EasyDict

# class EasyDict(dict):
#     def __getitem__(self, item):
#         if item in self:
#             return super().__getitem__(item)
#
#     def __getattr__(self, item):
#         return super().__getitem__(item)
#
#
# easydict = EasyDict({'name': 'Timur', 'city': 'Moscow'})
#
# print(easydict['name'])
# print(easydict.city)


# Класс TwoWayDict

# from collections import UserDict
#
# class TwoWayDict(UserDict):
#     def __setitem__(self, key, value):
#         self.data.__setitem__(key, value)
#         self.data.__setitem__(value, key)
#
#
# twowaydict = TwoWayDict({'apple': 1})
#
# twowaydict['banana'] = 2
#
# print(twowaydict['apple'])
# print(twowaydict[1])
# print(twowaydict['banana'])
# print(twowaydict[2])


# Класс AdvancedList

# class AdvancedList(list):
#     def join(self, sep=' '):
#         return f"{sep}".join(map(str, self))
#
#     def map(self, func):
#         self[:] = [func(el) for el in self]
#
#     def filter(self, func):
#         self[:] = [el for el in self if func(el)]
#
#
# advancedlist = AdvancedList([1, 2, 3, 4, 5])
#
# advancedlist.filter(lambda x: x % 2 == 0)
#
# print(advancedlist)


# Класс NumberList

# from collections import UserList
#
# class NumberList(UserList):
#     def __init__(self, iterable=()):
#         if all(map(lambda x: isinstance(x, (int, float)), iterable)):
#             super().__init__(iterable)
#         else:
#             raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
#
#     def __add__(self, other):
#         if all(map(lambda x: isinstance(x, (int, float)), other)):
#             return NumberList(self.data + other)
#         else:
#             raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
#
#     __iadd__ = __add__
#
#     def append(self, item):
#         if isinstance(item, (int, float)):
#             self.data.append(item)
#         else:
#             raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
#
#     def extend(self, other):
#         if all(map(lambda x: isinstance(x, (int, float)), other)):
#             self.data.extend(other)
#         else:
#             raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
#
#     def insert(self, index, item):
#         if isinstance(item, (int, float)):
#             self.data.insert(index, item)
#         else:
#             raise TypeError('Элементами экземпляра класса NumberList должны быть числа')
#
#
#
# numberlist = NumberList([1, 2, 3])
#
# try:
#     numberlist.append('4')
# except TypeError as error:
#     print(error)


# Класс ValueDict

# class ValueDict(dict):
#     def key_of(self, value):
#         for k, v in self.items():
#             if v == value:
#                 return k
#         else:
#             return None
#
#     def keys_of(self, value):
#         tmp = []
#         for k, v in self.items():
#             if v == value:
#                 tmp.append(k)
#         return tmp
#
# countries = {'Monaco': 'Monaco', 'Iceland': 'Reykjavik', 'Kenya': 'Nairobi', 'Kazakhstan': 'Nur-Sultan',
#              'Mali': 'Bamako', 'Colombia': 'Bogota', 'Finland': 'Helsinki', 'Costa Rica': 'San Jose',
#              'Cuba': 'Havana', 'France': 'Paris', 'Gabon': 'Libreville', 'Liberia': 'Monrovia',
#              'Angola': 'Luanda', 'India': 'New Delhi', 'Canada': 'Ottawa', 'Australia': 'Canberra'}
#
# valuedict = ValueDict(countries)
#
# print(valuedict.key_of('Moscow'))
# print(*valuedict.keys_of('Washington'))


# Класс BirthdayDict

# from collections import UserDict
#
# class BirthdayDict(UserDict):
#     def __setitem__(self, key, value):
#         if value in self.data.values():
#             print(f"Хей, {key}, не только ты празднуешь день рождения в этот день!")
#         super().__setitem__(key, value)
#
#     #def __add__(self, other):
#
#     __add__ = __setitem__
#
#
# from datetime import date
#
# birthdaydict = BirthdayDict()
#
# birthdaydict['Боб'] = date(1987, 6, 15)
# birthdaydict['Том'] = date(1984, 7, 15)
# birthdaydict['Мария'] = date(1987, 6, 15)


# Класс MutableString

# from collections import UserString
#
# class MutableString(UserString):
#     def lower(self):
#         self.data = self.data.lower()
#
#     def upper(self):
#         self.data = self.data.upper()
#
#     def sort(self, key=None, reverse=False):
#         tmp = sorted(self.data, key=key, reverse=reverse)
#         self.data = ''.join(map(str, tmp))
#
#     def __getitem__(self, index):
#         tmp = list(self.data)
#         if isinstance(index, slice):
#             tmp = tmp[index]
#             return MutableString(''.join(tmp))
#         return tmp[index]
#
#     def __setitem__(self, key, value):
#         tmp = list(self.data)
#         tmp[key] = value
#         self.data = ''.join(tmp)
#
#     def __delitem__(self, key):
#         tmp = list(self.data)
#         del tmp[key]
#         self.data = ''.join(tmp)
#
#     def __add__(self, other):
#         if isinstance(other, MutableString):
#             return MutableString(self.data + other.data)
#         else:
#             return NotImplemented
#
# mutablestring = MutableString('beegeek')
#
# print(mutablestring)
# mutablestring[0] = 'B'
# mutablestring[-4] = 'G'
# print(mutablestring)