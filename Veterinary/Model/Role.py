from Model.Base import *

class Role(Base):
    id = PrimaryKeyField()
    role = CharField()