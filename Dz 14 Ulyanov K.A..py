# 1.	Написать программу, которая читает из файла список студентов и их
# оценки, а затем сохраняет только тех студентов, у которых средний балл выше 4.0.


# import csv
#
# with open('data3.csv', newline='', encoding='utf-8') as file:
#     reader = csv.reader(file, delimiter=';')
#     for row in reader:
#         surname = row[0]
#         scores = []
#         for i in row[1:]:
#             scores.append(int(i))
#         if sum(scores) / len(scores) > 4:
#             print(f"Фамилия студента: {surname} Оценки: {scores}")
#


# 2.	Написать программу, которая создает резервные копии всех файлов
# с расширением .txt, добавляя к их именам текущую дату и время.



# import os
# import shutil
# import datetime
#
# # Получаем текущую дату и время в формате "гггг-мм-дд_чч-мм-сс"
# times = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
#
# for file in os.listdir():
#   if file.endswith(".txt"):
#
#     backup_file = f"{file}_{times}.txt"
#     shutil.copy2(file, backup_file)
#
# print("Резервные копии созданы!")