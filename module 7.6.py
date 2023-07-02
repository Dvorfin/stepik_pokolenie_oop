# 7.6 Множественное наследование


# Иерархия классов 🔠

# class A:
#     pass
#
# class C(A):
#     pass
#
# class B(A):
#     pass
#
# class D(A):
#     pass
#
# class E(B, D):
#     pass


# Иерархия классов 🔠

# class H:
#     pass
#
#
# class D(H):
#     pass
#
#
# class E(H):
#     pass
#
#
# class B(D, E):
#     pass
#
#
# class F(H):
#     pass
#
#
# class G(H):
#     pass
#
#
# class C(F, G):
#     pass
#
#
# class A(B, C):
#     pass


# Функция get_method_owner()

# def get_method_owner(cls, method):
#     for m in cls.mro():
#         if method in m.__dict__:
#             return m
#     return None
#
#
# class A:
#     def m(self):
#         pass
#
#
# class B(A):
#     pass
#
# print(B.mro())
# print(get_method_owner(B, 'm'))


# Семья

# class Father:
#     def __init__(self, mood='neutral'):
#         self.mood = mood
#
#     def greet(self):
#         return "Hello!"
#
#     def be_strict(self):
#         self.mood = 'strict'
#
#
# class Mother:
#     def __init__(self, mood='neutral'):
#         self.mood = mood
#     def greet(self):
#         return 'Hi, honey!'
#
#     def be_kind(self):
#         self.mood = 'kind'
#
#
# class Daughter(Mother, Father):
#     pass
#
#
# class Son(Father, Mother):
#     pass
#
#
# print(Son.mro())
# print(Daughter.mro())
#
# son = Son()
#
# print(son.greet())
# print(son.mood)
# son.be_kind()
# print(son.mood)
# son.be_strict()
# print(son.mood)


# Класс MROHelper

# class MROHelper:
#
#     @staticmethod
#     def len(cls):
#         return len(cls.mro())
#
#     @staticmethod
#     def class_by_index(cls, n=0):
#         return cls.mro()[n]
#
#     @staticmethod
#     def index_by_class(child, parent):
#         return child.mro().index(parent)
#
#
# class A:
#     pass
#
#
# class B(A):
#     pass
#
#
# class C(A):
#     pass
#
#
# class D(B, C):
#     pass
#
#
# print(MROHelper.index_by_class(D, A))