from peewee import PrimaryKeyField, CharField

from Models.Base import Base
class Traning(Base):
    id = PrimaryKeyField()
    name = CharField(max_length=255)