from peewee import PrimaryKeyField, CharField, DateField, ForeignKeyField
from Models.Base import Base
from Models.Traning import Traning


class Clint(Base):
    id = PrimaryKeyField()
    FirstName = CharField(max_length=20)
    LastName = CharField(max_length=255)
    Birthday = DateField()
    Phone = CharField(max_length=20)
    email = CharField(max_length=155)
    training = ForeignKeyField(Traning)