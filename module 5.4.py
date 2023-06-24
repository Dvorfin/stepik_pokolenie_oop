# 5.4 Унарные операторы и функции


# Класс ReversibleString

# class ReversibleString:
#     def __init__(self, string):
#         self.string = string
#
#     def __str__(self):
#         return f"{self.string}"
#
#     def __pos__(self):
#         return ReversibleString(self.string)
#
#     def __neg__(self):
#         return ReversibleString(self.string[::-1])
#
# string = ReversibleString('python')
#
# print(string)
# print(-string)


# Класс Money

# class Money:
#     def __init__(self, amount):
#         self.amount = amount
#
#     def __str__(self):
#         return f"{self.amount} руб."
#
#     def __pos__(self):
#         if self.amount < 0:
#             return Money(-self.amount)
#         return Money(self.amount)
#
#     def __neg__(self):
#         if self.amount < 0:
#             return Money(self.amount)
#         return Money(-self.amount)
#
# money = Money(-100)
#
# print(money)
# print(+money)
# print(-money)


# Класс Vector

# class Vector:
#     def __init__(self,  x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def __pos__(self):
#         return Vector(self.x, self.y)
#
#     def __neg__(self):
#         return Vector(-self.x, -self.y)
#
#     def __abs__(self):
#         return (self.x ** 2 + self.y ** 2) ** 0.5
#
#
# vector = Vector(3, -4)
#
# print(+vector)
# print(-vector)
# print(abs(vector))


# Класс ColoredPoint

# class ColoredPoint:
#     def __init__(self, x, y, color=(0, 0, 0)):
#         self.x = x
#         self.y = y
#         self.color = color
#
#     def __repr__(self):
#         return f"ColoredPoint({self.x}, {self.y}, {self.color})"
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#     def __pos__(self):
#         return ColoredPoint(self.x, self.y, self.color)
#
#     def __neg__(self):
#         return ColoredPoint(-1 * self.x, -1 * self.y, self.color)
#
#     def __invert__(self):
#         return ColoredPoint(self.y, self.x, tuple(map(lambda x: 255 - x, self.color)))
#
#
# point1 = ColoredPoint(2, -3)
# point2 = ColoredPoint(10, 20, (34, 45, 67))
# point2 = ~point2
# print(point1.color)
# print(point2.color)


# Класс Matrix 🌶️🌶️
# import copy
#
#
# class Matrix:
#     def __init__(self, rows, cols, value=0):
#         self.rows = rows
#         self.cols = cols
#         self.value = value
#         self.matrix = [[value]*cols for _ in range(rows)]
#
#     def get_value(self, row, col):
#         return self.matrix[row][col]
#
#     def set_value(self, row, col, value):
#         self.value = value
#         self.matrix[row][col] = value
#
#     def __repr__(self):
#         return f"Matrix({self.rows}, {self.cols})"
#
#     def __str__(self):
#         res = ''
#         for row in self.matrix:
#             res += ' '.join(map(str, row)) + '\n'
#         return res.strip()
#
#     def __pos__(self):
#         return Matrix(self.rows, self.cols, self.value)
#
#     def __neg__(self):
#         new = Matrix(self.rows, self.cols, self.value)
#         new.matrix = [list(map(lambda x: -x, r)) for r in self.matrix]
#         return new
#
#     def __invert__(self):
#         new = Matrix(self.cols, self.rows, self.value)
#         for r in range(self.rows):
#             for c in range(self.cols):
#                 new.set_value(c, r, self.get_value(r, c))
#         return new
#
#     def __round__(self, n=None):
#         new = Matrix(self.rows, self.cols, self.value)
#         prev = copy.deepcopy(self.matrix)
#         if n is None:
#             new.matrix = [list(map(round, r)) for r in prev]
#             return new
#         new.matrix = [[round(c, n) for c in r] for r in prev]
#         return new
#
#
# matrix = Matrix(5, 10)
#
# floats = [[7125.900408, 633.354471, -9237.8575119, 2865.3825158, 5509.2609336, 8712.260779, 8317.523947, 2512.4736075,
#            -3087.5496014, 3861.68814],
#           [-7852.451832, 376.465911, -8142.7867326, -6921.8371407, 3735.7516227, -3322.8019034, 7115.79968,
#            -8949.9313078, -7032.4347679, -5217.8236385],
#           [-7817.9657992, -4319.716346, -1038.6294521, -2959.8970273, -9263.5713405, 9358.607686, 1429.6576196,
#            -9484.68116, 639.6343972, 3444.9938213],
#           [-2844.2405153, -2078.2441427, 6812.1367017, 112.3910618, -1116.8662449, 5042.7026276, -5981.6930342,
#            4370.9173164, -8851.7648474, 8990.6896422],
#           [90.8102435, 5256.6137481, -9743.8477321, -131.5501688, -5920.5976176, 4963.8336619, -4907.3622526,
#            8531.2015615, -244.3630074, 3421.8817151]]
#
# for r in range(5):
#     for c in range(10):
#         matrix.set_value(r, c, floats[r][c])
#
# print(matrix)
# print()
# print(~matrix)
# print()
# print(round(matrix, 2))
# print()
# print(-matrix)


