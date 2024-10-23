# импортируем модули
import sqlalchemy.exc
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import psycopg2


app = Flask(__name__) #Создает экземпляр приложения Flask.

#Устанавливает строку подключения к базе данных PostgreSQL.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5433/contacts'
#Отключает отслеживание изменений модели в SQLAlchemy
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app) #Инициализирует SQLAlchemy для приложения Flask.


class Contact(db.Model):#Определяет модель Contact для представления контактов в базе данных.
    __tablename__ = 'contacts' #Имя таблицы в базе данных.
    id = db.Column(db.Integer, primary_key=True)# Столбец для идентификатора контакта (первичный ключ).
    name = db.Column(db.String(80), nullable=False)#Столбец для имени контакта.
    email = db.Column(db.String(120), nullable=False, unique=True)#Столбец для электронной почты контакта.

    def __repr__(self):# Метод для представления объекта Contact в виде строки.
        return f'<Contact {self.name}>'


with app.app_context():#Создает  контекст  приложения  Flask,  чтобы  модель  Contact  могла  быть  использована  для
    #  создания  таблицы  в  базе  данных.
    db.create_all()# Создает  таблицу  contacts  в  базе  данных,  если  она  еще  не  существует.

#Маршруты
@app.route('/')#Главная  страница  сайта  (отображает  index.html).
def index():
    return render_template('index.html')


@app.route('/contacts')# Отображает  список  контактов  (отображает  contacts.html).
def contacts():
    contacts = Contact.query.all()
    return render_template('contacts.html', contacts=contacts)

@app.route('/add_contact', methods=['POST'])#Обрабатывает  POST-запрос  для  добавления  нового  контакта.
def add_contact():
    name = request.form['name']
    email = request.form['email']

    if not name or not email:
        return render_template('index.html', message='Все поля должны быть заполнены')

    # existing_contact = Contact.query.filter_by(email=email).first()
    # if existing_contact:
    #     return render_template('index.html', message='Этот email уже используется')

    new_contact = Contact(name=name, email=email)
    db.session.add(new_contact)
    try:
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        db.session.rollback()
        return render_template('index.html', message='Этот email уже используется')

    return redirect(url_for('contacts'))


@app.route('/delete/<int:contact_id>')#Обрабатывает  запрос  для  удаления  контакта  по  его  ID.
def delete(contact_id):
    contact = Contact.query.get_or_404(contact_id)
    db.session.delete(contact)
    db.session.commit()
    return redirect(url_for('contacts'))

#Запускает приложение Flask только при прямом запуске скрипта (не при импорте).
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)