# 7.8 Композиция


# Классы Point и Circle


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y =y
#
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#
#
#
# class Circle:
#     def __init__(self, radius, center):
#         self.radius = radius
#         self.center = center
#
#     def __str__(self):
#         return str(self.center) + f", r = {self.radius}"
#
#
# point = Point(1, 1)
# circle = Circle(5, point)
#
# print(point)
# print(circle)


# Классы Item и ShoppingCart

# class Item:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def __str__(self):
#         return f"{self.name}, {self.price}$"
#
#
# class ShoppingCart:
#     def __init__(self, items=()):
#         self.items = list(items)
#
#     def add(self, item):
#         self.items.append(item)
#
#     def total(self):
#         return sum(item.price for item in self.items)
#
#     def remove(self, item):
#         self.items = [el for el in self.items if item != el.name]
#
#     def __str__(self):
#         return '\n'.join(f"{item.name}, {item.price}$" for item in self.items)
#
#
# shopping_cart = ShoppingCart([Item('Yoga Mat', 130), Item('Flannel Shirt', 22)])
#
# shopping_cart.remove('Yoga Mat')
# print(shopping_cart)
# print(shopping_cart.total())


# Классы Card и Deck

# from itertools import product
# from random import shuffle
#
#
# class Card:
#     def __init__(self, suit, rank):
#         self.suit = suit
#         self.rank = rank
#
#     def __str__(self):
#         return f"{self.suit}{self.rank}"
#
#
# class Deck:
#     def __init__(self):
#         self.deck = [Card(suit, rank) for suit, rank in product(['♣', '♢', '♡', '♠'], ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'])]
#
#     def __str__(self):
#         return f"Карт в колоде: {len(self.deck)}"
#
#     def shuffle(self):
#         if len(self.deck) == 52:
#             shuffle(self.deck)
#         else:
#             raise ValueError('Перемешивать можно только полную колоду')
#
#     def deal(self):
#         if len(self.deck) != 0:
#             return self.deck.pop()
#         else:
#             raise ValueError('Все карты разыграны')
#
#
# deck = Deck()
#
# print(deck)
# print(deck.deal())
# print(deck.deal())
# print(deck.deal())
# print(deck)


# Класс Queue

# class Queue:
#     def __init__(self, pairs=()):
#         self.data = dict()
#
#         self.data.update(pairs)
#
#     def add(self, item):
#         if item[0] in self.data:
#             tmp = self.data.pop(item[0])
#             tmp = list(self.data.items())
#             tmp.extend([item])
#             self.data = {k:v for k, v in tmp}
#         else:
#             self.data.update({item[0]: item[1]})
#
#     def pop(self):
#         try:
#             first = next(iter(self.data))
#             tmp = first, self.data.pop(first)
#             return tmp
#         except StopIteration:
#             raise KeyError('Очередь пуста')
#
#     def __str__(self):
#         return f"Queue({list(self.data.items())})"
#
#     def __len__(self):
#         return len(self.data)
#
#
# queue = Queue()
#
# queue.add(('one', 1))
# queue.add(('two', 2))
# print(queue)
# queue.add(('one', 10))
# print(queue)


# Классы Lecture и Conference🌶️

# from datetime import time, timedelta
#
#
# class Lecture:
#     def __init__(self, topic, start_time, duration):
#         self.topic = topic
#         h, m = map(int, start_time.split(':'))
#         self.start_time = timedelta(hours=h, minutes=m)
#         h, m = map(int, duration.split(':'))
#         self.duration = timedelta(hours=h, minutes=m)
#         self.stop_time = self.start_time + self.duration
#
#     def __str__(self):
#         return f"{self.start_time}, {self.stop_time}"
#
#
# class Conference:
#     def __init__(self):
#         self.confs = []
#
#     def add(self, lecture):
#         flag = False
#         if len(self.confs) != 0:
#             for lct in self.confs:
#                 if (lct.start_time < lecture.stop_time < lct.stop_time) or (
#                         lct.start_time < lecture.start_time < lct.stop_time):
#                     flag = True
#                 if (lecture.start_time <= lct.start_time) and (lct.stop_time <= lecture.stop_time):
#                     flag = True
#
#             if flag:
#                 raise ValueError('Провести выступление в это время невозможно')
#             else:
#                 self.confs.append(lecture)
#         else:
#             self.confs.append(lecture)
#
#     def total(self):
#         t = timedelta(seconds=sum(lct.duration.total_seconds() for lct in self.confs))
#         h, m = t.seconds // 3600, (t.seconds // 60) % 60
#         return time(hour=h, minute=m).strftime(f"%H:%M")
#
#     def longest_lecture(self):
#         l = max(lct.duration for lct in self.confs)
#         h, m = l.seconds // 3600, (l.seconds // 60) % 60
#         return time(hour=h, minute=m).strftime(f"%H:%M")
#
#     def longest_break(self):
#         res = timedelta(seconds=0)
#         tmp = sorted(self.confs, key=lambda x: x.start_time)
#
#         for i in range(1, len(self.confs)):
#             if tmp[i].start_time - tmp[i - 1].stop_time > res:
#                 res = tmp[i].start_time - tmp[i - 1].stop_time
#
#         h, m = res.seconds // 3600, (res.seconds // 60) % 60
#         return time(hour=h, minute=m).strftime(f"%H:%M")
#
#
# conference = Conference()
# conference.add(Lecture('Декораторы @classmethod и @staticmethod', '09:30', '00:30'))
#
# try:
#     conference.add(Lecture('Декоратор @singledispatchmethod', '09:30', '00:30'))
# except ValueError as e:
#     print(e)


