# 8.3 Битовые флаги, класс Flag


# Класс OrderStatus

# from enum import Flag, auto
#
#
# class OrderStatus(Flag):
#     ORDER_PLACED = auto()
#     PAYMENT_RECEIVED = auto()
#     SHIPPING_COMPLETE = auto()
#
#
# order_status = OrderStatus(0)
# order_status |= OrderStatus.ORDER_PLACED
#
# if OrderStatus.ORDER_PLACED in order_status:
#     print('Заказ оформлен!')
#
# order_status |= OrderStatus.PAYMENT_RECEIVED
#
# if OrderStatus.PAYMENT_RECEIVED in order_status:
#     print('Оплата получена!')
#
# order_status |= OrderStatus.SHIPPING_COMPLETE
#
# if OrderStatus.SHIPPING_COMPLETE in order_status:
#     print('Доставка завершена!')


# Классы MovieGenres и Movie

# from enum import Flag, auto
#
#
# class MovieGenres(Flag):
#     ACTION = auto()
#     COMEDY = auto()
#     DRAMA = auto()
#     FANTASY = auto()
#     HORROR = auto()
#
#
# class Movie:
#     def __init__(self, name, genres):
#         self.name = name
#         self.genres = genres
#
#     def in_genre(self, genre):
#         return genre in self.genres
#
#     def __str__(self):
#         return self.name

