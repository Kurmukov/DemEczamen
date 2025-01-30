from peewee import PrimaryKeyField, CharField

from Models.Base import Base

class Roles(Base):
    id = PrimaryKeyField()
    role_name = CharField(max_length=255)