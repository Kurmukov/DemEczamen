from Model.Base import *
from Model.Role import *
class Staff(Base):
    id = PrimaryKeyField()
    name = CharField()
    role_id = ForeignKeyField(Role)
    login = CharField()
    password = CharField()
