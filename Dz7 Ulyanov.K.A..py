# задача 1
# Дано: Множество уникальных заказов и список выполненных заказов.
# Найти: Невыполненные заказы.
# Пример:
# Входные данные:
# Уникальные заказы: {1, 2, 3, 4, 5}
# Выполненные заказы: [2, 4]
#
# Выходные данные:
# Невыполненные заказы: {1, 3, 5}

# unique_orders = {1, 2, 3, 4, 5}
# completed_orders = [2, 4]
# completed_orders = set(completed_orders) # преобразовал список в множество
# print((f' Невыполненные заказы: {unique_orders - completed_orders}')) # unique_orders - completed_orders = оставил
# # элементы, которые есть в первом множестве, но нет во втором

# задача 2
# Дан список целых или дробных чисел
# Найдите количество уникальных элементов данного массива.

# list_of_nums = [1, 2, 4, 3, 8, 4, 1, 5]
# list_of_nums = set(list_of_nums)
# print(f'Уникальных элементов - {len(list_of_nums)}')

# задача 3
# Дан список целых или дробных чисел
# Найдите количество различных элементов данного массива.

# list_of_nums = [1, 2, 4, 3, 3, 5, 9, 8, 4, 1, 5]
# quantity = len(set(list_of_nums))
# print("Кол-во различных чисел:", quantity)

