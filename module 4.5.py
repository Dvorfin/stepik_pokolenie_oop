# 4.5 Свойства, функция property()

# Класс Rectangle

# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
#     def get_perimeter(self):
#         return self.length * 2 + self.width * 2
#
#     def get_area(self):
#         return self.length * self.width
#
#     perimeter = property(fget=get_perimeter)
#     area = property(fget=get_area)
#
# rectangle = Rectangle(4, 5)
#
# print(rectangle.length)
# print(rectangle.width)
# print(rectangle.perimeter)
# print(rectangle.area)


# Класс HourClock

# class HourClock:
#     def __init__(self, hours):
#         self.hours = hours
#
#     def set_hour(self, hours):
#         if isinstance(hours, int) and (1 <= hours <= 12):
#             self._hours = hours
#         else:
#             raise ValueError('Некорректное время')
#
#     def get_hours(self):
#         return self._hours
#
#     hours = property(fset=set_hour, fget=get_hours)
#
#
# try:
#     HourClock('pizza time 🕷')
# except ValueError as e:
#     print(e)


# Класс Person

# class Person:
#     def __init__(self, name, surname):
#         self.name = name
#         self.surname = surname
#
#     def set_name(self, name):
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#     def set_surname(self, surname):
#         self._surname = surname
#
#     def get_surname(self):
#         return self._surname
#
#     def set_name_surname(self, srr):
#         name, surname = srr.split()
#         self.name = name
#         self.surname = surname
#
#     def get_name_surname(self):
#         return f'{self.get_name()} {self.get_surname()}'
#
#     name = property(fset=set_name, fget=get_name)
#     surname = property(fset=set_surname, fget=get_surname)
#     fullname = property(fset=set_name_surname, fget=get_name_surname)
#
# person = Person('Меган', 'Фокс')
#
# print(person.name)
# print(person.surname)
# print(person.fullname)