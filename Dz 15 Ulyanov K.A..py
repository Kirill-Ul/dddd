# 1)	Создайте класс Car с полями mass, km, power, speed, brand и реализуйте методы info() для вывода полной информации об автомобиле на экран
#
# 2)	Добавьте в класс методы lock(), unlock() и соответствующие параметры, необходимые для этих функций.
#
# 3)	Добавьте в класс методы start_engine(), stop_engine() и соответствующие параметры, необходимые для этих функций.
#
# class Car:
#     def __init__(self, mass = 1200, km = 170000, power = 123, speed = 200, brand = 'Rio'):
#         self.mass = mass
#         self.km = km
#         self.power = power
#         self.speed = speed
#         self.brand = brand
#         self.locked = True
#
#
#     def info(self):
#         print(self)
#
#     def __str__(self):
#         info = (f'mass: {self.mass}\n'
#                 f'km: {self.km}\n'
#                 f'power: {self.power}\n'
#                 f'speed: {self.speed}\n'
#                 f'brand: {self.brand}\n'
#                 f'locked: {self.locked}\n')
#         return info
#
#     def lock(self):
#         self.locked = True
#         print('Автомобиль заблокирован')
#
#     def unlock(self):
#             self.locked = False
#             print('Автомобиль разблокирован')
#
#     def start_engine(self):
#         if self.locked:
#             print('Машина заблокирована, нельзя запустить двигатель')
#         else:
#             print('Запуск двигателя')
#
#     def stop_engine(self):
#         print('Остановка двигателя')
#
# cars = Car()
# print(cars)
# cars.lock()
# cars.unlock()
# cars.start_engine()
# cars.stop_engine()

# 1)	Создайте класс Book, который будет иметь атрибуты title, author и pages.
# Добавьте метод, который будет выводить информацию о книге в формате:
# "Название: [title], Автор: [author], Страницы: [pages]".

# class Book:
#     def __init__(self,title = 'Высоконагруженные приложения', author = 'Клеппман Мартин', pages = 640):
#         self.title = title
#         self.author = author
#         self.pages = pages
#
#     # def info(self):
#     #     print(self)
#
#     def __str__(self):
#         info = (f'Название: [{self.title}]\n'
#                 f'Автор: [{self.author}]\n'
#                 f'Страницы: [{self.pages}]')
#         return info
#
# books = Book()
# print(books)

# 2)	Создайте класс Student, который будет иметь атрибуты name, age и grades (список оценок).
# Добавьте метод для вычисления среднего балла студента.
class Student:
    def __init__(self, name = 'Alex', age = 18, grades = [4, 4, 5, 5, 5]):
        self.name = name
        self.age= age
        self.grades = grades

    def __str__(self):
        info = (f'Имя: {self.name}\n'
                f'Возраст: {self.age}\n'
                f'Список оценок: {self.grades}\n')
        return info
    def average_score(self):
        print(f'Средний балл: {sum(self.grades)/ len(self.grades)}')


students = Student()
print(students)
students.average_score()