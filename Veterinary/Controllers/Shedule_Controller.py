from Model.ReceptionShedule import *
from Model.Staff import *

class Controller():

    @classmethod
    def add(cls, date_of_admission, client, staff_id, services):
        Reception_shedule.create(data = date_of_admission, client = client, staff = staff_id, services = services)
    @classmethod
    def get(cls):
        return Reception_shedule.select().execute()
    @classmethod
    def avtoriz(cls,in_login, in_password):
        user = Staff.get_or_none(Staff.login == in_login, Staff.password == in_password)
        if user:
            return True
        else:
            return False
