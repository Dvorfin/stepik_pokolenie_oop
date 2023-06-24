# 5.5 Арифметические операции

# Класс FoodInfo

# class FoodInfo:
#     def __init__(self, proteins, fats, carbohydrates):
#         self.proteins = proteins
#         self.fats = fats
#         self.carbohydrates = carbohydrates
#
#     def __repr__(self):
#         return f"FoodInfo({self.proteins}, {self.fats}, {self.carbohydrates})"
#
#     def __add__(self, other):
#         if isinstance(other, FoodInfo):
#             return FoodInfo(self.proteins + other.proteins, self.fats + other.fats, self.carbohydrates + other.carbohydrates)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return FoodInfo(*map(lambda attr: attr * other, self.__dict__.values()))
#         return NotImplemented
#
#     def __truediv__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return FoodInfo(*map(lambda attr: attr / other, self.__dict__.values()))
#         return NotImplemented
#
#     def __floordiv__(self, other):
#         if isinstance(other, int) or isinstance(other, float):
#             return FoodInfo(*map(lambda attr: attr // other, self.__dict__.values()))
#         return NotImplemented
#
#
#
# pfc = [(751.26, 778.77, 947.51), (597.41, 508.5, 532.96), (800.55, 617.5, 525.14), (741.99, 785.53, 664.71),
#        (525.69, 892.41, 541.41), (888.8, 802.56, 868.78), (609.65, 855.43, 949.44), (705.25, 592.28, 738.72),
#        (514.88, 617.22, 557.5), (948.62, 938.7, 817.17), (783.98, 628.32, 686.38), (894.9, 815.81, 715.19),
#        (586.79, 826.68, 637.5), (670.53, 683.69, 841.56), (583.9, 607.34, 853.35), (954.67, 950.76, 822.19),
#        (718.94, 658.12, 537.2), (556.53, 686.17, 622.61), (699.8, 872.49, 908.3), (622.3, 920.97, 801.17)]
#
# FoodInfo.__round__ = lambda instance: FoodInfo(
#     round(instance.proteins, 2),
#     round(instance.fats, 2),
#     round(instance.carbohydrates, 2)
# )
#
# food1 = FoodInfo(1000, 2000, 3000)
# for p, f, c in pfc:
#     food2 = FoodInfo(p, f, c)
#     add = food1 + food2
#     mul = food1 * p
#     truediv = food1 // c
#     print(round(add), round(mul), round(truediv))


# Класс Vector

# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
#     def __add__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return NotImplemented
#
#     def __sub__(self, other):
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x * other, self.y * other)
#         return NotImplemented
#
#     def __rmul__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x * other, self.y * other)
#         return NotImplemented
#
#     def __truediv__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x / other, self.y / other)
#         return NotImplemented
#
#     def __rtruediv__(self, other):
#         if isinstance(other, (int, float)):
#             return Vector(self.x / other, self.y / other)
#         return NotImplemented
#
#
# a = Vector(3, 4)
#
# print(a * 2)
# print(2 * a)
# print(a / 2)


# Класс SuperString

# class SuperString:
#     def __init__(self, string=''):
#         self.string = string
#
#     def __str__(self):
#         return self.string
#
#     def __add__(self, other):
#         if isinstance(other, SuperString):
#             return SuperString(self.string + other.string)
#         return NotImplemented
#
#     def __mul__(self, other):
#         if isinstance(other, int):
#             return SuperString(self.string * other)
#         return NotImplemented
#
#     def __rmul__(self, other):
#         return self.__mul__(other)
#
#     def __truediv__(self, other):
#         if isinstance(other, int):
#             return SuperString(self.string[0:len(self.string) // other])
#         return NotImplemented
#
#     def __lshift__(self, other):
#         if isinstance(other, int):
#             if len(self.string) <= other:
#                 return SuperString()
#             return SuperString(self.string[0:len(self.string) - other])
#         return NotImplemented
#
#     def __rshift__(self, other):
#         if isinstance(other, int):
#             if len(self.string) <= other:
#                 return SuperString()
#             return SuperString(self.string[other:])
#         return NotImplemented
#
#
# s = SuperString('beegeek')
# for i in range(9):
#     print(f'{s} << {i} =', s << i)


# Класс Time

# class Time:
#     @staticmethod
#     def convert_hours(h, m):
#         return h % 24 + m // 60
#
#     @staticmethod
#     def convert_min(m):
#         return m % 60
#
#     def __init__(self, hours, minutes):
#         self.hours = Time.convert_hours(hours, minutes)
#         self.minutes = Time.convert_min(minutes)
#
#     def __str__(self):
#         if len(str(self.hours)) != 2:
#             h = '0' + str(self.hours)
#         else:
#             h = str(self.hours)
#         if len(str(self.minutes)) != 2:
#             m = '0' + str(self.minutes)
#         else:
#             m = str(self.minutes)
#         return f"{h}:{m}"
#
#     def __add__(self, other):
#         if isinstance(other, Time):
#             return Time(self.hours + other.hours, self.minutes + other.minutes)
#         return NotImplemented
#
#     def __iadd__(self, other):
#         if isinstance(other, Time):
#             self.hours = Time.convert_hours(Time.convert_hours(other.hours, other.minutes) + self.hours, 0)
#             self.minutes += Time.convert_min(other.minutes)
#             return self
#         return NotImplemented
#
#
# time1 = Time(2, 30)
# time2 = Time(3, 10)
#
# time1 += time2
#
# print(time1)
# print(time2)
#
# t = Time(22, 0)
# t += Time(3, 0)
# print(t)


# Класс Queue 🌶️

# class Queue:
#     def __init__(self, *args):
#         self.queue = list(args)
#
#     def __str__(self):
#         return ' -> '.join(map(str, self.queue))
#
#     def add(self, *other):
#         self.queue += list(other)
#
#     def pop(self):
#         if self.queue is None or len(self.queue) == 0:
#             return None
#         r = self.queue.pop(0)
#         return r
#
#     def __eq__(self, other):
#         return self.queue == other
#
#     def __add__(self, other):
#         if isinstance(other, Queue):
#             return Queue(*self.queue + other.queue)
#         return NotImplemented
#
#     def __iadd__(self, other):
#         if isinstance(other, Queue):
#             self.queue += other.queue
#             return self
#         return NotImplemented
#
#     def __rshift__(self, other):
#         if isinstance(other, int):
#             if len(self.queue) <= other:
#                 return Queue()
#             return Queue(*self.queue[other:])
#         return NotImplemented
#
#
# queue = Queue(1)
# item = queue.pop()
# print(item)
# print(queue.pop())