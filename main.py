# 4.3 Методы экземпляра класса. Часть 2

# Класс Gun

# class Gun:
#     def shoot(self):
#         print('pif')
#
# gun = Gun()
#
# gun.shoot()


# Класс User

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.friends = 0
#
#     def add_friends(self, n):
#         self.friends += n


# Класс House

# class House:
#     def __init__(self, color, rooms):
#         self.color = color
#         self.rooms = rooms
#
#     def paint(self, new_color):
#         self.color = new_color
#
#     def add_rooms(self, n):
#         self.rooms += n


# Класс Circle

# from math import pi
#
#
# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
#         self.diameter = radius * 2
#         self.area = pi*radius**2


# Класс Bee

# class Bee:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def move_up(self, n):
#         self.y += n
#
#     def move_down(self, n):
#         self.y -= n
#
#     def move_right(self, n):
#         self.x += n
#
#     def move_left(self, n):
#         self.x -= n


# Класс Gun

# class Gun:
#     def __init__(self):
#         self.flag = True
#
#     def shoot(self):
#         if self.flag:
#             print('pif')
#             self.flag = not self.flag
#         else:
#             print('paf')
#             self.flag = not self.flag


# Класс Gun

# class Gun:
#     def __init__(self):
#         self.count = 0
#
#     def shoot(self):
#         print(('pif', 'paf')[self.count % 2])
#         self.count += 1
#
#     def shots_count(self):
#         return self.count
#
#     def shots_reset(self):
#         self.count = 0


# Класс Scales

# class Scales:
#     def __init__(self):
#         self.right_mass = 0
#         self.left_mass = 0
#
#     def add_right(self, m):
#         self.right_mass += m
#
#     def add_left(self, m):
#         self.left_mass += m
#
#     def get_result(self):
#         if self.right_mass > self.left_mass:
#             return 'Правая чаша тяжелее'
#         elif self.right_mass < self.left_mass:
#             return 'Левая чаша тяжелее'
#         else:
#             return 'Весы в равновесии'


# Класс Vector

# class Vector:
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def abs(self):
#         return (self.x**2 + self.y**2) ** 0.5


# Класс Numbers

# class Numbers:
#     def __init__(self):
#         self.nums = list()
#
#     def add_number(self, num):
#         self.nums.append(num)
#
#     def get_even(self):
#         return list(filter(lambda x: x % 2 == 0, self.nums))
#
#     def get_odd(self):
#         return list(filter(lambda x: x % 2, self.nums))


# Класс TextHandler

# class TextHandler:
#     def __init__(self):
#         self.words = list()
#
#     def add_words(self, words):
#         self.words.extend(words.split())
#         print(self.words)
#
#     def get_shortest_words(self):
#         if not self.words:
#             return []
#         min_word_len = len(min(self.words, key=len))
#         return list(filter(lambda w: min_word_len == len(w), self.words))
#
#     def get_longest_words(self):
#         if not self.words:
#             return []
#         max_word_len = len(max(self.words, key=len))
#         return list(filter(lambda w: max_word_len == len(w), self.words))


# Класс Todo

# class Todo:
#     def __init__(self):
#         self.things = list()
#         self.low = 1
#         self.high = 0
#
#     def add(self, name, priority):
#         self.things.append((name, priority))
#         if self.low > priority:
#             self.low = priority
#         if self.high < priority:
#             self.high = priority
#         print(self.low, self.high)
#
#     def get_by_priority(self, n):
#         return [task[0] for task in self.things if task[1] == n]
#
#     def get_low_priority(self):
#         return [task[0] for task in self.things if task[1] == self.low]
#
#     def get_high_priority(self):
#         return [task[0] for task in self.things if task[1] == self.high]


# Класс Postman

# class Postman:
#     def __init__(self):
#         self.delivery_data = list()
#
#     def add_delivery(self, street, house, apartment):
#         self.delivery_data.append((street, house, apartment))
#
#     def get_houses_for_street(self, street):
#         res = list()
#         for st in self.delivery_data:
#             if st[0] == street and st[1] not in res:
#                 res.append(st[1])
#         return res
#
#     def get_flats_for_house(self, street, house):
#         res = list()
#         for st in self.delivery_data:
#             if st[0] == street and st[1] == house and st[2] not in res:
#                 res.append(st[2])
#         return res


# Класс Wordplay

# class Wordplay:
#     def __init__(self, words=None):
#         if words is None:
#             self.words = list()
#         else:
#             self.words = words.copy()
#
#     def add_word(self, word):
#         if word not in self.words:
#             self.words.append(word)
#
#     def words_with_length(self, n):
#         return [w for w in self.words if len(w) == n]
#
#     def only(self, *args):
#         #print(set(args))
#         return [w for w in self.words if set(w) <= set(args)]
#
#     def avoid(self, *args):
#         return [w for w in self.words if set(w).isdisjoint(set(args))]


# Класс Knight ♞

# class Knight:
#     def __init__(self, horizontal, vertical, color):
#         self.horizontal = horizontal
#         self.vertical = vertical
#         self.color = color
#
#         self.x, self.y = self.convert(horizontal, vertical)
#
#     def convert(self, h, v):
#         return 7 - '12345678'.index(str(v)), 'abcdefgh'.index(h)
#
#     def get_char(self):
#         return 'N'
#
#     def can_move(self, new_h, new_v):
#         new_h, new_v = self.convert(new_h, new_v)
#         return (self.x - new_h) ** 2 + (self.y - new_v) ** 2 == 5
#
#     def move_to(self, new_h, new_v):
#         if self.can_move(new_h, new_v):
#             self.horizontal = new_h
#             self.vertical = new_v
#             self.x, self.y = self.convert(new_h, new_v)
#
#     def draw_board(self):
#         board = [['.']*8 for _ in range(8)]
#         board[self.x][self.y] = self.get_char()
#
#         for i in 'abcdefgh':
#             for j in '12345678':
#                 if self.can_move(i, j):
#                     i_, j_ = self.convert(i, j)
#                     board[i_][j_] = '*'
#
#         for i in range(8):
#             for j in range(8):
#                 print(board[i][j], end='')
#             print()
#
#
# knight = Knight('e', 5, 'black')
#
# knight.draw_board()
# knight.move_to('d', 3)
# print()
# knight.draw_board()

