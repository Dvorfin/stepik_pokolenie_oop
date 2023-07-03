# 7.7 Полиморфизм


# Классы USADate и ItalianDate

# from datetime import date
#
# class USADate:
#     def __init__(self, year, month, day):
#         self.date = date(year=year, month=month, day=day)
#
#     def format(self):
#         return self.date.strftime("%m-%d-%Y")
#
#     def iso_format(self):
#         return self.date.isoformat()
#
#
# class ItalianDate:
#     def __init__(self, year, month, day):
#         self.date = date(year=year, month=month, day=day)
#
#     def format(self):
#         return self.date.strftime("%d/%m/%Y")
#
#     def iso_format(self):
#         return self.date.isoformat()
#
#
# italiandate = ItalianDate(2023, 4, 6)
#
# print(italiandate.format())
# print(italiandate.iso_format())


# Классы MinStat, MaxStat и AverageStat

# from abc import ABC, abstractmethod
#
#
# class Root(ABC):
#     def __init__(self, iterable=()):
#         self._data = list(iterable)
#
#     def add(self, num):
#         self._data.append(num)
#
#     @abstractmethod
#     def result(self):
#         pass
#
#     def clear(self):
#         self._data.clear()
#
#
# class MinStat(Root):
#     def result(self):
#         return min(self._data) if self._data else None
#
#
# class MaxStat(Root):
#     def result(self):
#         return max(self._data) if self._data else None
#
#
# class AverageStat(Root):
#     def result(self):
#         return sum(self._data) / len(self._data) if self._data else None
#
#
# minstat = MinStat()
# maxstat = MaxStat()
# averagestat = AverageStat()
#
# print(minstat.result())
# print(maxstat.result())
# print(averagestat.result())


# Классы LeftParagraph и RightParagraph

from abc import ABC, abstractmethod


class Paragraph(ABC):
    def __init__(self, length=0):
        self._length = length
        self._paragraph = ''

    def add(self, words: str):
        words = ' '.join(words.split())
        #print(words)
        if self._paragraph:
            self._paragraph = self._paragraph + ' ' + words
        else:
            self._paragraph = self._paragraph + words

    @abstractmethod
    def end(self):
        pass


class LeftParagraph(Paragraph):
    def end(self):
        total = 0
        print(self._paragraph.split())
        tmp = []
        for word in self._paragraph.split():
            if len(' '.join(tmp)) < self._length:
                tmp.append(word)
            else:
                print(' '.join(tmp))
                tmp.clear()


leftparagraph = LeftParagraph(10)

leftparagraph.add('death')
leftparagraph.add('can have me')
leftparagraph.add('when it earns me')
leftparagraph.end()