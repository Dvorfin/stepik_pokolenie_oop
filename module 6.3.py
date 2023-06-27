# 6.3 Оператор with

# Функция print_file_content()

# def print_file_content(filename:str):
#     try:
#         with open(filename, 'r', encoding='utf-8') as file:
#             for srr in file.readlines():
#                 print(srr.strip())
#     except:
#         print('Файл не найден')
#
#
# print_file_content('Precepts_of_Zote2.txt')


# Функция non_closed_files()

# def non_closed_files(files):
#     return [f for f in files if not f.closed]


# Функция log_for()

# def log_for(logfile, date_str):
#     with open(f'log_for_{date_str}.txt', 'w', encoding='utf-8') as file:
#         with open(logfile, 'r', encoding='utf-8') as log:
#             for line in log.readlines():
#                 if date_str in line.strip():
#                     info = line[line.find(' ') + 1:-1]
#                     print(info, file=file)
#
# with open('log.txt', 'w', encoding='utf-8') as file:
#     print('2022-01-01 INFO: User logged in', file=file)
#     print('2022-01-01 ERROR: Invalid input data', file=file)
#     print('2022-01-02 INFO: User logged out', file=file)
#     print('2022-01-03 INFO: User registered', file=file)
#
# log_for('log.txt', '2022-01-01')

with open('log_for_2022-01-01.txt', encoding='utf-8') as file:
    print(file.read())