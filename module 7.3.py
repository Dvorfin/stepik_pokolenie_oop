# 7.3 Наследование. Часть 3


# Класс UpperPrintString

# class UpperPrintString(str):
#     def __str__(self):
#         return super().__str__().upper()
#
#
# s1 = UpperPrintString('beegeek')
# s2 = UpperPrintString('BeeGeek')
#
# print(s1)
# print(s2)


# Класс LowerString


# class LowerString(str):
#     def __new__(cls, obj=''):
#         instance = super().__new__(cls, str(obj).lower())
#         return instance
#
# print(LowerString(['Bee', 'Geek']))
# print(LowerString({'A': 1, 'B': 2, 'C': 3}))


# Класс FuzzyString

# class FuzzyString(str):
#     def __new__(cls, string=''):
#         instance = super().__new__(cls, str(string).lower())
#         return instance
#
#     def __eq__(self, other):
#         if isinstance(other, (FuzzyString, str)):
#             return self.upper() == other.upper()
#         else:
#             return NotImplemented
#
#     def __ne__(self, other):
#         if isinstance(other, (FuzzyString, str)):
#             return self.upper() != other.upper()
#         else:
#             return NotImplemented
#
#     def __lt__(self, other):
#         if isinstance(other, (FuzzyString, str)):
#             return self.upper() < other.upper()
#         else:
#             return NotImplemented
#
#     def __gt__(self, other):
#         if isinstance(other, (FuzzyString, str)):
#             return self.upper() > other.upper()
#         else:
#             return NotImplemented
#
#     def __le__(self, other):
#         if isinstance(other, (FuzzyString, str)):
#             return self.upper() <= other.upper()
#         else:
#             return NotImplemented
#
#     def __ge__(self, other):
#         if isinstance(other, (FuzzyString, str)):
#             return self.upper() >= other.upper()
#         else:
#             return NotImplemented
#
#     def __contains__(self, item):
#         if isinstance(item, (FuzzyString, str)):
#             return self.upper() in item.upper()
#         else:
#             return NotImplemented
#
#
# s = FuzzyString('BeeGeek')
#
# print(s != 'BEEGEEK')
# print(s == 'BEEGEEK')
# print(s != 'beegeek')
# print(s == 'beegeek')
# print(s >= 'BEEGEEK')
# print(s <= 'BEEGEEK')
# print(s > 'BEEGEEK')
# print(s < 'BEEGEEK')



# Класс TitledText

# class TitledText(str):
#     def __new__(cls, content, text_title):
#         instance = super().__new__(cls, content)
#         instance.text_title = text_title
#         return instance
#
#     def title(self):
#         return self.text_title
#
#
# titled = TitledText('Сreate a class Soda', 'Homework')
#
# print(titled)
# print(titled.title())
# print(issubclass(TitledText, str))


# Класс SuperInt

# class SuperInt(int):
#     def __new__(cls, val):
#         instance = super().__new__(cls, val)
#         return instance
#
#     def repeat(self, n=2):
#         tmp = str(self) * n
#         tmp = tmp.replace('-', '')
#         if self < 0:
#             tmp = '-' + tmp
#         return SuperInt(tmp)
#
#     def to_bin(self):
#         return "{0:b}".format(self)
#
#     def next(self):
#         return SuperInt(self + 1)
#
#     def prev(self):
#         return SuperInt(self - 1)
#
#     def __iter__(self):
#         yield from map(lambda x: SuperInt(x), str(abs(self)))
#
#
# superint1 = SuperInt(1337)
# superint2 = SuperInt(-2077)
#
# print(*superint1)
# print(*superint2)


# Класс RoundedInt

# class RoundedInt(int):
#     def __new__(cls, num, even=True):
#         if even:
#             instance = super().__new__(cls, num + num%2)
#         else:
#             instance = super().__new__(cls, num + (1-num%2))
#         return instance
#
#
# print(RoundedInt(7))
# print(RoundedInt(8))
# print(RoundedInt(7, False))
# print(RoundedInt(8, False))


# Класс AdvancedTuple

# class AdvancedTuple(tuple):
#     def __new__(cls, *args, **kwargs):
#         instance = super().__new__(cls, *args)
#         return instance
#
#     def __add__(self, other):
#         if isinstance(other, (AdvancedTuple, tuple)) or other.__iter__:
#             return AdvancedTuple(tuple(self) + tuple(other))
#         else:
#             return NotImplemented
#
#     def __radd__(self, other):
#         if isinstance(other, (AdvancedTuple, tuple)) or other.__iter__:
#             return AdvancedTuple(tuple(other) + tuple(self))
#         else:
#             return NotImplemented
#
#     def __iadd__(self, other):
#         if isinstance(other, (AdvancedTuple, tuple)) or other.__iter__:
#             return AdvancedTuple(tuple(self) + tuple(other))
#
#
# advancedtuple = AdvancedTuple([1, 2, 3])
#
# advancedtuple += [4, 5]
# advancedtuple += iter([6, 7, 8])
# print(advancedtuple)
# print(type(advancedtuple))


# Класс ModularTuple

# class ModularTuple(tuple):
#     def __new__(cls, iterable=(), size=100, *args, **kwargs):
#         instance = super().__new__(cls, map(lambda x: x % size, iterable))
#         return instance
#
#
# modulartuple = ModularTuple([1, 2, 3, 4, 5], 2)
#
# print(modulartuple)