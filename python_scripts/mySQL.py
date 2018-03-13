## Will be use to show an other way to build the datamodel  

import peewee

db = peewee.SqliteDatabase('')

class User(peewee.Model):
    id = peewee.IntegerField()
    start_date = peewee.DateTimeField()
    height_cm  = peewee.FloatField()

    class Meta:
        database = db # This model uses the "people.db" database.


import inspect
import peewee
import tables
models = [
    obj for name, obj in inspect.getmembers(
        tables, lambda obj: type(obj) == type and issubclass(obj, peewee.Model)
    )
]
peewee.create_model_tables(models)