from SRC.Model.Base import *
from SRC.Model.Roles import Roles


class Users(Base):
    id = PrimaryKeyField()
    login = CharField()
    password = CharField()
    name = CharField()
    status = IntegerField()
    role_id = ForeignKeyField(Roles)