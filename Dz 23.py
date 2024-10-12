# 1.	Пользователь с клавиатуры вводит значения в список. После чего запускаются две потока.
# Первый поток находит максимум в списке 5 раз. Второй поток находит минимум в списке 5 раз.
# Результаты вычислений выводятся на экран. Поочередно.
import threading
import time

#
# a = [2,5,8,1,0]
#
# def max_numbers():
#     for _ in a:
#         print(f'{max(a)}')
#         time.sleep(2)
#
# def min_numbers():
#     for _ in a:
#         print(f'{min(a)}')
#         time.sleep(3)
#
# thread1 = threading.Thread(target=max_numbers)
# thread2 = threading.Thread(target=min_numbers)
#
# thread1.start()
# thread2.start()
#
# thread1.join()
# thread2.join()
#
# print("Конец")



# 2.	Пользователь с клавиатуры вводит значения в список. После чего запускаются две потока.
# Первый поток находит сумму элементов в списке 5 раз. Второй поток находит среднеарифметическое в списке 5 раз.
# Результаты вычислений выводятся на экран. Поочередно.

# a = [2,5,8,1,0]
#
# def sum_numbers():
#     b = 0
#     for i in a:
#         b += i
#     print(f'Сумма равна: {b} ')
#     time.sleep(0)
# def average_numbers():
#     print(f'Среднее арифметическое равно: {sum(a) / len(a)} ')
#     time.sleep(1)
# for _ in range(5):
#     thread1 = threading.Thread(target=sum_numbers)
#     thread2 = threading.Thread(target=average_numbers)
#
#     thread1.start()
#     thread2.start()
#
#     thread1.join()
#     thread2.join()
#
# print("Конец")


# 3.	При старте приложения запускаются три потока. Первый поток заполняет список случайными числами.
# Два других потока ожидают заполнения. Когда список заполнен оба потока запускаются.
# Первый поток находит сумму элементов списка, второй поток среднеарифметическое значение в списке.
# Полученный список, сумма и среднеарифметическое выводятся на экран.

# import random
#
# numbers = []
# counter = False
#
# def random_numbers():
#   global numbers, counter
#   for _ in range(5):
#     numbers.append(random.randint(1, 20))
#     time.sleep(0.5)
#   counter = True
#   print("Список заполнен!")
#
#
# def sum_numbers():
#   global counter
#   while not counter:
#     time.sleep(0.1)
#   sum = 0
#   for num in numbers:
#     sum += num
#   print(f"Сумма элементов: {sum}")
#
#
# def average_numbers():
#   global counter
#   while not counter:
#     time.sleep(0.1)
#   average = sum(numbers) / len(numbers)
#   print(f"Среднее арифметическое: {average}")
#
#
# thread1 = threading.Thread(target=random_numbers)
# thread2 = threading.Thread(target=sum_numbers)
# thread3 = threading.Thread(target=average_numbers)
#
# thread1.start()
# thread2.start()
# thread3.start()
#
# thread1.join()
# thread2.join()
# thread3.join()
#
# print("Список:", numbers)
# print("Конец")

