from peewee import *

db = SqliteDatabase('lifesum.db')

class User(Model):
    id = IntField()
    start_date = DateTimeField()
    height_cm  = FloatField()

    class Meta:
        database = db # This model uses the "people.db" database.
