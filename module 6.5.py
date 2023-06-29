# 6.5 Протокол контекстных менеджеров. Часть 2

# Класс SuppressAll

# class SuppressAll:
#     def __enter__(self):
#         return self
#
#     def __exit__(self, *args, **kwargs):
#         return True


# Класс Greeter

# class Greeter:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print(f"Приветствую, {self.name}!")
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print(f"До встречи, {self.name}!")
#
#
# with Greeter('Кейв'):
#     print('...')


# Класс Closer

# class Closer:
#     def __init__(self, obj):
#         self.obj = obj
#
#     def __enter__(self):
#         return self.obj
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         try:
#             self.obj.close()
#             return True
#         except:
#             print('Незакрываемый объект')
#             return False
#
#
# output = open('output.txt', 'w', encoding='utf-8')
#
# with Closer(output) as file:
#     print(file.closed)
#
# print(file.closed)


# Класс ReadableTextFile

# class ReadableTextFile:
#     def __init__(self, filename):
#         self.filename = filename
#
#     def __enter__(self):
#         self.data = open(self.filename, 'r', encoding='utf-8')
#         return (srr.strip() for srr in self.data.readlines())
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.data:
#             self.data.close()
#
#
#
# with open('glados_quotes.txt', 'w', encoding='utf-8') as file:
#     print('Только посмотрите!', file=file)
#     print('Как величаво она парит в воздухе', file=file)
#     print('Как орел', file=file)
#     print('На воздушном шаре', file=file)
#
# with ReadableTextFile('glados_quotes.txt') as file:
#     for line in file:
#         print(line)


# Класс Reloopable

# class Reloopable:
#     def __init__(self, file):
#         self.file = file
#
#     def __enter__(self):
#         return self.file.readlines()
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.file:
#             self.file.close()
#
#
# with open('file.txt', 'w') as file:
#     file.write('Evil is evil\n')
#     file.write('Lesser, greater, middling\n')
#     file.write('Makes no difference\n')
#
#
# with Reloopable(open('file.txt')) as reloopable:
#     for line in reloopable:
#         print(line.strip())
#     for line in reloopable:
#         print(line.strip())


# Класс UpperPrint

import sys


# class UpperPrint:
#     def __enter__(self):
#         self.tmp = sys.stdout
#         sys.stdout = open('tmp.txt', 'w', encoding='utf-8')
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         sys.stdout = self.tmp
#         with open('tmp.txt', 'r', encoding='utf-8') as f:
#             s = f.readline()
#             while s:
#                 print(s.upper().strip('\n'))
#                 s = f.readline()
#
#
#
# print('Если жизнь одаривает вас лимонами — не делайте лимонад')
# print('Заставьте жизнь забрать их обратно!')
#
# with UpperPrint():
#     print('Мне не нужны твои проклятые лимоны!')
#     print('Что мне с ними делать?')
#
# print('Требуйте встречи с менеджером, отвечающим за жизнь!')


# Класс Suppress

# class Suppress:
#     def __init__(self, *args):
#         self.exceptions = args
#         self.exception = None
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if isinstance(exc_val, self.exceptions):
#             self.exception = exc_val
#             return True
#         return False
#
#
# with Suppress() as context:
#     print('All success!')
#
# print(context.exception)


# Класс WriteSpy🌶️

# class WriteSpy:
#     def __init__(self, file1, file2, to_close=False):
#         self.file1 = file1
#         self.file2 = file2
#         self.to_close = to_close
#
#     def __enter__(self):
#         return self
#
#     def __exit__(self, *args, **kwargs):
#         if self.to_close:
#             self.file1.close()
#             self.file2.close()
#
#     def write(self, text):
#         try:
#             self.file1.write(text)
#             self.file2.write(text)
#         except:
#             raise ValueError('Файл закрыт или недоступен для записи')
#
#     def close(self):
#         self.to_close = True
#         self.__exit__(self)
#
#     def closed(self):
#         return self.file1.closed and self.file2.closed
#
#     def writable(self):
#         if self.file1.closed or self.file2.closed:
#             return False
#         return self.file1.mode == 'w' and self.file2.mode == 'w'
#
#
# f1 = open('file1.txt', mode='w')
# f2 = open('file2.txt', mode='w')
# f1.close()
#
# with WriteSpy(f1, f2, to_close=True) as combined:
#     print(combined.writable())


# Класс Atomic 🌶️

