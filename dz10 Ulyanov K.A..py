#
# Написать программу, которая генерирует форматированную строку.
#
# Программа в цикле получает из stdin названия фруктов (цикл прерывается при вводе пустой строки).
# Программа выводит в stdout строку с перечислением всех фруктов, добавляя перед последним фруктом союз "и", а перед предыдущими (при их наличии) фруктами добавляя запятые (см. примеры вывода).
#
# Пример ввода 1:
#     яблоко
#
# Пример вывода 1:
#     яблоко
#
# Пример ввода 2:
#     яблоко
#     груша
#
# Пример вывода 2:
#     яблоко и груша
#
# Пример ввода 3:
#     яблоко
#     груша
#     апельсин
#
# Пример вывода 3:
#     яблоко, груша и апельсин
#
# Пример ввода 4:
#     яблоко
#     груша
#     апельсин
#     лимон
#
# Пример вывода 4:
#     яблоко, груша, апельсин и лимон

fruits = [] # список для хранения фруктов
while True:
  fruit = input('Введите название фрукта')
  if fruit == "":
    break # цикл прервется только при введении пустой строки
  fruits.append(fruit) # вкладываем значения в список

if len(fruits) == 1:
  print(fruits[0])
elif len(fruits) > 1:
  print(", ".join(fruits[:-1]) + " и " + fruits[-1]) # соединяем все элементы списка