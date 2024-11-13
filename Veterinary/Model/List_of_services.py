from Model.Base import *
from peewee import PrimaryKeyField, TextField, CharField


class ListOfServices(Base):
    id = PrimaryKeyField()
    serices = TextField()
    price = CharField()