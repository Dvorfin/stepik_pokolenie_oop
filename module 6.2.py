# 6.2 Протокол последовательностей


# Класс ReversedSequence

# class ReversedSequence:
#     def __init__(self, sequence):
#         self.seq = sequence
#
#     def __len__(self):
#         return len(self.seq)
#
#     def __iter__(self):
#         yield from reversed(self.seq)
#
#     def __getitem__(self, item):
#         if isinstance(item, int):
#             return self.seq[-item - 1]
#
#
# numbers = [1, 2, 3, 4, 5]
# reversed_numbers = ReversedSequence(numbers)
# print(len(reversed_numbers))
#
# numbers.append(6)
# numbers.append(7)
# print(len(reversed_numbers))


# Класс SparseArray

# class SparseArray:
#     def __init__(self, default):
#         self.default = default
#         self.seq = []
#
#     def __getitem__(self, key):
#         if isinstance(key, int):
#             try:
#                 return self.seq[key]
#             except:
#                 return self.default
#
#     def __setitem__(self, key, value):
#         if isinstance(key, int):
#             if key >= len(self.seq):
#                 size = key + 1 - len(self.seq)
#                 self.seq.extend([self.default] * size)
#             self.seq[key] = value
#
#
# array = SparseArray(None)
#
# array[0] = 'Timur'
# array[1] = 'Arthur'
#
# print(array[0])
# print(array[1])
# print(array[2])


# Класс CyclicList

# from itertools import cycle
#
# class CyclicList:
#     def __init__(self, iterable):
#         self.it = cycle(iterable.copy())
#         self.seq = list(iterable)
#
#     def __iter__(self):
#         return self.it
#
#     def append(self, item):
#         self.seq.append(item)
#         self.it = cycle(self.seq)
#
#     def pop(self, index=-1):
#         pop = self.seq.pop(index)
#         self.it = cycle(self.seq)
#         return pop
#
#     def __getitem__(self, item):
#         index = item % len(self.seq)
#         return self.seq[index]
#
#     def __len__(self):
#         return len(self.seq)
#
#
# data = [1, 2, 3, 4, 5]
# cycliclist = CyclicList(data)
# data.extend([6, 7, 8, 9, 10])
#
# count = 0
# for item in cycliclist:
#     if count == 10:
#         break
#     print(item, end=' ')
#     count += 1


# Класс SequenceZip

# from copy import deepcopy
#
# class SequenceZip:
#     def __init__(self, *args):
#         self.data = deepcopy(args)
#
#     def __len__(self):
#         args = (ar.copy() if isinstance(ar, (list, tuple)) else ar for ar in self.data)
#         tmp = list(zip(*args))
#         return len(tmp)
#
#     def __getitem__(self, item):
#         for index, el in enumerate(zip(*self.data), 0):
#             if index == item:
#                 return el
#
#     def __iter__(self):
#         args = (ar.copy() if isinstance(ar, (list, tuple)) else ar for ar in self.data)
#         tmp = list(zip(*args))
#         yield from tmp.copy()
#
#
#
# x, y, z = [1, 2, 3], [4, 5, 6], [7, 8, 9]
# sequencezip = SequenceZip(x, y, z)
#
# print(sequencezip[2])
# x[-1], z[-1] = z[-1], x[-1]
# print(sequencezip[2])


# Класс OrderedSet

# import copy
# from functools import total_ordering
#
#
# class OrderedSet:
#     def __init__(self, iterable=None):
#         self.data = dict()
#         self.last_item = None
#
#         if iterable:
#             for index, el in enumerate(copy.deepcopy(iterable)):
#                 if el not in self.data:
#                     self.last_item = self.data.setdefault(el, el)
#
#         self.length = len(self.data)
#
#     def add(self, item):
#         if not self.__contains__(item):
#             self.data[item] = item
#             self.length += 1
#             self.last_item = item
#
#     def discard(self, item):
#         if self.__contains__(item):
#             del self.data[item]
#             self.length -= 1
#
#     def __contains__(self, item):
#         return item in self.data.values()
#
#     def __len__(self):
#         return self.length
#
#     def __iter__(self):
#         yield from self.data.values()
#
#     @total_ordering
#     def __eq__(self, other):
#         if isinstance(other, OrderedSet):
#             if self.__len__() == other.__len__():
#                 return list(self.data) == list(other.data)
#         elif isinstance(other, set):
#             if self.__len__() == len(other):
#                 return set(self.data.values()) == other
#         else:
#             return NotImplemented
#
#     def __str__(self):
#         return f"{self.data}"
#
# #
# print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
# print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
# print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
# print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
# print(OrderedSet(['green', 'red', 'blue']) == 100)



# Класс AttrDict