# import copy
#
# class Atomic:
#     def __init__(self, data, deep=False):
#         self.data = data
#         self.deep = deep
#
#     def __enter__(self):
#         if self.deep:
#             self.copy_data = copy.deepcopy(self.data)
#         else:
#             self.copy_data = copy.copy(self.data)
#         return self.copy_data
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if exc_type is not None:
#             return True
#         else:
#             if isinstance(self.data, list):
#                 self.data[:] = self.copy_data
#             if isinstance(self.data, set):
#                 self.data.clear()
#                 self.data |= self.copy_data
#             if isinstance(self.data, dict):
#                 self.data.clear()
#                 self.data.update(self.copy_data)
#             return False
#
#
# numbers = {1, 2, 3, 4, 5}
#
# with Atomic(numbers) as atomic:
#     atomic.add(6)
#     atomic.append(7)           # добавление элемента с помощью несуществующего метода
#
# print(sorted(numbers))
#
# with Atomic(numbers) as atomic:
#     atomic.add(6)
#
# print(sorted(numbers))


# Класс AdvancedTimer

# from time import perf_counter
#
#
# class AdvancedTimer:
#     def __init__(self):
#         self.runs = []
#         self.last_run = None
#         self.min = None
#         self.max = None
#
#     def __enter__(self):
#         self.start = perf_counter()
#
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.last_run = perf_counter() - self.start
#         self.runs.append(self.last_run)
#         self.max = max(self.runs)
#         self.min = min(self.runs)
#
#
#
# from time import sleep
#
# timer = AdvancedTimer()
#
# with timer:
#     sleep(1.5)
#
# with timer:
#     sleep(0.7)
#
# with timer:
#     sleep(1)
#
# print([round(runtime, 1) for runtime in timer.runs])
# print(round(timer.min, 1))
# print(round(timer.max, 1))


# Класс HtmlTag 🌶️

# class HtmlTag:
#     indent = 0
#
#     def __init__(self, tag, inline=False):
#         self.tag = tag
#         self.inline = inline
#
#     def __enter__(self):
#         if self.inline:
#             print(' ' * self.indent + f"<{self.tag}>", end='')
#         else:
#             print(' ' * self.indent + f"<{self.tag}>")
#             self.__class__.indent += 2
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         if self.inline:
#             print(f"</{self.tag}>")
#         else:
#             self.__class__.indent -= 2
#             print(' ' * self.indent + f"</{self.tag}>")
#
#     def print(self, text):
#         if self.inline:
#             print(f"{text}", end='')
#         else:
#             print(' ' * self.indent + f"{text}")
#
#
# with HtmlTag('body') as _:
#     with HtmlTag('h1', True) as header:
#         header.print('Здесь есть что-то интересное')
#     with HtmlTag('a', True) as section:
#         section.print('https://stepik.org/media/attachments/course/98974/watch_me.mp4')


# Класс TreeBuilder 🌶️🌶️
from collections import defaultdict
import copy


class TreeBuilder:
    tree = []
    position = 0
    d = defaultdict(list)
    d['0'] = []

    def __enter__(self):
        self.position += 1
        self.curr_tree = []
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.d[str(self.position)].append(copy.deepcopy(self.curr_tree))
        self.position -= 1

    def add(self, obj):
        if hasattr(self, 'curr_tree'):
            self.curr_tree.append(obj)
        else:
            self.curr_tree = []
            self.curr_tree.append(obj)

        # if hasattr(self, 'curr_position'):
        #     self.d[str(self.position)].append([])
        #     self.d[str(self.position)][self.curr_position].append(obj)
        # else:
        #     self.d[str(self.position)].append(obj)

        # if str(self.position +1) not in self.d:
        #     self.d[str(self.position +1 )].append(obj)
        # else:
        #     self.d[str(self.position)].append(obj)

            #self.d[str(self.position)] = copy.copy(self.curr_tree)
            #print(self.curr_tree)
        # else:
        #     self.d[str(self.position)].append(obj)

    def structure(self):
        return list(self.d.values())


tree = TreeBuilder()
print(tree.structure())

tree.add('1st')
print(tree.structure())

with tree:
    tree.add('2nd')
    with tree:
        tree.add('3rd')
    tree.add('4th')
    with tree:
        pass

print(tree.structure())


# def __enter__(self):
#     self.curr_tree = []
#     self.position += 1
#     return self
#
#
# def __exit__(self, exc_type, exc_val, exc_tb):
#     self.d[str(self.position)] = copy.copy(self.curr_tree)
#     self.position -= 1
#     self.curr_tree.clear()
#
#
# def add(self, obj):
#     if hasattr(self, 'curr_tree'):
#         self.curr_tree.append(obj)
#         self.d[str(self.position)].append(obj)
#         self.d[str(self.position)] = copy.copy(self.curr_tree)
#         # print(self.curr_tree)
#     else:
#         self.d[str(self.position)].append(obj)
#
#
# def structure(self):
#     return self.d.items()



# def __enter__(self):
#     self.curr_tree = []
#     return self
#
#
# def __exit__(self, exc_type, exc_val, exc_tb):
#     self.tree.append(self.curr_tree)
#
#
# def add(self, obj):
#     if hasattr(self, 'curr_tree'):
#         self.curr_tree.append(obj)
#     else:
#         self.tree.append(obj)
#
#
# def structure(self):
#     return self.tree