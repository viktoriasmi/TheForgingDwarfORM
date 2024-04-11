import random
import sqlite3
import peewee

from models import *
import datetime

import hashlib
from playhouse.shortcuts import *
from functools import reduce
import operator

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
        production_time = 120,
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
        print('10 - очистить доходы кузницы')
        number = int(input("Выберите для продолжения: "))
        if number == 1:
            add_new_order()
        if number == 2:
            add_new_client()
        if number == 3:
            print('Таблица заказов из каталога: ')
            column_names = ['id', 'client', 'catalog', 'created_at', 'amount', 'status']
            print(' | '.join(column_names))
            for row in OrderCatalog.select():
                print(row.id, row.client, row.catalog, row.created_at, row.amount, row.status)
            print('Таблица индивидуальных заказов: ')
            column_names = ['id', 'client', 'req', 'created_at', 'amount', 'status', 'production_time', 'price']
            print(' | '.join(column_names))
            for row in OrderIndividual.select():
                print(row.id, row.client, row.req, row.created_at, row.amount, row.status, row.production_time, row.price)
            table = input("Введите 'c' для удаления заказа из каталога или 'i' для удаления заказа из индивидуальных заказов: ")
            order_id = int(input("Введите ID заказа, который хотите удалить: "))
            delete_order(table, order_id)
        if number == 4:
            change_order()
        if number == 5:
            add_item_to_catalog()
        if number == 6:
            change_catalog_item()
        if number == 7:
            search = input("Введите запрос для поиска: ")
            search_results = search_database(search)
            for result in search_results:
                print(result)
            print('\n')
        if number == 8:
            display_order_queue()
        if number == 9:
            calculate_income()
        if number == 10:
            IncomeData.delete().execute()
            IncomeIndividualData.delete().execute()
            print('Данные успешно удалены\n')




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
        if number == 2:
            add_new_order_user()
        if number == 3:
            search = input("Введите запрос для поиска: ")
            search_results = search_database_user(search)
            for result in search_results:
                print(result)
            print('\n')
        if number == 4:
            print("Каталог: ")
            column_names = ['id', 'name', 'type', 'material', 'style', 'description', 'production_time', 'price']
            print(' | '.join(column_names))
            catalog_items = CatalogItem.select()
            for item in catalog_items:
                print(item.id, item.name, item.type, item.material, item.style, item.description, item.production_time, item.price)
            print('\n')

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
        column_names = ['id', 'last_name', 'first_name', 'address']
        print(' | '.join(column_names))
        for client in clients:
            print(client.id, client.first_name, client.last_name, client.address)

        client_id = int(input("Введите ID клиента: "))

        print("Каталог:")
        column_names = ['id', 'name', 'type', 'material', 'style', 'description', 'production_time', 'price']
        print(' | '.join(column_names))
        catalog_items = CatalogItem.select()
        for item in catalog_items:
            print(item.id, item.name, item.type, item.material, item.style, item.description, item.production_time, item.price)

        catalog_id = int(input("Введите ID изделия: "))

        amount = int(input("Введите количество: "))

        new_order = OrderCatalog.create(client=client_id, catalog=catalog_id, amount=amount)
        print("Заказ успешно добавлен!\n")

    elif order_type == 2:
        print("Клиенты:")
        column_names = ['id', 'last_name', 'first_name', 'address']
        print(' | '.join(column_names))
        clients = Client.select()
        for client in clients:
            print(client.id, client.first_name, client.last_name, client.address)

        client_id = int(input("Введите ID клиента: "))

        req = input("Введите описание заказа: ")
        amount = int(input("Введите количество: "))
        price = random.randint(10000,100000)
        production_time = random.randint(100,500)

        new_order = OrderIndividual.create(client=client_id, req=req, amount=amount, production_time=production_time, price=price)
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

def delete_order(table, order_id):
    if table == 'c':
        OrderCatalog.delete().where(OrderCatalog.id == order_id).execute()
    elif table == 'i':
        OrderIndividual.delete().where(OrderIndividual.id == order_id).execute()
    else:
        print("Неверный выбор таблицы.")
    print('Заказ успешно удален.\n')