# class AttrDict:
#     def __init__(self, data=[]):
#         self._data = dict(data)
#
#     def __len__(self):
#         return len(self._data)
#
#     def __getitem__(self, item):
#         return self._data[item]
#
#     def __getattr__(self, item):
#         return self._data[item]
#
#     def __setitem__(self, key, value):
#         self._data[key] = value
#
#     def __iter__(self):
#         yield from self._data
#
#
# d = dict.fromkeys(range(100), None)
# attrdict = AttrDict(d)
# print(*attrdict)
#
# d[100] = None
# print(*attrdict)


# Класс PermaDict

# class PermaDict:
#     def __init__(self, data=[]):
#         self._data = dict(data)
#
#     def keys(self):
#         return self._data.keys()
#
#     def values(self):
#         return self._data.values()
#
#     def items(self):
#         return self._data.items()
#
#     def __len__(self):
#         return len(self._data)
#
#     def __iter__(self):
#         yield from self._data
#
#     def __setitem__(self, key, value):
#         if key in self._data:
#             raise KeyError('Изменение значения по ключу невозможно')
#         else:
#             self._data[key] = value
#
#     def __getitem__(self, item):
#         return self._data[item]
#
#     __getattr__ = __getitem__
#
#     def __delattr__(self, item):
#         del self._data[item]
#
#     __delitem__ = __delattr__
#
#
# permadict = PermaDict({'name': 'Timur', 'city': 'Moscow'})
#
# try:
#     permadict['name'] = 'Arthur'
# except KeyError as e:
#     print(e)


# Класс HistoryDict 🌶️


# class HistoryDict:
#     def __init__(self, data=None):
#         self._data = dict()
#         if data:
#             for key, value in data.items():
#                 self._data.setdefault(key, [])
#                 self._data[key].append(value)
#
#     def keys(self):
#         return self._data.keys()
#
#     def values(self):
#         return [el[-1] for el in self._data.values()]
#
#     def items(self):
#         return [(el[0], el[-1][-1]) for el in self._data.items()]
#
#     def history(self, key):
#         if key in self._data:
#             return self._data[key]
#         return []
#
#     def all_history(self):
#         return self._data
#
#     def __len__(self):
#         return len(self._data)
#
#     def __iter__(self):
#         yield from self._data
#
#     def __setitem__(self, key, value):
#         if key not in self._data:
#             self._data.setdefault(key, [])
#         self._data[key].append(value)
#
#     def __getitem__(self, item):
#         return self._data[item][-1]
#
#     __getattr__ = __getitem__
#
#     def __delattr__(self, item):
#         del self._data[item]
#
#     __delitem__ = __delattr__
#
#
# historydict = HistoryDict()
# print('Keys:', *historydict.keys())
# print('Values:', *historydict.values())
# print('Items:', *historydict.items())
# print('History(key=1):', historydict.history(1))
# print('History(key=1):', historydict.history(1))
# print('All history:', historydict.all_history())


# Класс MutableString 🌶️


# class MutableString:
#     def __init__(self, string=''):
#         self._string = string
#
#     def lower(self):
#         self._string = self._string.lower()
#
#     def upper(self):
#         self._string = self._string.upper()
#
#     def __str__(self):
#         return self._string
#
#     def __repr__(self):
#         return f"MutableString({repr(self._string)})"
#
#     def __len__(self):
#         return len(self._string)
#
#     def __iter__(self):
#         return iter(self._string)
#
#     def __getitem__(self, index):
#         tmp = list(self._string)
#         if isinstance(index, slice):
#             tmp = tmp[index]
#             return MutableString(''.join(tmp))
#         return tmp[index]
#
#     def __setitem__(self, key, value):
#         tmp = list(self._string)
#         tmp[key] = value
#         self._string = ''.join(tmp)
#
#     def __delitem__(self, key):
#         tmp = list(self._string)
#         del tmp[key]
#         self._string = ''.join(tmp)
#
#     def __add__(self, other):
#         if isinstance(other, MutableString):
#             return MutableString(self._string + other._string)
#         else:
#             return NotImplemented
#
#
# mutablestring = MutableString('beegeek')
#
# print(mutablestring)
# mutablestring[0] = 'B'
# mutablestring[-4] = 'G'
# print(mutablestring)


# Класс Grouper🌶️🌶️

# class Grouper:
#     def __init__(self, iterable, key):
#         self._group = dict()
#         for el in iterable:
#             self._group.setdefault(key(el), [])
#             self._group[key(el)].append(el)
#         self._key = key
#
#     def add(self, item):
#         key = self._key(item)
#         if key not in self._group:
#             self._group.setdefault(key, [])
#         self._group[key].append(item)
#
#     def group_for(self, obj):
#         return self._key(obj)
#
#     def __iter__(self):
#         return ((k, v)for k, v in self._group.items())
#
#     def __contains__(self, item):
#         return item in self._group.keys()
#
#     def __getitem__(self, item):
#         return self._group[item]
#
#
# grouper = Grouper(['hi'], key=lambda s: s[0])
#
# print(grouper.group_for('hello'))
# print(grouper.group_for('bee'))
# print(grouper['h'])
# print('b' in grouper)