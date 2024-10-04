from SRC.Model.Base import *

class Drinks(Base):
    id = PrimaryKeyField()
    name  =CharField()
    price = DoubleField()