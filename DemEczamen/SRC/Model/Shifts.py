from SRC.Model.Base import *
from SRC.Model.Roles import Roles


class Shifts(Base):
    id = PrimaryKeyField()
    date = DateTimeField()
    cook = ForeignKeyField(Roles)
    oficiant_1 = ForeignKeyField(Roles)
    oficiant_2 = ForeignKeyField(Roles)