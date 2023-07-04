# 8.4 Декораторы. Часть 1

import functools

class do_twice:
    def __init__(self, func):
        functools.update_wrapper(self, func)  # сохранение информации о декорируемой функции
        self.func = func

    def __call__(self, *args, **kwargs):
        for _ in range(2):
            value = self.func(*args, **kwargs)
        return value



# Декоратор @reverse_args

# import functools
#
#
# class reverse_args:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         return self.func(*reversed(args), **kwargs)
#
#
# @reverse_args
# def concat(a, b, c):
#     return a + b + c


#  Декоратор @limited_calls

# import functools
#
#
# class MaxCallsException(Exception):
#     pass
#
#
# class limited_calls:
#     def __init__(self, n):
#         self.n = n
#
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             if self.n == 0:
#                 raise MaxCallsException('Превышено максимальное количество вызовов')
#             value = func(*args, **kwargs)
#             self.n -= 1
#             return value
#         return wrapper
#
#
# @limited_calls(3)
# def add(a, b):
#     return a + b
#
#
# print(add(1, 2))
# print(add(3, 4))
# print(add(5, 6))
#
# try:
#     print(add())
# except MaxCallsException as e:
#     print(e)


# Декоратор @takes_numbers

# import functools
#
#
# class takes_numbers:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         elements = list(args) + list(kwargs.values())
#         if all(map(lambda x: isinstance(x, (int, float)), elements)):
#             return self.func(*args, **kwargs)
#         else:
#             raise TypeError('Аргументы должны принадлежать типам int или float')
#
#
# @takes_numbers
# def mul(a, b):
#     return a * b
#
#
# try:
#     print(mul(1, '2'))
# except TypeError as error:
#     print(error)


# Декоратор @returns

# import functools
#
#
# class returns:
#     def __init__(self, datatype):
#         self.datatype = datatype
#
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             res = func(*args, **kwargs)
#             if type(res) == self.datatype:
#                 return res
#             raise TypeError
#         return wrapper
#
#
# @returns(int)
# def add(a, b):
#     return a + b
#
# try:
#     print(add('1', '2'))
# except Exception as error:
#     print(type(error))


# Декоратор @exception_decorator

# import functools
#
#
# class exception_decorator:
#     def __init__(self, func):
#         functools.update_wrapper(self, func)
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         try:
#             res = self.func(*args, **kwargs)
#             return res, None
#         except BaseException as error:
#             return None, type(error)
#
#
# @exception_decorator
# def func(x):
#     return 2 * x + 1
#
#
# print(func(1))
# print(func('bee'))


# Декоратор @ignore_exception

# import functools
#
#
# class ignore_exception:
#     def __init__(self, *args):
#         self.exceptions = list(args)
#
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             try:
#                 res = func(*args, **kwargs)
#                 return res
#             except Exception as e:
#                 if type(e) in self.exceptions:
#                     print(f"Исключение {type(e).__name__} обработано")
#                 else:
#                     raise e
#         return wrapper
#
#
# @ignore_exception(ZeroDivisionError, TypeError, ValueError)
# def func(x):
#     return 1 / x
#
#
# func(0)


# Декоратор @type_check

# import functools
#
#
# class type_check:
#     def __init__(self, types):
#         self.types = types
#
#     def __call__(self, func):
#         @functools.wraps(func)
#         def wrapper(*args, **kwargs):
#             for el, tp in zip(args, self.types):
#                 if not isinstance(el, tp):
#                     raise TypeError
#             return func(*args, **kwargs)
#         return wrapper
#
#
# @type_check([int, int])
# def add(a, b):
#     return a + b
#
# try:
#     print(add(1, '2'))
# except Exception as error:
#     print(type(error))