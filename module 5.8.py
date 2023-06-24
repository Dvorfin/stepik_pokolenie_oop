# 5.8 Работа с атрибутами объектов

# https://music.yandex.ru/album/18863108/track/93563853

# Класс Item

# class Item:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#
#     def __getattribute__(self, name):
#         if name == 'total':
#             return object.__getattribute__(self, 'price') * object.__getattribute__(self, 'quantity')
#         elif name == 'name':
#             return object.__getattribute__(self, name).title()
#         return object.__getattribute__(self, name)
#
#
# fruit = Item('banana', 15, 5)
#
# print(fruit.name)
# print(fruit.total)


# Класс Logger

# class Logger:
#     def __setattr__(self, name, value):
#         print(f'Изменение значения атрибута {name} на {value}')
#         self.__dict__[name] = value
#
#     def __delattr__(self, name):
#         print(f'Удаление атрибута {name}')
#         del self.__dict__[name]
#
#
# obj = Logger()
#
# obj.attr = 1
# del obj.attr


# Класс Ord

# class Ord:
#     def __getattr__(self, item):
#         return ord(item)
#
# obj = Ord()
#
# print(obj.a)
# print(obj.b)


# Класс DefaultObject

# class DefaultObject:
#     def __init__(self, default=None, **kwargs):
#         self.default = default
#         for k, v in kwargs.items():
#             setattr(self, k, v)
#
#     def __getattr__(self, item):
#         return self.default
#
#
# god = DefaultObject(name='Ares', mythology='greek')
#
# print(god.name)
# print(god.mythology)
# print(god.age)


# Класс NonNegativeObject

# class NonNegativeObject:
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             if type(v) in (int, float):
#                 setattr(self, k, abs(v))
#             else:
#                 setattr(self, k, v)
#
#
# point = NonNegativeObject(x=1, y=-2, z=0, color='black')
#
# print(point.x)
# print(point.y)
# print(point.z)
# print(point.color)


# Класс AttrsNumberObject

# class AttrsNumberObject:
#     def __init__(self, **kwargs):
#         self.attrs_num = 0
#         for k, v in kwargs.items():
#             setattr(self, k, v)
#
#     def __setattr__(self, key, value):
#         self.__dict__[key] = value
#         self.__dict__['attrs_num'] += 1
#
#     def __getattr__(self, item):
#         return self.__dict__['attrs_num']
#
#     def __delattr__(self, item):
#         del self.__dict__[item]
#         self.__dict__['attrs_num'] -= 1
#
#
# music_group = AttrsNumberObject()
#
# print(music_group.attrs_num)


# Класс Const

# class Const:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)
#
#     def __delattr__(self, item):
#         raise AttributeError('Удаление атрибута невозможно')
#
#     def __setattr__(self, key, value):
#         if key in self.__dict__:
#             raise AttributeError('Изменение значения атрибута невозможно')
#         else:
#             self.__dict__[key] = value
#
# videogame = Const(name='Dicso Elysium')
#
# try:
#     videogame.name = 'Half-Life: Alyx'
# except AttributeError as e:
#     print(e)


# Класс ProtectedObject

# class ProtectedObject:
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             object.__setattr__(self, k, v)
#
#     def __getattribute__(self, item):
#         if item.startswith('_'):
#             raise AttributeError('Доступ к защищенному атрибуту невозможен')
#         else:
#             return object.__getattribute__(self, item)
#
#     def __setattr__(self, key, value):
#         if key.startswith('_'):
#             raise AttributeError('Доступ к защищенному атрибуту невозможен')
#         else:
#             object.__setattr__(self, key, value)
#
#     def __delattr__(self, item):
#         if item.startswith('_'):
#             raise AttributeError('Доступ к защищенному атрибуту невозможен')
#         else:
#             object.__delattr__(self, item)
#
#
# user = ProtectedObject(login='PG_kamiya', _password='alreadybanned')
#
#
#
# try:
#     print(user.login)
#     print(user._password)
# except AttributeError as e:
#     print(e)