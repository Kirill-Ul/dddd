# 1)	Создайте базовый класс Dog, который будет иметь атрибуты name и age.
# Затем создайте подклассы WorkingDog (с атрибутом job) и PetDog.
# Реализуйте методы, которые выводят информацию о работе собаки или о том,
# как она ведет себя как домашний питомец.

# class Dog:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
#     def info(self):
#         print(f'Имя {self.name}, Возраст {self.age}')
#
# class WorkingDog(Dog):
#     def __init__(self, name, age, job):
#         super().__init__(name, age)
#         self.job = job
#
#     def work_info(self):
#         print(f"{self.name} - {self.job} двор")
#
# class PetDog(Dog):
#     def pet_info(self):
#         print(f"{self.name} - ест и спит")
#
# working_dog = WorkingDog("Арчи", 5, "сторожит")
# pet_dog = PetDog("Рекс", 2)
#
# working_dog.info()
# working_dog.work_info()
# pet_dog.info()
# pet_dog.pet_info()

# 2)	Создайте базовый класс Vehicle, который будет иметь атрибуты make, model и year.
# Затем создайте подклассы Car и Truck, добавив атрибуты, специфичные для каждого типа
# (например, passenger_capacity для автомобиля и payload_capacity для грузовика).
# Реализуйте метод для отображения информации о транспортном средстве.

# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def info(self):
#         print(f'Марка {self.make}, Модель {self.model}, Год выпуска {self.year}')
#
# class Car(Vehicle):
#     def __init__(self, make, model, year, passenger_capacity,fuel_consumption):
#         super().__init__(make, model, year)
#         self.passenger_capacity = passenger_capacity
#         self.fuel_consumption = fuel_consumption
#
#     def additional_information(self):
#         print(f'Марка - {self.make}, Пассажиро-вместимость - {self.passenger_capacity}, Расход топлива '
#               f'{self.fuel_consumption} - литров на 100 км.')
#
#
# class Truck(Vehicle):
#     def __init__(self, make, model, year, payload_capacity, fuel_tank_capacity):
#         super().__init__(make, model, year)
#         self.payload_capacity = payload_capacity
#         self.fuel_tank_capacity = fuel_tank_capacity
#
#     def specifications(self):
#         print(f'Марка - {self.make}, Грузоподъемность - до {self.payload_capacity} тонн, Объем топливного бака - '
#               f'{self.fuel_tank_capacity} литров.')
#
# car = Car('Kia','Rio',2014, '5 человек', 7 )
# truck = Truck('Volvo','FH16 Aero',2024, 85, 700)
#
# car.info()
# car.additional_information()
# truck.info()
# truck.specifications()


# 3)	Создайте базовый класс Animal, который будет иметь атрибуты name и species.
# Затем создайте под 6gклассы Mammal и Bird, добавив методы, специфичные для каждого
# класса (например, метод make_sound() для млекопитающих и метод fly() для птиц).

# class Animal:
#     def __init__(self, name, species):
#         self.name = name
#         self.species = species
#
#     def info(self):
#         print(f'Животное - {self.name}, Вид - {self.species}')
#
# class Mammal(Animal):
#     def make_sound(self):
#         print(f'{self.name} - мычит ')
#
#     def work(self):
#         print(f'{self.name} - дает молоко ')
#
#
# class Bird(Animal):
#     def fly(self):
#         print(f'{self.name} - летает')
#
#     def work(self):
#         print(f'{self.name} - охотится')
#
#
# mammal = Mammal('Корова', 'Млекопитающее')
# bird = Bird('Ворона', 'Воробьинообразная')
#
# mammal.info()
# mammal.make_sound()
# mammal.work()
# bird.info()
# bird.fly()
# bird.work()

# 4)	Создайте базовый класс Toy, который будет иметь атрибуты name и price.
# Затем создайте подклассы ActionFigure и BoardGame, добавив атрибуты,
# специфичные для каждого типа (например, character_name для фигурки и number_of_players
# для настольной игры). Реализуйте метод для вывода информации о каждой игрушке.

# class Toy:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price
#
#     def info(self):
#         print(f'Название игры - {self.name}, Стоимость - {self.price} рублей ')
#
# class ActionFigure(Toy):
#     def __init__(self, name, price, character_name, characterization_of_the_hero ):
#         super().__init__(name, price)
#         self.character_name = character_name
#         self.characterization_of_the_hero = characterization_of_the_hero
#
#     def personal_card(self):
#         print(f'Название игры - {self.name}, Имя персонажа - {self.character_name}, Миссия героя - '
#               f'{self.characterization_of_the_hero}')
#
# class BoardGame(Toy):
#     def __init__(self, name, price, number_of_players, genre):
#         super().__init__(name, price)
#         self.number_of_players = number_of_players
#         self.genre = genre
#
#     def description(self):
#         print(f'Название игры - {self.name}, Количество игроков - {self.number_of_players}, Жанр - {self.genre}')
#
# actionfigure = ActionFigure('Spider Man', 1000, 'Piter Parker', 'Борьба со злом')
# boardgame = BoardGame('Шахматы', 500, 2, 'Интеллектуальная')
#
# actionfigure.info()
# boardgame.info()
# actionfigure.personal_card()
# boardgame.description()


# 5)	Создайте базовый класс Event, который будет иметь атрибуты event_name,
# date и location. Затем создайте подклассы Concert и Conference, добавив атрибуты,
# специфичные для каждого типа (например, performer для концерта и speakers для
# конференции). Реализуйте метод для отображения информации о событии.

class Event:
    def __init__(self, event_name, date, location):
        self.event_name = event_name
        self.date = date
        self.location = location

    def info(self):
        print(f'Название события - {self.event_name}, Дата - {self.date}, Местоположение - {self.location}')

class Concert(Event):
    def __init__(self, event_name, date, location, performer, capacity):
        super().__init__(event_name, date, location)
        self.performer = performer
        self.capacity = capacity

    def add_information(self):
        print(f'Название события - {self.event_name}, Исполнитель - группа {self.performer}, Вместимость'
              f' {self.capacity} '
              f'человек')

class Conference(Event):
    def __init__(self, event_name, date, location, speakers, ticket_price, number_of_viewers ):
        super().__init__(event_name, date, location)
        self.speakers = speakers
        self.ticket_price = ticket_price
        self.number_of_viewers = number_of_viewers

    def infos(self):
        print(f'Название события - {self.event_name}, Выступающий - {self.speakers}, Цена билета - {self.ticket_price} '
              f'рублей'
              f', Количество зрителей - {self.number_of_viewers} человек')

    def income(self):
        print(f'Доход составил {self.ticket_price * self.number_of_viewers } рублей ')

concert = Concert('День города','7.09.2024', 'Москва', 'ЛЮБЭ', 10000)
conference = Conference('Бизнес конференция', '21.12.2023', 'Санкт-Петербург', 'XXX', 5000, 3000)
concert.info()
concert.add_information()
conference.info()
conference.infos()
conference.income()




