# 5.9 Хеширование объектов. Часть 1


# Функция hash_function()


# def hash_function(obj):
#     temp1, temp2 = 0, 0
#     obj = str(obj)
#
#     for i in range(len(obj) // 2):
#         temp1 += (ord(obj[i]) * ord(obj[-(i + 1)]))
#
#     if len(obj) % 2 != 0:
#         temp1 += ord(obj[len(obj) // 2])
#
#     for i in range(len(obj)):
#         temp2 += (ord(obj[i]) * (i + 1)) * (-1) ** i
#
#     return (temp1 * temp2) % 123456791
#
#
# print(hash_function('python'))
# print(hash_function(12345))
# print(hash_function(None))


# Функция limited_hash() 🌶️


# def limited_hash(left, right, hash_function=hash):
#
#     def hash_func(obj):
#         res = hash_function(obj)
#
#         while not (left <= res <= right):
#             if res > right:
#                 res = left + (res - right) - 1
#             if res < left:
#                 res = right - (left - res) + 1
#         return res
#
#
#     return hash_func
#
#
# hash_function = limited_hash(10, 15)
#
# print(hash_function(9))
# print(hash_function(8))
# print(hash_function(4))
# print(hash_function(3))
# print(hash_function(2))
