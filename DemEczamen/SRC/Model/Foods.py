from SRC.Model.Base import *

class Foods(Base):
    id = PrimaryKeyField()
    name  =CharField()
    price = DoubleField()