import datetime
from peewee import *

db = SqliteDatabase('TheForgingDwarfORM.db')

STATUS_CHOICES = [
    ('ip', 'In Progress'),
    ('d', 'Done'),
    ('c', 'Canceled'),
]

def create_tables_if_not_exist():
    # Проверяем, существуют ли таблицы, и создаем их, если они не существуют
    if not db.is_closed():
        db.connect()

    tables_to_create = [IncomeData, IncomeIndividualData,
                        QueueData, QueueIndividualData]
    for model in tables_to_create:
        if not model.table_exists():
            model.create_table(True)  # True для принудительного создания таблицы, даже если она уже существует
class BaseModel(Model):
    class Meta:
        database = db

class User(BaseModel):
    class Meta:
        table_name = 'users'
    name = CharField(max_length=100)
    password = TextField()

class Client(BaseModel):
    class Meta:
        table_name = 'clients'
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    address = CharField(max_length=255)

class CatalogItem(BaseModel):
    class Meta:
        table_name = 'catalog'
    name = CharField(max_length=255)
    type = CharField(max_length=255)
    material = CharField(max_length=255)
    style = CharField(max_length=255)
    description = TextField(null=True)
    production_time = IntegerField()
    price = FloatField()

class OrderCatalog(BaseModel):
    class Meta:
        table_name = 'orders_catalog'
    client = ForeignKeyField(Client)
    catalog = ForeignKeyField(CatalogItem)
    created_at = DateTimeField(default=datetime.datetime.now)
    amount = IntegerField(default=1)
    status = CharField(choices=STATUS_CHOICES, default='ip')

class OrderIndividual(BaseModel):
    class Meta:
        table_name = 'orders_individual'
    client = ForeignKeyField(Client)
    req = TextField(null=True)
    created_at = DateTimeField(default=datetime.datetime.now)
    amount = IntegerField(default=1)
    status = CharField(choices=STATUS_CHOICES, default='ip')
    production_time = IntegerField(default=100)
    price = FloatField()

class IncomeData(BaseModel):
    class Meta:
        table_name = 'income'
    income = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

class IncomeIndividualData(BaseModel):
    class Meta:
        table_name = 'income_individual'
    income = FloatField()
    created_at = DateTimeField(default=datetime.datetime.now)

class QueueData(BaseModel):
    class Meta:
        table_name = 'queue_regular'
    order = ForeignKeyField(OrderCatalog)
    created_at = DateTimeField()
    status = CharField(choices=STATUS_CHOICES, default='ip')
    production_time = IntegerField()

class QueueIndividualData(BaseModel):
    class Meta:
        table_name = 'queue_individual'
    order = ForeignKeyField(OrderIndividual)
    created_at = DateTimeField()
    status = CharField(choices=STATUS_CHOICES, default='ip')
    production_time = IntegerField()

if __name__ == '__main__':
    create_tables_if_not_exist()