def change_order():
    while True:
        table_choice = input("Выберите таблицу для изменения заказа, заказы из каталога или индивидуальные заказы (c/i): ")
        if table_choice not in ['c', 'i']:
            print("Некорректное название таблицы. Пожалуйста, попробуйте снова.")
            continue
        if table_choice == 'c':
            orders = OrderCatalog.select()
            column_names = ['id', 'client_id', 'catalog_id', 'created_at', 'amount', 'status']
            print(' | '.join(column_names))
            for order in orders:
                print(order.id, order.client_id, order.catalog_id, order.created_at, order.amount, order.status)
        elif table_choice == 'i':
            orders = OrderIndividual.select()
            column_names = ['id', 'client_id', 'req', 'created_at', 'amount', 'status', 'production_time', 'price']
            print(' | '.join(column_names))
            for order in orders:
                print(order.id, order.client_id, order.req, order.created_at, order.amount, order.status, order.production_time, order.price)


        order_id = input("Введите ID заказа, который хотите изменить: ")
        order_id = int(order_id)

        try:
            if table_choice == 'c':
                order = OrderCatalog.get(OrderCatalog.id == order_id)
            elif table_choice == 'i':
                order = OrderIndividual.get(OrderIndividual.id == order_id)
        except DoesNotExist:
            print("Заказ с таким ID не найден. Пожалуйста, попробуйте снова.")
            continue

        field = input("Введите название поля, которое хотите изменить: ")
        new_value = input(f"Введите новое значение для поля {field}: ")
        try:
            if field == "status" and new_value not in ['ip', 'c', 'd']:
                raise ValueError("Неверное значение для поля status. Пожалуйста, введите значение ip, c или d.")
            if field == 'req' and not isinstance(new_value, str):
                raise TypeError("Ошибка: Неверный формат. Значение должно быть строкой.")
            if field in ['id', 'client_id', 'amount'] and not isinstance(new_value, int):
                raise TypeError("Ошибка: Неверный формат. Значение должно быть целым числом.")
            if field == 'price' and not isinstance(new_value, (float, int)):
                raise TypeError("Ошибка: Неверный формат. Значение должно быть числом.")
        except ValueError as ve:
            print(ve)
            break
        except TypeError as te:
            print(te)
            break
        setattr(order, field, new_value)
        order.save()
        print("Изменения сохранены.")
        next_action = input("Желаете продолжить изменение заказов? (y/n): ")
        if next_action.lower() != 'y':
            print('\n')
            break

def add_item_to_catalog():
    name = input("Введите название изделия: ")
    type = input("Введите тип изделия: ")
    material = input("Введите материал изделия: ")
    style = input("Введите стиль изделия: ")
    description = input("Введите описание изделия: ")
    production_time = int(input("Введите время производства: "))
    price = input("Введите цену изделия: ")
    price = float(price)

    new_item = CatalogItem.create(
        name=name,
        type=type,
        material=material,
        style=style,
        description=description,
        production_time=production_time,
        price=price
    )
    print("Новое изделие добавлено в каталог.\n")


def change_catalog_item():
    catalog_items = CatalogItem.select()
    column_names = ['id', 'name', 'type', 'material', 'style', 'description', 'production_time', 'price']
    print(' | '.join(column_names))
    for item in catalog_items:
        print(item.id, item.name, item.type, item.material, item.style, item.description, item.production_time,
              item.price)

    item_id = int(input("Введите id изделия для изменения: "))

    item_to_update = CatalogItem.get(CatalogItem.id == item_id)

    field_name = input(
        "Какое поле вы хотите изменить? (name, type, material, style, description, production_time, price): ")

    new_value = input("Введите новое значение: ")
    try:
        if field_name == 'price':
            new_value = float(new_value)
        elif field_name == 'production_time':
            new_value = int(new_value)
    except ValueError:
        print("Ошибка: Неверный формат. Значение должно быть числом.")
        exit()

    setattr(item_to_update, field_name, new_value)
    item_to_update.save()

    print("Изделие успешно изменено.\n")


def search_database(query):
    results = []
    tables = [Client, CatalogItem, OrderCatalog, OrderIndividual]
    for table in tables:
        queryset = table.select()
        for result in queryset:
            data = model_to_dict(result)
            if query.lower() in str(data).lower():
                results.append(data)
    return results

def search_database_user(query):
    results = []
    tables = [CatalogItem]
    for table in tables:
        queryset = table.select()
        for result in queryset:
            data = model_to_dict(result)
            if query.lower() in str(data).lower():
                results.append(data)
    return results

