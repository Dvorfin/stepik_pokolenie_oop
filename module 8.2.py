# 8.2 Перечисления, класс Enum

from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


print(Weekday)


# Класс HTTPStatusCodes

# from enum import Enum
#
#
# class HTTPStatusCodes(Enum):
#     CONTINUE = 100
#     OK = 200
#     USE_PROXY = 305
#     NOT_FOUND = 404
#     BAD_GATEWAY = 502
#
#     def info(self):
#         return self.name, self.value
#
#     def code_class(self):
#         d = {'CONTINUE': 'информация', 'OK': 'успех', 'USE_PROXY': 'перенаправление', 'NOT_FOUND': 'ошибка клиента',
#              'BAD_GATEWAY': 'ошибка сервера'}
#         return d[self.name]


# Класс Seasons

# from enum import Enum
#
#
# class Seasons(Enum):
#     WINTER = 1
#     SPRING = 2
#     SUMMER = 3
#     FALL = 4
#
#     def text_value(self, code):
#         translations = {
#             "WINTER": {"en": "winter", "ru": "зима"},
#             "SPRING": {"en": "spring", "ru": "весна"},
#             "SUMMER": {"en": "summer", "ru": "лето"},
#             "FALL": {"en": "fall", "ru": "осень"}
#         }
#
#         return translations[self.name][code]


# Классы Weekday и NextDate


from enum import Enum


class Weekday(Enum):
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6


from datetime import date

class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        if self.after_today:
            #print(self.today.weekday() +1)
            return date(day=Weekday(self.today.weekday() + 1))
        return date(date= Weekday(self.today.weekday()))

    def days_until(self):
        pass



from datetime import date

today = date(2023, 4, 17)  # понедельник
#print(today.weekday())
next_friday = NextDate(today, Weekday.FRIDAY)  # следующая пятница

print(next_friday.date())