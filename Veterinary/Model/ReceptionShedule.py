from Model.Base import *
from Model.List_of_services import *
from Model.Staff import *
class Reception_shedule(Base):
    id = PrimaryKeyField()
    date_of_admission = DateTimeField()
    client = CharField()
    staff_id = ForeignKeyField(Staff)
    services = ForeignKeyField(ListOfServices)