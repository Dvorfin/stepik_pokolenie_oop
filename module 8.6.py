# 8.6 Модуль dataclasses


# Класс City

# from dataclasses import dataclass, field
#
#
# @dataclass
# class City:
#     name: str
#     population: int
#     founded: int
#
#
# city1 = City('Tokyo', 14043239, 1457)
# city2 = City('New York', 8467513, 1624)
# city3 = City('Tokyo', 14043239, 1457)
#
# print(city1 == city2)
# print(city1 != city2)
# print(city1 == city3)
# print(city1 != city3)


# Класс MusicAlbum

# from dataclasses import dataclass, field
#
#
# @dataclass(frozen=True)
# class MusicAlbum:
#     title: str
#     artist: str
#     genre: str = field(repr=False, compare=False)
#     year: int = field(repr=False)
#
#
# musicalbum1 = MusicAlbum('Calendar', 'Motorama', 'Post-punk', 2012)
# musicalbum2 = MusicAlbum('Calendar', 'Motorama', 'New Wave, Indie Rock', 2012)
#
# print(musicalbum1 == musicalbum2)
# print(musicalbum1 != musicalbum2)


# Класс Point

# from dataclasses import dataclass, field
#
#
# @dataclass
# class Point:
#     x: float = field(default=0.0)
#     y: float = field(default=0.0)
#     quadrant: int = None
#
#     def __post_init__(self):
#         if self.x < 0 and self.y > 0:
#             self.quadrant = 2
#         elif self.x > 0 and self.y > 0:
#             self.quadrant = 1
#         elif self.x < 0 and self.y < 0:
#             self.quadrant = 3
#         elif self.x > 0 and self.y < 0:
#             self.quadrant = 4
#         else:
#             self.quadrant = 0
#
#     def symmetric_x(self):
#         return Point(self.x, -self.y)
#
#     def symmetric_y(self):
#         return Point(-self.x, self.y)
#
#
#
# point = Point(1.0, 2.0)
#
# print(point.symmetric_x())
# print(point.symmetric_y())


# Классы FootballPlayer и FootballTeam

# from dataclasses import dataclass, field
#
#
# @dataclass(order=True)
# class FootballPlayer:
#     name: str = field(compare=False)
#     surname: str = field(compare=False)
#     value: int = field(repr=False)
#
# @dataclass
# class FootballTeam:
#     name: str
#     players: list = field(default_factory=list, repr=False, compare=False)
#
#     def add_players(self, *args):
#         self.players.extend(args)
#
#
# player1 = FootballPlayer('Jude', 'Bellingham', 120000000)
# player2 = FootballPlayer('Vinicius', 'Junior', 120000000)
# player3 = FootballPlayer('Kylian', 'Mbappe', 180000000)
#
# print(player1 == player2)
# print(player1 == player3)
# print(player1 > player3)
# print(player1 < player3)