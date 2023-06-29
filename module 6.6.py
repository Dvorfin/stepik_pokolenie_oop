# 6.6 Декоратор @contextmanager


# Контекстный менеджер make_tag

# from contextlib import contextmanager
#
# @contextmanager
# def make_tag(tag):
#     print(tag)
#     yield
#     print(tag)
#
#
# with make_tag('---'):
#     print('Поколение Python')


# Контекстный менеджер reversed_print

# from contextlib import contextmanager
# import sys
#
#
# @contextmanager
# def reversed_print():
#     tmp = sys.stdout.write
#     sys.stdout.write = lambda x: tmp(x[::-1])
#     yield
#     sys.stdout.write = tmp
#
#
# print('Вывод вне блока with')
#
# with reversed_print():
#     print('Вывод внутри блока with')
#
# print('Вывод вне блока with')


# Контекстный менеджер safe_write

# from contextlib import contextmanager
#
# @contextmanager
# def safe_write(filename):
#     error = False
#     try:
#         buf = open('buff.txt', 'w', encoding='utf-8')
#         yield buf
#         buf.close()
#     except Exception as e:
#         print(f"Во время записи в файл было возбуждено исключение {type(e).__name__}")
#         error = True
#     finally:
#
#         if not error:
#             with open('buff.txt', 'r', encoding='utf-8') as tmp:
#                 data = tmp.read()
#             file = open(filename, 'w')
#             file.write(data)
#             file.close()
#
#
# with safe_write('undertale.txt') as file:
#     file.write('Тень от руин нависает над вами, наполняя вас решительностью\n')
#
# with safe_write('undertale.txt') as file:
#     print('Под весёлый шорох листвы вы наполняетесь решительностью', file=file)
#     raise ValueError
#
# with open('undertale.txt') as file:
#     print(file.read())



# Контекстный менеджер safe_open
#
# from contextlib import contextmanager
#
#
# @contextmanager
# def safe_open(filename, mode='r'):
#     try:
#         file = open(filename, mode)
#         yield file, None
#         file.close()
#     except Exception as e:
#         yield None, str(e)
#
#
#
# with open('Couplet.txt', 'w') as file:
#     file.write('Так уносились мы мечтой\n')
#     file.write('К началу жизни молодой')
#
# with safe_open('Couplet.txt') as file:
#     file, error = file
#     print(error)
#     print(file.read())
#
#     print(file.closed)
#
# print(file.closed)