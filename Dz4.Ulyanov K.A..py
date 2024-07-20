# задача 1
# Дана пицца 8 кусочков. Доступны команды:
# 1. print(‘Взять кусок’)
# 2. print(‘съесть кусок’)
# написать программу, симулирующую поедание кусочков пиццы (По желанию можно анимацию убывание кусочков пиццы добавить)
# number_pieces = 8
# while number_pieces > 0:
#     user_selection = input('Вы хотите взять или съесть пиццу?')
#     if user_selection == 'взять':
#         print('Вы взяли кусок')
#         number_pieces -= 1
#     elif user_selection == 'съесть':
#         number_pieces -= 1
#         print(f'Вы съели кусок.Осталось {number_pieces}')
#     else:
#         print('Неправильная команда')
# #

# задача 2
# Выведите столбец чисел от 1 до 100, используя цикл while
# numb = 1
# while numb <= 100:
#     print(numb)
#     numb += 1

# задача 3
# Дана пицца 16 кусочков. Доступны команды:
# 1.print(‘Взять кусок’)
# 2. print(‘съесть кусок’)
# 3. print(‘положить кусок обратно’)
# написать программу, симулирующую поедание кусочков пиццы,  в  программе обязательно должно присутствовать команда №3
# два раза. Проверять условием, если пиццы в руках нет.

# number_pieces = 16
# while number_pieces > 0:
#     user_selection = input('Вы хотите взять, съесть или положить обратно кусочек пиццы?')
#     if user_selection == 'положить':
#         print('Вы еще не взяли кусочек')
#     elif user_selection == 'съесть':
#         number_pieces -= 1
#         print(f'Вы съели 1 кусочек.Осталось {number_pieces}')
#     elif user_selection == 'взять':
#         print('Вы взяли 1 кусочек')
#         user_selection = input('Вы хотите съесть или положить обратно кусочек пиццы?')
#         if user_selection == 'съесть':
#             number_pieces -= 1
#             print(f'Вы съели 1 кусочек. Осталось {number_pieces}')
#         elif user_selection == 'положить':
#             print(f'Вы положили обратно 1 кусочек. Осталось {number_pieces}')
#     else:
#         print('Неверная команда')
#
# задача 4
# Дано число n. Вывести степени этого числа с 1 по 10
# пример
# n=2
# 2^1=2
# 2^2=4
# …
# 2^9=512
# 2^10 = 1024

# Решение
# number = 3
# degree_of = 0
# while degree_of < 10:
#     degree_of += 1
#     print(f'{number}^{degree_of} = {number**degree_of}')

# задача 5
# Выведите столбец чисел от start (определяется пользователем) до end, используя цикл while. Найти произведение чисел


# Диапазон от 2 до 6
# start = int(input('Введите первое число в диапазоне от 2 до 6 '))
# end = int(input('Введите второе число в диапазоне от 2 до 6 '))
# product_of_numbers = start
# while True:
#     start += 1
#     product_of_numbers *= start
#     print(f'start - {start}, Произведение равно  {product_of_numbers }')
#     if start == end:
#         break
#
# print(f'Произведение равно = {product_of_numbers}')


