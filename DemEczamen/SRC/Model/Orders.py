from SRC.Model.Base import *
from SRC.Model.Drinks import Drinks
from SRC.Model.Foods import Foods
from SRC.Model.Shifts import Shifts
from SRC.Model.Statuces import Statuces
from SRC.Model.Tables import Tables


class Orders(Base):
    id = PrimaryKeyField()
    count_cliens = IntegerField()
    table_id = ForeignKeyField(Tables)
    drink_id = ForeignKeyField(Drinks)
    food_id = ForeignKeyField(Foods)
    shift_id = ForeignKeyField(Shifts)
    status_id = ForeignKeyField(Statuces)