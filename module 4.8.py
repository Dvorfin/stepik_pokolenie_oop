# 4.8 Декоратор @singledispatchmethod

# Класс Processor

# from functools import singledispatchmethod
#
# class Processor:
#     @singledispatchmethod
#     @staticmethod
#     def process(arg):
#         raise TypeError('Аргумент переданного типа не поддерживается')
#
#     @process.register(int)
#     @staticmethod
#     def _from_int(arg):
#         return arg * 2
#
#     @process.register(float)
#     @staticmethod
#     def _from_float(arg):
#         return arg * 2
#
#     @process.register(str)
#     @staticmethod
#     def _from_str(arg):
#         return arg.upper()
#
#     @process.register(list)
#     @staticmethod
#     def _from_list(arg):
#         return sorted(arg)
#
#     @process.register(tuple)
#     @staticmethod
#     def _from_tuple(arg):
#         return tuple(sorted(arg))
#
#
# print(Processor.process(10))
# print(Processor.process(5.2))
# print(Processor.process('hello'))
# print(Processor.process((4, 3, 2, 1)))
# print(Processor.process([3, 2, 1]))


# Класс Negator

# from functools import singledispatchmethod
#
# class Negator:
#     @singledispatchmethod
#     @staticmethod
#     def neg(arg):
#         raise TypeError('Аргумент переданного типа не поддерживается')
#
#     @neg.register(int)
#     @neg.register(float)
#     @staticmethod
#     def _from_int_float(arg):
#         return -1*arg
#
#     @neg.register(bool)
#     @staticmethod
#     def _from_bool(arg):
#         return not arg
#
# print(Negator.neg(11.0))
# print(Negator.neg(-12))
# print(Negator.neg(True))
# print(Negator.neg(False))


# Класс Formatter

# from functools import singledispatchmethod
#
# class Formatter:
#     @singledispatchmethod
#     @staticmethod
#     def format(arg):
#         raise TypeError('Аргумент переданного типа не поддерживается')
#
#     @format.register(int)
#     @staticmethod
#     def _from_int(arg):
#         print(f'Целое число: {arg}')
#
#     @format.register(float)
#     @staticmethod
#     def _from_float(arg):
#         print(f'Вещественное число: {arg}')
#
#     @format.register(list)
#     @staticmethod
#     def _from_list(arg):
#         if isinstance(arg[0], int):
#             print(f'Элементы списка: ' + ', '.join(map(str, arg)))
#         else:
#             print(f'Элементы списка: ' + ', '.join(arg))
#
#     @format.register(tuple)
#     @staticmethod
#     def _from_tuple(arg):
#         if isinstance(arg[0], int):
#             print(f'Элементы кортежа: ' + ', '.join(map(str, arg)))
#         else:
#             print(f'Элементы кортежа: ' + repr(arg)[1:-1])
#
#     @format.register(dict)
#     @staticmethod
#     def _from_dict(arg):
#         print(f'Пары словаря: ' + ', '.join([repr(el) for el in arg.items()]))
#
#
# Formatter.format([10, 20, 30, 40, 50])
# Formatter.format(([1, 3], [2, 4, 6]))
# Formatter.format({'Cuphead': 1, 'Mugman': 3})
# Formatter.format({1: 'one', 2: 'two'})
# Formatter.format({1: True, 0: False})


# Класс BirthInfo 🌶️

# from functools import singledispatchmethod
# from datetime import date, timedelta, datetime
#
# class BirthInfo:
#     @singledispatchmethod
#     def __init__(self, d):
#         raise TypeError('Аргумент переданного типа не поддерживается')
#
#     @__init__.register(date)
#     def _from_datetime(self, d):
#         self.birth_date = d
#
#     @__init__.register(str)
#     def _from_str(self, d):
#         self.birth_date = date.fromisoformat(d)
#
#     @__init__.register(list)
#     @__init__.register(tuple)
#     def _from_list_tuple(self, d):
#         self.birth_date = date(*d)
#
#     @property
#     def age(self):
#         return current_age(self.birth_date, date.today())
#
#
# birthinfo1 = BirthInfo('2020-09-18')
# birthinfo2 = BirthInfo(date(2010, 10, 10))
# birthinfo3 = BirthInfo([2016, 1, 1])
#
# print(birthinfo1.birth_date)
# print(birthinfo2.birth_date)
# print(birthinfo3.birth_date)