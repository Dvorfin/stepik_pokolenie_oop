# 7.1 Наследование. Часть 1


# Иерархия классов 🛸

# class Vehicle:
#     pass
#
#
# class LandVehicle(Vehicle):
#     pass
#
#
# class WaterVehicle(Vehicle):
#     pass
#
#
# class AirVehicle(Vehicle):
#     pass
#
#
# class Car(LandVehicle):
#     pass
#
#
# class Motocycle(LandVehicle):
#     pass
#
#
# class Bicycle(LandVehicle):
#     pass
#
#
# class Propeller(AirVehicle):
#     pass
#
#
# class Jet(AirVehicle):
#     pass


# Иерархия классов 🔶

# class Shape:
#     pass
#
#
# class Circle(Shape):
#     pass
#
#
# class Polygon(Shape):
#     pass
#
#
# class Quadrilateral(Polygon):
#     pass
#
#
# class Triangle(Polygon):
#     pass
#
#
# class Parallelogram(Quadrilateral):
#     pass
#
#
# class Rectangle(Parallelogram):
#     pass
#
#
# class Square(Rectangle):
#     pass
#
#
# class IsoscelesTriangle(Triangle):
#     pass
#
#
# class EquilateralTriangle(Triangle):
#     pass


# Иерархия классов 🐍

# class Animal:
#     def sleep(self):
#         pass
#
#     def eat(self):
#         pass
#
#
# class Fish(Animal):
#     def swim(self):
#         pass
#
#
# class Bird(Animal):
#     def lay_eggs(self):
#         pass
#
#
# class FlyingBird(Bird):
#     def fly(self):
#         pass


# Классы User и PremiumUser

# class User:
#     def __init__(self, name):
#         self._name = name
#
#     def skip_ads(self):
#         return False
#
#
# class PremiumUser(User):
#     def skip_ads(self):
#         return True


# Классы Validator и NumberValidator

# class Validator:
#     def __init__(self, obj):
#         self._obj = obj
#
#     def is_valid(self):
#         return None
#
#
# class NumberValidator(Validator):
#     def __init__(self, obj):
#         Validator.__init__(self, obj)
#
#     def is_valid(self):
#         return isinstance(self._obj, (int, float))


# Класс Counter и подклассы

# class Counter:
#     def __init__(self, start=0):
#         self.value = start
#
#     def inc(self, n=1):
#         self.value += n
#
#     def dec(self, n=1):
#         if self.value - n < 0:
#             self.value = 0
#         else:
#             self.value -= n
#
#
# class NonDecCounter(Counter):
#     def dec(self, n=1):
#         pass
#
#
# class LimitedCounter(Counter):
#     def __init__(self, start=0, limit=10):
#         Counter.__init__(self, start)
#         self._limit = limit
#
#     def inc(self, n=1):
#         if self.value + n > self._limit:
#             self.value = self._limit
#         else:
#             self.value += n
#
#
# counter = LimitedCounter()
#
# print(counter.value)
# counter.inc()
# counter.inc(4)
# print(counter.value)
# counter.dec()
# counter.dec(2)
# print(counter.value)
# counter.inc(20)
# print(counter.value)