from peewee import *
from playhouse.db_url import connect

database = SqliteDatabase('database.db')

class BaseModel(Model):
    class Meta:
        database = database

class Post(BaseModel):
    title = CharField()
    body = CharField()


def create_tables():
    database.connect()
    database.create_tables([Post])
