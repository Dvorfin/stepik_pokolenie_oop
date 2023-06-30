# 7.2 Наследование. Часть 2


# Классы BasicPlan и подклассы


# class BasicPlan:
#     can_stream = True
#     can_download = True
#     has_SD = True
#     has_HD = False
#     has_UHD = False
#     num_of_devices = 1
#     price = '8.99$'
#
#
# class SilverPlan(BasicPlan):
#     has_HD = True
#     num_of_devices = 2
#     price = '12.99$'
#
#
# class GoldPlan(BasicPlan):
#     has_HD = True
#     has_UHD = True
#     num_of_devices = 4
#     price = '15.99$'
#
#
# print(GoldPlan.can_stream)
# print(GoldPlan.can_download)
# print(GoldPlan.has_SD)
# print(GoldPlan.has_HD)
# print(GoldPlan.has_UHD)
# print(GoldPlan.num_of_devices)
# print(GoldPlan.price)


# Классы WeatherWarning и WeatherWarningWithDate


# class WeatherWarning:
#     def rain(self):
#         print("Ожидаются сильные дожди и ливни с грозой")
#
#     def snow(self):
#         print("Ожидается снег и усиление ветра")
#
#     def low_temperature(self):
#         print("Ожидается сильное понижение температуры")
#
#
# class WeatherWarningWithDate(WeatherWarning):
#     def rain(self, d):
#         print(d.strftime("%d.%m.%Y"))
#         super().rain()
#
#     def snow(self, d):
#         print(d.strftime("%d.%m.%Y"))
#         super().snow()
#
#     def low_temperature(self, d):
#         print(d.strftime("%d.%m.%Y"))
#         super().low_temperature()
#
#
# from datetime import date
#
# weatherwarning = WeatherWarningWithDate()
# dt = date(2022, 12, 12)
#
# weatherwarning.rain(dt)
# weatherwarning.snow(dt)
# weatherwarning.low_temperature(dt)


# Классы Triangle и EquilateralTriangle

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def perimeter(self):
#         return sum(self.__dict__.values())
#
#
# class EquilateralTriangle(Triangle):
#     def __init__(self, side):
#         super().__init__(side, side, side)


# Класс Counter и DoubledCounter

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
# class DoubledCounter(Counter):
#     def inc(self, n=1):
#         super().inc(n * 2)
#
#     def dec(self, n=1):
#         super().dec(n * 2)
#
#
# counter = DoubledCounter(20)
#
# print(counter.value)
# counter.inc()
# counter.inc(5)
# print(counter.value)
# counter.dec()
# counter.dec(10)
# print(counter.value)
# counter.dec(10)
# print(counter.value)


# Классы Summator и подклассы🌶️

# class Summator:
#     def __init__(self):
#         self.pow = 1
#
#     def total(self, n):
#         return sum(i ** self.pow for i in range(n + 1))
#
#
# class SquareSummator(Summator):
#     def __init__(self):
#         self.pow = 2
#
#
# class QubeSummator(Summator):
#     def __init__(self):
#         self.pow = 3
#
#
# class CustomSummator(Summator):
#     def __init__(self, m):
#         self.pow = m
#
#
# summator1 = Summator()
# summator2 = SquareSummator()
# summator3 = QubeSummator()
#
# print(summator1.total(3))    # 1 + 2 + 3
# print(summator2.total(3))    # 1 + 4 + 9
# print(summator3.total(3))    # 1 + 8 + 27


# Класс FieldTracker🌶️🌶️

class FieldTracker:
    def base(self, attr):
        return self.__getattribute__(attr)