def display_order_queue():
    QueueData.delete().execute()
    QueueIndividualData.delete().execute()

    for order in OrderCatalog.select():
        if order.status == 'ip':  # Проверка статуса перед добавлением в очередь
            catalog_item = CatalogItem.get(CatalogItem.id == order.catalog)
            QueueData.create(
                order=order,
                created_at=order.created_at,
                status=order.status,
                production_time=catalog_item.production_time
            )
    for order in OrderIndividual.select():
        if order.status == 'ip':  # Проверка статуса перед добавлением в очередь
            QueueIndividualData.create(
                order=order,
                created_at=order.created_at,
                status=order.status,
                production_time=order.production_time
            )
    print("Очередь заказов из каталога:")
    column_names = ['id', 'created_at', 'status', 'production_time']
    print(' | '.join(column_names))
    for queue_data in QueueData.select().order_by(QueueData.created_at):
        print(queue_data.order, queue_data.created_at, queue_data.status, queue_data.production_time)

    print("Очередь индивидуальных заказов:")
    column_names = ['id', 'created_at', 'status', 'production_time']
    print(' | '.join(column_names))
    for queue_data in QueueIndividualData.select().order_by(QueueIndividualData.created_at):
        print(queue_data.order, queue_data.created_at, queue_data.status, queue_data.production_time)
    print('\n')

def calculate_income():
    total_income_individual = OrderIndividual.select(fn.SUM(OrderIndividual.price)).where(
        OrderIndividual.status != 'c').scalar()
    IncomeIndividualData.create(income=total_income_individual, created_at=datetime.datetime.now())

    total_price = OrderCatalog.select(fn.SUM(CatalogItem.price)).join(CatalogItem, on=(
                OrderCatalog.catalog == CatalogItem.id)).where(OrderCatalog.status != 'c').scalar()
    IncomeData.create(income=total_price, created_at=datetime.datetime.now())

    print("Доходы кузницы с заказов из каталога: ")
    column_names = ['income', 'created_at']
    print(' | '.join(column_names))
    for income_data in IncomeData.select():
        print(income_data.income, income_data.created_at)

    print("Доходы кузницы с индивидуальных заказов: ")
    column_names = ['income', 'created_at']
    print(' | '.join(column_names))
    for income_individual_data in IncomeIndividualData.select():
        print(income_individual_data.income, income_individual_data.created_at)
    print('\n')


def add_new_order_user():
    # Считывание данных от пользователя
    first_name = input("Введите ваше имя : ")
    last_name = input("Введите вашу фамилию: ")

    # Поиск клиента в базе данных
    clients = Client.select().where(Client.first_name == first_name, Client.last_name == last_name)

    if clients.count() > 1:
        address = input("Уточните ваш адрес: ")
        clients = Client.select().where(Client.first_name == first_name, Client.last_name == last_name,
                                        Client.address == address)

    if clients.count() == 0:
        register = input("Клиент не найден. Желаете зарегистрироваться? (y/n) ")

        if register.lower() == "n":
            print("Без регистрации нельзя отправить заявку на заказ.")
            return
        address = input("Введите ваш адрес: ")
        new_client = Client.create(first_name=first_name, last_name=last_name, address=address)
        client = new_client
    else:
        client = clients.get()

    order_type = input("Выберите тип заказа: каталог/индивидуальный (c/i)?: ")

    if order_type.lower() == "c":
        # Вывод каталога и выбор изделия
        catalog_items = CatalogItem.select()
        for item in catalog_items:
            print(f"ID: {item.id}, Название: {item.name}, Тип: {item.type}, Материал: {item.material}, Стиль: {item.style}, Описание: {item.description},  Цена: {item.price}")

        catalog_id = int(input("Введите ID изделия из каталога: "))
        catalog_item = CatalogItem.get_by_id(catalog_id)

        amount = int(input("Введите количество изделий: "))

        OrderCatalog.create(client=client, catalog=catalog_item, created_at=datetime.datetime.now(), amount=amount,
                            status="ip")
    elif order_type.lower() == "i":
        req = input("Введите требования к заказу: ")
        amount = int(input("Введите количество изделий: "))

        production_time = random.randint(100, 500)
        price = random.randint(5000, 50000)

        OrderIndividual.create(client=client, req=req, created_at=datetime.datetime.now(), amount=amount,
                               status="ip", price=price, production_time=production_time)

    print("Заказ успешно добавлен.")

authenticate_user()