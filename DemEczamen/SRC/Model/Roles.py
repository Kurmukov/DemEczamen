from SRC.Model.Base import *

class Roles(Base):
    id = PrimaryKeyField()
    role = IntegerField()