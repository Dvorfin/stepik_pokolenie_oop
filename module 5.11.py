# 5.11 Особенности работы словарей и множеств
import random


# Класс Point


# class Point:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z
#         self.coords = [self.x, self.y, self.z]
#
#     def __repr__(self):
#         return f"Point({self.x}, {self.y}, {self.z})"
#
#     def __iter__(self):
#         yield from self.coords
#
#
# point = Point(1, 2, 3)
#
# print(list(point))


# Класс DevelopmentTeam


# class DevelopmentTeam:
#     def __init__(self):
#         self.juns = []
#         self.seniors = []
#     def add_junior(self, *args):
#         self.juns += args
#
#     def add_senior(self, *args):
#         self.seniors += args
#
#     def __iter__(self):
#         for el in self.juns:
#             yield (el, 'junior')
#
#         for el in self.seniors:
#             yield (el, 'senior')
#
#
# beegeek = DevelopmentTeam()
#
# beegeek.add_junior('Timur')
# beegeek.add_junior('Arthur', 'Valery')
# beegeek.add_senior('Gvido')
# print(*beegeek, sep='\n')


# Класс AttrsIterator


# class AttrsIterator:
#     def __init__(self, obj):
#         self.obj = iter(obj.__dict__.items())
#         self.length = len(list(obj.__dict__.items()))
#         self.counter = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.counter > self.length:
#             raise StopIteration
#         else:
#             self.counter += 1
#             return next(self.obj)
#
#
# class User:
#     def __init__(self, name, surname, age):
#         self.name = name
#         self.surname = surname
#         self.age = age
#
#
# user = User('Debbie', 'Harry', 77)
# attrsiterator = AttrsIterator(user)
#
# print(*attrsiterator)


# Класс SkipIterator


# class SkipIterator:
#     def __init__(self, iterable, n):
#         lst = list(iterable)
#         self._iterable = (lst[i] for i in range(0, len(lst), n +1))
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self._iterable)
#
#
# skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента
#
# print(*skipiterator)


# Класс RandomLooper

# class RandomLooper:
#     def __init__(self, *args):
#         self.iters = []
#         for ar in args:
#             self.iters.extend(list(ar))
#
#         random.shuffle(self.iters)
#         self.iters = iter(self.iters)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         return next(self.iters)
#
#
# colors = ['red', 'blue', 'green', 'purple']
# shapes = ['square', 'circle', 'triangle', 'octagon']
# randomlooper = RandomLooper(colors, shapes)
#
# print(list(randomlooper))


# Класс Peekable 🌶️

# class Peekable:
#     def __init__(self, iterable):
#         self.source = list(iterable)
#         self.iter = iter(iterable)
#         self.cnt = 0
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.cnt += 1
#         return next(self.iter)
#
#     def peek(self, default=StopIteration):
#         try:
#             elem = self.source[self.cnt]
#             return elem
#         except:
#             if default == StopIteration:
#                 raise StopIteration
#             else:
#                 return default
#
#
# iterator = Peekable('beegeek')
#
# print(next(iterator))
# print(next(iterator))
# print(*iterator)


#  Класс LoopTracker🌶️🌶️

# class LoopTracker:
#     def __init__(self, iterable):
#         self.source = list(iterable)
#         self.iter = iter(iterable)
#         self.cnt = 0
#         self.length = len(self.source)
#         self.generated = 0
#         self.try_count = 0
#         self.last_element = None
#         self.empty = False
#
#     @property
#     def accesses(self):
#         return self.generated
#
#     @property
#     def empty_accesses(self):
#         return self.try_count
#
#     @property
#     def first(self):
#         try:
#             return self.source[0]
#         except:
#             raise AttributeError('Исходный итерируемый объект пуст')
#
#     @property
#     def last(self):
#         if self.last_element is None:
#             raise AttributeError('Последнего элемента нет')
#         else:
#             return self.last_element
#
#     def is_empty(self):
#         return self.empty
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         try:
#             res = next(self.iter)
#             self.cnt += 1
#             self.generated += 1
#             self.last_element = res
#             if self.cnt == self.length:
#                 self.empty = True
#             return res
#         except StopIteration:
#             self.empty = True
#             self.try_count += 1
#             raise StopIteration
#
#
# loop_tracker = LoopTracker([1, 2])
#
# print(loop_tracker.is_empty())
# next(loop_tracker)
# print(loop_tracker.is_empty())
# next(loop_tracker)
# print(loop_tracker.is_empty())
