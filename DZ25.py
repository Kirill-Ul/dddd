
# Модель
class Book:
  """Модель книги."""

  def __init__(self, title, author, year):
    self.title = title
    self.author = author
    self.year = year

  def __str__(self):
    """Представление книги в виде строки."""
    return f"Книга: {self.title} ({self.year}), автор: {self.author}"

# Репозиторий (хранилище)
class BookRepository:
  """Репозиторий для работы с книгами."""

  def __init__(self):
    self.books = [] # Инициализация хранилища книг

  def add_book(self, book):
    """Добавление новой книги."""
    self.books.append(book)

  def get_book(self, title, author, year):
    """Получение книги по названию, автору и году."""
    for book in self.books:
      if book.title == title and book.author == author and book.year == year:
        return book
    return None

  def get_all_books(self):
    """Получение всех книг."""
    return self.books

  def remove_book(self, book):
    """Удаление книги."""
    self.books.remove(book)

# Интерфейс для работы с книгами
class BookService:
  """Интерфейс для работы с книгами."""

  def add_book(self, book):
    """Добавление новой книги."""
    raise NotImplementedError

  def get_book(self, title, author, year):
    """Получение книги по названию, автору и году."""
    raise NotImplementedError

  def get_all_books(self):
    """Получение всех книг."""
    raise NotImplementedError

  def remove_book(self, book):
    """Удаление книги."""
    raise NotImplementedError

# Конкретная реализация сервиса
class BookServiceImpl(BookService):
  """Реализация сервиса для работы с книгами."""

  def __init__(self, repository):
    self.repository = repository

  def add_book(self, book):
    self.repository.add_book(book)

  def get_book(self, title, author, year):
    return self.repository.get_book(title, author, year)

  def get_all_books(self):
    return self.repository.get_all_books()

  def remove_book(self, book):
    self.repository.remove_book(book)

# Вид
class BookView:
  """Отображение информации о книгах."""

  def __init__(self, service):
    self.service = service

  def show_books(self):
    """Отображение списка книг."""
    books = self.service.get_all_books()
    if books:
      print("Список книг:")
      for book in books:
        print(book)
    else:


      print("Список книг пуст.")

  def add_book(self):
    """Добавление новой книги."""
    title = input("Введите название книги: ")
    author = input("Введите автора: ")
    year = int(input("Введите год издания: "))
    book = Book(title, author, year)
    self.service.add_book(book)
    print("Книга добавлена!")

  def remove_book(self):
    """Удаление книги."""
    title = input("Введите название книги для удаления: ")
    author = input("Введите автора книги для удаления: ")
    year = int(input("Введите год издания книги для удаления: "))
    book = self.service.get_book(title, author, year)
    if book:
      self.service.remove_book(book)
      print(f"Книга '{book.title}' удалена.")
    else:
      print(f"Книга с указанными данными не найдена.")

# Контроллер
class BookController:
  """Контроллер для обработки запросов."""

  def __init__(self, view, service):
    self.view = view
    self.service = service

  def run(self):
    """Запуск приложения."""
    while True:
      print("\nВыберите действие:")
      print("1. Показать книги")
      print("2. Добавить книгу")
      print("3. Удалить книгу")
      print("4. Выход")

      choice = input("Введите номер действия: ")

      if choice == "1":
        self.view.show_books()
      elif choice == "2":
        self.view.add_book()
      elif choice == "3":
        self.view.remove_book()
      elif choice == "4":
        break
      else:
        print("Неверный выбор. Пожалуйста, введите число от 1 до 4.")

# Создание экземпляров компонентов
repository = BookRepository()
service = BookServiceImpl(repository)
view = BookView(service)
controller = BookController(view, service)

# Запуск приложения
controller.run()