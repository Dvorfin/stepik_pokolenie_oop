# 7.5 Абстрактные классы, модуль abc

# Классы Average, Median и Harmonic

# from abc import ABC, abstractmethod
#
# class Middle(ABC):
#     @abstractmethod
#     def get_correct_user_votes(self):
#         pass
#
#     @abstractmethod
#     def get_correct_expert_votes(self):
#         pass
#
#     @abstractmethod
#     def get_average(self):
#         pass


# Классы ChessPiece, King и Knight

from abc import ABC, abstractmethod

# from abc import ABC, abstractmethod
#
#
# class ChessPiece(ABC):
#     def __init__(self, horizontal, vertical):
#         self.horizontal = horizontal
#         self.vertical = vertical
#
#     @abstractmethod
#     def can_move(self, col, row):
#         pass
#
#
# class King(ChessPiece):
#     def can_move(self, col, row):
#         return (ord(self.horizontal) - ord(col)) ** 2 + (self.vertical - row) ** 2 in (1, 2)
#
#
# class Knight(ChessPiece):
#     def can_move(self, col, row):
#         return (ord(self.horizontal) - ord(col)) ** 2 + (self.vertical - row) ** 2 == 5
#
#
# king = King('e', 3)
#
# print(king.can_move('e', 3))
# print(king.can_move('e', 4))
# print(king.can_move('b', 1))


# Классы Validator, Number и String

from abc import ABC, abstractmethod


class Validator(ABC):
    def __init__(self, attr):
        self._attr = attr

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if self._attr in obj.__dict__:
            return obj.__dict__[self._attr]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value

    def __delete__(self, obj):
        del obj.__dict__[self._attr]

    @abstractmethod
    def validate(self, *args):
        pass


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        super().__init__(self)
        self._minvalue = minvalue
        self._maxvalue = maxvalue

    def __set__(self, key, value):
        self.validate(value)

        super().__set__(key, value)

    # def __set_name__(self, owner, name):
    #     self.validate(name)
    #     super().__set_name__(self, name)

    __set_name__ = __set__

    # def __set_name__(self, cls, value):
    #     print(value)
    #     super().__set__(self, value)

    def validate(self, val):
        if isinstance(val, (int, float)):
            if self._minvalue:
                if val < self._minvalue:
                    raise ValueError(f'Устанавливаемое число должно быть больше или равно {self._minvalue}')
            if self._maxvalue:
                if val > self._maxvalue:
                    raise ValueError(f'Устанавливаемое число должно быть меньше или равно {self._maxvalue}')

            self._attr = val
        else:
            raise TypeError('Устанавливаемое значение должно быть числом')


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        super().__init__(self)
        self._minsize = minsize
        self._maxsize = maxsize
        self._predicate = predicate

    def __set__(self, key, value):
        self.validate(value)
        super().__set__(key, value)

    def validate(self, val):
        if isinstance(val, str):
            if self._minsize:
                if len(val) < self._minsize:
                    raise ValueError(f'Длина устанавливаемой строки должна быть больше или равна {self._minsize}')
                else:
                    if self._predicate:
                        if self._predicate(val):
                            self._attr = val
                        else:
                            raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')

            if self._maxsize:
                if len(val) > self._maxsize:
                    raise ValueError(f'Длина устанавливаемой строки должна быть меньше или равна {self._maxsize}')
                else:
                    if self._predicate:
                        if self._predicate(val):
                            self._attr = val
                        else:
                            raise ValueError('Устанавливаемая строка не удовлетворяет дополнительным условиям')

        else:
            raise TypeError('Устанавливаемое значение должно быть строкой')


# class PositiveNumber:
#     num = Number(0)


# positivenumber = PositiveNumber()
# positivenumber.num = 0
# print(positivenumber.num)
#
# try:
#     positivenumber.num = -1
# except ValueError as e:
#     print(e)


# Функции is_iterator() и is_iterable()

# from collections.abc import *
#
#
# def is_iterable(obj):
#     return isinstance(obj, Iterable)
#
#
# def is_iterator(obj):
#     return isinstance(obj, Iterator)
#
#
# print(is_iterable(123))
# print(is_iterable([1, 2, 3]))
# print(is_iterable((1, 2, 3)))
# print(is_iterable('123'))
# print(is_iterable(iter('123')))
# print(is_iterable(map(int, '123')))


# Класс CustomRange

