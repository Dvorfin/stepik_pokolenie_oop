# 5.10 Хеширование объектов. Часть 2


# Класс ColoredPoint

# class ColoredPoint:
#     def __init__(self, x, y, color):
#         self._x = x
#         self._y = y
#         self._color = color
#
#     @property
#     def x(self):
#         return self._x
#
#
#     @property
#     def y(self):
#         return self._y
#
#     @property
#     def color(self):
#         return self._color
#
#     def __repr__(self):
#         return f"ColoredPoint({self.x}, {self.y}, '{self.color}')"
#
#     @property
#     def _fields(self):
#         return self.x, self.y, self.color
#
#     def __eq__(self, other):
#         if isinstance(other, ColoredPoint):
#             return self._fields == other._fields
#         return NotImplemented
#
#     def __hash__(self):
#         return hash(self._fields)
#
#
# point = ColoredPoint(1, 2, 'white')
#
# try:
#     point.color = 'black'
# except AttributeError as e:
#     print('Error')


# Класс Row🌶️

# class Row:
#     def __init__(self, **kwargs):
#         for k, v in kwargs.items():
#             object.__setattr__(self, k, v)
#
#     def __setattr__(self, key, value):
#         if key in self.__dict__:
#             raise AttributeError('Изменение значения атрибута невозможно')
#         else:
#             raise AttributeError('Установка нового атрибута невозможна')
#
#     def __delattr__(self, item):
#         raise AttributeError('Удаление атрибута невозможно')
#
#     def __repr__(self):
#         res = ', '.join(f"{k}={repr(v)}" for k,v in self.__dict__.items())
#         return f"Row({res})"
#
#     @property
#     def _fields(self):
#         return self.__dict__
#
#     def __eq__(self, other):
#         if isinstance(other, Row):
#             return tuple(self._fields.items()) == tuple(other._fields.items())
#         return NotImplemented
#
#     def __hash__(self):
#         items = self._fields.items()
#         items = tuple(items)
#         return hash(items)
#
#
# print()
# print([1,2,3] == [2,1,3])
# print()
#
# row1 = Row(a=1, b=2, c=3)
# row2 = Row(a=1, b=2, c=3)
# row3 = Row(b=2, c=3, a=1)
#
# print(row1 == row2)
# print(hash(row1) == hash(row2))
# print(row1 == row3)
# print(hash(row1) == hash(row3))