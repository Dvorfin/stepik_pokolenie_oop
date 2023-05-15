# Тема урока: модификаторы доступа и аксессоры

# Класс Circle
# from math import pi
#
#
# class Circle:
#     def __init__(self, radius):
#         self._radius = radius
#         self._diameter = self._radius * 2
#         self._area = pi * self._radius ** 2
#
#     def get_radius(self):
#         return self._radius
#
#     def get_diameter(self):
#         return self._diameter
#
#     def get_area(self):
#         return self._area


# Класс BankAccount

# class BankAccount:
#     def __init__(self, balance=0):
#         self._balance = balance
#
#     def get_balance(self):
#         return self._balance
#
#     def deposit(self, amount: int):
#         self._balance += amount
#
#     def withdraw(self, amount: int):
#         if amount > self._balance:
#             raise ValueError('На счете недостаточно средств')
#         self._balance -= amount
#
#     def transfer(self, account, amount):
#         try:
#             self.withdraw(amount)
#             account.deposit(amount)
#         except ValueError as e:
#             print(e)
#
#
# account1 = BankAccount(100)
# account2 = BankAccount(200)
#
# try:
#     account1.transfer(account2, 150)
# except ValueError as e:
#     print(e)


#  Класс User

# class User:
#     def __init__(self, name: str, age: int):
#         if self.check_name(name):
#             self._name = name
#         if self.check_age(age):
#             self._age = age
#
#     def check_name(self, name):
#         if isinstance(name, str) and name.isalpha():  # проверка имени перед заменой
#             return True
#         else:
#             raise ValueError('Некорректное имя')
#
#     def check_age(self, age):
#         if isinstance(age, int) and (0 <= age <= 110):
#             return True
#         else:
#             raise ValueError('Некорректный возраст')
#
#     def get_name(self):
#         return self._name
#
#     def set_name(self, name):
#         if self.check_name(name):
#             self._name = name
#
#     def get_age(self):
#         return self._age
#
#     def set_age(self, new_age):
#         if self.check_age(new_age):
#             self._age = new_age
#
# user = User('Меган', 37)
#
# invalid_names = (-1, True, '', [], '123456', 'Меган906090')
#
# for name in invalid_names:
#     try:
#         user.set_name(name)
#     except ValueError as e:
#         print(e)