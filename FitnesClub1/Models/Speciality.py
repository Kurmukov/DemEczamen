from Models.Base import *

class Speciality(Base):
    id = PrimaryKeyField()
    name = CharField(max_length=255)