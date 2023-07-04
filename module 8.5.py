# 8.5 Декораторы. Часть 2

import functools


def count_instances(cls):
    old_init = cls.__init__
    cls.count = 0  # счетчик созданных экземпляров декорируемого класса

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.count += 1  # увеличиение счетчика на единицу

    cls.__init__ = new_init
    return cls


# Декоратор @track_instances

# import functools
#
#
# def track_instances(cls):
#     old_init = cls.__init__
#     cls.instances = []
#
#     @functools.wraps(old_init)
#     def new_init(self, *args, **kwargs):
#         old_init(self, *args, **kwargs)
#         cls.instances.append(self)
#
#     cls.__init__ = new_init
#     return cls
#
#
# @track_instances
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def __repr__(self):
#         return f'Person({self.name!r})'
#
#
# obj1 = Person('object 1')
# obj2 = Person('object 2')
#
# print(Person.instances)


# Декоратор @add_attr_to_class

# import functools
#
#
# def add_attr_to_class(**kwargs):
#     def wrapper(cls):
#         for k, v in kwargs.items():
#             setattr(cls, k, v)
#         return cls
#     return wrapper
#
#
# @add_attr_to_class(first_attr=1, second_attr=2)
# class MyClass:
#     pass
#
# print(MyClass.first_attr)
# print(MyClass.second_attr)


# Декоратор @jsonattr

# import functools
# import json
#
# def jsonattr(filename):
#     def wrapper(cls):
#         with open(filename, 'r', encoding='utf-8') as file:
#             data = json.load(file)
#             for k, v in data.items():
#                 setattr(cls, k, v)
#         return cls
#     return wrapper
#
#
# with open('test.json', 'w') as file:
#     file.write('{"x": 1, "y": 2}')
#
#
# @jsonattr('test.json')
# class MyClass:
#     pass
#
#
# print(MyClass.x)
# print(MyClass.y)


# Декоратор @singleton

# import functools
#
#
# def singleton(cls):
#     old_new = cls.__new__
#     cls._instance = None
#
#     @functools.wraps(old_new)
#     def new_new(*args, **kwargs):
#         if cls._instance is None:
#             cls._instance = object.__new__(cls)
#         return cls._instance
#
#     cls.__new__ = new_new
#
#     return cls
#
#
# @singleton
# class MyClass:
#     pass
#
#
# obj1 = MyClass()
# obj2 = MyClass()
#
# print(obj1 is obj2)


# Декоратор @snake_case

# import functools
# from inflection import *
#
#
# def snake_case(attrs=False):
#
#     def wrapper(cls):
#         cls_attrs = cls.__dict__
#         to_add = dict()
#         to_dell = []
#
#         for atr, v in cls_attrs.items():
#             if atr.startswith('__'):
#                 continue
#
#             if attrs:
#                 if not callable(v):
#                     to_add[underscore(atr)] = v
#                     to_dell.append(atr)
#                     continue
#             if callable(v):
#                 to_add[underscore(atr)] = v
#                 to_dell.append(atr)
#
#         for atr in to_dell:
#             delattr(cls, atr)
#
#         for k, v in to_add.items():
#
#             setattr(cls, k, v)
#
#         return cls
#     return wrapper
#
#
# @snake_case()
# class MyClass:
#     FirstAttr = 1
#
#     def FirstMethod(self):
#         return 1
#
#
# print(MyClass.__dict__)
# obj = MyClass()
#
# print(MyClass.FirstAttr)
# print(obj.first_method())


# Декоратор @auto_repr🌶️

# import functools
#
#
# def auto_repr(args, kwargs):
#
#     def wrapper(cls):
#         def rep(self):
#             res = f"{cls.__name__}("
#
#             if args:
#                 res += ', '.join(map(repr, (getattr(self, arg) for arg in args)))
#                 if kwargs:
#                     res += ', '
#                     res += ', '.join(f"{k}={repr(self.__dict__[k])}" for k in kwargs)
#             elif kwargs:
#                 res += ', '.join(f"{k}={repr(self.__dict__[k])}" for k in kwargs)
#
#             res += ')'
#
#             return res
#         setattr(cls, '__repr__', rep)
#         return cls
#     return wrapper
#
#
#
# @auto_repr(args=['name', 'surname'], kwargs=[])
# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#
# person = Person('Gvido', 'van Rossum')
#
# print(person)


# Декоратор @limiter🌶️🌶️

def limiter():