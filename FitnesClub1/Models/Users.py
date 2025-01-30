from peewee import PrimaryKeyField, CharField, IntegerField, ForeignKeyField
from Models.Base import Base
from Models.Roles import Roles
from Models.Speciality import Speciality


class Users(Base):
    id = PrimaryKeyField()
    FirstName = CharField(max_length=255)
    LastName = CharField(max_length=255)
    role_id = ForeignKeyField(Roles)
    speciality_id = ForeignKeyField(Speciality)
    login = CharField(max_length=10)
    password = CharField(max_length=15)