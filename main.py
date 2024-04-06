from models import *

Client(
    first_name='Ричард',
    last_name='Торрес',
    address='9902 Майерт Ленд Соледадвилль'
)
Client(
    first_name='Дебра',
    last_name='Флорес',
    address='5390 Люкс Вивьен Маунт'
)
Client(
    first_name='Карен',
    last_name='Бейкер',
    address='77402 Люкс Энджел Клифф'
)
CatalogItem(
    name='Меч Экскалибур',
    type='Холодное оружие',
    material='Дамасская сталь',
    style='Готика',
    production_time=120,
    price=10000.00
)

CatalogItem(
    name='Скульптура Давида',
    type='Скульптуры',
    material='Тигельная сталь',
    style='Историческое',
    production_time=100,
    price=100000.00
)
CatalogItem(
    name='Средневековая броня',
    type='Броня',
    material='Железо',
    style='Готика',
    production_time=100,
    price=12000.00
)
CatalogItem(
    name='Броня эпохи Возрождения',
    type='Броня',
    material='Дамасская сталь',
    style='Фэнтези',
    production_time=100,
    price=130000.00
)
CatalogItem(
    name='Меч Гарольда',
    type='Холодное оружие',
    material='Дамасская сталь',
    style='Готика',
    production_time=120,
    price=110000.00
)
CatalogItem(
    name='Ворота Тадж-Махала',
    type='Ворота',
    material='Мозаичный',
    style='Исторический',
    production_time=1000,
    price=1000000.00
)
CatalogItem(
    name='Ворота Колизея',
    type='Ворота',
    material='Мозаичный',
    style='Исторический',
    production_time=900,
    price=1000000.00
)
cli1 = Client.get(id=1)
cli2 = Client.get(id=2)
cli3 = Client.get(id=3)
cat1 = CatalogItem.get(id=1)
cat2 = CatalogItem.get(id=2)
cat4 = CatalogItem.get(id=4)

OrderCatalog(
    client=cli1,
    catalog = cat2,
    created_at = '2024-03-14 15:08:05',
    amount = 3,
    status = 'd'
)
OrderCatalog(
    client=cli2,
    catalog = cat1,
    created_at = '2024-03-14 15:08:05',
    amount = 3,
    status = 'ip'
)
OrderCatalog(
    client=cli3,
    catalog = cat4,
    created_at = '2024-03-14 15:08:05',
    amount = 1,
    status = 'ip'
)


