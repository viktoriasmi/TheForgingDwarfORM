import random
from models import *
import datetime
from peewee import *
import hashlib

def encrypt_password_first():
    users = User.select()
    for user in users:
        password = user.password.encode('utf-8')
        hashed_password = hashlib.sha256(password).hexdigest()

        user.password = hashed_password
        user.save()
    #print("Пароли успешно зашифрованы")


if not Client.table_exists():
    db.create_tables([Client])
    Client(
        first_name='Ричард',
        last_name='Торрес',
        address='9902 Майерт Ленд Соледадвилль'
    ).save()
    Client(
        first_name='Дебра',
        last_name='Флорес',
        address='5390 Люкс Вивьен Маунт'
    ).save()
    Client(
        first_name='Карен',
        last_name='Бейкер',
        address='77402 Люкс Энджел Клифф'
    ).save()
if not CatalogItem.table_exists():
    db.create_tables([CatalogItem])
    CatalogItem(
        name='Меч Экскалибур',
        type='Холодное оружие',
        material='Дамасская сталь',
        style='Готика',
        production_time=120,
        price=10000.00
    ).save()

    CatalogItem(
        name='Скульптура Давида',
        type='Скульптуры',
        material='Тигельная сталь',
        style='Историческое',
        production_time=100,
        price=100000.00
    ).save()
    CatalogItem(
        name='Средневековая броня',
        type='Броня',
        material='Железо',
        style='Готика',
        production_time=100,
        price=12000.00
    ).save()
    CatalogItem(
        name='Броня эпохи Возрождения',
        type='Броня',
        material='Дамасская сталь',
        style='Фэнтези',
        production_time=100,
        price=130000.00
    ).save()
    CatalogItem(
        name='Меч Гарольда',
        type='Холодное оружие',
        material='Дамасская сталь',
        style='Готика',
        production_time=120,
        price=110000.00
    ).save()
    CatalogItem(
        name='Ворота Тадж-Махала',
        type='Ворота',
        material='Мозаичный',
        style='Исторический',
        production_time=1000,
        price=1000000.00
    ).save()
    CatalogItem(
        name='Ворота Колизея',
        type='Ворота',
        material='Мозаичный',
        style='Исторический',
        production_time=900,
        price=1000000.00
    ).save()
cli1 = Client.get(id=1)
cli2 = Client.get(id=2)
cli3 = Client.get(id=3)
cat1 = CatalogItem.get(id=1)
cat2 = CatalogItem.get(id=2)
cat4 = CatalogItem.get(id=4)

if not OrderCatalog.table_exists():
    db.create_tables([OrderCatalog])
    OrderCatalog(
        client=cli1,
        catalog = cat2,
        created_at = '2024-03-14 15:08:05',
        amount = 3,
        status = 'd'
    ).save()
    OrderCatalog(
        client=cli2,
        catalog = cat1,
        created_at = '2024-03-14 15:08:05',
        amount = 3,
        status = 'ip'
    ).save()
    OrderCatalog(
        client=cli3,
        catalog = cat4,
        created_at = '2024-03-14 15:08:05',
        amount = 1,
        status = 'ip'
    ).save()
if not User.table_exists():
    db.create_tables([User])
    User(
        name='user',
        password='uuu'
    ).save()
    User(
        name='admin',
        password='aaa'
    ).save()
    encrypt_password_first()
if not OrderIndividual.table_exists():
    db.create_tables([OrderIndividual])
    OrderIndividual(
        client = cli3,
        created_at = '2024-03-15 15:33:21',
        amount = 2,
        price = 84000.00
    ).save()

# основной код тут

def encrypt_password(password):
    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
    return hashed_password

def theforgingdwarfadmin():
    while True:
        #начало админ
        print('Добро пожаловать в кузницу The Forging Dwarf!')
        print('Выберите одну из опций: ')
        print('1 - добавить новый заказ')
        print('2 - добавить нового клиента')
        print('3 - удалить заказ')
        print('4 - изменить заказ')
        print('5 - добавить новое изделие в каталог')
        print('6 - изменить изделие в каталоге')
        print('7 - поиск')
        print('8 - показать очередь заказов')
        print('9 - вывести доход кузницы')
        number = int(input("Выберите для продолжения: "))
        if number == 1:
            add_new_order()
        if number == 2:
            add_new_client()

def theforgingdwarfuser():
    while True:
        # начало юзер
        print('Добро пожаловать в кузницу The Forging Dwarf!')
        print('Выберите одну из опций: ')
        print('1 - зарегестрироваться как клиент')
        print('2 - отправить заявку на заказ')
        print('3 - поиск')
        print('4 - вывести каталог изделий')
        number = int(input("Выберите для продолжения: "))
        # добавить себя как клиента
        if number == 1:
            add_new_client()


def authenticate_user():
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    hashed_password = encrypt_password(password)
    user = User.select().where(User.name == username).first()

    if user:
        if user.password == hashed_password:
            if username == "admin":
                theforgingdwarfadmin()
            else:
                theforgingdwarfuser()
        else:
            print("Неверный пароль\n")
    else:
        print("Пользователь не найден")

def add_new_order():
    print("Выберите тип заказа:")
    print("1. Заказ из каталога")
    print("2. Индивидуальный заказ")

    order_type = int(input("Введите ваш выбор: "))

    if order_type == 1:
        print("Клиенты: ")
        clients = Client.select()
        for client in clients:
            print(client.id, client.first_name, client.last_name, client.address)

        client_id = int(input("Введите ID клиента: "))

        print("Каталог:")
        catalog_items = CatalogItem.select()
        for item in catalog_items:
            print(item.id, item.name, item.type, item.material, item.style)

        catalog_id = int(input("Введите ID изделия: "))

        amount = int(input("Введите количество: "))

        new_order = OrderCatalog.create(client=client_id, catalog=catalog_id, amount=amount)
        print("Заказ успешно добавлен!\n")

    elif order_type == 2:
        print("Клиенты:")
        clients = Client.select()
        for client in clients:
            print(client.id, client.first_name, client.last_name, client.address)

        client_id = int(input("Введите ID клиента: "))

        req = input("Введите описание заказа: ")
        amount = int(input("Введите количество: "))
        price = random.randint(10000,100000)

        new_order = OrderIndividual.create(client=client_id, req=req, amount=amount, price=price)
        print("Заказ успешно добавлен!\n")

    else:
        print("Неправильный выбор")

def add_new_client():
    first_name = input("Введите ваше имя: ")
    last_name = input("Введите вашу фамилию: ")
    address = input("Введите ваш адрес: ")

    new_client = Client(first_name=first_name, last_name=last_name, address=address)
    new_client.save()
    print("Клиент успешно добавлен.\n")



authenticate_user()