from peewee import *
from Connect.connect import *



class Base(Model):
    class Meta:
        database = mysql_db