# from collections.abc import Sequence
#
# class CustomRange(Sequence):
#     def __init__(self, *args):
#         self._data = []
#         for el in args:
#             if isinstance(el, str):
#                 a, b = map(int, el.split('-'))
#                 self._data.extend(range(a, b+1))
#             else:
#                 self._data.append(el)
#
#     def __getitem__(self, item):
#         if isinstance(item, int):
#             return self._data[item]
#
#     def __len__(self):
#         return len(self._data)
#
#
# customrange = CustomRange()
#
# print(len(customrange))
# print(*customrange)
# print(*reversed(customrange))


# Класс BitArray

# from collections.abc import Sequence
#
# class BitArray(Sequence):
#     def __init__(self, iterable=()):
#         self._data = [el for el in iterable]
#
#     def __str__(self):
#         return str(self._data)
#
#     __repr__ = __str__
#
#     def __len__(self):
#         return len(self._data)
#
#     def __getitem__(self, item):
#         if isinstance(item, (int, slice)):
#             return self._data[item]
#         return NotImplemented
#
#     def __invert__(self):
#         tmp = [0 if el else 1 for el in self._data]
#         return BitArray(tmp)
#
#     def __and__(self, other):
#         if isinstance(other, BitArray):
#             if len(self._data) == len(other._data):
#                 tmp = [el1 & el2 for el1, el2 in zip(self._data, other._data)]
#                 return BitArray(tmp)
#         return NotImplemented
#
#     def __or__(self, other):
#         if isinstance(other, BitArray):
#             if len(self._data) == len(other._data):
#                 tmp = [el1 or el2 for el1, el2 in zip(self._data, other._data)]
#                 return BitArray(tmp)
#         return NotImplemented
#
#
# data = [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0,
#         0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0]
#
# bitarray = BitArray(data)
#
# print(bitarray)
# data.extend([0, 0, 1, 0, 1, 1])
#
# print(data)
# print(bitarray)


# Класс DNA

from collections.abc import Sequence

class DNA(Sequence):
    def __init__(self, chain):
        self._data = list(chain)

    def __str__(self):
        return ''.join(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, item):
        if isinstance(item, (int, slice)):
            return self._data[item]
        else:
            return NotImplemented



# Класс SortedList

# from collections.abc import Sequence
#
#
# class SortedList(Sequence):
#     def __init__(self, iterable=()):
#         self._data = sorted(iterable)
#
#     def __getitem__(self, item):
#         if isinstance(item, (int, slice)):
#             return self._data[item]
#         else:
#             return NotImplementedError
#
#     def __setitem__(self, key, value):
#         raise NotImplementedError
#
#     def __len__(self):
#         return len(self._data)
#
#     def add(self, item):
#         self._data.append(item)
#         self._data.sort()
#
#     def discard(self, item):
#         self._data = [el for el in self._data if el != item]
#
#     def update(self, iterable):
#         self._data.extend(iterable)
#         self._data.sort()
#
#     def append(self, item):
#         raise NotImplementedError
#
#     def __repr__(self):
#         return f"SortedList({repr(self._data)})"
#
#     def __add__(self, other):
#         if isinstance(other, SortedList):
#             return SortedList(self._data + other._data)
#         else:
#             return NotImplemented
#
#     def __iadd__(self, other):
#         if isinstance(other, SortedList):
#             self._data.extend(other._data)
#             self._data.sort()
#             return self
#         else:
#             return NotImplemented
#
#     def __mul__(self, n):
#         if isinstance(n, int):
#             return SortedList(el for _ in range(n) for el in self._data)
#         else:
#             return NotImplemented
#
#     def __imul__(self, n):
#         if isinstance(n, int):
#             self._data[:] = [el for _ in range(n) for el in self._data]
#             self._data.sort()
#             return self
#         else:
#             return NotImplemented
#
#     def __delitem__(self, key):
#         del self._data[key]
#         self._data.sort()
#
#     def insert(self, *args):
#         raise NotImplementedError
#
#     def __reversed__(self, *args):
#         raise NotImplementedError
#
#     def reverse(self):
#         raise NotImplementedError
#
#     def extend(self, *args):
#         raise NotImplementedError
#
#
#
# numbers1 = SortedList([1, 3, 5])
# numbers2 = SortedList([2, 4])
#
# id1_numbers1 = id(numbers1)
# id1_numbers2 = id(numbers2)
#
# numbers1 += numbers2
# numbers2 *= 2
#
# id2_numbers1 = id(numbers1)
# id2_numbers2 = id(numbers2)
#
#
# print(id1_numbers1 == id2_numbers1)
# print(id1_numbers2 == id2_numbers2)
# print(3 in numbers1)